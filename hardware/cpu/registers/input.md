# Input-only ports (K ports)

The PM offers 10 bits of K ports stored over two bytes. The first byte contains all the button inputs while the second contains inputs from the cartridge bus.

Although things like shock and IR can be thought of as inputs, they're instead located among the [configurable I/O ports](io.md).

All ports use the following registers where xx is the port number:

* KxxD - data port, represents the data on the port
* KCPxx - comparison register, determines on which edge to fire the respective interrupt
* EKxx - enable interrupt register
* FKxx - factor flag

The priority `PKx` and check time setup `CTKx` registers are done in groups. While priority is grouped by byte, the CTK grouping is currently unknown.

## Keypad ports

| Port   | Button |
| ------ | ------ |
| [07][] | Power  |
| [06][] | Right  |
| [05][] | Left   |
| [04][] | Down   |
| [03][] | Up     |
| [02][] | A      |
| [01][] | B      |
| [00][] | C      |

All keypad ports work the same.

K0xD ($2052) registers are read-only. When a pin is low (a value of 0), it indicates the button is being pressed.

Thus when KCP0x is 1 (the default), it detects the falling edge of a change in this value, which indicates the button was pressed. Resetting KCP0x to 0 detects the rising edge, which indicates the button was released.

Likely as part of [MINLIB](../../../software/minlib.md), most games have a method which stores the keypad data to RAM which they poll in order to check for player input. The method looks something like this:

```s1c88
; Store current keypad state in KeyPad
; Shutdown system if the power key was pressed
; Return newly pressed keys in A
get_keypad:
	PUSH BA
	LD [BR:27h], #80h          ; clear Frame Copy Complete
gkp__wait_for_vsync:
	BIT [BR:27h], #80h         ; wait for Frame Copy Complete to trigger
	JRS Z, gkp__wait_for_vsync
	LD B, [BR:52h]             ; read current keymap state
	CPL B                      ; invert so 1 is pressed
	LD A, [KeyPad]             ; load previous keymap state
	LD [KeyPad], B             ; write current keymap state
	XOR A, B                   ; only keep those which became pressed this frame
	AND A, B                   ; ...
	BIT A, #80h                ; check if the power key was just pressed
	JRS Z, gkp__return
	INT [48h]                  ; if so, call shutdown routine
gkp__return:
	POP BA
	RET
```

[00]: #port-00
[01]: #port-01
[02]: #port-02
[03]: #port-03
[04]: #port-04
[05]: #port-05
[06]: #port-06
[07]: #port-07

### Port 00

This port reflects the input from the [C button](../../board.md#sw1). When this pin is low, it indicates the button is being pressed.

The C input is often polled (indirectly) to open a pause menu during gameplay.

### Port 01

This port reflects the input from the [B contact](../../board.md#b). When this pin is low, it indicates the button is being pressed.

The B input is often polled (indirectly) for use as a back button in menus or otherwise as a normal gameplay button.

### Port 02

This port reflects the input from the [A contact](../../board.md#a). When this pin is low, it indicates the button is being pressed. It also connects to the TP1(A) test point near the negative battery terminal.

The A input is often polled (indirectly) for use as a select button in menus or otherwise as the primary gameplay button.

### Port 03

This port reflects the input from the [UP contact](../../board.md#up). When this pin is low, it indicates the button is being pressed.

### Port 04

This port reflects the input from the [DOWN contact](../../board.md#down). When this pin is low, it indicates the button is being pressed.

### Port 05

This port reflects the input from the [LEFT contact](../../board.md#left). When this pin is low, it indicates the button is being pressed.

### Port 06

This port reflects the input from the [RIGHT contact](../../board.md#right). When this pin is low, it indicates the button is being pressed.

### Port 07

This port reflects the input from the [POWER contact](../../board.md#power). When this pin is low, it indicates the button is being pressed.

In official games, the power interrupt is not used, and the power button is instead polled similarly to the other keypad inputs. Commonly, a game will call the suspend routine ([42h](../bios.md#suspend-system)) during gameplay and otherwise call the shutdown routine ([48h](../bios.md#shutdown-system)).

## Cartridge ports

### Port 10

This port reflects the input from [pin A14](../../board.md#user-content-a14) of the cartidge bus. This pin is normally low, but hardware on a flash cart could cause it to go high which would trigger the [cartridge interrupt](../interrupts.md#cartridge-irq).

Although KCP10 likely controls on what edge the IRQ fires, it hasn't been confirmed, and there's little reason to detect a falling edge.

### Port 11

This port reflects the input from [pin B16](../../board.md#user-content-b16) of the cartidge bus. When this pin is low, it indicates the presence of a cartidge.

Thus when KCP11 is 0 (the default), it detects the rising edge of a change in this value, which indicates the cartridge was ejected. Setting KCP11 to 1 detects the falling edge, which indicates the cartridge was inserted.
