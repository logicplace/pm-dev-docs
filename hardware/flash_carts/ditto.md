# DITTO mini

Designed by Zoranc and produced by Plamen, the [DITTO mini](https://dittomini.com/) is a 2 MiB flash cart which has been in production since [January 2019](https://www.pokemon-mini.net/forum/viewtopic.php?p=6455#p6455).

Since this board can fit in an official PM cartridge, it can use any of [those models](../cartridge.md#shells). [Ksanto's](https://www.thingiverse.com/thing:3592237) was specifically designed for the DITTO mini.

When you order a DITTO mini from a2heaven, it comes with official cartridge labels designed by RazorLeafAttack you can stick onto a cartridge.
![DITTO mini label by RazorLeafAttack](/assets/img/flash/ditto_label.png)

## Features

* Capacity: 2 MiB, capable of storing 3 commercial games
* Multicart support
* Fits in an official case with no modification
* Software can write to the cart from within the PM
* Comes with stickers

## Issues / limitations

* Like all flash carts, commercial games must be patched to play in multicart mode, which disables any mid-game sleeping functionality (like pressing the power button in the middle of a Tetris game)
* Must be used in a case, board will not make contact loose

## Technical specifications

* Capacity: 2 MiB
* Theoretical flashing speeds: 30s (512 KiB), 2m (2 MiB)
* Flash memory: [SST39VF1681](http://ww1.microchip.com/downloads/en/devicedoc/25040a.pdf)
* Bridge chip: [XC9572XL-10VQ64C](https://www.xilinx.com/support/documentation/data_sheets/ds057.pdf)

## Flashing

There are two options for flashing, the official [DITTO mini Flasher](#ditto-mini-flasher) or the [PokMini Flasher](#pokmini-flasher)

### DITTO mini Flasher

The official tool for flashing through this linker is [Ditto Flash](http://dittomini.com/dittoflash/Ditto_Flash_1.00.zip).

This is the same flasher which is used for other a2heaven flash carts, namely the Supervision one.

To use this tool, remove your DITTO mini from your console (or at least remove the battery), connect your DITTO mini Flasher to your DITTO mini with the provided cable, then connect the flasher to your computer with a USB 2.0 Micro-B connector. Now run Ditto Flash, it should automatically connect (you can tell because the icons will become clickable).

#### Flashing

1. Follow the steps above to connect the flash cart
2. Click `Load File` to load a ROM file into Ditto Flash
3. Click `Write to Card` to write it
4. Wait until it says "Programming is successful" and the red light turns off on the DITTO mini Flasher
5. You may now disconnect the DITTO mini

#### Dumping

This is primarily useful after you've backed up your [EEPROM](#eeprom-tool) or [BIOS](#bios-dumper).

1. Follow the steps above to connect the flash cart
2. Click `Read Card`, it will read the whole 2 MiB
3. After it says "Reading Done", click `Save File` and choose where to save the file

#### Issues with Ditto Flash

* "ftd2xx.dll was not found"
  * Install the [FTDI D2XX drivers](https://ftdichip.com/wp-content/uploads/2025/03/CDM2123620_Setup.zip) (from [here](https://ftdichip.com/drivers/d2xx-drivers/))
* "Value must be between 1 and 2,147,483,647"
  * Cable might be loose, try reconnecting the bit that plugs into the cart, maybe push the wires in a bit
* Error when reading/writing after writing once
  * Just restart Ditto Flash
* "No Ditto Programmer devices found"
  * Possibly using a charge-only cable
  * Make sure light is blue on the flasher

#### Technical specifications

* Connector: USB 2.0 Mini-B
* Chip: [FT2232HL](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT2232H.pdf)
* Cable:
  * Flasher-side head: [2.0mm pitch 2x5 pin IDP FC female socket connector](https://www.aliexpress.us/item/2251832621509694.html)
  * Cart-side head: [6-pin JST SH-style female cable](https://www.aliexpress.us/item/3256803842644814.html)
    * The single-head one, and note that SH-style means 1.0mm pitch.

##### Pinout

```txt
Flasher-side connector (IDP), nub on top

 _____----_____
|01 02 03 04 05| Port in flasher
|06 07 08 09 10| Male end
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
 _______-----_______
| | 01 02 03 04 05| | Teeth on connector
| |06 07 08 09 10 | | Back side of female end
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

| Pin | Purpose  | FT2232D Pin | MPSSE  | SPI  | Color* | JST Pin |
|:---:| -------- | ----------- | ------ | ---- | ------ |:-------:|
|  01 | (GND)    | 34 - GND    | -      | -    | -      |    -    |
|  02 | (GND)    | 34 - GND    | -      | -    | -      |    -    |
|  03 | (GND)    | 34 - GND    | -      | -    | -      |    -    |
|  04 | GND      | 34 - GND    | -      | -    | red    |    6    |
|  05 | VCC 3.3V | 14 - VCCIOA | -      | -    | black  |    5    |
|  06 | (GND)    | 34 - GND    | -      | -    | -      |    -    |
|  07 | Input    | 22 - ADBUS2 | TDO/DI | MISO | blue   |    2    |
|  08 | Output   | 23 - ADBUS1 | TDI/DO | MOSI | green  |    3    |
|  09 | Clock    | 24 - ADBUS0 | TCK/SK | SCLK | white  |    1    |
|  10 | Program  | 21 - ADBUS3 | TMS/CS | CS   | yellow |    4    |

\*Color on the official connector cable

### PokMini Flasher

*For its usage with the PokMini flash cart, see its [main page](./pokmini.md#flashing)*

To flash a ROM using this device, connect the DITTO mini with the cable provided with the PokMini Flasher and use the special [PokMini DM Flasher](https://shop.insidegadgets.com/wp-content/uploads/2023/03/PokMini_DM_Flasher_v1.0.zip) tool.

Drag and drop the ROM onto pokmini_dm_flasher.exe to flash. There is no dump or erase support.

## Multicart

There are two options for multicart on DITTO mini: [official](#official-multicart) and [slimloader](#slimloader)

### Official multicart

Find the instructions and ROM [here](https://www.pokemon-mini.net/forum/viewtopic.php?t=4278)

1. Download the bootloader ROM
2. Ensure your ROMs are either 512 KiB or 64 KiB. If you mix them, you must order all the 512 KiB ones before the 64 KiB ones
3. Concatenate the files together
```sh
# Windows, in Command Prompt (CMD)
copy bootloader.min/b + p1.min/b + p2.min/b + p3.min/b result.min
# *nix
cat bootloader.min p1.min p2.min p3.min > result.min
```
4. [Flash](#flashing) to your DITTO mini

To pad homebrew ROMs, a decent way to do it is to use a hex editor like [HxD](https://mh-nexus.de/en/hxd/) to insert bytes until it's the right size. HxD also supports concatenating files.

### Slimloader

Find the latest version [here](https://github.com/Jhynjhiruu/slimloader/)

1. Download this repo
2. Ensure you have the [Epson tooling installed](/dev/Getting_Started.md)
3. Place exactly four ROMs in the `slimloader` folder named `in.min`, `in2.min`, `in3.min`, & `in4.min`
4. Open your terminal to this folder
5. `mk88 combined`

The first game will have a portion of its available space replaced with Slimloader's code. To be completely safe, this first ROM should be less than 260 KiB (267008 B).

## BIOS dumper

Find the instructions and ROM [here](https://www.pokemon-mini.net/forum/viewtopic.php?t=4274)

TODO: instructions here, upload ROM to PM.net and link that

## EEPROM Tool

Find the ROM and source code [here](https://www.pokemon-mini.net/download/eeprom-tool/)

TODO: instructions

This tool manages the entire EEPROM, not individual save slots. To manage individual save slots after backing up to your PC, use [this tool](https://pokeminisaves.github.io/) by thx.

Users have reported an occasional failure to restore the backup to a PM. Ensure the save looks correct by using the above tool before attempting a restore.

## Writing from software

TODO: library

The DITTO mini offers full flash control from software. So any command - such as writing, erasing, getting manufacturer information, etc. - can be run from software.

Since flashing data to the cartridge requires entering command sequences which would be interrupted by reads, any functions which write to the cart must be run from RAM with interrupts masked (`LD SC, #0C0h`).

There are two registers the DITTO mini offers:

```c
#define FLASH_ADDR1 (*((volatile uint8_t _far *)0x1FFAAA))
#define FLASH_ADDR2 (*((volatile uint8_t _far *)0x1FF555))
```

In order to flash a single byte, perform the following sequence:

```c
FLASH_ADDR1 = 0x55;
FLASH_ADDR2 = 0xAA;
FLASH_ADDR1 = 0x05;
*((volatile uint8_t _far *)address) = value;
// wait ~24 more cycles, such as with _nop()s
```

## Bank switching

Because bank switching changes where the CPU reads from immediately, it's recommended to switch from code running in RAM. Once a bank is selected, the software cannot access memory outside the selected bank. If this is for a multicart, you can call `_int(0x02)` after to reset the console and load software from the new slot.

```c
#define BANK_SWITCH (*((volatile uint8_t _far *)0x1FFFFF))

BANK_SWITCH = 0;     // Use full 2 MiB

BANK_SWITCH = 1;     // Use 64 KiB bank 0
BANK_SWITCH = 2;     // Use 64 KiB bank 1
// ...
BANK_SWITCH = 31;    // Use 64 KiB bank 30

BANK_SWITCH = 0x80;  // Use 512 KiB bank 0
BANK_SWITCH = 0x81;  // Use 512 KiB bank 1
BANK_SWITCH = 0x82;  // Use 512 KiB bank 2
BANK_SWITCH = 0x83;  // Use 512 KiB bank 3
```

## Gallery

![DITTO mini](/assets/img/flash/ditto.png "DITTO mini")
![DITTO mini proto PCB front](/assets/img/flash/ditto_proto1_front.png "DITTO mini proto PCB front")
![DITTO mini proto PCB back](/assets/img/flash/ditto_proto1_back.png "DITTO mini proto PCB back")
![DITTO mini Flasher PCB](/assets/img/flash/ditto_flasher_pcb.jpg "DITTO mini Flasher PCB, may have changed slightly since")
![DITTO mini Flasher](/assets/img/flash/ditto_flasher2.jpg "DITTO mini Flasher, may have changed slightly since")
