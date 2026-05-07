# Oscillators

*For more on the PM's oscillators, see [here](../timers.md#oscillators)*

In general, software does not need to access these registers and the PM seems to crash if you do alter them, even properly.

[72h]: ../bios.md#enter-normal-operation
[74h]: ../bios.md#enter-low-power-operation
[VDC]: vdc.md#vdc

## OSCC

$2002 bit 2 is a R/W register.

Oscillator Control

* 0 = OSC3 disabled
* 1 = OSC3 enabled

When disabled, OSC3 receives no power, allowing the console to operate in low power mode. OSCC must not be set to 1 while operating in low power mode. OSCC must not be set to 0 while CLKCHG is 1.

TODO: what happens when OSCC is set to 0 when PTs are using it as a clock source

This is the official register name.

## CLKCHG

$2002 bit 3 is a R/W register.

Change the operating Clock source for the CPU.

* 0 = OSC1 clocking CPU
* 1 = OSC3 clocking CPU

CLKCHG must not be set to 1 until OSC3 has been enabled and stabilized.

CLKCHG must be 1 to control external circuits, such as IR or the LCD.

This is the official register name.

## Changing operating modes

You should use the appropriate software interrupts to do this, if you can find when they even work, but this describes the methods for changing modes properly according to the technical manuals.

### Initial system state

Although unconfirmed, the system allegedly starts in normal mode. The BIOS quickly [ensures this](../../../software/bios/disasm/#user-content-00B6) and by the time it enters software, does remain in normal mode with OSC3 enabled and clocking the CPU.

### Low power to normal mode

This operation is handled by the software interrupt [72h][].

1. Presume OSC3 is disabled appropriately, as it's not allowed in low power mode.
2. Set [VDC][] to 00, entering normal operating voltage.
3. Wait 80 CPU cycles.
4. Set OSCC to 1, enabled OSC3.
5. Wait 1636 CPU cycles.
6. Set CLKCHG to 1, clocking the CPU with OSC3.

### Low power to high speed mode

This operation is useless on the PM.

1. Presume OSC3 is disabled appropriately, as it's not allowed in low power mode.
2. Set [VDC][] to 00, entering normal operating voltage.
3. Wait 80 CPU cycles.
4. Set [VDC][] to 10, entering high speed operating voltage.
5. Wait 80 CPU cycles.
6. Set OSCC to 1, enabled OSC3.
7. Wait 1636 CPU cycles.
8. Set CLKCHG to 1, clocking the CPU with OSC3.

### Normal to low power mode

This operation is handled by the software interrupt [74h][].

1. Set CLKCHG to 0, clocking the CPU with OSC1.
2. In a separate operation, set OSCC to 0, disabling OSC3.
3. Set [VDC][] to 01, entering low power operating voltage.

### Normal to high speed mode

This operation is useless on the PM.

1. Set CLKCHG to 0, clocking the CPU with OSC1.
2. In a separate operation, set OSCC to 0, disabling OSC3.
3. Set [VDC][] to 10, entering high speed operating voltage.
4. Wait 80 CPU cycles.
5. Set OSCC to 1, enabled OSC3.
6. Wait 1636 CPU cycles.
7. Set CLKCHG to 1, clocking the CPU with OSC3.

### High speed to normal mode

1. Set CLKCHG to 0, clocking the CPU with OSC1.
2. In a separate operation, set OSCC to 0, disabling OSC3.
3. Set [VDC][] to 00, entering normal operating voltage.
4. Wait 80 CPU cycles.
5. Set OSCC to 1, enabled OSC3.
6. Wait 1636 CPU cycles.
7. Set CLKCHG to 1, clocking the CPU with OSC3.

### High speed to low power mode

1. Set CLKCHG to 0, clocking the CPU with OSC1.
2. In a separate operation, set OSCC to 0, disabling OSC3.
3. Set [VDC][] to 00, entering normal operating voltage.
4. Wait 80 CPU cycles.
5. Set [VDC][] to 01, entering low power operating voltage.

### HALT status

*For more on this mode, see [here](../standby.md#HALT)*

If in high speed operation, switch to normal before attempting to HALT via any software interrupt (sleep or shutdown). When HALTing manually, any operating mode is fine but higher ones still have increased current consumption.

### SLEEP status

*For more on this mode, see [here](../standby.md#SLEEP)*

No software interrupt enters SLEEP status. When using SLP manually, both oscillators will turn off and the CPU will stop running entirely. The state of OSCC and CLKCHG will be restored upon returning from SLEEP. You may SLP when in any operating mode but higher ones still have increased current consumption (the difference between low and normal is negligible).
