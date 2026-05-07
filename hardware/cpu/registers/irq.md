# Interrupt registers

*For more information on using interrupts, see their [main page](../interrupts.md)*

There are primarily three sets of registers which control how interrupt requests are handled by the system: priority, enable flags, and factor flags.

When an interrupt is generated, it sets the relevant factor flag. When the CPU is next able to, it jumps to the vectors for interrupts which are both enabled and have the factor flag set in priority order (excluding any <= the [interrupt flags](../README.md#interrupt-flags)).

Pseudo-code explanation:

```py
to_run = []
for i in interrupts:
	if i.enabled and i.factor:
		to_run.append(i)

# Priority encoder
prioritized = []
for i in to_run:
	if i.priority > SC.i:
		add_sorted(i)

def add_sorted(i):
	global prioritized
	for idx, i2 in enumerate(prioritized):
		if (
			i.priority > i2.priority
			or (
				i.priority == i2.priority
				and i.vector_address < i2.vector_address
			)
		):
			prioritized.insert(idx, i)
			return
	prioritized.append(i)

# Call interrupts
for i in prioritized:
	_int(i.vector_address)
```

[S1C88408]: ../s1c88/408.md
[409]: ../s1c88/409.md
[S1C88649]: ../s1c88/649.md

## Registers

Individual interrupts have both enable (E) and factor (F) registers but are grouped together under a priority (P) register. In the list below, we use x in place of E or F.

### PLCD

$2020 bits 7~6 is a R/W register.

Priority for the [LCD controller interrupts](../interrupts.md#lcd-controller-priority-group).

[S1C88408][]/[409][] contain LCD-related interrupts for which the priority register uses this name.

#### xLCD

$2023 bit 7 (ELCD) and $2027 bit 7 (FLCD) are R/W registers.

[LCD copy complete](../interrupts.md#lcd-copy-complete). FLCD is set to 1 when a frame has finished copying to the LCD.

In other S1C88 chips, FLCD represents the completion of a one-shot data transfer or a hardware auto transfer to the LCD. It's unclear how relevant this concept is to the PM or which one it might use if it is relevant.

#### xLCFR

$2023 bit 6 (ELCFR) and $2027 bit 6 (FLCFR) are R/W registers.

[Frame divider overflow](../interrupts.md#frame-divider-overflow).

This is an unofficial name composed of LC from LCD and FR from [the pin](../../board.md#user-content-lcd-29)'s name which contributes to this interrupt.

### Programmable timer interrupts

Every member of the S1C88 family has programmable timers, at least one pair of which is configurable between acting as one 16-bit timer vs two separate 8-bit timers, but the most similar member is the [S1C88649][].

No other member of the family has three 16-bit programmable timers, but the other possible timers (watchdog, stopwatch, buzzer) don't seem to match up with any of the PM's.

Every member supports underflow interrupts. On ones which do not have compare data support, these interrupts are called xPT0 (where 0 is the 8-bit timer it refers to). Otherwise, they use xTU0 for underflow and xTC0 for compare match.

The chips which support both xTU and xTC registers offer them for every timer, whereas the PM only offers the xTC register for one timer and doesn't offer every xTU register.

#### PPTB

$2020 bits 5~4 is a R/W register.

Priority for the [PTM_B interrupts](../interrupts.md#ptm_b-priority-group).

PT stands for Programmable Timer and the B is taken from the official name [MODE16_B](timers.md).

##### xTU3

$2023 bit 5 (ETU3) and $2027 bit 5 (FTU3) are R/W registers.

[Timer Underflow for PTM3](../interrupts.md#ptm3-underflow).

##### xTU2

$2023 bit 4 (ETU2) and $2027 bit 4 (FTU2) are R/W registers.

[Timer Underflow for PTM2](../interrupts.md#ptm2-underflow).

This interrupt is unavailable when [MODE16_B](timers.md#mode16) is set to 1.

#### PPTA

$2020 bits 3~2 is a R/W register.

Priority for the [PTM_A interrupts](../interrupts.md#ptm_a-priority-group).

PT stands for Programmable Timer and the A is taken from the official name [MODE16_A](timers.md).

##### xTU1

$2023 bit 3 (ETU1) and $2027 bit 3 (FTU1) are R/W registers.

[Timer Underflow for PTM1](../interrupts.md#ptm1-underflow).

##### xTU0

$2023 bit 2 (ETU0) and $2027 bit 2 (FTU0) are R/W registers.

[Timer Underflow for PTM0](../interrupts.md#ptm0-underflow).

This interrupt is unavailable when [MODE16_A](timers.md#mode16) is set to 1.

#### PPTC

$2020 bits 1~0 is a R/W register.

Priority for the [PTM_C interrupts](../interrupts.md#ptm_c-priority-group).

PT stands for Programmable Timer and the C is presumed. No other member of the S1C88 family has three programmable timers, but this timer's register layout and usage doesn't match with the BZ (buzzer) timer nor do any of the timers match with other options (such as the stopwatch timer).

However, it is strange that PM seemingly doesn't have the buzzer/Sound Generator subsystem when every other entry in the family does, so it's still possible that this is some extension on that system in order to make it more like a programmable timer but with segments of the system unmapped like the buzzer frequency.

##### xTU5

$2023 bit 1 (ETU5) and $2027 bit 1 (FTU5) are R/W registers.

[Timer Underflow for PTM5](../interrupts.md#ptm5-underflow).

##### xTC5

$2023 bit 0 (ETC5) and $2027 bit 0 (FTC5) are R/W registers.

[Timer Compare data match for PTM5](../interrupts.md#ptm_c-compare-match).

### PTM

$2021 bits 7~6 is a R/W register.

Priority for the [Clock Timer interrupts](../interrupts.md#clock-timer-priority-group).

In some official documentation these are named xCTM instead of just xTM. The only difference between the two is the order of the enable/factor registers, and PM's matches the xTM order.

Most members of the S1C88 family use the xTM order, but one example is [S1C88649][].

#### xTM32

$2024 bit 5 (ETM32) and $2028 bit 5 (FTM32) are R/W registers.

[32 Hz overflow](../interrupts.md#32hz).

#### xTM8

$2024 bit 4 (ETM8) and $2028 bit 4 (FTM8) are R/W registers.

[8 Hz overflow](../interrupts.md#8hz).

#### xTM2

$2024 bit 3 (ETM2) and $2028 bit 3 (FTM2) are R/W registers.

[2 Hz overflow](../interrupts.md#2hz).

#### xTM1

$2024 bit 2 (ETM1) and $2028 bit 2 (FTM1) are R/W registers.

[1 Hz overflow](../interrupts.md#1hz).

### K port interrupts

The firing of K (input-only) port interrupts can be configured on every S1C88 chip by the KCP registers and, on the [S1C88649][], by the CTK registers.

It's not entirely clear whether or not the PM has the CTK registers, which ones, which inputs they apply to, or what the timings are. This will likely need hardware probing to properly determine.

#### KCP1 / KCP0

Each bit of $2050 (KCP0x) and $2051 bits 1 (KCP11) and 0 (KCP10) are R/W registers.

These are the K port Comparison registers. If set to 1, it detects the falling edge (the respective [KxxD](input.md) bit changing from 1 to 0). If set to 0, it detects the rising edge (that bit moving from 0 to 1).

If KCP11 is set to 0 (the default), then the interrupt fires when the cartridge is ejected. If it's set to 1, then it fires when a cartridge is inserted.

Presumably KCP10 controls the interpretation of the custom cartridge interrupt. KCP10 is set to 0 by default. For official carts, where this pin is completely unconnected, K10D reads 0.

KCP0x configure the comparison for the keypad buttons. In K0xD, a value of 0 indicates the button is being pressed. Thus, a KCP0x value of 0 (the default) fires the interrupt on press and a value of 1 fires it on release.

When the console turns on, the BIOS sets KCP0x to 1 (on press). When the system is suspended via appropriate BIOS calls, it sets KCP0x to 0 (on release) except for KCP07 (power) which it sets to 1.

#### CTK

On the [S1C88649][], these registers control the debounce rate for the input ports, specifically related to firing the interrupt. It does not affect the value in [KxxD](input.md) registers, so it does not affect polling these, though it would affect polling the factor flags.

The values on the [S1C88649][] are as follows:

| Binary | Check time |
| ------ | ---------- |
| 1xx    | 128 msec   |
| 011    | 64 msec    |
| 010    | 16 msec    |
| 001    | 4 msec     |
| 000    | None       |

##### CTK0H

$2054 bits 6~4 is a R/W register.

On the [S1C88649][], this register controls the debounce rate for the inputs K04-K07.

On the PM, this register is never used in any way, by the BIOS or otherwise. It however does act like a R/W register.

##### CTK0L

$2054 bits 3~0 is a R/W register.

On the [S1C88649][], this register controls the debounce rate for the inputs K00-K03.

On the PM, this register is set to 1 by the BIOS in a couple locations. Of special note, the range of inputs (K00-K03) does not include the power button. As such, it's possible this register covers all K00-K07 on the PM, but this has not been confirmed.

##### CTK1L

$2055 bits 3~0 is a R/W register.

This register is not defined on the [S1C88649][], but it is a R/W register on the PM which is used similar to CTK0L in the BIOS, such that we presume if it is a CTK register, it affects K ports 10 and 11.

On the PM, this register is set to 1 by the BIOS in a couple locations.

#### PK1

$2021 bits 5~4 is a R/W register.

Priority for [K ports 10-11](../interrupts.md#cartridge-priority-group). K ports are the input-only ports.

The 1 here refers to "byte 1" (0-based) in terms of K register bytes. The second number, for instance EK10's 0, refers to the bit index within that byte.

##### xK11

$2024 bit 1 (EK11) and $2028 bit 1 (FK11) are R/W registers.

[Cartridge ejected/detected](../interrupts.md#cartridge-ejected).

This interrupt is based on changes in the value of [K11D](input.md#port-11) and whether it's detecting insertion or ejection can be controlled by its polarity register, [KCP11](#kcp1--kcp0).

##### xK10

$2024 bit 0 (EK10) and $2028 bit 0 (FK10) are R/W registers.

[Cartridge interrupt](../interrupts.md#cartridge-irq).

This interrupt is initiated by hardware on the cartridge. The pin is not connected in official cartridges but is something that could theoretically be activated by a flash cart. For more, see [here](input.md#port-10).

#### PK0

$2021 bits 3~2 is a R/W register.

Priority for [K ports 00-07](../interrupts.md#keypad-priority-group). K ports are the input-only ports.

The 0 here refers to "byte 0" in terms of K register bytes. The second number, for instance EK07's 7, refers to the bit index within that byte.

Typically games will poll the K0xD registers instead of relying on interrupts, because the buttons will do different things in different contexts. Since the power button usually only does one thing, the IRQ is often actually hooked up in homebrew, but this is not the case in official games.

##### xK07

$2025 bit 7 (EK07) and $2029 bit 7 (FK07) are R/W registers.

[Power key](../interrupts.md#power-key)

##### xK06

$2025 bit 6 (EK06) and $2029 bit 6 (FK06) are R/W registers.

[Right key](../interrupts.md#right-key)

##### xK05

$2025 bit 5 (EK05) and $2029 bit 5 (FK05) are R/W registers.

[Left key](../interrupts.md#left-key)

##### xK04

$2025 bit 4 (EK04) and $2029 bit 4 (FK04) are R/W registers.

[Down key](../interrupts.md#down-key)

##### xK03

$2025 bit 3 (EK03) and $2029 bit 3 (FK03) are R/W registers.

[Up key](../interrupts.md#up-key)

##### xK02

$2025 bit 2 (EK02) and $2029 bit 2 (FK02) are R/W registers.

[A key](../interrupts.md#a-key)

##### xK01

$2025 bit 1 (EK01) and $2029 bit 1 (FK01) are R/W registers.

[B key](../interrupts.md#b-key)

##### xK00

$2025 bit 0 (EK00) and $2029 bit 0 (FK00) are R/W registers.

[C key](../interrupts.md#c-key)

### PP0

$2022 bits 1~0 is a R/W register.

Priority for [P ports 00-07](../interrupts.md#io-priority-group). P ports are the configurable I/O ports.

No other member of the S1C88 family offers interrupts which are triggered by activity on their configurable I/O ports. It's unknown what method the PM uses to achieve this.

#### xP0

$2026 bit 7 (EP0) and $202A bit 7 (FP0) are R/W registers.

[IR receiver](../interrupts.md#ir-receiver)

#### xP6

$2026 bit 6 (EP6) and $202A bit 6 (FP6) are R/W registers.

[Shock sensor](../interrupts.md#shock-sensor)
