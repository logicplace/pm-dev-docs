# Pokémon mini Hardware Documentation

The Pokémon mini is a hand held created by Nintendo R\&D3 around 1999. It is based around the Epson S1C88 Core (then Timex/Seiko), and derives most peripherals from this system.

The machine has a 4 KiB on-board OTP BIOS, 4 KiB of internal RAM (shared with the LCD Controller) and a 21-bit cartridge bus. The entire system is controlled by writting to 256 hardware registers, most of which are [Open-Bus](../Glossary.md#open-bus).

- [CPU: S1C88V20](cpu/S1C88_Core.md)
  - [Instruction Set](cpu/S1C88_InstructionSet.md)
  - [The Memory Map](PM_Memory.md)
    - [The Hardware Registers](cpu/PM_Registers.md)
  - [Internal BIOS](PM_Bios.md)
  - [Interrupt Vectors](PM_IRQs.md)
  - [Watchdog Timer](PM_Second_Counter.md)
  - [Clock Timer](256Hz_Timer.md)
  - [Programmable Timers](Timers.md)
  - [Interrupt Hardware](PM_IRQs.md)
  - [I/O Ports](PM_I_O_Port.md)
  - [Audio / Sound](PM_Audio.md)
  - [LCD Controller](PM_PRC.md)
- [LCD: SED1565](LCD_Controller.md)
- EEPROM: 24xx64 alike
- IR Transceiver
- Piezo Speaker
- [Cartridges and port](PM_Cartridge.md)
  - [Cartridge Pinouts](PM_Pinouts.md)
- Pokémon mini Shell
- Flash Cartridges
