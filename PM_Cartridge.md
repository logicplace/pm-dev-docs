## Cartridge Overview

The Pokémon mini cartridge has a 21 bit addressing bus, which up until recently has gone completely unused. Since the PM has a relatively wide address space, it can provide up to a 2MB worth of data without additional hardware. One of the more bizzare design choices by Nintendo is that the cartridge address space starts relative to the beginning of the Pokémon mini's memory space, which is then overwritten by [BIOS](PM_Bios.md "wikilink"), [RAM](PM_RAM.md "wikilink") and [Internal Register](PM_Registers.md "wikilink"), making $2100 bytes of ROM space inaccessible except through mirrors.

After the overloaded memory space, the Pokémon mini has $D0 byte header standard. The vast majority of this space is reserved for IRQ jump locations. Much of the remaining space is plain asciiz info about the game, with a couple of BIOS checked watermarks to verify a ROM is a PM image.

Following the header is completely user mapped data. It is typical for the reset IRQ location to simply jump to $21D0. The IRQ locations are 6 bytes in size to accommodate for a U load (3 bytes) and a long jump (3 bytes)

## Cartridge Header

| Location | Size | Required | Description                   |
| -------- | ---- | -------- | ----------------------------- |
| $2100    | 2    | No       | "PM" marker                   |
| $2102    | 6    | Yes      | Reset Location                |
| $2108    | 6    | \*       | PRC Frame Copy IRQ            |
| $210e    | 6    | \*       | PRC Render IRQ                |
| $2114    | 6    | \*       | Timer 2 Underflow (upper) IRQ |
| $211a    | 6    | \*       | Timer 2 Underflow (lower) IRQ |
| $2120    | 6    | \*       | Timer 1 Underflow (upper) IRQ |
| $2126    | 6    | \*       | Timer 1 Underflow (lower) IRQ |
| $212c    | 6    | \*       | Timer 3 Underflow (upper) IRQ |
| $2132    | 6    | \*       | Timer 3 Comparator IRQ        |
| $2138    | 6    | \*       | 32hz Timer (256hz linked) IRQ |
| $213e    | 6    | \*       | 8hz Timer (256hz linked) IRQ  |
| $2144    | 6    | \*       | 2hz Timer (256hz linked) IRQ  |
| $214a    | 6    | \*       | 1hz Timer (256hz linked) IRQ  |
| $2150    | 6    | \*       | IR Receiver IRQ               |
| $2156    | 6    | \*       | Shake Sensor IRQ              |
| $215c    | 6    | \*       | Power Key IRQ                 |
| $2162    | 6    | \*       | Right Key IRQ                 |
| $2168    | 6    | \*       | Left Key IRQ                  |
| $216e    | 6    | \*       | Down Key IRQ                  |
| $2174    | 6    | \*       | Up Key IRQ                    |
| $217a    | 6    | \*       | C Key IRQ                     |
| $2180    | 6    | \*       | B Key IRQ                     |
| $2186    | 6    | \*       | A Key IRQ                     |
| $218c    | 6    | \*       |                               |
| $2192    | 6    | \*       |                               |
| $2198    | 6    | \*       |                               |
| $219e    | 6    | \*       | Cartridge IRQ                 |
| $21A4    | 8    | Yes      | "NINTENDO" in plain text      |
| $21AC    | 4    | No       | Game Code                     |
| $21B0    | 12   | No       | Game Title (Zero Padded)      |
| $21BC    | 2    | No       | "2P" (Unknown purpose)        |
| $21BE    | 18   | No       | Reserved (Zero)               |

\* = This is only required if the IRQ is ever enabled.
