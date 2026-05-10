# Input / Output

The PM has 10 dedicated input ports and 8 configurable I/O pins. For other pins which are considered I/O or dedicated output pins, see [here](../board.md#u3)

The [reset button](../board.md#reset) is not a general purpose input, though it is an [input pin to the CPU](../board.md#user-content-cpu-11) it is also an input to other parts of the hardware, likely powering off other systems directly.

## Dedicated inputs

| Port    | Description  | Interrupts | Registers |
| ------- | ------------ |:----------:|:---------:|
| [K00][] | C button     | [→][K00i]  | [→][K00r] |
| [K01][] | B button     | [→][K01i]  | [→][K01r] |
| [K02][] | A button     | [→][K02i]  | [→][K02r] |
| [K03][] | Up button    | [→][K03i]  | [→][K03r] |
| [K04][] | Down button  | [→][K04i]  | [→][K04r] |
| [K05][] | Left button  | [→][K05i]  | [→][K05r] |
| [K06][] | Right button | [→][K06i]  | [→][K06r] |
| [K07][] | Power button | [→][K07i]  | [→][K07r] |
| [K10][] | Cart input   | [→][K10i]  | [→][K10r] |
| [K11][] | Cart detect  | [→][K11i]  | [→][K11r] |

[K00]: #input-button
[K01]: #input-button
[K02]: #input-button
[K03]: #input-button
[K04]: #input-button
[K05]: #input-button
[K06]: #input-button
[K07]: #power-button
[K10]: #cartridge-input
[K11]: #cartridge-detect
[K00i]: ./interrupts.md#c-key
[K00r]: ./registers/input.md#port-00
[K01i]: ./interrupts.md#b-key
[K01r]: ./registers/input.md#port-01
[K02i]: ./interrupts.md#a-key
[K02r]: ./registers/input.md#port-02
[K03i]: ./interrupts.md#up-key
[K03r]: ./registers/input.md#port-03
[K04i]: ./interrupts.md#down-key
[K04r]: ./registers/input.md#port-04
[K05i]: ./interrupts.md#left-key
[K05r]: ./registers/input.md#port-05
[K06i]: ./interrupts.md#right-key
[K06r]: ./registers/input.md#port-06
[K07i]: ./interrupts.md#power-key
[K07r]: ./registers/input.md#port-07
[K10i]: ./interrupts.md#cartridge-irq
[K10r]: ./registers/input.md#port-10
[K11i]: ./interrupts.md#cartridge-ejected
[K11r]: ./registers/input.md#port-11

### Input button

Every keypad input except [power](#power-button) and reset work the same way. They have interrupts available but largely they're never used.

![button layout diagram](/assets/img/layout.png)

[MINLIB](/software/minlib.md) offers a method for fetching the current input every frame, reproduced [here](./registers/input.md#keypad-ports). This allows software to call this method once per main loop (since it also performs a vsync) and check RAM for keys that are currently being pressed. Many commercial games implement their own versions of this, regardless of its existence in MINLIB.

It's probably (TODO) possible to [configure de-jitter](./registers/irq.md#ctk) for the interrupts as well as [configure which edge][KCP] they fire on. If you want to use these but still poll inputs, do *not* enable the interrupts for K0x, and use code something like this in your main loop:

```s1c88
	LD A, [BR:29h]     ; read current keymap IRQ state
	LD [BR:29h], 0FFh  ; clear IRQ state
	; Newly pressed (or released) keys as 1s in A
```

See also: interrupts [A][K02i] [B][K01i] [C][K00i] [up][K03i] [down][K04i] [left][K05i] [right][K06i], registers [A][K02r] [B][K01r] [C][K00r] [up][K03r] [down][K04r] [left][K05r] [right][K06r]

[KCP]: ./registers/irq.md#kcp1--kcp0

### Power button

The power button is the only keypad input which has a unique code path for the interrupt handler. It can be used as an extra button in the same way as any other button, so long as the console is on. However if the console has been put to sleep, it follows a unique [wake-up routine](./interrupts.md#waking-up).

Homebrew games, such as the [hello world example](/dev/Hello_World.md), often just hook up the power IRQ handler to directly shut the console down. Commercial games tend to not define a handler ([some do][K07i]), and instead rely on polling it, either directly or in the same way as other inputs.

See also: [interrupt][K07i], [registers][K07r]

### Cartridge input

This input is a cartridge-defined input, essentially. A cartridge can decide what it means. It can be polled or handled by interrupt.

No commercial game uses this pin for anything. Several flash cards have this pin connected such that it could be driven to do something with custom firmware, but no existing firmware drives it for any purpose.

TODO: info on how to drive it for certain flash cards

See also: [interrupt][K10i], [registers][K10r]

### Cartridge detect

By default this interrupt is [configured][KCP] to fire when the cartridge is ejected. This is what the BIOS expects, so there isn't a dedicated vector for it on the cartridge which the BIOS jumps to. However, software can still handle this.

To handle ejection, copy a handler method to RAM then write a JRL to it at $1FFD, and sleep the console (either [44h](./bios.md#sleep) or [46h](./bios.md#sleep-with-display-on)).

To handle insertion, set KCP11 to 1 and set up a handler in RAM same as before.

```s1c88
; Any calls or jumps to outside what was copied won't work.
COPY_TO_RAM MACRO start, end
	LD IY, #start
^loop:
	LD [IX], IY
	INC IX
	INC IY
	CP IY, #end
	JRS C, ^loop
ENDM

prepare_eject:
	; Copy both handlers to RAM
	LD IX, #CartEjectHandlerRAM
	COPY_TO_RAM cart_eject_handler, ceh__end
	LD IX, #CartInsertHandlerRAM
	COPY_TO_RAM cart_insert_handler, cih__end

	; write the JRL
	LD SP, #2000h
	LD BA, #(CartEjectHandlerRAM - 1FFDh + 1)
	PUSH BA              ; write the address for the JRL
	LD A, #0F3h          ; JRL opcode
	PUSH A               ; push it

	OR [BR:24h], #02h    ; enable interrupt
	OR [BR:21h], #30h    ; set priority to 3
	OR [BR:01h], #80h    ; avoid console shutdown on eject
	; draw some info to the screen, then:
	INT [46h]            ; sleep with display on

cart_eject_handler:
	LD [BR:28h], #02h    ; clear factor flag

	; we use the insert interrupt as an example
	; you could poll K11D instead or do something else entirely
	OR [BR:51h], #02h    ; KCP11 = 1, to detect insert

	; write the JRL
	LD SP, #2000h
	LD BA, #(CartInsertHandlerRAM - 1FFDh + 1)
	PUSH BA              ; write the address for the JRL
	LD A, #0F3h          ; JRL opcode
	PUSH A               ; push it

	; do what you want!
ceh__loop:
	; but remember there's no returning to software!!
	JRS ceh__loop
ceh__end:

cart_insert_handler:
	LD [BR:28h], #02h    ; clear factor flag
	AND [BR:51h], #~02h  ; KCP11 = 0, to detect eject
	AND [BR:01h], #~80h  ; allow console to shutdown if ejected again
	LD SP, #2000h        ; software can overwrite the JRL we had here now
	; do what you want!
	; if you're going to re-enter software somewhere, jump
cih__end:
```

See also: [interrupt][K11i], [registers][K11r]

## I/O ports

| Port    | I/O | Description    | Interrupts | Registers |
| ------- | --- | -------------- |:----------:|:---------:|
| [P00][] | I/o | IR receiver    | [→][P00i]  | [→][P00r] |
| [P01][] | i/O | IR transmitter |     -      | [→][P01r] |
| [P02][] | I/O | EEPROM data    |     -      | [→][P02r] |
| [P03][] | I/O | EEPROM clock   |     -      | [→][P03r] |
| [P04][] |  O  | Rumble motor   |     -      | [→][P04r] |
| [P05][] | i/O | IR disable     |     -      | [→][P05r] |
| [P06][] | I/o | Shock sensor   | [→][P06i]  | [→][P06r] |
| P07     |  ?  | ?              |     -      |     -     |

I/O ports (or P ports) are ports which can be configured to act either as input or output by the software. Not all ports on the PM may be used as both. In the above table's I/O column, upper-case indicates the mode is intended, lower-case indicates it's possible but not intended.

Configure a port with its respective IOC register. A value of 0 configures it as input, a value of 1 configures it as output.

|         | IOC=0       | IOC=1         |
| -------:|:-----------:|:-------------:|
|  Read D | Input data* | Last written? |
| Write D | ???         | Output data   |

\* If there is no data being externally driven on the pin, the state is left undetermined as that bit is defined as floating.

During initialization the BIOS configures P01 (IR TxD), P04 (Rumble), and P05 (IR disable) as output ports, and everything else as input [here](/software/bios/disasm.md#user-content-01C5).

Although switching the EEPROM clock to input is used normally, it's used to disable clocking to the EEPROM and does not expect to actually receive signal.

Previous documentation suggested that P07 may also be an IR transmission pin: `(IR Transmitter? Used to double power?)` but this is unconfirmed.

[P00]: ../ir.md
[P00i]: ./interrupts.md#ir-receiver
[P00r]: ./registers/io.md#p00
[P01]: ../ir.md
[P01r]: ./registers/io.md#p01
[P02]: ../eeprom.md
[P02r]: ./registers/io.md#p02
[P03]: ../eeprom.md
[P03r]: ./registers/io.md#p03
[P04]: #rumble
[P04r]: ./registers/io.md#p04
[P05]: ../ir.md
[P05r]: ./registers/io.md#p05
[P06]: #shock
[P06i]: ./interrupts.md#shock-sensor
[P06r]: ./registers/io.md#p06

### Rumble

Write a 1 to P04D to start the rumble motor, write a 0 to turn it off.

The recommended way to rumble for a certain amount of time would be to have a method that checks if rumble is desired, starts rumbling, then writes a value to RAM representing the number of frames it should rumble for. Then in your main loop/vsync, decrement that value by 1, and if it reaches 0, disable rumble.

```c
// rumble.h
void start_rumble(char frames);
void step_rumble(void);

_inline void stop_rumble(void) {
	IO_DATA &= ~0x10;
}

// rumble.c
#include <pm.h>
#include "rumble.h"

char rumble_frames = 0;

void start_rumble(char frames) {
	IO_DATA |= 0x10;
	rumble_frames = frames;
}

void step_rumble(void) {
	if (rumble_frames > 0 && !rumble_frames--) {
		stop_rumble();
	}
}

// main.c
#include <pm.h>
#include "rumble.h"

int main(void) {
	// ...setup...
	for (;;) {
		// ...
		wait_vsync();
		step_rumble();
	}
}
```

See also: [registers][P04r]

### Shock

When the player shakes the console, P06D goes low and the shock sensor interrupt triggers. It's possible to poll P06D but it's not recommended. For polling, poll FP6 instead.

```c
int main(void) {
	// ...setup...
	IRQ_ENA4 &= ~IRQ4_SHOCK;  // this is the default, disabled

	for (;;) {
		// ...
		wait_vsync();
		if (IRQ_ACT4 & IRQ4_SHOCK) {
			IRQ_ACT4 = IRQ4_SHOCK;
			// handle shock
		}
	}
}
```

See also: [interrupt][P06i], [registers][P06r]
