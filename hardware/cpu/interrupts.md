# Interrupt requests

*For software interrupts called by the `INT` operation, find the list [here](./bios.md#software-interrupts)*

Interrupt requests (IRQs), broadly conflated with exceptions, are interruptions to processing which happen in response to some event like timer underflows. After handling the event, the handler is expected to use `RETE` to return the CPU back to what it was doing.

There is some distinction to the terminology:

* Exception: exceptions happen internally to a CPU, like division by 0.
* Interrupts: interrupts are signals generated from outside a CPU, signalling for it to stop and handle this event instead.
* Vector: a vector is the entry in the vector table which describes where the handler for an interrupt is.
* Factor: refers to the flag that says that an interrupt has been triggered.

The S1C88V20 provides up to 32 interrupts and up to 96 software interrupts (for BIOS calls). Out of the 32 interrupts, three are not [maskable](#masking), $00~$02.

## Enabling interrupts

All 29 of the maskable interrupts can be disabled in 3 ways:

1. It can be [masked](#masking).
2. Its [priority](#interrupt-priority) can be set to 0, disabling its whole group.
3. Its enabled bit is 0.

The enabled bits are stored in $2023~$2026 (TODO: link) and will be associated in the list below.

## Masking

The [SC](./README.md#sc-and-cc-registers) register's top two bits, 7~6, limit which exceptions cause interrupts based on their [priority](#interrupt-priority).

| I1~I0 | Enabled |
|:-----:| ------- |
|  11   | NMI     |
|  10   | IRQ3+   |
|  01   | IRQ2+   |
|  00   | IRQ1+   |

When the interrupt triggers, the value of I1~I0 is incremented, preventing the interrupt from continuously triggering. The handler must reset the [factor flag]() so that when SC is reset by `RETE` it's not immediately triggered again.

## Interrupt priority

The 29 maskable interrupts are divided into 9 groups. Each of these groups are then provided a 2 bit priority encoder. These encoders define the order in which exception interrupts are processed. They're processed by priority first, then by the vector address (earlier = higher priority). If an interrupt group is assigned a priority of 0, all the interrupts for the group are implicity disabled.

In the table below, x = does not trigger, o = does trigger. This is the same table as above just a different view.

| Priority | I=11 | I=10 | I=01 | I=00 |
| --------:|:----:|:----:|:----:|:----:|
|       11 |  x   |  o   |  o   |  o   |
|       10 |  x   |  x   |  o   |  o   |
|       01 |  x   |  x   |  x   |  o   |
|       00 |  x   |  x   |  x   |  x   |

## When interrupts occur

Before the processor reads the next opcode, it checks for any interrupt signals sent, sets the appropriate factor flags, then processes the interrupt (if currently allowed).

For the interrupt to trigger its handler, it must be: [enabled](#enabling-interrupts), [unmasked](#masking), and not following an uninterruptible operation. For any time these three things are true while the factor flag is set, the interrupt will trigger. So if the factor flag is not cleared during the handler, it will re-trigger immediately.

Any operation which changes NB or SC is uninterruptible, which means interrupts cannot trigger between that operation and the operation following it.

## Vector table

*For software interrupts called by the `INT` operation, find the list [here](./bios.md#software-interrupts)*

Although they're all interrupts, we make a distinction between hardware interrupts and software interrupts. Hardware interrupts are interrupts triggered in response to requests from the hardware (IRQs) whereas software interrupts are only triggered from software via the `INT` operation.

Listed below are only the hardware interrupts, together with their vector address (in the official BIOS), stub address in software, and associated registers.

Each interrupt's section lists which official games define a non-dummy handler for that interrupt, but official games may also poll the factor flag without enabling the interrupt! These uses are not listed here, but on the [factor flags page](./registers/factor_flags.md).

| `INT [kk]` | Vector | Software | Priority | Enable | Factor | Description                                  |
| ---------- | ------ | -------- | -------- | ------ | ------ | -------------------------------------------- |
| [00h][]    | $009A  | $2102\*  | NMI                      ||| System start-up / System reset               |
| [02h][]    | $00AB  |          | NMI                      ||| Divide by zero ?                             |
| [04h][]    | $00AB  |          | NMI                      ||| Watchdog timer ?                             |
| [06h][]    | $01CF  | $2108    | $20.7~6  | $23.7  | $27.7  | [LCD copy complete][lcdc]                    |
| [08h][]    | $01E0  | $210E    | $20.7~6  | $23.6  | $27.6  | [Frame divider overflow][lcdc]               |
| [0Ah][]    | $01F1  | $2114    | $20.5~4  | $23.5  | $27.5  | [PTM3 underflow][gpt]              |
| [0Ch][]    | $0202  | $211A    | $20.5~4  | $23.4  | $27.4  | [PTM2 underflow (8-bit only)][gpt] |
| [0Eh][]    | $0213  | $2120    | $20.3~2  | $23.3  | $27.3  | [PTM1 underflow][gpt]              |
| [10h][]    | $0224  | $2126    | $20.3~2  | $23.2  | $27.2  | [PTM0 underflow (8-bit only)][gpt] |
| [12h][]    | $0235  | $212C    | $20.1~0  | $23.1  | $27.1  | [PTM5 underflow][gpt3]             |
| [14h][]    | $0246  | $2132    | $20.1~0  | $23.0  | $27.0  | [PTM4-5 compare match][gpt3]                         |
| [16h][]    | $025A  | $2138    | $21.7~6  | $24.5  | $28.5  | [32Hz (from Clock Timer)][clk]               |
| [18h][]    | $026B  | $213E    | $21.7~6  | $24.4  | $28.4  | [8Hz (from Clock Timer)][clk]                |
| [1Ah][]    | $027C  | $2144    | $21.7~6  | $24.3  | $28.3  | [2Hz (from Clock Timer)][clk]                |
| [1Ch][]    | $028D  | $214A    | $21.7~6  | $24.2  | $28.2  | [1Hz (from Clock Timer)][clk]                |
| [1Eh][]    | $029E  | $2150    | $22.1~0  | $26.7  | $2A.7  | [IR receiver][ir]                            |
| [20h][]    | $02AF  | $2156    | $22.1~0  | $26.6  | $2A.6  | [Shock sensor][shock]                        |
| [22h][]    | $00AB  |          |          | $26.5  | $2A.5  | Unused                                       |
| [24h][]    | $00AB  |          |          | $26.4  | $2A.4  | Unused                                       |
| [26h][]    | $043E  |          | $21.5~4  | $24.1  | $28.1  | Cartridge ejected                            |
| [28h][]    | $02C0  | $219E    | $21.5~4  | $24.0  | $28.0  | Cartridge IRQ                                |
| [2Ah][]    | $03BA  | $215C    | $21.3~2  | $25.7  | $29.7  | Power key                                    |
| [2Ch][]    | $02D1  | $2162    | $21.3~2  | $25.6  | $29.6  | Right key                                    |
| [2Eh][]    | $02E2  | $2168    | $21.3~2  | $25.5  | $29.5  | Left key                                     |
| [30h][]    | $02F3  | $216E    | $21.3~2  | $25.4  | $29.4  | Down key                                     |
| [32h][]    | $0304  | $2174    | $21.3~2  | $25.3  | $29.3  | Up key                                       |
| [34h][]    | $0315  | $217A    | $21.3~2  | $25.2  | $29.2  | C key                                        |
| [36h][]    | $0326  | $2180    | $21.3~2  | $25.1  | $29.1  | B key                                        |
| [38h][]    | $0337  | $2186    | $21.3~2  | $25.0  | $29.0  | A key                                        |
| [3Ah][]    | $0348  | $218C    |          | $26.2  | $2A.2  |                                              |
| [3Ch][]    | $035C  | $2192    |          | $26.1  | $2A.1  |                                              |
| [3Eh][]    | $036D  | $2198    |          | $26.0  | $2A.0  |                                              |

\* Getting here can be interrupted if the system is an [official flash cart](../dev_cart.md) or the system has a [low battery](./bios.md#low-battery-check).

[lcdc]: ./lcd_controller.md
[gpt]: ../timers.md#programmable-timers
[gpt3]: ../timers.md#ptm4-5
[clk]: ../timers.md#clock-timer
[ir]: ../ir.md
[shock]: ./io.md#shock
[00h]: #reset
[02h]: #reset
[04h]: #reset
[06h]: #lcd-copy-complete
[08h]: #frame-divider-overflow
[0Ah]: #timer2-upper-8-underflow
[0Ch]: #timer2-lower-8-underflow
[0Eh]: #timer1-upper-8-underflow
[10h]: #timer1-lower-8-underflow
[12h]: #timer3-upper-8-underflow
[14h]: #timer3-pivot
[16h]: #32hz
[18h]: #8hz
[1Ah]: #2hz
[1Ch]: #1hz
[1Eh]: #ir-receiver
[20h]: #shock-sensor
[22h]: #reset
[24h]: #reset
[26h]: #cartridge-ejected
[28h]: #cartridge-irq
[2Ah]: #power-key
[2Ch]: #right-key
[2Eh]: #left-key
[30h]: #down-key
[32h]: #up-key
[34h]: #c-key
[36h]: #b-key
[38h]: #a-key
[3Ah]: #unknown
[3Ch]: #unknown
[3Eh]: #unknown
<!-- Glossary entries pages -->
[overflows]: ../../glossary.md#overflow
[underflows]: ../../glossary.md#underflow
<!-- Game pages -->
[Lunch Time]: ../../software/official/lunch_time.md
[Party]: ../../software/official/party.md
[Pichu Bros]: ../../software/official/pichu_bros.md
[Pinball]: ../../software/official/pinball.md
[Puzzle]: ../../software/official/puzzle.md
[Puzzle 2]: ../../software/official/puzzle2.md
[Race]: ../../software/official/race.md
[Shock Tetris]: ../../software/official/tetris.md
[Sodateyasan]: ../../software/official/sodate.md
[Togepi's Adventure]: ../../software/official/togepi.md
[Zany Cards]: ../../software/official/cards.md

### Reset

00h is a hard reset while any other reset interrupt (02h, 04h, 22h, & 24h) is a soft reset.

00h fires on startup (after battery was removed etc) and goes through the system startup routines. It eventually makes it to $002102 in software if all goes well. For a full explanation of the boot process, see [here](./bios.md#initialization).

00h, 02h, and 04h are [non-maskable](#masking) nor would it even be possible to mask 00h.

It is unclear what 02h, 04h, 22h, and 24h are meant to handle, and it's very possible they're not hooked up on PM.

### LCD Controller priority group

These use the priority specified in $2020 bits 7~6.

#### LCD copy complete

* Enable flag: $2023 bit 7
* Factor flag: $2027 bit 7
* Jumps to: $002108

Fires when the [LCD controller][lcdc] finishes sending a frame to the LCD driver.

Official games which use this interrupt:

* [Lunch Time][]: TODO: why
* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Shock Tetris][]: TODO: why
* [Zany Cards][]: TODO: why

#### Frame divider overflow

* Enable flag: $2023 bit 6
* Factor flag: $2027 bit 6
* Jumps to: $00210E

Every refresh (1Hz) of the LCD, the frame counter ($2081 bits 7~4) increments by 1. When this [overflows][], this IRQ fires.

Official games which use this interrupt:

* [Pinball][]: TODO: why
* [Puzzle][]: TODO: why
* [Puzzle 2][]: TODO: why
* [Race][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why

### PTM2-3 priority group

These use the priority specified in $2020 bits 5~4.

#### PTM3 underflow

* Enable flag: $2023 bit 5
* Factor flag: $2027 bit 5
* Jumps to: $002114

Fires when the PTM3 counter ($203F) [underflows][], both in 8-bit mode and 16-bit mode.

Official games which use this interrupt:

* [Lunch Time][]: TODO: why
* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Pinball][]: TODO: why
* [Puzzle][]: TODO: why
* [Puzzle 2][]: TODO: why
* [Race][]: TODO: why
* [Shock Tetris][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why
* [Zany Cards][]: TODO: why

#### PTM2 underflow

* Enable flag: $2023 bit 4
* Factor flag: $2027 bit 4
* Jumps to: $00211A

Fires when the PTM2 counter ($203E) [underflows][] *only* in 8-bit mode.

Official games which use this interrupt:

### PTM0-1 priority group

These use the priority specified in $2020 bits 3~2.

#### PTM1 underflow

* Enable flag: $2023 bit 3
* Factor flag: $2027 bit 3
* Jumps to: $002120

Fires when the PTM1 counter ($2037) [underflows][], both in 8-bit mode and 16-bit mode.

Official games which use this interrupt:

* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Sodateyasan][]: TODO: why

#### PTM0 underflow

* Enable flag: $2023 bit 2
* Factor flag: $2027 bit 2
* Jumps to: $002126

Fires when the PTM0 counter ($2036) [underflows][] *only* in 8-bit mode.

Official games which use this interrupt:

* [Party][]: TODO: why
* [Puzzle][]: TODO: why
* [Puzzle 2][]: TODO: why
* [Race][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why

### PTM4-5 priority group

These use the priority specified in $2020 bits 1~0.

There is no underflow interupt for PTM4.

#### PTM5 underflow

* Enable flag: $2023 bit 1
* Factor flag: $2027 bit 1
* Jumps to: $00212C

Fires when the PTM5 counter ($204F) [underflows][], both in 8-bit mode and 16-bit mode.

Official games which use this interrupt:

* [Lunch Time][]: TODO: why
* [Party][]: TODO: why
* [Pinball][]: TODO: why
* [Puzzle][]: TODO: why
* [Puzzle 2][]: TODO: why
* [Race][]: TODO: why
* [Shock Tetris][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why

#### PTM4-5 compare match

* Enable flag: $2023 bit 0
* Factor flag: $2027 bit 0
* Jumps to: $002132

In 16-bit mode, fires when PTM4-5 counters ($204F~$204E) matches the compare data registers ($204D~$204C). If <abbr title="compare data register">CDR</abbr> = 0, no audio signal will be output on match (TODO: verify for PM).

In 8-bit mode, fires when PTM5 counter ($204F) matches its compare data register ($204D) (TODO: confirm).

For more information on using these registers for audio, see [here](./sound.md). This interrupt typically isn't used for producing audio, itself.

Official games which use this interrupt:

### Clock timer priority group

These use the priority specified in $2021 bits 7~6.

The count value for this timer is stored in the <abbr title="[clock] timer data">TMD</abbr> register, $2041. The timer counts up, which corresponds to each bit in the register being 0 at some frequency, listed in the table below. When this happens to bits 2, 4, 6, or 7, an interrupt is generated.

The entire value [overflows][] once per second (hence 1 Hz), making this timer and its interrupts ideal for updating clocks.

|Bits:|  7  |  6  |  5  |  4  |  3  |  2  |  1  |  0  |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Hz: |  1  |  2  |  4  |  8  | 16  | 32  | 64  | 128 |

#### 32Hz

* Enable flag: $2024 bit 5
* Factor flag: $2028 bit 5
* Jumps to: $002138

Official games which use this interrupt:

* [Lunch Time][]: TODO: why
* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Pinball][]: TODO: why
* [Puzzle][]: TODO: why
* [Puzzle 2][]: TODO: why
* [Race][]: TODO: why
* [Shock Tetris][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why
* [Zany Cards][]: TODO: why

#### 8Hz

* Enable flag: $2024 bit 4
* Factor flag: $2028 bit 4
* Jumps to: $00213E

Official games which use this interrupt:

#### 2Hz

* Enable flag: $2024 bit 3
* Factor flag: $2028 bit 3
* Jumps to: $002144

Official games which use this interrupt:

#### 1Hz

* Enable flag: $2024 bit 2
* Factor flag: $2028 bit 2
* Jumps to: $00214A

Official games which use this interrupt:

### I/O priority group

These use the priority specified in $2022 bits 1~0.

#### IR receiver

* Enable flag: $2026 bit 7
* Factor flag: $202A bit 7
* Jumps to: $002150

Official games which use this interrupt:

* [Lunch Time][]: TODO: why
* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Shock Tetris][]: TODO: why
* [Zany Cards][]: TODO: why

#### Shock sensor

* Enable flag: $2026 bit 6
* Factor flag: $202A bit 6
* Jumps to: $002156

Official games which use this interrupt:

* [Race][]: TODO: why
* [Sodateyasan][]: TODO: why
* [Togepi's Adventure][]: TODO: why

### Cartridge priority group

These use the priority specified in $2021 bits 5~4.

#### Cartridge ejected

* Enable flag: $2024 bit 1
* Factor flag: $2028 bit 1

The polarity of this interrupt is configurable. If $2051 bit 1 is set to 0 (the default) then this detects the cartridge being ejected. If it's set to 1, then this detects the cartridge being inserted.

Despite being able to be configured for detecting insertion, it doesn't have an option for jumping to a software handler, however it can [jump to RAM](#waking-up) so that can be configured to do so.

#### Cartridge IRQ

* Enable flag: $2024 bit 0
* Factor flag: $2028 bit 0
* Jumps to: $00219E

This is an interrupt the cartridge can send (TODO: how?). No official cartridge is equipped for this.

Official games which use this interrupt:

### Keypad priority group

These use the priority specified in $2021 bits 3~2.

#### Power key

* Enable flag: $2025 bit 7
* Factor flag: $2029 bit 7
* Jumps to: $00215C

Official games which use this interrupt:

* [Party][]: TODO: why
* [Pichu Bros][]: TODO: why
* [Sodateyasan][]: TODO: why

#### Right key

* Enable flag: $2025 bit 6
* Factor flag: $2029 bit 6
* Jumps to: $002162

Official games which use this interrupt:

#### Left key

* Enable flag: $2025 bit 5
* Factor flag: $2029 bit 5
* Jumps to: $002168

Official games which use this interrupt:

#### Down key

* Enable flag: $2025 bit 4
* Factor flag: $2029 bit 4
* Jumps to: $00216E

Official games which use this interrupt:

#### Up key

* Enable flag: $2025 bit 3
* Factor flag: $2029 bit 3
* Jumps to: $002174

Official games which use this interrupt:

#### C key

* Enable flag: $2025 bit 2
* Factor flag: $2029 bit 2
* Jumps to: $00217A

Official games which use this interrupt:

#### B key

* Enable flag: $2025 bit 1
* Factor flag: $2029 bit 1
* Jumps to: $002180

Official games which use this interrupt:

* [Sodateyasan][]: TODO: why

#### A key

* Enable flag: $2025 bit 0
* Factor flag: $2029 bit 0
* Jumps to: $002186

Official games which use this interrupt:

### Unknown

The priority bits are unconfirmed as the method to trigger these interrupts is unknown.

* Enable flag: $2026 bit 2~0
* Factor flag: $202A bit 2~0
* Jumps to: $00218C, $002192, $002198

No official games use these interrupts. Some NOP/00 these, some have dummy handlers.

## Waking up

All interrupts besides [power key][2Ah] and [cartridge eject][26h] have essentially the same code:

```s1c88
_some_irq:
	PUSH EP
	PUSH BR
	LD EP, #00h
	LD BR, #20h
	BIT [BR:01h], #20h    ; if console is asleep,
	CARS Z, wake_from_irq ; wake it up
	POP BR
	POP EP
	JRL (software handler address)
```

The power key and cartridge eject IRQs still have similar code for waking up, but they don't use [wake_from_irq][].

$2001 bit 5 can be reset, causing this path to be followed, under the following conditions:

* during halt_cpu, which is called by TODO
* by [5Ch](./bios.md#5ch), if $2001 bit 7 is 0
* by [64h](./bios.md#64h), if $2001 bit 7 is 0

and can be set under the following conditions:

* soft reset
* during this wake up, if $2001 bit 7 is 0
* waking up by the power button, if $2001 bit 7 is 0
* by [5Eh](./bios.md#5eh), if $2001 bit 6 is 1
* by [66h](./bios.md#66h), if $2001 bit 7~6 is 0b10

Pseudocode of the routines (for the real code see [wake_from_irq][], [_key_power_irq][], and [_cart_eject_irq][]):
```py
def wake_from_irq():
	if cpu.osc == OSC1:
		with suppress_interrupts():
			enter_high_speed_operation()
	if not cartridge.powered and reg[0x02] & 0x40:
		with suppress_interrupts():
			power_cart()
			if reg[0x01] & 0x40:
				prepare_selected_game()
	if reg[0x01] & 0x80:
		skip_remainder_of_parent()
		return jump(0x1FFD)  # last 3 bytes of RAM
	with suppress_interrupts():
		prepare_selected_game()
		console.awake = True
	return

def _key_power_irq():
	if not console.awake:
		if reg[0x01] & 0x10:
			return jump(_reset2)
		# same as in wake_from_irq
		if cpu.osc == OSC1:
			with suppress_interrupts():
				enter_high_speed_operation()
		if not cartridge.powered and reg[0x02] & 0x40:
			with suppress_interrupts():
				power_cart()
				if reg[0x01] & 0x40:
					prepare_selected_game()
		# differs
		if reg[0x01] & 0x80 and not reg[0x02] & 0x20:
			return jump(0x1FFD)  # last 3 bytes of RAM
		if not reg[0x01] & 0x80:
			# same as in wake_from_irq
			with suppress_interrupts():
				prepare_selected_game()
				console.awake = True
		if reg[0x02] & 0x20:
			factor.power_key.clear()
			return
	return jump(0x215C)  # software handler

def _cart_eject_irq():
	if console.awake or reg[0x01] & 0x10:
		return jump(_reset2)
	if cpu.osc == OSC1:
		with suppress_interrupts():
			enter_high_speed_operation()
	if not reg[0x01] & 0x80 or reg[0x01] & 0x40:
		return jump(_shutdown)
	if not cartridge.powered and reg[0x02] & 0x40:
		with suppress_interrupts():
			power_cart()
	return jump(0x1FFD)  # last 3 bytes of RAM
```

These routines indicate that when $2001 bit 7 is 1, there should be a [JRL](S1C88_InstructionSet.md#jrl-relative-long-jump), which is exactly 3 bytes, at $1FFD to another location in RAM which has code that can, for instance, check if another cartridge has been inserted and/or do something when one is.

[wake_from_irq]: ../../software/bios/disasm.md#user-content-wake_from_irq
[_key_power_irq]: ../../software/bios/disasm.md#user-content-_key_power_irq
[_cart_eject_irq]: ../../software/bios/disasm.md#user-content-_cart_eject_irq
