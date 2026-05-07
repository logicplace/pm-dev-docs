# Display

Registers related to LCD settings and communication or rendering graphics.

## Startup contrast

$2000 bits 7~2 is a [reserved R/W register](../../../glossary.md#reserved-rw-register).

This is the contrast value set by the BIOS during startup [here](../../../software/bios/disasm.md#user-content-00A5).

This is managed from software through the use of these software interrupts:

* [Set contrast](../bios.md#set-startup-lcd-contrast) - store a new value and apply it
* [Step contrast](../bios.md#step--apply-startup-contrast) - step contrast up/down by 1 and apply it
* [Apply contrast](../bios.md#apply-startup-lcd-contrast) - just apply what's currently in this register, essentially recovering from [set temporary contrast](../bios.md#set-temporary-lcd-contrast)
* [Get contrast](../bios.md#get-startup-contrast)

It's important to note that being that this is a reserved R/W register, it does not directly drive or represent the current contrast the LCD is using. It *only* reflects the current value on the panel if software uses these interrupts to modify it.

## LCD controller

In order to use the [LCD Controller](../lcd_controller.md) at all, it must be enabled by setting $2080 bit 3 to 1. This allows it to render (if any other rendering is enabled) and also copies the frame to the LCD.

By default, it's disabled when entering software, set [here][prepare_boot].

The term "LCD Controller" comes from the [S1C88408][] and [S1C88409][] documentation. Although it appears to be a different system, it is the most similar. Note that these chips don't have a sprite system, so this page relates the tilemap to the bare system, whereas the technical manuals speak of the registers relating to the display as a whole.

[S1C88408]: ../s1c88/408.md
[S1C88409]: ../s1c88/409.md
[prepare_boot]: ../../../software/bios/disasm.md#user-content-prepare_boot
[RAM]: ../memory.md#ram

### Tilemap

Enable tilemap rendering by setting $2080 bit 1 to 1. Set the tileset base address in $2084~$2082 and set up the tilemap, though the map itself is part of [display RAM][RAM].

Every commercial game uses the tilemap, it's fundamental! The only reason for a homebrew game to not use the tilemap would be if it's directly driving the LCD.

#### Map size

The tilemap size must be set from a list of predefined sizes by assigning its associated index to $2080 bits 5~4. As a reminder, the screen size in tiles is 12 x 8. The default index, set [here][prepare_boot], is 0, which is 12 x 16.

| Index | Size (WxH) |
| ----- | ---------- |
| 0     | 12 x 16    |
| 1     | 16 x 12    |
| 2     | 24 x 8     |
| 3     | 24 x 16    |

12 x 16 is a good size for double buffering: rendering one frame starting at tile index 0 and the other starting at tile index 96, then switching between them using [Y scroll](#scrolling).

TODO: which games use which sizes when

The tilemap size is similar to the <abbr title="Address Pitch Adjustment">APADJ</abbr> register from the [S1C88408][]/[S1C88409][]. This register allows inserting a number of bytes to skip after sending a full line to the LCD, which allows for map sizes wider than 12 tiles.

The LBC register (unmapped) would be fixed at 12 (screen width / 8, so screen width in tiles), the SLT register (unmapped) would be fixed at 64 (screen height), and the <abbr title="Display Start Address">SAD</abbr> register (unmapped) would be fixed at $1000.

#### Scrolling

The map can be scrolled in both the X and Y directions by modifying the $2086 and $2087 registers, respectively. These registers represent a number of pixels to scroll, not tiles. These registers are 7-bit, so the technical maximum is 127, though no map size allows this.

These values do not wrap the screen but are instead soft capped to stay within the map size. Assigning a higher value will simply not scroll the screen.

| Index | Size (WxH) | Max X scroll | Max Y scroll |
| ----- | ---------- | ------------ | ------------ |
| 0     | 12 x 16    | 0            | 64           |
| 1     | 16 x 12    | 32           | 32           |
| 2     | 24 x 8     | 96           | 0            |
| 3     | 24 x 16    | 96           | 64           |

When either $2086 or $2087 is set, it checks if the value is valid within the current [map size](#map-size), and, if so, copies it to an internal register. Changing the map size does not validate the current values, and can cause the controller to render unexpected data as tiles. (TODO: check if it uses the current value internally or if it uses the current values in the scroll registers)

### Sprites

Enable sprite rendering by setting $2080 bit 2 to 1. Set the sprite set base address in $2089~$2087 then enable each sprite you want to use and set up the indexes and positions for them in [OAM][RAM].

## Frame rate

$2081 bits 7~4 is a read-only register and bits 3~1 is a R/W register.

Every time the [line counter](#lcd-line-counter) resets, the frame counter ($2081 bits 7~4) are increased by 1. When this value is >= a value indexed by $2081 bits 3~1 (`Divider` in the table below), the controller renders the frame and copies it to the LCD in stages.

According to the code for pokemini, when the line counter reaches 24 it renders the tiles and sprites. When it reaches 57 it starts sending the frame buffer to the LCD. (TODO: test ROM)

| $2081.3~1 | Divider |
|:---------:| ------- |
|   0 0 0   | 3       |
|   0 0 1   | 6       |
|   0 1 0   | 9       |
|   0 1 1   | 12      |
|   1 0 0   | 2       |
|   1 0 1   | 4       |
|   1 1 0   | 6       |
|   1 1 1   | 8       |

## LCDEN

$2081 bit 0 is a R/W register.

LCD Enable

This is controlled by the [LCD on][] and [LCD off][] software interrupts. If this isn't a [reserved R/W register](../../../glossary.md#reserved-rw-register), it controls the power supply to the LCD and messing with it directly could damage your LCD.

[LCD on]: ../bios.md#turn-lcd-on
[LCD off]: ../bios.md#turn-lcd-off

## LCD line counter

$208A bits 6~0 is a read-only register.

This value starts at 1 and counts up by 1 every time the [FR](../../board.md#user-content-lcd-29) pin goes low. It counts to 65 then on the next count it resets to 1.

## Direct LCD control

*For more information on using these registers, see their [main page](../../lcd)*

$20FE bits 7~0 (LCD_CTRL) and $20FF bits 7~0 (LCD_DATA) are R/W registers.

These registers directly drive the LCD bus pins (whether you're reading or writing, as well as which you're working with, drives the selection pins). Because of this and the way the LCD works, reading is subject to data ghosts and requires dummy reads.
