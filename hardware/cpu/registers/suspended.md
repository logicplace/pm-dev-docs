# Console is suspended

$2002 bit 5 is a [reserved R/W register](../../../glossary.md#reserved-rw-register).

It's initialized to 0 and set to 1 before suspending the system (through any software interrupt) and reset to 0 on resuming the system.

This essentially means that it's only 1 if the system is currently asleep. This differs from [awake](awake.md) in that it's only set in one place. This is more authentic in terms of whether the console is asleep or not, but is only checked during [_key_power_irq](../interrupts.md#power-key) by the BIOS.

In previous documentation, this register was known as "Suspend mode".
