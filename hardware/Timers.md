# Timers & Oscillators

- [Oscillators][]
  - [OSC1][]
    - [OSC1 specs][]
  - [OSC3][]
    - [OSC3 specs][]
- [Seconds Timer][]
- [Clock Timer][]
- [Programmable timers][]
  - [Programmable timer configuration][]
  - [Programmable timer interrupts][]

[Oscillators]: #oscillators
[OSC1]: #osc1
[OSC1 specs]: #osc1-specs
[OSC3]: #osc3
[OSC3 specs]: #osc3-specs
[Seconds Timer]: #seconds-timer
[Clock Timer]: #clock-timer
[Programmable timers]: #programmable-timers
[Programmable timer configuration]: #programmable-timer-configuration
[Programmable timer interrupts]: #programmable-timer-interrupts

[sleep]: Standby.md#sleep

## Oscillators

There are two oscillators on the board (external to the CPU) named OSC1 and OSC3.

### OSC1

This is a low-power 32.768 kHz crystal resonator (passive oscillator) notably used for maintaining the real-time clock, but is also used elsewhere. There is no way to disable this oscillator outside of putting the system into [sleep][] mode.

This oscillator is labeled `Y1` on the circuit board and it does have text but it may not be visible; it's an engraved text `KDS` followed by a number representing the final digit of the year it was printed in then a letter representing the month (A for January up to M for December). It's not a surface-mount component, but is glued down.

In previous documentation and code, this oscillator was once known in the community as "oscillator 2".

#### OSC1 specs

* Part number: [DT-26](https://www.kds.info/product/dt-26/) ([datasheet](https://datasheet.lcsc.com/lcsc/1811121541_KDS-Daishinku-DT-26-32.768K-6pF-20PPM_C127496.pdf))
  * D - Daishinku Corp (company name)
  * T - Tuning fork crystal resonator
  * 2 - 2 mm diameter
  * 6 - 6 mm height
* Load Capacitance: unconfirmed
* Drive Level: 1.0μW (2.0μW max.)
* Frequency Tolerance: ±20 ppm max. (at 25℃)
* Series Resistance: unconfirmed
* Turnover Temperature: +25℃±5℃
* Parabolic Coefficient: -0.04 ppm/℃² max.
* Operating Temperature Range: -10 to +60℃
* Storage Temperature Range: -20 to +70℃
* Shunt Capacitance: 1.1pF typ.
* Aging: ±5 ppm/year

### OSC3

This is the high-speed 4.00 MHz ceramic resonator (passive oscillator) used for the general purpose timers. It can be disabled by writing a 0 to the OSCC register and is also disabled when the system enters [sleep][] mode.

This oscillator is labeled `Y2` on the circuit board and has text printed on the top which looks like a curved M in a box followed by `4.00` and then a single-character serial such as `L` or `J`. It is a surface-mount component.

Disabling this oscillator when not needed can save power. You can also adjust the speed this runs at by writing to register VD1C according to the following table:

| VD1C1 | VD1C0 | Operating voltage | Oscillation        |
|:-----:|:-----:| ----------------- | ------------------ |
|   1   |  1/0  | 3.2 V             | 0.03~8.2 MHz       |
|   0   |   1   | 1.6 V             | 0.03~1.1 MHz / off |
|   0   |   0   | 2.4 V             | 0.03~4.4 MHz       |

When switching voltages you cannot jump directly between 1.6 V and 3.2 V safely and you must wait some time after switching. See the VD1C register details for usage information. Note that the BIOS will switch between 1.6 V and 2.4 V during some operations.

In previous documentation and code, this oscillator was once known in the community as "oscillator 1".

#### OSC3 specs

These specs are unfortunately from the 2009 datasheet, when ideally we would like a 2001 datasheet.

* Part number: [EFOS4004E5](https://www.digikey.com/en/products/detail/panasonic-electronic-components/EFO-S4004E5/160457) ([datasheet](https://media.digikey.com/pdf/Data%20Sheets/Panasonic%20Capacitors%20PDFs/EFO_3Array.pdf))
  * EFO - Ceramic resonator
  * S - 2 to 13 MHz type with built-in capacitors and 3 terminals
  * 4004 - 4.00 MHz nominal oscillation frequency
  * E - Embossed taping style packaging
  * 5 - ±0.5% frequency tolerance
* Built-in Capacitors: 33 pF
* Oscillation frequency drift: ±0.2% overall stability
  * -20°C ≈ -0.1
  * 20°C ≈ 0.0
  * 40°C ≈ 0.02
  * 60°C ≈ 0.0
  * 80°C ≈ -0.04

## Seconds Timer

A timer which increments once every second. It uses [OSC1][] as its clock source.

This timer informs the real-time clock (RTC) in commercial games. As such, if homebrew resets or pauses the timer or sleeps the console (TODO?), it will force commercial games to ask for the user to enter the time again.

* Write 0 to STRUN to pause this timer or 1 to start it.
  * When reading, 0 means paused and 1 means running.
  * In pm.h, STRST is bit 0 of SEC_CTRL
* Write 1 to STRST to reset this timer.
  * In pm.h, STRST is bit 1 of SEC_CTRL
* Read the count from the STD register
  * In pm.h, STD is called SEC_CNT

There are no interrupts related to this timer.

## Clock Timer

A timer which increments 256 times per second. It uses [OSC1][] as its clock source.

* Write 0 to TMRUN to pause this timer or 1 to start it.
  * When reading, 0 means paused and 1 means running.
  * In pm.h, TMRUN is bit 0 of TMR256_CTRL
* Write 1 to TMRST to reset this timer.
  * In pm.h, TMRST is bit 1 of TMR256_CTRL
* Read the count from the TMD register
  * The individual bits decompose into different counts for different Hz. That is, each bit increments at a different Hz by nature of the whole byte incrementing 256 times per second.
    * TMD7 - overflows every 1 Hz, increments every 2 Hz
    * TMD6 - overflows every 2 Hz, increments every 4 Hz
    * TMD5 - overflows every 4 Hz, increments every 8 Hz
    * TMD4 - overflows every 8 Hz, increments every 16 Hz
    * TMD3 - overflows every 16 Hz, increments every 32 Hz
    * TMD2 - overflows every 32 Hz, increments every 64 Hz
    * TMD1 - overflows every 64 Hz, increments every 128 Hz
    * TMD0 - overflows every 128 Hz, increments every 256 Hz
  * In pm.h, TMD is called TMR256_CNT

There are four interrupts tripped by this timer at different Hz.

* Clock timer 1 Hz interrupt
  * Triggers every second, when TMD7 overflows.
  * Write 1 to ECTM1 to enable, 0 to disable.
    * When reading, 1 means enabled and 0 means disabled.
    * With pm.h, use `IRQ_ENA2 |= IRQ2_1HZ;` to enable, `IRQ_ENA2 &= ~IRQ2_1HZ;` to disable.
  * Write 1 to FCTM1 to reset the activation.
    * When reading, 1 means the interrupt is active (ready to trigger), 0 otherwise.
    * With pm.h, use `IRQ_ACT2 |= IRQ2_1HZ;` to reset, use `IRQ_ACT2 & IRQ2_1HZ` as a boolean to read.
* Clock timer 2 Hz interrupt
  * Triggers every 500 ms, when TMD6 overflows.
  * Registers are: ECTM2, FCTM2, and IRQ2_2HZ in pm.h
* Clock timer 8 Hz interrupt
  * Triggers every 125 ms, when TMD4 overflows.
  * Registers are: ECTM8, FCTM8, and IRQ2_8HZ in pm.h
* Clock timer 32 Hz interrupt
  * Triggers every 31250 µs, when TMD2 overflows.
  * Registers are: ECTM32, FCTM32, and IRQ2_32HZ in pm.h
* Write to PCTM to set the priority for all clock timer interrupts.
  * You can read out the current priority as well.
  * With pm.h, use `IRQ_PRI2 &= ~PRI2_TIM256(3);` to clear it then `IRQ_PRI2 |= PRI2_TIM256(x);` to set the new priority, where x can be 0-3 (0 = disabled).
    * When setting priorities in initial setup, you don't need to clear anything and can instead use `IRQ_PRI2 = PRI2_TIM256(x) | ...;` where `...` is anything else that needs to be set in IRQ_PRI2.

In previous documentation and code, this timer was once known in the community as the "256Hz Timer".

## Programmable timers

The Pokémon mini offers 3 pairs of general purpose programmable timers. Each set can independently be used either as a single 16-bit timer or split into two 8-bit channels with their own interrupts. These timers count down at a configurable rate.

Each of the 6 8-bit timers can individually be configured to use either OSC1 or OSC3 as its source clock. When using a pair as a 16-bit timer, it uses the clock source of the first member of the pair (for example, PTM0) and the interupt of the second member (for example, PTM1).

In previous documentation, these timers were known as the "general purpose timers", which is still an acceptable name, but this documentation will use "programmable timers" or PTs.

### PTM0-1

16-bit timer comprised of PTM0 as the lower order 8 bits and PTM1 as the higher order 8 bits. That is, `PTM1:PTM0` or given PTM1 is 0x10 and PTM0 is 0xf3, the value is 0x10f3.

In previous documentation and code, this timer has been known in the community as the "timer 1".

### PTM2-3

16-bit timer comprised of PTM2 as the lower order 8 bits and PTM3 as the higher order 8 bits. That is, `PTM3:PTM2` or given PTM3 is 0x10 and PTM2 is 0xf3, the value is 0x10f3.

In previous documentation and code, this timer has been known in the community as the "timer 2".

### PTM4-5

16-bit timer comprised of PTM4 as the lower order 8 bits and PTM5 as the higher order 8 bits. That is, `PTM5:PTM4` or given PTM5 is 0x10 and PTM4 is 0xf3, the value is 0x10f3.

In previous documentation and code, this timer has been known in the community as the "timer 3".

### Programmable timer configuration

When choosing which timer to use for some purpose, you must choose whether to use some pair as a 16-bit timer or to split it and use one of the 8-bit timers. To use the 16-bit timer, write a 1 to the respective MODE16 register (see table below) and to use one of the 8-bit timers, write a 0 to it (this is the initial value).

| Register | pm.h        | Timer L | Timer H | Timer 16 |
| -------- | ----------- | ------- | ------- | -------- |
| MODE16_A | TMR1_CTRL_L | PTM0    | PTM1    | PTM0-1   |
| MODE16_B | TMR2_CTRL_L | PTM2    | PTM3    | PTM2-3   |
| MODE16_C | TMR3_CTRL_L | PTM4    | PTM5    | PTM4-5   |

To set MODE16 with pm.h, use, for example, `TMR1_CTRL_L |= 0x80;`
To unset MODE16 with pm.h, use, for example, `TMR1_CTRL_L &= ~0x80;`

Before you first enable a timer, you'll want to configure its basic settings. Set the clock source via PRTF*x* where *x* is the timer index. Write a 1 to use [OSC1][] and a 0 to use [OSC3][]. You likely won't change this again unless you intend to repurpose the timer. To make this selection, refer the table below.

| For timer(s)  | Use OSC1         | Use OSC3          |
| ------------- | ---------------- | ----------------- |
| PTM0 & PTM0-1 | `TMR1_OSC |= 1;` | `TMR1_OSC &= ~1;` |
| PTM1          | `TMR1_OSC |= 2;` | `TMR1_OSC &= ~2;` |
| PTM2 & PTM2-3 | `TMR2_OSC |= 1;` | `TMR2_OSC &= ~1;` |
| PTM3          | `TMR2_OSC |= 2;` | `TMR2_OSC &= ~2;` |
| PTM4 & PTM4-5 | `TMR3_OSC |= 1;` | `TMR3_OSC &= ~1;` |
| PTM5          | `TMR3_OSC |= 2;` | `TMR3_OSC &= ~2;` |

After this you configure the division ratio (prescale), reload data (preset), and compare data (pivot). This can be changed regularly while the timer is running in order to adjust when some overflow occurs.

The prescale along with the clock source determines how quickly the counter decrements. Refer to the table below:

| Prescale | fOSC1 / div = Hz    | OSC3 / div = Hz      |
| -------- | ------------------- | -------------------- |
| 0        | 32768 / 1   = 32768 | 4M / 2    = 2M       |
| 1        | 32768 / 2   = 16384 | 4M / 8    = 500k     |
| 2        | 32768 / 4   = 8192  | 4M / 32   = 125k     |
| 3        | 32768 / 8   = 4096  | 4M / 64   = 62500    |
| 4        | 32768 / 16  = 2048  | 4M / 128  = 31250    |
| 5        | 32768 / 32  = 1024  | 4M / 256  = 15625    |
| 6        | 32768 / 64  = 512   | 4M / 1024 = 3906.25  |
| 7        | 32768 / 128 = 256   | 4M / 4096 = 976.5625 |

When a timer underflows, it loads the preset into the counter as the starting value to count down from. It can also be reset to this value manually by writing a 1 to PSET*x* where *x* is the timer index.

When the pivot is matched, a compare match interrupt is triggered but the timer is not reset at that point. On matching PTM4-5 (TODO: or just PTM5?), an output signal is sent to the speaker.

The table below lists the timers and which registers control these three values. The use of a colon between two registers indicates the values are concatenated together such that `0x10:0xa5` would become `0x10a5`. The register using the timer's name (for example, PTM0) is the data register which contains the count value for reading; for the 16-bit timers this is `PTMy:PTMx` for any `PTMx-y`.

| Timer  | Prescale | Preset    | Pivot     |
| ------ | -------- | --------- | --------- |
| PTM0   | PST0     | RDR0      | CDR0      |
| PTM1   | PST1     | RDR1      | CDR1      |
| PTM2   | PST2     | RDR2      | CDR2      |
| PTM3   | PST3     | RDR3      | CDR3      |
| PTM4   | PST4     | RDR4      | CDR4      |
| PTM5   | PST5     | RDR5      | CDR5      |
| PTM0-1 | PST0     | RDR1:RDR0 | CDR1:CDR0 |
| PTM2-3 | PST2     | RDR3:RDR2 | CDR3:CDR2 |
| PTM4-5 | PST4     | RDR5:RDR4 | CDR5:CDR4 |

With pm.h:

| Timer  | Prescale   | Preset     | Pivot      | Data       |
| ------ | ---------- | ---------- | ---------- | ---------- |
| PTM0   | TMR1_SCALE | TMR1_PRE_L | TMR1_PVT_L | TMR1_CNT_L |
| PTM1   | TMR1_SCALE | TMR1_PRE_H | TMR1_PVT_H | TMR1_CNT_H |
| PTM2   | TMR2_SCALE | TMR2_PRE_L | TMR2_PVT_L | TMR2_CNT_L |
| PTM3   | TMR2_SCALE | TMR2_PRE_H | TMR2_PVT_H | TMR2_CNT_H |
| PTM4   | TMR3_SCALE | TMR3_PRE_L | TMR3_PVT_L | TMR3_CNT_L |
| PTM5   | TMR3_SCALE | TMR3_PRE_H | TMR3_PVT_H | TMR3_CNT_H |
| PTM0-1 | TMR1_SCALE | TMR1_PRE   | TMR1_PVT   | TMR1_CNT   |
| PTM2-3 | TMR2_SCALE | TMR2_PRE   | TMR2_PVT   | TMR2_CNT   |
| PTM4-5 | TMR3_SCALE | TMR3_PRE   | TMR3_PVT   | TMR3_CNT   |

The scale registers are constructed as `PRPRTy:PSTy:PRPRTx:PSTx` where each PST register is 3 bits and y = x + 1. This means that in order to set the prescale for PTM0 you must do `TMR1_SCALE &= ~0x07;` to clear then `TMR1_SCALE |= prescale;` to assign it. For PTM1 you must do `TMR1_SCALE &= ~0x70;` to clear then `TMR1_SCALE |= prescale << 4;` to assign it. They are initialized to 0 so there's no need to clear it in startup code. PRPRT registers should always be set to 1.

### Programmable timer interrupts

There are two interrupts for each timer: the underflow and the compare data interrupts. Underflow occurs the tick after a count reaches 0, causing it to preset. The compare data interrupt occurs when the count is equal to the value stored in the relevant CDR register.

Although all of these interrupts exist and can be accessed by reading the count or factor flag directely, not all of them are mapped to ROM locations (that is, there's no means to make them jump to software code automatically).

| Timer interrupt  | Factor | Enable | Priority | Software entry address |
| ---------------- | ------ | ------ | -------- | ---------------------- |
| PTM0 underflow   | FTU0   | ETU0   | PPT0-1   | $2126                  |
| PTM0 CDR match   | FTC0   | ETC0   | n/a      | n/a                    |
| PTM1 underflow   | FTU1   | ETU1   | PPT0-1   | $2120                  |
| PTM1 CDR match   | FTC1   | ETC1   | n/a      | n/a                    |
| PTM2 underflow   | FTU2   | ETU2   | PPT2-3   | $211a                  |
| PTM2 CDR match   | FTC2   | ETC2   | n/a      | n/a                    |
| PTM3 underflow   | FTU3   | ETU3   | PPT2-3   | $2114                  |
| PTM3 CDR match   | FTC3   | ETC3   | n/a      | n/a                    |
| PTM4 underflow   | FTU4   | ETU4   | n/a      | n/a                    |
| PTM4 CDR match   | FTC4   | ETC4   | n/a      | n/a                    |
| PTM5 underflow   | FTU5   | ETU5   | PPT4-5   | $212c                  |
| PTM5 CDR match   | FTC5   | ETC5   | PPT4-5   | $2132                  |
| PTM0-1 underflow | FTU1   | ETU1   | PPT0-1   | $2120                  |
| PTM0-1 CDR match | FTC1   | ETC1   | n/a      | n/a                    |
| PTM2-3 underflow | FTU3   | ETU3   | PPT2-3   | $2114                  |
| PTM2-3 CDR match | FTC3   | ETC3   | n/a      | n/a                    |
| PTM4-5 underflow | FTU5   | ETU5   | PPT4-5   | $212c                  |
| PTM4-5 CDR match | FTC5   | ETC5   | PPT4-5   | $2132                  |

For more information about how interrupts work, see [Interrupts](cpu/Interrupts.md).
For information on using PTM4-5 for audio, see [Audio / Sound](cpu/Sound.md).

### Enabling and pausing programmable timers

In order to turn a timer on, the following must be done, where x is some timer index (use 0 for PTM0-1, etc):

* CKSEL*x* should already be set to 0 by default, do not change it
* Set PRPRT*x* register to 1
* Set PTRUN*x* register to 1

To pause the timer, reset PTRUN*x* register to 0. The timer will decrement once more before pausing.
To resume the timer, set PTRUN*x* register back to 1.
To preset the timer count, write 1 to PSET*x*.

When using the HALT operation, the timers are not paused. When using the SLP operation, the timers will be paused and will resume from where they left off when the console reawakens.
