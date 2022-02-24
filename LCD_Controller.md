## LCD Controller Overview

The Pokémon mini LCD is a serial display with it's own on-board framebuffer, and display settings. These are all abstracted by the [PRC](PM_PRC.md "wikilink"), which handles display copies ($1000 \~ $12FF) and other various functions. No commercial roms directly access the display, relying on the PRC and BIOS to perform the various communications. This allows for the PM to have hardware changes without having to rely on the same display controller.

The display is driven by two data ports, $20FE and $20FF. Both ports are read\\write, the only difference between them is one sets the CTRL line when accessing the data port on the LCD. The port is 8-bits wide, and has a small set of standard commands.

The LCD is probably using the on-glass <s>[SSD1828 LCD controller](http://www.solomon-systech.com/products/ssd1828.htm) or something very simliar.</s>[SED1565 LCD Controller](http://www.bolymin.com.tw/Doc/SED1565.pdf)

The controller got <s>96x65</s> 132x65 Graphic Display Data RAM (GDDRAM) with 96x64 pixels visible on the LCD. The additional RAM is for an unused symbol driver. The PM most likely uses a parallel interface to the controller, but serial interface might be available on the connector of the LCD.

## LCD Controller Commands

Lower case "x" denotes parameters used by the command. A question mark "?" denotes bits that are don't care.

The commands in this list are verified to work. The <s>SSD1828</s> datasheet holds <s>much</s> more commands <S>that are hard</S>of which a few are hard to verify <s>or didn't work</s> on the PM.

| Command   | Description                     | Notes                                                                                                                                                                                                                                                                    |
| --------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0000 xxxx | Set Column (low nibble)         | xxxx = Column 0-15 (low nibble)                                                                                                                                                                                                                                          |
| 0001 0xxx | Set Column (high nibble)        | xxxx = Column 0-8 (high nibble)                                                                                                                                                                                                                                          |
| 01xx xxxx | Display Start line              | xxxxxx = 0-63 first line on display                                                                                                                                                                                                                                      |
| 1011 xxxx | Set Page                        | xxxx = Page (0-8, pages 0-7 are 8px high, Page 8 = 1px high)                                                                                                                                                                                                             |
| 1000 0001 | Set Contrast                    | Next write to FE or FF sets Constrast Level ($00-$3F)                                                                                                                                                                                                                    |
| 1010 000x | Segment Driver Direction Select | x=0 (Normal) 1 (Reverse) Note on Reverse 131 is the leftmost pixel and 36 the rightmost visible pixel. Pixels 35-0 are not visible. This command only affects the addressing arithmetics on the next read/writes and does not change any data that is already displayed. |
| 1010 001x | LCD Voltage Bias                | x=0 (1/9th = normal) 1 (1/7th = darker )                                                                                                                                                                                                                                 |
| 1010 010x | Entire Display select           | x = 0 (normal) or 1 (all Pixels on)                                                                                                                                                                                                                                      |
| 1010 011x | Invert Display select           | x = 0 (normal) or 1 (invert) effective immediately. Ram is not affected.                                                                                                                                                                                                 |
| 1010 111x | Display ON/OFF                  | x = 0 (off) or 1 (on)                                                                                                                                                                                                                                                    |
| 1100 x??? | Set scan direction (rows)       | x = 0 (normal from row 0 to 63) or 1 (from row 63 to 0 - verical mirror)                                                                                                                                                                                                 |
| 1110 0000 | Read Modify Write               | A read to display ram wil not advance the ram pointer. Only a write will advance the ram pointer. When active, column commands are not available.                                                                                                                        |
| 1110 1110 | End                             | Ends Read Modify Write mode.                                                                                                                                                                                                                                             |
| 1110 0010 | Reset                           | Initializes Display.                                                                                                                                                                                                                                                     |
| 1110 0011 | NOP                             | No Operation. Also used to exit test mode.                                                                                                                                                                                                                               |

**LCD Commands**

## Data reads/writes

Data can be read and written from/to the LCD at any time (but not when contrast command was executed, this is a special case). The programmer should make sure that the page and column address pointers are pointing to the correct location.

When data was read or written the column address automatically increases by one.

After executing page address and both of the column address set operations data can be written to the selected location.
