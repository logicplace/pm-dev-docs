# Multicart information

*Also see [here](../../dev_cart.md#2001)*

$2001 bits 3~0 are [reserved R/W registers](../../../glossary.md#reserved-rw-register) used for storing information related to the BIOS's [multicart](../bios.md#valid-multi-cart-game-index). Bit 3 is essentially a flag stating what sort of information is in bits 2~0.

Bit 3 is set as 1 [here](../../../software/bios/disasm/#user-content-06D6). It's reset to 0 during [initial boot](../../../software/bios/disasm/#user-content-00C7) and during [shutdown](../../../software/bios/disasm/#user-content-07AB).

The conditions under which it's set to 1 are essentially:

1. Using an official flash cart
2. If the [startup action is 3](../../dev_cart.md#startup-action-3)
3. No flash writes failed while loading the game list
4. There are playable games in the list

These are the same conditions it takes to reach the game select screen, thus this bit is set to 1 when it decides to go to the game select screen.

When a game is selected from the game select menu, the ID is stored in bits 2~0. This is an index into the structure list in ROM.

When the [startup action is 2](../../dev_cart.md#startup-action-2), bit 3 remains 3 and bit 0 is set to 1. This mode essentially has structural information in ROM but it's opting to automatically boot the first game in that list, instead of showing a select screen.

Bits 2~1 are ignored when bit 3 is 0.

If all bits 3~0 are 0, this is essentially the normal play mode. The cartridge is either not an official flash cart or it's using startup action 0.
