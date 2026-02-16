# Official flash cartridge

Much of the BIOS is dedicated to handling an official flash cart using a SST39LF016 or SST39VF016 (or possibly SST39VN016) chip. Since the screen says "GAME SELECT" we can presume it's either a flash cart intended for developers, a demo cart for displays, or possibly the [sample cart](#sample-cart) with some caveats.

It's designed to hold up to 8 games of 256 KiB each (or fewer, larger games). As such (along with other evidence), each bank is presumably 256 KiB. Because banks can be mixed and matched, it would be theoretically possible to store more than 8 games on it if they had common code (for example, MINLIB) but the selection menu isn't designed for that case.

## Sample cart

The sample cart is a flash cartridge distributed to (likely) reporters in Japan at the time. One sample cart (00954) has been dumped, which contained the full release version of Pokémon Party mini (JP).

These contain a SST39VN016-120-4C-WH flash chip which is a 32-pin version of the typically 40-pin SST39VF016. However it should be software compatible, so even if the code does not refer to this chip, it should be mostly compatible.

* SST - Manufacturer (Silicon Storage Technology, Inc.)
* 39 - Product Series: Multi-Purpose Flash
* V - 2.7-3.6V
* N - ???
* 016 - Device Density: 16 Megabit (2 MiB)
* 120 - Read Access Speed: 120 ns
* 4 - Minimum Endurance: 10,000 cycles
* C - Temperature Range: Commercial (0⁰C to +70⁰C)
* W - Package Type: TSOP
* H - Package Modifier: 32 leads

The circuit board however does not contain a separate mapper chip and there definitely should be a mapper. However, it's possible that the chip contains the mapper as well.

## Chip details

[SST39LF/VF016 Data Sheet](https://www.backoldgaming.com/data/medias/files/39vf016/SST39VF080_SiliconStorageTechnology.pdf)

Although the exact part number hasn't been confirmed, the product ID is 0xBFD9 which corresponds to:

* BF - Manufacturer's ID: SST
* D9 - Device ID: SST39LF/VF016

Considering the [sample cart](#sample-cart), we can presume it uses the SST39VF016 chip if not the SST39VN016 chip.

It's a 2 MiB chip matching the addressable limit of the PM. The mapper separates this space into 8 configurable banks of 256 KiB offering 4 data pages (or 8 code banks) per external bank/page (what the mapper considers a page).

### Commands

The BIOS implements routines to access most of the chip commands as well as 3 mapper commands. It's unclear when or why official software may have used these software interrupts.

| Command               | INT [kk] | Addr 1 | Data 1 | Addr 2 | Data 2 | Addr 3 | Data 3 | Addr 4 | Data 4 | Addr 5 | Data 5 | Addr 6 | Data 6 |
| --------------------- |:--------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| [Program byte][]      |   88h    | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  A0h   |   \*   |   \*   |        |        |        |        |
| [Erase sector][]      |   8Ah    | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  80h   | $5555  |  AAh   | $2AAA  |  55h   |   \*   |  30h   |
| [Erase block][]       |    -     | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  80h   | $5555  |  AAh   | $2AAA  |  55h   |   \*   |  50h   |
| [Erase chip][]        |    -     | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  80h   | $5555  |  AAh   | $2AAA  |  55h   |   \*   |  10h   |
| [Software ID entry][] |   84h    | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  90h   |        |        |        |        |        |        |
| [CFI query entry][]   |    -     | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  98h   |        |        |        |        |        |        |
| [Reset][]             |    -     |   \*   |  F0h   |        |        |        |        |        |        |        |        |        |        |
| also [Reset][]        |   86h    | $5555  |  AAh   | $2AAA  |  55h   | $5555  |  F0h   |        |        |        |        |        |        |

[Program byte]: #program-byte
[Erase sector]: #erase-sector
[Erase block]: #erase-block
[Erase chip]: #erase-chip
[Software ID entry]: #software-id-entry
[CFI query entry]: #cfi-query-entry
[Reset]: #reset

#### Program byte

Write a single byte to the given address.

Usable from software via:

```s1c88
LD XP, #(data page)
LD IX, #(address)
LD A, #(byte to write)
INT [88h]
OR A, A
JRS NZ, write_successful
```

In order to write to $000000~$0020FF you'll need to remap the bank to another external page first.

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0xA0
* write address <- data byte

The BIOS does use this to track plays in a ridiculous manner.

#### Erase sector

Erase a 4 KiB sector (at 4 KiB boundaries).

Usable from software via:

```s1c88
LD XP, #(data page) ; any address in the sector
LD IX, #(address)   ; ...
INT [8Ah]
OR A, A
JRS NZ, erase_successful
```

In order to erase sector 0 or 1 you'll need to remap bank 0 to another external page first.

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x80
* $5555 <- 0xAA
* $2AAA <- 0x55
* sector address <- 0x30

The BIOS does NOT use this routine.

#### Erase block

Erase a 64 KiB sector (at 64 KiB boundaries).

In order to erase block 0 you'll need to remap bank 0 to another external page first.

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x80
* $5555 <- 0xAA
* $2AAA <- 0x55
* sector address <- 0x50

The BIOS does NOT implement or use this command.

#### Erase chip

Erase the entire chip.

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x80
* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x10

The BIOS does NOT implement or use this command.

#### Software ID entry

Enter Product Identification Mode which is used to read back the product identification.

Usable from software via:

```s1c88
INT [92h] ; prepare mapper for reading result
INT [84h]
INT [86h] ; exit Software ID Mode
; B contains the manufacturer's ID
; A contains the device ID
```

The raw command sequence (for just this part) is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x90

The BIOS does use this to identify whether or not the inserted cart is a dev cart.

#### CFI query entry

Enter <abbr title="Common Flash Memory Interface">CFI</abbr> Mode which is used to query extended device information.

In order to read the result from software you will need to use the [remap IDs command](#remap-ids).

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0x98

After enabling this mode, read from certain addresses to get information about the chip:

| Address | Data\*   | Description                                                                                                            |
| ------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| $10~$12 | 0x515259 | Query Unique ASCII string `QRY`                                                                                        |
| $13~$14 | 0x0107   | Primary OEM command set                                                                                                |
| $15~$16 | 0x0000   | Address for Primary Extended Table                                                                                     |
| $17~$18 | 0x0000   | Alternate OEM command set (0 = none exists)                                                                            |
| $19~$1A | 0x0000   | Address for Alternate OEM extended Table (0 = none exits)                                                              |
| $1B     | 0x27     | VDD Min (Program/Erase) DQ7-DQ4: Volts, DQ3-DQ0: 100 millivolts                                                        |
| $1C     | 0x36     | VDD Max (Program/Erase) DQ7-DQ4: Volts, DQ3-DQ0: 100 millivolts                                                        |
| $1D     | 0x00     | VPP min. (00H = no VPP pin)                                                                                            |
| $1E     | 0x00     | VPP max. (00H = no VPP pin)                                                                                            |
| $1F     | 0x04     | Typical time out for [Byte-Program](#program-byte) 2ᴺ µs (2⁴ = 16 µs)                                                  |
| $20     | 0x00     | Typical time out for min. size buffer program 2ᴺ µs (0 = not supported)                                                |
| $21     | 0x04     | Typical time out for individual [Sector](#erase-sector)/[Block-Erase](#erase-block) 2ᴺ ms (2⁴ = 16 ms)                 |
| $22     | 0x06     | Typical time out for [Chip-Erase](#erase-chip) 2ᴺ ms (2⁶ = 64 ms)                                                      |
| $23     | 0x01     | Maximum time out for [Byte-Program](#program-byte) 2ᴺ times typical (2¹ x 2⁴ = 32 µs)                                  |
| $24     | 0x00     | Maximum time out for buffer program 2ᴺ times typical (0 = not supported)                                               |
| $25     | 0x01     | Maximum time out for individual [Sector](#erase-sector)/[Block-Erase](#erase-block) 2ᴺ times typical (2¹ x 2⁴ = 32 ms) |
| $26     | 0x01     | Maximum time out for [Chip-Erase](#erase-chip) 2ᴺ times typical (2¹ x 2⁶ = 128 ms)                                     |
| $27     | 0x15     | Device size = 2ᴺ Bytes (15H = 21; 2²¹ = 2 MiB)                                                                         |
| $28~$29 | 0x0000   | Flash Device Interface description; 0000H = x8-only asynchronous interface                                             |
| $2A~$2B | 0x0000   | Maximum number of byte in multi-byte write = 2ᴺ (00H = not supported)                                                  |
| $2C     | 0x02     | Number of Erase Sector/Block sizes supported by device                                                                 |
| $2D~$30 |0xFF011000| Sector Information: 512 (0x0200) sectors; 16 (0x0010) * 256 B = 4 KiB/sector                                           |
| $31~$34 |0x1F000001| Block Information: 32 (0x0020) blocks; 256 (0x0100) * 256 B = 64 KiB/block                                             |
\* Note that since the chip is not confirmed, all data is unconfirmed as well. The provided data is what's expected from a SST39LF/VF016 chip.

The BIOS does NOT implement or use this command.

#### Reset

Exit any special modes and reset the device to a normal read state.

Usable from software via:

```s1c88
INT [86h]
```

The raw command sequence (for just this part) is either:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0xF0

or

* any address <- 0xF0

The BIOS does use this to exit the Product Identification Mode as well as to end mapper modes.

#### Remap IDs

This is a mapper command which causes access to *at least* $2100 and $2101 to be remapped to reading the physical addresses $000000 and $000001, respectively. Because the BIOS regularly remaps external page 1 to read from bank 0, this command likely has a size limitation of less than an external page size, possibly of one sector (0x001000 bytes).

Usable from software via:

```s1c88
INT [92h]
; other commands
INT [86h] ; exit remap
```

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0xC0

The BIOS uses this to be able to read the product identification.

#### Enable remapping page 0

Normally assignments to $03FFFF when the mapper is in [bank select mode](#enter-bank-select-mode) are (presumably) ignored. However, calling this first will allow reassigning external page 0 to read from another bank.

Usable from software via:

```s1c88
INT [90h]
INT [8Ch] ; enter bank select mode
LD XP, #03h
LD XI, #0FFFFh
LD [XI], #(bank ID)
INT [86h] ; exit special modes
```

The raw command sequence (for just this) is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0xC9

The BIOS uses this if the selected game remaps page 0 (but not if it marks it as disabled).

#### Enter bank select mode

Use this mode to configure which bank each external page reads from. To configure page 0, [unlock that capability](#enable-remapping-page-0) first.

Usable from software via:

```s1c88
INT [8Ch]
LD XP, #(final data page in external page)
LD XI, #0FFFFh
LD [XI], #(bank ID)
INT [86h] ; exit bank select mode
```

The raw command sequence is:

* $5555 <- 0xAA
* $2AAA <- 0x55
* $5555 <- 0xD0

The bank select register addresses for each page are:

| Page | Register address | Data pages | Code pages |
| ----:| ---------------- | ---------- | ---------- |
|    0 | $03_FFFF         | $00~$03    | $00~$07    |
|    1 | $07_FFFF         | $04~$07    | $08~$0F    |
|    2 | $0B_FFFF         | $08~$0B    | $10~$17    |
|    3 | $0F_FFFF         | $0C~$0F    | $18~$1F    |
|    4 | $13_FFFF         | $10~$13    | $20~$27    |
|    5 | $17_FFFF         | $14~$17    | $28~$2F    |
|    6 | $1B_FFFF         | $18~$1B    | $30~$37    |
|    7 | $1F_FFFF         | $1C~$1F    | $38~$3F    |

The BIOS uses this when booting software from the Game Select screen.

## Layout

This section covers all the memory locations the BIOS accesses in order to perform functions related to the dev cart and what they're for. These locations will often have multiple addresses. The *physical address* is the address where data resides on ROM, either in the flash chip or in the BIOS. The *logical address* is the address that data is being accessed through, which is translated to a physical address either by the S1C88 itself or the mapper on the cartridge, or both. All relevant addresses will be documented. Since the banks are configurable and there's theoretically 8 possible logical addresses for each one, only the one the BIOS uses will be listed.

Entries with no physical address below are either RAM locations or mapper registers.

| Physical address space | Logical address | Description                |
| ---------------------- | --------------- | -------------------------- |
|                        | $0014E0         | [Remaining plays][]        |
|                        | $0014E2~$00152C | [Game Select variables][]  |
|                        | $0014E4         | [Game structs (RAM)][]     |
|                        | $0019D0~$001C10 | [Game name tiles][]        |
|                        | $2001           | [$2001][]                  |
| $0000~$0001\*          | $002100~$002101 | [Product identification][] |
|                        | $002AAA         | [JEDEC SDP address][]      |
|                        | $005555         | [JEDEC SDP address][]      |
|                        | $03FFFF         | [Bank select register][]   |
| $1000~$12FF            | $041000~$0412FF | [Game structs][]           |
| $1300                  | $041300         | [Startup action][]         |
| $1400+                 | $041400+        | [Startup routine][]        |
|                        | $07FFFF         | [Bank select register][]   |
|                        | $0BFFFF         | [Bank select register][]   |
|                        | $0FFFFF         | [Bank select register][]   |
|                        | $13FFFF         | [Bank select register][]   |
|                        | $17FFFF         | [Bank select register][]   |
|                        | $1BFFFF         | [Bank select register][]   |
|                        | $1FFFFF         | [Bank select register][]   |
\* In [Product Identification Mode](#software-id-entry)

[Remaining plays]: #remaining-plays
[Game Select variables]: #game-select-variables
[Game structs (RAM)]: #game-structs-ram
[Game name tiles]: #game-name-tiles
[$2001]: #2001
[Product identification]: #product-identification
[JEDEC SDP address]: #software-data-protection
[Bank select register]: #enter-bank-select-mode
[Game structs]: #game-structs
[Startup action]: #startup-action
[Startup routine]: #startup-routine
[Game Select screen]: ./cpu/bios.md#game-select-screen

### Remaining plays

Stored in RAM at $14E0

This was called the "cart type" in previous documentation. In reality, it represents the number of remaining plays until a game is removed from the [Game Select screen][]. This count is not visible on the screen. It can be set dynamically by the [startup routine][] and is forwarded to the game software in the A register (it's no longer accessible from $14E0 after the software starts as the RAM is cleared).

This value can be:

* 0xFE - developer cart (unlimited play)
* 0xFF - normal/unrecognized cartridges
* 0x00~0x77 - number of remaining plays (0 = none left, removed from menu)

### Game Select variables

There are several variables in RAM which control the [Game Select screen][]:

| Name                   | Size | Address |
| ---------------------- | ----:| ------- |
| [RemainingPlays][]     |  1 B | $14E0   |
| NumGameStructs         |  1 B | $14E2   |
| LoopN                  |  1 B | $14E3   |
| [GameStructs][]        | 64 B | $14E4   |
| NextGameStruct         |  2 B | $1524   |
| NextTilePos            |  2 B | $1526   |
| CurrentRowStart        |  1 B | $1528   |
| FinalNameRowStartMin48 |  1 B | $1529   |
| FinalNameRowStart      |  1 B | $152A   |
| MoveCooldown           |  1 B | $152B   |
| KeyHistory             |  1 B | $152C   |

For the details of what these do, read the disassembly [here](../software/bios/disasm.md).

[RemainingPlays]: #remaining-plays
[GameStructs]: #game-structs-ram

### Game structs (RAM)

Stored in RAM starting at $14E4

This is an array of 8 byte structures which contains up to 8 entries. It does not directly correlate to the [game structs][] which are stored on ROM, but does refer to them.

| Offset  | Description                             |
| -------:| --------------------------------------- |
|     $00 | Game index on cart                      |
|     $01 | Number of plays remaining               |
|     $02 | "Remaining plays" byte to write on play |
| $04~$03 | Where to write $02                      |
| $05~$07 | padding                                 |

### Game name tiles

This is standard [tile graphics](./cpu/lcd_controller.md) written to memory from the [game structs][]

### $2001

The lower 4 bits of this hardware register which are mapped as general purpose contain some information about game selection.

* 0bxxxxVGGG
  * x not relevant
  * V: bits 2~0 are a valid game index
  * GGG: the index of the selected game
  * If V is 0, a value of xx1 in GGG indicates that startup action 2 was used.

### Product identification

The manufacturer and device IDs are accessed by [remapping](#remap-ids) the earliest address which goes over the cartridge bus ($2100) to $0000, where the product IDs are actually read from the chip.

The returned data is discussed [here](#chip-details). It's possible to fake being a development cartridge by specifying `BF D9` at $2100 instead of `77 78` (`MN`) in a statically mapped ROM.

### Software Data Protection

The chip provides the <abbr title="Joint Electron Device Engineering Council">JEDEC</abbr>-approved <abbr title="Software Data Protection">SDP</abbr> scheme for all data alteration options: [writing bytes](#program-byte) and all [erase](#erase-sector) operations.

Specifically, this refers to the sequence of specific writes alternating between $5555 and $2AAA which maximize entropy in order to minimize the probability of accidental write operations.

Refer to the sequences [listed above](#commands) and [flash_begin_cmd](../software/bios/disasm.md#user-content-flash_begin_cmd) which extracts the common write cycles.

### Game structs

These are stored at the physical address $001000 and accessed through $041000 by the BIOS after remapping external page 1 to access bank 0.

Notably, $1000 is the first address after the BIOS. However, it's unknown if a software-level BIOS was ever possible.

This is an array of 96 byte structures which contains 8 entries. Any entry which does not contain real data should be filled with 0x00 or 0xFF.

| Offset  | Description                                     |
| -------:| ----------------------------------------------- |
| $00~$47 | Game name tile graphics (9 tiles)               |
| $48~$4F | External page -> bank mapping                   |
|     $50 | 0xFF/0x00 = skip, 0xFE = unlimited, * = limited |
| $51~$5F | Remaining plays (base 1)                        |

The game name tiles are [copied to RAM](#game-name-tiles) by [this subroutine](../software/bios/disasm.md#user-content-gsm__ldl__load_name_tiles).

When the game is selected to be played from the menu, the BIOS loads the selected game's ID into [$2001][], [maps the banks](../software/bios/disasm.md#user-content-_flash_prepare_game), and, if this is limited play, [writes the decremented number of plays byte](../software/bios/disasm.md#user-content-run_selected_game).

While offset $50 being 0x00 or 0xFF causes the game loading code to skip the entry, this is likely less of an itentional identifier and more likely that it's looking for cleared data. A value of 0xFE skips checking/writing to the remaining plays information, effectively providing infinite plays. Any other value (0x01~0xFD) is treated as a limited play entry, and nothing is known about what the intended values might be nor any finer meanings.

For whatever god forsaken reason, they decided to implement the remaining plays over 15 bytes in base 1 (tally marks!!). The [subroutine](../software/bios/disasm.md#user-content-0642) first checks the <abbr title="Most Significant Bit">MSB</abbr> of the first byte to extrapolate that any are set, then loops through each byte <abbr title="Most Significant Bit">MSB</abbr> to <abbr title="Least Significant Bit">LSB</abbr>, stopping at the first 0 encountered. It then removes the 1 prior to the 0 found, storing that change and its address in [RAM](#game-structs-ram) to later be written should the user select this game.

While to some extent the remaining plays bytes allow non-sequential bits containing 1s, they're effectively ignored. For whatever reason, the system is designed to [intentionally](../software/bios/disasm.md#user-content-0671) lose a byte of data if all 15 bytes are full, so a value of 120 would reduce to 111 after playing, despite reporting 119 to the software in A. This makes the effective maximum number of plays 119 instead of 120.

If "base 1" is unclear, the values look like this:

* 0b10000000 = 1
* 0b11000000 = 2
* 0b11100000 = 3
* ...

### Startup action

This byte is stored at the physical address $001300 and accessed through $041300 by the BIOS after remapping external page 1 to access bank 0.

#### Startup action 0

Runs the [startup routine][] then writes A to [RemainingPlays][] and proceeds to the copyright check to continue booting. [code](../software/bios/disasm.md#user-content-05E5)

Using this action does not affect the value of [$2001][].

#### Startup action 1

Runs the [startup routine][] then writes A to [RemainingPlays][] and proceeds to the copyright check to continue booting. [code](../software/bios/disasm.md#user-content-05E5)

When calling `INT [68h]`, requires the [$2001][] to be set as a valid game ID. This means the startup routine must set one.

When calling `INT [6Ah]`, this does not prepare any game for boot.

#### Startup action 2

Prepares bank selections for game 0, writes 0b0001 to [$2001][], writes 0xFF to [RemainingPlays][], then proceeds to the copyright check to continue booting. [code](../software/bios/disasm.md#user-content-05F6)

#### Startup action 3

Loads the [Game Select screen][].

When calling `INT [68h]`, requires the [$2001][] to be set as a valid game ID. This is true so long as the selected software doesn't alter the contents.

When calling `INT [6Ah]`, this does not prepare any game for boot.

### Startup routine

This is code stored at the physical address $001400 and accessed through $089400 (if it were data, $041400) by the BIOS after remapping external page 1 to access bank 0. This has 3328 bytes available as space.

The [startup action][] is available in A. The subroutine must return the value to be placed in the [remaining plays][] in A and it may clobber any registers, but must be careful about RAM access. Prefer to create any new variables starting at $1C10 (ideal) or $152D (overwriting animation variables, which *shouldn't* be necessary anymore).

It's unclear the exact intention of what this routine should do, but when startup action 1 is used this does need to set a valid game ID in [$2001][].
