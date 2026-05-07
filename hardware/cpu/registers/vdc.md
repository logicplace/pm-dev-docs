# System voltage

The PM allows software to configure the system voltage. The BIOS only uses two modes, so it's ill-advised to attempt the other mode(s).

The two modes which the BIOS does use correlate with using [CLKCHG](osc.md#CLKCHG) and likely there is no reason to alter VDC outside of this context. Since the VDC can't be changed without disabling the OSC3 it's unlikely there's a method of doing this from software, anyway.

VDC is also available on the chips: [S1C88112/88104](../s1c88/112.md), [S1C88348/317/316/308](../s1c88/348.md), [S1C88349](../s1c88/349.md), and [S1C8F360](../s1c88/F360.md). A similar register, VD1C, is available on the [S1C88408](../s1c88/408.md) and [S1C88409](../s1c88/409.md).

## VDC

$2002 bits 1~0 is a R/W register.

The values in this table aren't confirmed for the PM, but are the same across most of the family. The 8F360, 88408, and 88409 use slightly different voltages, and the 88409 offers a fourth mode which is higher power.

| VDC1~VDC0 | Operating mode        |
|:---------:| --------------------- |
|    1 x    | High speed (VD1=3.3V) |
|    0 1    | Low power  (VD1=1.3V) |
|    0 0    | Normal     (VD1=2.2V) |

When changing modes, you MUST step up/down one level at a time and [OSC3 must be off](osc.md#OSCC). That is:

* 1.3V (01) -> 2.2V (00) -> 3.3V (10)
* 1.3V (01) <- 2.2V (00) <- 3.3V (10)

The BIOS only changes between Normal and Low Power modes, and is written in a way that presumes VDC1 will never be set ([here](../../../software/bios/disasm/#user-content-0AB3) and [here](../../../software/bios/disasm/#user-content-0AE2)). Thus if software ever enters High Speed operation, it will need to exit it (step down to Normal operation) before sleeping or shutting down the console via software interrupts.

When in Low Power mode, OSC3 must stay disabled.

High Speed operation's primary advantage seems to be higher MHz when clocking the CPU with OSC3 (up to 8.2 MHz) but only if such an oscillator is connected, which the PM does not use. As such, this mode should theoretically only burn battery unnecessarily.

In previous documentation, bit 1 was known as "RTC Timer valid".
