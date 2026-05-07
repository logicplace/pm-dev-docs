# Timers

*For more information, see its [main page](../timers.md)*

The PM offers a seconds timer, a clock timer, and three dividable 16-bit programmable timers.

The PM's timers most resemble the [S1C88649][].

The seconds timer is unique to the PM. No other chip has a similar looking timer, particularly any timer with 3 bytes of data.

Every chip offers a clock timer but there are two types which differ based on the order of its interrupts. The following chips use the same order as the PM: [S1C88112/88104][], [S1C88348/317/316/308][], [S1C88349][], [S1C8F360][], [S1C88649][], [S1C88816][], [S1C88832/88862][], and [S1C88848][].

Every chip offers programmable timers (PTs), but no chip offers three dividable 16-bit ones. We use the naming scheme from the [S1C88649][] since it has two dividable 16-bit PTs and its registers have the same structure as the PM's. The [S1C88408][] and [S1C88409][] also have the same register structure, but only have one dividable 16-bit PT (and one 8-bit PT).

Every chip has a watchdog timer and most have a stopwatch timer, while the PM has no indication of having either. It's possible the PM has a watchdog timer which has no software access but it's unlikely it has a stopwatch timer.

[S1C88112/88104]: ../s1c88/112.md
[S1C88348/317/316/308]: ../s1c88/348.md
[S1C88349]: ../s1c88/349.md
[S1C8F360]: ../s1c88/F360.md
[S1C88408]: ../s1c88/408.md
[S1C88409]: ../s1c88/409.md
[S1C88649]: ../s1c88/649.md
[S1C88816]: ../s1c88/816.md
[S1C88832/88862]: ../s1c88/832.md
[S1C88848]: ../s1c88/848.md

## Seconds timer

*For more information, see its [main page](../timers.md#seconds-timer)*

The BIOS resets and starts the timer during a hard reset. Generally speaking, software should not be resetting nor stopping this timer.

### STRST

$2008 bit 1 is a write-only register.

Seconds Timer Reset

* Write 1 to reset the seconds timer.
  * It's not recommended to use this, see [below](#std).
* Always reads back as 0.

Since the timer is novel, the name is as well. It's styled after the clock timer which has the same register layout for TMRST and TMRUN.

### STRUN

$2008 bit 0 is a R/W register.

Seconds Timer Run

* Write 0 to stop this timer (does not reset the counter).
  * It's not recommended to use this, see [below](#std).
* Write 1 to start this timer.
* Reads back the current state of the timer: 0=Stopped, 1=Running.

Since the timer is novel, the name is as well. It's styled after the clock timer which has the same register layout for TMRST and TMRUN.

### STD

$200B~$2009 is a read-only register.

Seconds Timer Data

Represents the number of seconds since the console was first started after a dead state (for example, if the battery was replaced). This continues to count up while the console is asleep/shutdown.

Since the STD register is 24 bits (3 bytes) it can count 16777215 seconds, or for a little under 32 years.

This value is stored in the EEPROM in order to update the real time. If STD is less than the time stored in the EEPROM (such as because of a reset), it signals that the current time is invalid and needs to be set again by the user.

Since the timer is novel, the name is as well. It's styled after the clock timer which has the same register layout for TMRST and TMRUN.

## Clock timer

*For more information, see its [main page](../timers.md#clock-timer)*

Many chips have equivalent clock timers (see above), but due to programmable timer similarities, see the [S1C88649][] technical manual for detailed information on the clock timer.

### TMRST

$2040 bit 1 is a write-only register.

Clock Timer Reset

* Write 1 to reset the clock timer.
* Always reads back as 0.

This is the official register name.

### TMRUN

$2040 bit 0 is a R/W register.

Clock Timer Run

* Write 0 to stop this timer (does not reset the counter).
* Write 1 to start this timer.
* Reads back the current state of the timer: 0=Stopped, 1=Running.

This is the official register name.

### TMD

$2041 bits 7~0 is a read-only register.

Clock Timer Data

This value increments 256 times per second. Alternatively this can be thought of as this value overflowing every second.

While you can read this register directly, using the [interrupts](#interrupts) is likely more appropriate.

Each bit can be thought of as overflowing at some frequency, represented below:

| Bit |   Hz   | IRQ  |
|:---:|:------:| ---- |
|  7  |   1 Hz | TM1  |
|  6  |   2 Hz | TM2  |
|  5  |   4 Hz |      |
|  4  |   8 Hz | TM8  |
|  3  |  16 Hz |      |
|  2  |  32 Hz | TM32 |
|  1  |  64 Hz |      |
|  0  | 128 Hz |      |

This is the official register name.

### Interrupts

*For more information, see [here](irq.md#ptm)*

* Priority register: PTM
  * 32 Hz - ETM32 / FTM32
  * 8 Hz - ETM8 / FTM8
  * 2 Hz - ETM2 / FTM2
  * 1 Hz - ETM1 / FTM1

## Programmable timers

*For more information, see its [main page](../timers.md#programmable-timers)*

The official documentation only ever refers to 8-bit timers by name, such as PTM0. We use the naming scheme from the MODE16 registers on the [S1C88649][] in order to name the 16-bit verions as PTM_A etc. In the manual here is the only time you will see a reference to `PTM0-1` but this is clunky as a name and implies the wrong order when it's in 16-bit mode; it's likely not meant as a name.

Note that PTM is also the name of the priority register for the clock timer. As such, PTM0 refers to an 8-bit timer, PTM_A refers to a 16-bit timer (which contains PTM1 and PTM0), and PT refers to programmable timers generally.

Each 16-bit PT has the same register layout, but all registers are listed below.

| Offset.Bit | Name     | Function                    | 1              | 0              | R/W |
| ---------- | -------- | --------------------------- | -------------- | -------------- |:---:|
| $18.7      | PRPRT1   | PTM1 clock control          | On             | Off            | R/W |
| $18.6      | PST12    | PTM1 division ratio         |                |                | R/W |
| $18.5      | PST11    |                             |                |                | R/W |
| $18.4      | PST10    |                             |                |                | R/W |
| $18.3      | PRPRT0   | PTM0 clock control          | On             | Off            | R/W |
| $18.2      | PST02    | PTM0 division ratio         |                |                | R/W |
| $18.1      | PST01    |                             |                |                | R/W |
| $18.0      | PST00    |                             |                |                | R/W |
| $19.7      | -        | -                           | -              | -              |     |
| $19.6      | -        | -                           | -              | -              |     |
| $19.5      | -        | -                           | -              | -              | R/W |
| $19.4      | -        | -                           | -              | -              | R/W |
| $19.3      | -        | -                           | -              | -              |     |
| $19.2      | -        | -                           | -              | -              |     |
| $19.1      | PRTF1    | PTM1 source clock selection | fOSC1          | fOSC3          | R/W |
| $19.0      | PRTF0    | PTM0 source clock selection | fOSC1          | fOSC3          | R/W |
| $1A.7      | PRPRT3   | PTM3 clock control          | On             | Off            | R/W |
| $1A.6      | PST32    | PTM3 division ratio         |                |                | R/W |
| $1A.5      | PST31    |                             |                |                | R/W |
| $1A.4      | PST30    |                             |                |                | R/W |
| $1A.3      | PRPRT2   | PTM2 clock control          | On             | Off            | R/W |
| $1A.2      | PST22    | PTM2 division ratio         |                |                | R/W |
| $1A.1      | PST21    |                             |                |                | R/W |
| $1A.0      | PST20    |                             |                |                | R/W |
| $1B.7      | -        | -                           | -              | -              |     |
| $1B.6      | -        | -                           | -              | -              |     |
| $1B.5      | -        | -                           | -              | -              |     |
| $1B.4      | -        | -                           | -              | -              |     |
| $1B.3      | -        | -                           | -              | -              |     |
| $1B.2      | -        | -                           | -              | -              |     |
| $1B.1      | PRTF3    | PTM3 source clock selection | fOSC1          | fOSC3          | R/W |
| $1B.0      | PRTF2    | PTM2 source clock selection | fOSC1          | fOSC3          | R/W |
| $1C.7      | PRPRT5   | PTM5 clock control          | On             | Off            | R/W |
| $1C.6      | PST52    | PTM5 division ratio         |                |                | R/W |
| $1C.5      | PST51    |                             |                |                | R/W |
| $1C.4      | PST50    |                             |                |                | R/W |
| $1C.3      | PRPRT4   | PTM4 clock control          | On             | Off            | R/W |
| $1C.2      | PST42    | PTM4 division ratio         |                |                | R/W |
| $1C.1      | PST41    |                             |                |                | R/W |
| $1C.0      | PST40    |                             |                |                | R/W |
| $1D.7      | -        | -                           | -              | -              |     |
| $1D.6      | -        | -                           | -              | -              |     |
| $1D.5      | -        | -                           | -              | -              |     |
| $1D.4      | -        | -                           | -              | -              |     |
| $1D.3      | -        | -                           | -              | -              |     |
| $1D.2      | -        | -                           | -              | -              |     |
| $1D.1      | PRTF5    | PTM5 source clock selection | fOSC1          | fOSC3          | R/W |
| $1D.0      | PRTF4    | PTM4 source clock selection | fOSC1          | fOSC3          | R/W |
| $30.7      | MODE16_A | 8/16-bit mode selection     | 16-bit x 1     | 8-bit x 2      | R/W |
| $30.6      | -        | -                           | -              | -              |     |
| $30.5      | -        | -                           | -              | -              |     |
| $30.4      | -        | -                           | -              | -              |     |
| $30.3      | PTOUT0   | PTM0 clock output control   | On             | Off            | R/W |
| $30.2      | PTRUN0   | PTM0 Run/Stop control       | Run            | Stop           | R/W |
| $30.1      | PSET0    | PTM0 preset                 | Preset         | No operation   |  W  |
| $30.0      | CKSEL0   | PTM0 input clock selection  | External clock | Internal clock | R/W |
| $31.7      | -        | -                           | -              | -              | R/W |
| $31.6      | -        | -                           | -              | -              |     |
| $31.5      | -        | -                           | -              | -              |     |
| $31.4      | -        | -                           | -              | -              |     |
| $31.3      | PTOUT1   | PTM1 clock output control   | On             | Off            | R/W |
| $31.2      | PTRUN1   | PTM1 Run/Stop control       | Run            | Stop           | R/W |
| $31.1      | PSET1    | PTM1 preset                 | Preset         | No operation   |  W  |
| $31.0      | CKSEL1   | PTM1 input clock selection  | External clock | Internal clock | R/W |
| $32        | RDR0     | PTM0 preset                 |                |                | R/W |
| $33        | RDR1     | PTM1 preset                 |                |                | R/W |
| $34        | CDR0     | PTM0 compare data           |                |                | R/W |
| $35        | CDR1     | PTM1 compare data           |                |                | R/W |
| $36        | PTM0     | PTM0 count                  |                |                |  R  |
| $37        | PTM1     | PTM1 count                  |                |                |  R  |
| $38.7      | MODE16_B | 8/16-bit mode selection     | 16-bit x 1     | 8-bit x 2      | R/W |
| $38.6      | -        | -                           | -              | -              |     |
| $38.5      | -        | -                           | -              | -              |     |
| $38.4      | -        | -                           | -              | -              |     |
| $38.3      | PTOUT2   | PTM2 clock output control   | On             | Off            | R/W |
| $38.2      | PTRUN2   | PTM2 Run/Stop control       | Run            | Stop           | R/W |
| $38.1      | PSET2    | PTM2 preset                 | Preset         | No operation   |  W  |
| $38.0      | CKSEL2   | PTM2 input clock selection  | External clock | Internal clock | R/W |
| $39.7      | -        | -                           | -              | -              | R/W |
| $39.6      | -        | -                           | -              | -              |     |
| $39.5      | -        | -                           | -              | -              |     |
| $39.4      | -        | -                           | -              | -              |     |
| $39.3      | PTOUT3   | PTM3 clock output control   | On             | Off            | R/W |
| $39.2      | PTRUN3   | PTM3 Run/Stop control       | Run            | Stop           | R/W |
| $39.1      | PSET3    | PTM3 preset                 | Preset         | No operation   |  W  |
| $39.0      | CKSEL3   | PTM3 input clock selection  | External clock | Internal clock | R/W |
| $3A        | RDR2     | PTM2 preset                 |                |                | R/W |
| $3B        | RDR3     | PTM3 preset                 |                |                | R/W |
| $3C        | CDR2     | PTM2 compare data           |                |                | R/W |
| $3D        | CDR3     | PTM3 compare data           |                |                | R/W |
| $3E        | PTM2     | PTM2 count                  |                |                |  R  |
| $3F        | PTM3     | PTM3 count                  |                |                |  R  |
| $48.7      | MODE16_C | 8/16-bit mode selection     | 16-bit x 1     | 8-bit x 2      | R/W |
| $48.6      | -        | -                           | -              | -              |     |
| $48.5      | -        | -                           | -              | -              |     |
| $48.4      | -        | -                           | -              | -              |     |
| $48.3      | PTOUT4   | PTM4 clock output control   | On             | Off            | R/W |
| $48.2      | PTRUN4   | PTM4 Run/Stop control       | Run            | Stop           | R/W |
| $48.1      | PSET4    | PTM4 preset                 | Preset         | No operation   |  W  |
| $48.0      | CKSEL4   | PTM4 input clock selection  | External clock | Internal clock | R/W |
| $49.7      | -        | -                           | -              | -              | R/W |
| $49.6      | -        | -                           | -              | -              |     |
| $49.5      | -        | -                           | -              | -              |     |
| $49.4      | -        | -                           | -              | -              |     |
| $49.3      | PTOUT5   | PTM5 clock output control   | On             | Off            | R/W |
| $49.2      | PTRUN5   | PTM5 Run/Stop control       | Run            | Stop           | R/W |
| $49.1      | PSET5    | PTM5 preset                 | Preset         | No operation   |  W  |
| $49.0      | CKSEL5   | PTM5 input clock selection  | External clock | Internal clock | R/W |
| $4A        | RDR4     | PTM4 preset                 |                |                | R/W |
| $4B        | RDR5     | PTM5 preset                 |                |                | R/W |
| $4C        | CDR4     | PTM4 compare data           |                |                | R/W |
| $4D        | CDR5     | PTM5 compare data           |                |                | R/W |
| $4E        | PTM4     | PTM4 count                  |                |                |  R  |
| $4F        | PTM5     | PTM5 count                  |                |                |  R  |

### PRPRT

Prescaler output control for Programmable Timer

* When set to 0 (default), prescaler output is disabled (disabling the timer entirely).
* When set to 1, prescaler output is enabled.

This is the official register name. In PRPRT0, 0 refers to PTM0.

### PST

*For more information, see its [main page](../timers.md#programmable-timer-configuration)*

Prescale division ratio Selection (ST may be from *sentaku (選択)*)

| PSTx2-PSTx0 | OSC3 | OSC1 |
|:-----------:| ---- | ---- |
|    1 1 1    | 4096 | 128  |
|    1 1 0    | 1024 | 64   |
|    1 0 1    | 256  | 32   |
|    1 0 0    | 128  | 16   |
|    0 1 1    | 64   | 8    |
|    0 1 0    | 32   | 4    |
|    0 0 1    | 8    | 2    |
|    0 0 0    | 2    | 1    |

This is the official register name. In PST10, 1 refers to PTM1 and 0 refers to the bit index in the PST1 data.

### PRTF

Programmable Timer fOSC input selection

* When set to 0 (default), source clock is OSC3.
* When set to 1, source clock is OSC1.

This is the official register name. In PRTF0, 0 refers to PTM0.

### MODE16

16-bit Mode for PT pair

This is the official register name. In MODE16_A, A unofficially refers to PTM_A, and officially is merely meant as a differentiator. The [S1C88848][] docs use `MODE160` instead, where 0 is the differentiator.

### PTOUT

Programmable Timer Output (TOUT)

It's unconfirmed whether or not this register is hooked up on the PM. If it is, it's unknown specifically what it does. TODO: PTOUT5 may control whether or not PTM_C is used for sound generation.

In 16-bit mode, the hi timer's PTOUT is used. That is: PTOUT1, PTOUT3, PTOUT5.

This is the official register name. In PTOUT0, 0 refers to PTM0.

### PTRUN

Programmable Timer Run

In 16-bit mode, the lo timer's PTRUN is used. That is: PTRUN0, PTRUN2, PTRUN4.

This is the official register name. In PTRUN0, 0 refers to PTM0.

### PSET

Preset

In 16-bit mode, the lo timer's PSET is used. That is: PSET0, PSET2, PSET4.

This is the official register name. In PSET0, 0 refers to PTM0.

### CKSEL

Clock Selection

It's unconfirmed whether or not this register is hooked up on the PM. If it is, it's unknown specifically what it does. TODO: According to the docs, setting CKSEL to 1 should count pulses on some K port(s), but it's unknown which ports or if this is the only register that needs to be set to enable it.

In 16-bit mode, the lo timer's CKSEL is used. That is: CKSEL0, CKSEL2, CKSEL4.

This is the official register name. In CKSEL0, 0 refers to PTM0.

### PTM_A

*For more information, see its [main page](../timers.md#ptm_a)*

A combination of PTM1 as the hi byte and PTM0 as the lo byte.

PTM_A offers two interrupts: [xTU1](irq.md#xtu1) and [xTU0](irq.md#xtu0)

This is an unofficial name. You may also see it named `PTM0-1` or `timer 0/1`.

### PTM_B

*For more information, see its [main page](../timers.md#ptm_b)*

A combination of PTM3 as the hi byte and PTM2 as the lo byte.

PTM_B offers two interrupts: [xTU3](irq.md#xtu3) and [xTU2](irq.md#xtu3)

This is an unofficial name. You may also see it named `PTM2-3` or `timer 2/3`.

### PTM_C

*For more information, see its [main page](../timers.md#ptm_c)*

A combination of PTM5 as the hi byte and PTM4 as the lo byte. Also see the [audio registers](audio.md).

PTM_C offers two interrupts: [xTU5](irq.md#xtu5) and [xTC5](irq.md#xtc5)

This is an unofficial name.
