# Memory

The Pokémon mini has a 24-bit internal addressing bus. The entire bus is decoded, and thus only cartridge memory mirrors. Externally, the cartridge bus is only 21 bits wide, so anything at or past $200000 is guaranteed to be a mirror of cartridge memory.

| Start   | End     | Size    | Description                    |
| ------- | ------- | ------- | ------------------------------ |
| $000000 | $000FFF | 4 KiB   | [Internal BIOS][]              |
| $001000 | $001FFF | 4 KiB   | [RAM][]                        |
| $002000 | $0020FF | 256 B   | [Hardware Registers][]         |
| $002100 | $1FFFFF | \~2 MiB | [Cartridge Memory][]           |
| $200000 | $FFFFFF | mirrors | [Cartridge Memory][] (mirrors) |

TODO: accessing higher cartridge memory on the PM2040 and its derivatives

[Internal BIOS]: #internal-bios
[RAM]: #ram
[Hardware Registers]: #hardware-registers
[Cartridge Memory]: #cartridge-memory

[LCD Controller]: LCD_Controller.md
[MINLIB]: ../../software/minlib.md

## Internal BIOS

*For more information on the BIOS, see its [main page](bios.md)*

The CPU stores the BIOS on a 4 KiB internal mask ROM. This means that while it can be read out, it cannot be reflashed. It's mapped to $000000-$001000.

The BIOS contains the interrupt vector table which eventually jump into [Cartridge Memory][], startup routines, subroutines used for interacting with the console hardware safely, subroutines for the official development cartridge, and the code and graphics for the "insert cartridge" and "low battery" screens.

The BIOS *does not* contain code for the [LCD Controller][] (which is likely microcode) nor the game title/copyright screens (these are in [MINLIB][]).

## RAM

The memory used in the Pokémon mini is general purpose static RAM. It is high speed and there is no performance hit for accessing it other than the instruction processing speed. The biggest problem with the system is that the RAM is small, only 4 KiB, and also shared with the [LCD Controller][]. Sections of this memory can be disabled, but up to 1248 bytes can be repurposed for video.

"General Purpose Memory" as listed in the tables below is considered unused and is safe for all use at any time. Disabling various parts of the [LCD Controller][] can free up additional memory.

If the frame buffer is disabled, the entire controller is disabled. The sprites and map can be disabled individually, however it's not recommended to disable the map yet enable sprites outside very special use cases. Should you disable either, those spaces in the below table are available for you to use generally. The start of the tile map does not move if only sprites are disabled.

The map size also affects available memory. For the 24x16 map size, selected by setting MAPSIZ to 3, the tile map area is 384 bytes. For every other size, the tile map area is 192 bytes.

| Start | End   | Size       | Description            |
| ----- | ----- | ---------- | ---------------------- |
| $1000 | $12FF | 768 bytes  | [Frame Buffer][]       |
| $1300 | $135F | 96 bytes   | [Sprite Attributes][]  |
| $1360 | $141F | 192 bytes  | [Tile Map][]           |
| $1420 | $14DF | 192 bytes  | [Tile Map][] (mode 3)  |
| $14E0 | $1FFF | 2848 bytes | General Purpose Memory |

[Frame Buffer]: [LCD_Controller.md#frame-copy-stage]
[Sprite Attributes]: [LCD_Controller.md#sprite-rendering-stage]
[Tile Map]: [LCD_Controller.md#map-rendering-stage]

Typically a game has copy, sprites, and map enabled and doesn't use a MAPSIZ of 3. This would have general purpose memory start at $1420. Because it starts at $14E0 with the maximal allocation for the LCD Controller, the official EPSON locator will allocate your declared variables after $14E0, though you can access the other space directly or by using the `_at` attribute in C during the declaration (TODO: check whether the locator complains and whether or not there's a way to get around that, maybe volatile).

With pm.h, you can disable everything by simply doing `PRC_MODE = 0` though this will also reset the MAPSIZ to 12x16 and disable INVMAP. If you want to temporarily disable the driver, use `PRC_MODE &= ~COPY_ENABLE` and then `PRC_MODE |= COPY_ENABLE` to reenable it. You can use that same structure to disable/enable sprites and the tile map with `SPRITE_ENABLE` and `MAP_ENABLE` respectively.

## Hardware Registers

*For a full list of hardware registers, see its [main page](Registers.md)*

The hardware registers are mapped to $002000-$0020FF. Typically they're access by setting the BR register to $20 and using operations which work on `[BR:ll]` where *ll* is the lower byte, which indicates the register to access. However, those operations only work on one byte at a time, so two access both bytes of two byte registers, you need to use, for example, `[$2030]` for TMR1_CTRL.

## Cartridge Memory

The Pokémon mini cartridge has a 21 bit addressing bus, allowing it to provide up to a 2MB worth of data without additional hardware.

The first $2100 bytes are "overwritten" by the BIOS, RAM, and register mappings. The original data can instead be accessed from the mirrors, such as by using the addresses $200000-$2020FF. Starting at $002100 is the cartridge header followed by user data.

### Cartridge Header

| Location | Size | Required | Description                   |
| -------- | ---- | -------- | ----------------------------- |
| $2100    | 2    | No       | `MN` marker                   |
| $2102    | 6    | Yes      | Reset Location                |
| $2108    | 6    | \*       | PRC Frame Copy IRQ            |
| $210E    | 6    | \*       | PRC Render IRQ                |
| $2114    | 6    | \*       | Timer 2 Underflow (upper) IRQ |
| $211A    | 6    | \*       | Timer 2 Underflow (lower) IRQ |
| $2120    | 6    | \*       | Timer 1 Underflow (upper) IRQ |
| $2126    | 6    | \*       | Timer 1 Underflow (lower) IRQ |
| $212C    | 6    | \*       | Timer 3 Underflow (upper) IRQ |
| $2132    | 6    | \*       | Timer 3 Comparator IRQ        |
| $2138    | 6    | \*       | 32hz Timer (256hz linked) IRQ |
| $213E    | 6    | \*       | 8hz Timer (256hz linked) IRQ  |
| $2144    | 6    | \*       | 2hz Timer (256hz linked) IRQ  |
| $214A    | 6    | \*       | 1hz Timer (256hz linked) IRQ  |
| $2150    | 6    | \*       | IR Receiver IRQ               |
| $2156    | 6    | \*       | Shake Sensor IRQ              |
| $215C    | 6    | \*       | Power Key IRQ                 |
| $2162    | 6    | \*       | Right Key IRQ                 |
| $2168    | 6    | \*       | Left Key IRQ                  |
| $216E    | 6    | \*       | Down Key IRQ                  |
| $2174    | 6    | \*       | Up Key IRQ                    |
| $217A    | 6    | \*       | C Key IRQ                     |
| $2180    | 6    | \*       | B Key IRQ                     |
| $2186    | 6    | \*       | A Key IRQ                     |
| $218C    | 6    | \*       |                               |
| $2192    | 6    | \*       |                               |
| $2198    | 6    | \*       |                               |
| $219E    | 6    | \*       | Cartridge IRQ                 |
| $21A4    | 8    | Yes²     | `NINTENDO` in plain text      |
| $21AC    | 4    | No       | Game Code                     |
| $21B0    | 12   | No       | Game Title (Zero Padded)      |
| $21BC    | 2    | No       | `2P` (Unknown purpose)        |
| $21BE    | 18   | No       | Reserved (Zero)               |

* \* = This is only required if the IRQ is ever enabled.
* ² = This is not required for freebios

### MN marker

For all release games this is `MN` however for the dev cart (as indicated in the BIOS) this is the hex sequence `BF D9` which is the [product identification](../dev_cart.md#chip-details) of the cart's flash chip.

### IRQs

When an IRQ is triggered, you must write a 1 to its factor flag before calling RETE (or modifying the interrupt flags) or else it will continuously trigger.

To fill in an IRQ as unused, you can use the following code:

```asm
LD BR, #20h       ; 2 bytes, This presumes it's ok to set BR to $20h whenever
OR [BR:ll], FLAG  ; 3 bytes, Fill in ll and FLAG as appropriate
RETE              ; 1 byte
```

But if this doesn't fit your needs, it can be 00s if you ensure you never enable that IRQ, or otherwise you can perform a far jump to code which handles it. startup.asm provides a `JP_FAR` macro for this.

### Game code

The game code is a 4 letter code of the form `MxxL` where:

* `M` presumably stands for Mini
* `xx` is a two letter shorthand of the game name
  * `AC` - Anime Card \[Daisakusen] (Zany Cards)
  * `BR` - Pichu Bros
  * `LT` - Lunch Time
  * `PB` - Pinball
  * `PT` - Party
  * `PZ` - Puzzle
  * `RC` - Race
  * `SD` - Sodate (Breeder)
  * `ST` - Shock Tetris
  * `TA` - Togepi's Adventure
  * `Z2` - Puzzle 2
* `L` is the one letter language code:
  * `D` - Deutsch (German)
  * `E` - English
  * `F` - French
  * `J` - Japanese
  * `P` - Multi-language (Plural?)

The language code is checked by [MINLIB][] to determine which copyright screen to display, though it only checks whether it's `J` or not.

Many homebrew use a four letter shorthand for the game instead, but I recommend sticking to this form and simply using `H` instead of `M` for the first letter, which stands for Homebrew.

### Game title

The title is a 12 character name, 00-padded, encoded in single byte Shift JIS with some variation. This name is written to the save file and rendered when selecting a save slot to delete.

Maximal encoding (each character that appears in at least two official games):

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 1 |^_^|>_<|OoO|   |   |-_-|   |   |   |   |   |   |   |   |   |   |
| 2 |   | ! | " | # | $ | % | & | ' | ( | ) | * | + | , | - | . | / |
| 3 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | : | ; | < | = | > | ? |
| 4 | @ | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| 5 | P | Q | R | S | T | U | V | W | X | Y | Z | [ | ¥ | ] | ^ | _ |
| 6 | ` | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o |
| 7 | p | q | r | s | t | u | v | w | x | y | z | { |\| | } | ~ |   |
| 8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| A |   | ｡ | ｢ | ｣ | ､ | ･ | ｦ | ｧ | ｨ | ｩ | ｪ | ｫ | ｬ | ｭ | ｮ | ｯ |
| B | ｰ | ｱ | ｲ | ｳ | ｴ | ｵ | ｶ | ｷ | ｸ | ｹ | ｺ | ｻ | ｼ | ｽ | ｾ | ｿ |
| C | ﾀ | ﾁ | ﾂ | ﾃ | ﾄ | ﾅ | ﾆ | ﾇ | ﾈ | ﾉ | ﾊ | ﾋ | ﾌ | ﾍ | ﾎ | ﾏ |
| D | ﾐ | ﾑ | ﾒ | ﾓ | ﾔ | ﾕ | ﾖ | ﾗ | ﾘ | ﾙ | ﾚ | ﾛ | ﾜ | ﾝ | ゛| ゜|

Safe characters (represented in every official game):

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 2 |   | ! | " | # | $ | % | & | ' | ( | ) | * | + | , | - | . | / |
| 3 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | : | ; | < | = | > | ? |
| 4 | @ | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| 5 | P | Q | R | S | T | U | V | W | X | Y | Z |   |   |   |   |   |
| 6 |   | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o |
| 7 | p | q | r | s | t | u | v | w | x | y | z |   |   |   |   |   |
| 8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| A |   |   |   |   |   |   | ｦ | ｧ | ｨ | ｩ | ｪ | ｫ | ｬ | ｭ | ｮ | ｯ |
| B | ｰ | ｱ | ｲ | ｳ | ｴ | ｵ | ｶ | ｷ | ｸ | ｹ | ｺ | ｻ | ｼ | ｽ | ｾ | ｿ |
| C | ﾀ | ﾁ | ﾂ | ﾃ | ﾄ | ﾅ | ﾆ | ﾇ | ﾈ | ﾉ | ﾊ | ﾋ | ﾌ | ﾍ | ﾎ | ﾏ |
| D | ﾐ | ﾑ | ﾒ | ﾓ | ﾔ | ﾕ | ﾖ | ﾗ | ﾘ | ﾙ | ﾚ | ﾛ | ﾜ | ﾝ | ゛| ゜|

* 0x, 1x, 7F, 8x, 9x, A0, Ex, and Fx are generally garbage data or other tiles for the save selection screen
* 20 is the intentional space character
* Only Pinball, Race, and Togepi support the emotes in 1x
* Party & Pichu Bros: Missing `｡｢｣､･`
* Pinball: Missing ``[¥]^_`{|}~``
  * Adds bolded `0123456789ABCDEF` as Ex row
* Lunch Time & Tetris: Missing `` `{|}~ ``
* Puzzle & Puzzle 2: Missing ``[¥]^_`{|}~``
* Race & Sodate: Missing ``[¥]^_`{|}~``
  * Junk data in 5B-5E (`[¥]^`)
* Togepi: Missing ``[¥]^_`{|}~``
  * Junk data in 5B-5F (`[¥]^`)
