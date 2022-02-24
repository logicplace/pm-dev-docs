\== XCHG = Exchange Registers ==

| Hex | Mnemonic       | Cycles |
| --- | -------------- | ------ |
| C8  | XCHG BA, HL    | 12     |
| C9  | XCHG BA, X     | 12     |
| CA  | XCHG BA, Y     | 12     |
| CB  | XCHG BA, SP    | 12     |
| CC  | XCHG A, B      | 8      |
| CD  | XCHG A, \[HL\] | 12     |

### Execute

`A        =  (8-Bits) Register A`
`B        =  (8-Bits) Register B`
`BA       = (16-Bits) Register BA: (B shl 8) or A`
`HL       = (16-Bits) Register HL: (H shl 8) or L`
`X        = (16-Bits) Register X`
`Y        = (16-Bits) Register Y`
`SP       = (16-Bits) Register SP (Stack Pointer)`
`[HL]     =  (8-Bits) Memory: (I shl 16) or HL`

`; XCHG Sc2, Sc`
`;`
`; Sc2 = Source 2`
`; Sc  = Source`
`; Tr = Temporary Register`

`Sc2   Sc`
`   \ /`
`    x`
`   / \`
`Sc2   Sc`

### Description

"Source" content is exchanged (swapped) with "Source 2".

### Conditions

None

### Examples

`; BA = 0x1337`
`; HL = 0xC0D3`
**`XCHG`` ``BA,`` ``HL`**
`; BA = 0xC0D3`
`; HL = 0x1337`

`; A = 0x45`
`; B = 0x12`
**`XCHG`` ``A,`` ``B`**
`; A = 0x12`
`; B = 0x45`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")