\== PACK = Pack Nibbles ==

| Hex | Mnemonic | Cycles |
| --- | -------- | ------ |
| DE  | PACK     | 8      |

### Execute

`A        =  (8-Bits) Register A`
`B        =  (8-Bits) Register B`

`; PACK`

`A = (A AND 0x0F) OR (B SHL 4)`

### Description

Pack low nibble of register A and B and return the formed byte into
register A.

Register A forms the lower nibble and register B forms the higher
nibble.

### Conditions

None

### Examples

`; A = 0x01`
`; B = 0x02`
**`PACK`**
`; A = 0x21`
`; B = 0x02 (Remain unchanged)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")