# Timers & Oscillators

- [Seconds Timer](#seconds-timer)
- [Clock Timer](#clock-timer)
- [General Purpose Timers](#general-purpose-timers)

## Oscillators

There are two oscillators on the board (external to the CPU) named OSC1 and OSC3.

### OSC1

This is a low-power 32768 Hz oscillator notably used for maintaining the real-time clock, but is also used elsewhere. There is no way to disable this oscillator outside of putting the system into [sleep](Standby.md#sleep) mode.

This oscillator is labeled `Y1` on the circuit board but does not have any text visible on the component itself. It's not a surface-mount component.

In previous documentation and code, this oscillator was once known in the community as "oscillator 2".

Things left to discover:

* Part number
* Accuracy
* Confirm that it's crystal

### OSC3

This is the high-speed 4.00 MHz ceramic oscillator used for the general purpose timers. It can be disabled by writing a 0 to the OSCC register and is also disabled when the system enters [sleep](Standby.md#sleep) mode.

This oscillator is labeled `Y2` on the circuit board and has text printed on the top which looks like a curved M in a box followed by `4.00` and then a single-character serial such as `L` or `J`. It is a surface-mount component.

Disabling this oscillator when not needed can save power. You can also adjust the speed this runs at by writing to register VD1C according to the following table:

| VD1C1 | VD1C0 | Operating voltage | Oscillation        |
|:-----:|:-----:| ----------------- | ------------------ |
|   1   |  1/0  | 3.2 V             | 0.03~8.2 MHz       |
|   0   |   1   | 1.6 V             | 0.03~1.1 MHz / off |
|   0   |   0   | 2.4 V             | 0.03~4.4 MHz       |

When switching voltages you cannot jump directly between 1.6 V and 3.2 V safely and you must wait some time after switching. See the VD1C register details for usage information. Note that the BIOS will switch between 1.6 V and 2.4 V during some operations.

In previous documentation and code, this oscillator was once known in the community as "oscillator 1".

#### OSC3 Specs

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

A timer which increments once every second. It uses OSC1 as its clock source.

This timer informs the real-time clock (RTC) in commercial games. As such, if homebrew resets or pauses the timer or sleeps the console, it will force commercial games to ask for the user to enter the time again.

* Write 0 to STRUN to pause this timer or 1 to start it.
  * When reading, 0 means paused and 1 means running.
  * In pm.h, STRST is bit 0 of SEC_CTRL
* Write 1 to STRST to reset this timer.
  * In pm.h, STRST is bit 1 of SEC_CTRL
* Read the count from the STD register
  * In pm.h, STD is called SEC_CNT

There are no interrupts related to this timer.

## Clock Timer

A timer which increments 256 times per second. It uses OSC1 as its clock source.

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

## General Purpose Timers

TODO

## Timer Overview

The Pokémon mini offers 3 general purpose timer units. Each timer is broken down into several blocks to provide it with variable clock rates, the ability to be broken down into two independent 8-bit timers, and each timer can generate two unique interrupts.

## Timer Control

Each timer is configured using 6 registers, TIM_SCALE\*, TIM_OSCI\*, TIM_CTL\*_L, TIM_CTL\*_H, TIM_PRE\*_L and TIM_PRE\*_H. These registers provide the ability to change the clock rate of both the low and high 8-bits of the counter, set if there is a borrow chain to the upper 8-bits (16-bit counter mode) as well as enable and reset the timer (load counter from the preset). Beginning with the TIM_OSCI\*, each timer has the ability to run from oscillator 1 (System Clock) or oscillator 2 (32768 Hz RTC Clock). The pre-scale is further decided by selecting one of 8 different pre-scale values from a table in the TIM_SCALE\* register.

Further more, timers must be enabled individually (by setting the enable flag in TIM_SCALE\* TIM_CTL\*_L and TIM_CTL\*_H) as well as by group (Upper half of TIM_ENA_OSCI1). TIM_ENA_OSCI1 disables oscillator 1 or 2 if either respective bit is clear ($10 and $20).

**Timer Prescale (Oscillator 1)**
| Prescale | Clk Div.   | Hz       |
| -------- | ---------- | -------- |
| 0        | CPU / 2    | 2000000  |
| 1        | CPU / 8    | 500000   |
| 2        | CPU / 32   | 125000   |
| 3        | CPU / 64   | 62500    |
| 4        | CPU / 128  | 31250    |
| 5        | CPU / 256  | 15625    |
| 6        | CPU / 1024 | 3906.25  |
| 7        | CPU / 4096 | 976.5625 |

**Timer Prescale (Oscillator 2)**
| Prescale | Clk Div.    | Hz    |
| -------- | ----------- | ----- |
| 0        | 32768 / 1   | 32768 |
| 1        | 32768 / 2   | 16384 |
| 2        | 32768 / 4   | 8192  |
| 3        | 32768 / 8   | 4096  |
| 4        | 32768 / 16  | 2048  |
| 5        | 32768 / 32  | 1024  |
| 6        | 32768 / 64  | 512   |
| 7        | 32768 / 128 | 256   |

The timer control registers affect the values of the timers themselves. Enable must be set for timing, this means there are a total of 3 bits that must be enabled for any timer to begin counting. writing a logical 1 to a reset bit in a control register will cause that respective 8-bit section to copy the respective value out of preset. All timers count down. When any timer underflows, it's value is copied from the preset value.

## 16-bit mode

When a timer is operating in 16-bit mode, all the upper-8 bit settings are unceremoniously ignored. Enables, reset and and everything no longer control the behavior of the timer. They remain writable, but they no longer actively function. This includes enables, resets and pre-scale values. The lower-8 bit configuration is effective over the full 16-bit value. Additionally, all lower-8 underflow IRQs are effectively disabled. The timer only presets when the full 16-bit value underflows.

## IRQ Operation

Each timer provides two irqs. These IRQs appear to be fixed function, which provides the only known difference between Timers 1-2 and Timer 3.

Timers 1-3 have a primary IRQ, this fires anytime the upper 8-bit of the counter underflows (16- or 8-bit operations) The secondary IRQ of Timer 1-2 occurs when the lower 8-bit counter underflows (8-bit mode only) The secondary IRQ of Timer 3 occurs when the value of the counter becomes less than or equal-to the value in it's comparator. In 8-bit mode only the upper 8-bit of the value is used.

## Sound

Timer 3 is also used for [sound](PM_Audio.md "wikilink") within the Pokémon mini.
