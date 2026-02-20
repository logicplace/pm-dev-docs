# Pokémon mini Hardware Documentation

The Pokémon mini is a hand held created by Nintendo R\&D3 around 1999. It is based around the Epson S1C88 Core (then Timex/Seiko), and it derives most peripherals from this system.

The machine has a 4 KiB internal mask ROM (BIOS), 4 KiB of internal RAM (shared with the LCD Controller) and a 21-bit cartridge bus. The entire system is controlled by writing to 256 hardware registers, most of which are [Open-Bus](../glossary.md#open-bus).

- [CPU: S1C88V20](cpu/README.md)
  - [Instruction Set](cpu/S1C88_InstructionSet.md)
  - [The Memory Map](cpu/Memory.md)
    - [The Hardware Registers](cpu/Registers.md)
  - [Internal BIOS](cpu/bios.md)
  - [Interrupts](cpu/interrupts.md)
  - [Oscillators & Timers](timers.md)
  - [I/O](cpu/io.md)
  - [Audio / Sound](cpu/sound.md)
  - [LCD Controller](cpu/lcd_controller.md)
  - [Standby modes](cpu/standby.md)
- [LCD: S1D15xxx](lcd)
- [EEPROM: 24xx64 alike](eeprom.md)
- [IR Transceiver](ir.md)
- [Piezo Speaker](speaker.md)
- [Cartridges and port](cartridge.md)
- [Pokémon mini Shell](shell.md)
- [Flash Cartridges](flash_carts)
  - [DITTO mini](flash_carts/ditto.md)
  - [PokeCard 512](flash_carts/pokecard.md)
  - [Others](flash_carts/other.md)

## [CPU](cpu)

Little-endian 8-bit model 3 S1C88V20 (aka E0C88V20) clocked 4.00 MHz. This is a S1C88 family chip, potentially customized for Nintendo (as there is no public documentation for the V20).

It has both 8-bit and 16-bit registers as well as 8-bit page registers for extended addressing.

External bus with 21 bits for address & 8 bits for data.

## [Memory](cpu/Memory.md)

- [*BIOS*](cpu/bios.md): 4096 bytes, read-only.
- [*Hardware Registers*](cpu/Registers.md): Used to control Pokémon mini system.
- [*Internal RAM*](cpu/Memory.md#ram): 4096 bytes, read/write access.
  Note: some RAM space may be required by the LCD controller and the bottom is used for the stack.
- [*Internal EEPROM*](eeprom.md): 8192 bytes, read/write access via the I2C interface, used to store game saves.
- [*Cartridge ROM*](cpu/Memory.md#cartridge-memory): Up to 2 MiB addressable (16 megabits). Official carts have 512 KiB mask ROM.

## [Video](lcd)

96x64 monochrome LCD, 1 bit per pixel (bpp), running at around a 75±10 Hz refresh rate. Toggling pixels allows to add a 3rd color with half tone.

It contains an on-glass driver which communicates on registers $20FE and $20FF as well as its own timer discussed below in [Timers](#timers).

### [LCD Controller](cpu/lcd_controller.md)

The rate at which the image is redrawn and copied to the LCD (and which stages of rendering are enabled) is configurable.

- Tiled backgrounds: 8x8 tiles, 4 different map sizes which expand beyond the screen boundaries and a moveable display area (which does not loop automatically). The entire tilemap can be color inverted.
- Sprites: 16x16 1 bpp with alpha mask, up to 24 sprites can be displayed at one time. Sprites can be individually activated, flipped, mirrored, and color inverted.

## [Sound](sound.md)

Single-channel square-wave with adjustable pulse-width played through a piezo speaker.

3 levels of volume: 0%, 50%, 100%. Commercial games achieve 25% and 75% by adjusting the pulse-width for a weaker sound.

Can read back timer values (since sound is assigned to Timer 3).

For commercial games, hold the C button while booting up to start muted. <!-- software comment but eh? -->

## [Timers](timers.md)

There are two oscillators and several timers/counters in the system. Additionally, the LCD controller has its own frame counter which is synced with the LCD.

OSC1 is 32768 Hz and is a low-power oscillator which cannot be disabled.
OSC3 is 4.00 MHz and can be disabled by software.
Entering sleep mode (but not halt mode) disables the oscillators.

- 1x 24-bit seconds timer - increments each second, used for RTC, clocked by OSC1
- 1x 8-bit 256Hz timer - increments each 1/256 of second, clocked by OSC1
- 1x 8-bit counter incremented by the LCD - counts 1 to 65 (inclusive)
- 3x configurable timers, clocked by either OSC1 or OSC3 (configurable)
  - Each timer can operate as 1 16-bit counter or 2 8-bit counters.
  - Timer 3 is used for audio, but it can be used for more general purposes as well if the audio output is muted.

## Extras

- [Rumble motor](rumble.md)
- [Shock detector](shock.md)
- [6-slot EEPROM for game saves](eeprom.md)
- [RTC (real time clock) Build-in](rtc.md)
- [IR transmitter / receiver](ir.md)

## Power

1.5V (converted to 3.3V internally) with 1 AAA Battery
