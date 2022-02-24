# Pokémon-Mini Specifications

The Pokémon-Mini is one of the smallest and cheapest handheld video game system designed and manufactured by Nintendo.

Only 10 games were released (All Pokémon related), each game (a very tiny video game cartridge) could be inserted by slotting-in on the top-back of the unit.

The system features a Tiny 96x64 Monochrome LCD, Rumble Motor, Shock Detector, EEPROM with 6 slots for game saves, Game cartridge slot and monophony sound.

## [CPU](CPU.md "wikilink")

Little-endian 8-Bits Nintendo custom IC codenamed "Nintendo Minx", clocked 4.00 MHz

8-Bits, 16-Bits and 24-Bits(addressing only) registers

External BUS with 21-Bits Address & 8-Bits Data

## [Memory](Memory.md "wikilink")

[*BIOS*](BIOS.md "wikilink"): 4096 Bytes, read-only

[*Hardware Registers*](Registers.md "wikilink"): Used to control Pokémon-mini system

[*Internal RAM*](Memory.md "wikilink"): 4096 Bytes, read/write access,
Note: some RAM space may be required by the hardware

[*Internal EEPROM*](EEPROM.md "wikilink"): 8192 Bytes, read/write access
(only accessible via SPI interface), used to store savegames

[*Cartridge ROM*](Cartridge.md "wikilink"): Up to 2 Megabytes (16 Megabits)

## [Video](Video.md "wikilink")

96x64 Mono-LCD, 1-bit per pixel

[2D engine](Video.md "wikilink"): Background support (formed with 8x8 tiles, 4 different map sizes), Sprites support (16x16 1bpp with mask, up to 24 sprites)

Toggling pixels allows to add a 3rd color with half tone

Moving tile-map support (not scrolling!!!)

## [Sound](Sound.md "wikilink")

Single-channel square-wave with adjustable pulse-width

3 Levels of volume: 0%, 50%, 100%

Can read back timer values (since sound is assigned to Timer 3)

## [Timers](Timers.md "wikilink")

1x 24-Bits seconds-timer - increments each second, used for RTC

1x 8-Bits 256Hz timer - increments each 1/256 of second

1x 8-Bits VPU timer

3x Configurable timers - 1 16-bits or 2 8-bits counters (3rd Timer can
be used to output sound)

## Extras

[Rumble motor](Rumble.md "wikilink")

[Shock detector](Shock.md "wikilink")

[6-Slots RAM for savegames](EEPROM.md "wikilink")

[RTC (real time clock) Build-in](RTC.md "wikilink")

[IR transmitter / receiver](IR.md "wikilink")

## Power

1.5V (converted to 3.3V internally) with 1 AAA Battery
