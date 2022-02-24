The Pokémon mini has a 24-bit internal addressing bus. The entire bus is decoded, and thus nothing mirrors except cartridge memory. Externally, the cartridge bus is only 21 bits wide, so anything at or past $20000 is guaranteed to be a mirror of cartridge memory.

## Pokémon mini Memory Map

| Start   | End     | Size            | Description                                             |
| ------- | ------- | --------------- | ------------------------------------------------------- |
| $000000 | $000FFF | $001000 (4KB)   | [Internal BIOS](PM_Bios.md "wikilink")                  |
| $001000 | $001FFF | $001000 (4KB)   | [PM RAM](PM_RAM.md "wikilink")                          |
| $002000 | $0020FF | $000100 (256B)  | [Hardware Registers](PM_Registers.md "wikilink")        |
| $002100 | $1FFFFF | $1FDF00 (\~2MB) | [Cartridge Memory](PM_Cartridge.md "wikilink")          |
| $200000 | $3FFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $400000 | $5FFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $600000 | $7FFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $800000 | $9FFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $A00000 | $BFFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $C00000 | $DFFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
| $E00000 | $FFFFFF | $200000 (2MB)   | [Cartridge Memory (Mirror)](PM_Cartridge.md "wikilink") |
