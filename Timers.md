## Timer Overview

The Pokemon Mini offers 3 general purpose timer units. Each timer is
broken down into several blocks to provide it with variable clock rates,
the ability to be broken down into two independent 8-bit timers, and
each timer can generate two unique interrupts.

## Timer Control

Each timer is configured using 6 registers, TIM_SCALE\*, TIM_OSCI\*,
TIM_CTL\*_L, TIM_CTL\*_H, TIM_PRE\*_L and TIM_PRE\*_H. These
registers provide the ability to change the clock rate of both the low
and high 8-bits of the counter, set if there is a borrow chain to the
upper 8-bits (16-bit counter mode) as well as enable and reset the timer
(load counter from the preset). Beginning with the TIM_OSCI\*, each
timer has the ability to run from oscillator 1 (System Clock) or
oscillator 2 (32768 Hz RTC Clock). The pre-scale is further decided by
selecting one of 8 different pre-scale values from a table in the
TIM_SCALE\* register.

Further more, timers must be enabled individually (by setting the enable
flag in TIM_SCALE\* TIM_CTL\*_L and TIM_CTL\*_H) as well as by
group (Upper half of TIM_ENA_OSCI1). TIM_ENA_OSCI1 disables
oscillator 1 or 2 if either respective bit is clear ($10 and $20).

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

**Timer Prescale (Oscillator 1)**

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

**Timer Prescale (Oscillator 2)**

The timer control registers affect the values of the timers themselves.
Enable must be set for timing, this means there are a total of 3 bits
that must be enabled for any timer to begin counting. writing a logical
1 to a reset bit in a control register will cause that respective 8-bit
section to copy the respective value out of preset. All timers count
down. When any timer underflows, it's value is copied from the preset
value.

## 16-bit mode

When a timer is operating in 16-bit mode, all the upper-8 bit settings
are unceremoniously ignored. Enables, reset and and everything no longer
control the behavior of the timer. They remain writable, but they no
longer actively function. This includes enables, resets and pre-scale
values. The lower-8 bit configuration is effective over the full 16-bit
value. Additionally, all lower-8 underflow IRQs are effectively
disabled. The timer only presets when the full 16-bit value underflows.

## IRQ Operation

Each timer provides two irqs. These IRQs appear to be fixed function,
which provides the only known difference between Timers 1-2 and Timer 3.

Timers 1-3 have a primary IRQ, this fires anytime the upper 8-bit of the
counter underflows (16- or 8-bit operations) The secondary IRQ of Timer
1-2 occurs when the lower 8-bit counter underflows (8-bit mode only) The
secondary IRQ of Timer 3 occurs when the value of the counter becomes
less than or equal-to the value in it's comparator. In 8-bit mode only
the upper 8-bit of the value is used.

## Sound

Timer 3 is also used for [sound](PM_Audio.md "wikilink") within the Pokemon
Mini.