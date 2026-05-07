# Chip enable

These values are set to 1 during [reset](../../../software/bios/disasm/#user-content-00C4) and should not be changed.

A value of 1 enables communication on the [CS](../../board.md#user-content-cpu-62) or [LCD_CS](../../board.md#user-content-cpu-35) pins as chip selects. A value of 0 will disable those signals, causing the cartridge or LCD to not respond to communications.

The exact extent of how these affect the system hasn't been researched.

## CE0

$2000 bit 0 is a R/W interrupt.

Chip Enable for LCD.

In previous documentation, this register was known as "LCD I/O Enable".

## CE1

$2000 bit 1 is a R/W interrupt.

Chip Enable for cartridge.

In previous documentation, this register was known as "Cartridge I/O Enable".
