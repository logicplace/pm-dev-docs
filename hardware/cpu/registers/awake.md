# Awake

$2001 bit 5 is a [reserved R/W register](../../../glossary.md#reserved-rw-register).

A value of 0 indicates the console is asleep and a value of 1 indicates it's awake.

This register is checked during every IRQ handler in the BIOS, if it's 0, it goes through a [wake-up routine](../interrupts.md#waking-up) before jumping to software. In the event that the wake-up routine jumps to RAM, this will not be set to 1 by the BIOS.

Software should not modify this value directly outside of wakeup handlers, and in order to ensure it's set correctly, software should use the appropriate sleep and shutdown software interrupts for putting the console to sleep.

In previous documentation, this register was known as "Enable cart interrupts".
