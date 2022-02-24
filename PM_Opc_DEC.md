\== DEC = Decrease Register by 1 ==

| Hex   | Mnemonic       | Cycles |
| ----- | -------------- | ------ |
| 88    | DEC A          | 8      |
| 89    | DEC B          | 8      |
| 8A    | DEC L          | 8      |
| 8B    | DEC H          | 8      |
| 8C    | DEC N          | 8      |
| 8D nn | DEC \[N+\#nn\] | 16     |
| 8E    | DEC \[HL\]     | 12     |
| 8F    | DEC SP         | 8      |
| 98    | DEC BA         | 8      |
| 99    | DEC HL         | 8      |
| 9A    | DEC X          | 8      |
| 9B    | DEC Y          | 8      |

### Execute

`A        =  (8-Bits) Register A`
`B        =  (8-Bits) Register B`
`L        =  (8-Bits) Register L`
`H        =  (8-Bits) Register H`
`N        =  (8-Bits) Register N`
`SP       = (16-Bits) Register SP (Stack Pointer)`
`BA       = (16-Bits) Register BA: (B shl 8) or A`
`HL       = (16-Bits) Register HL: (H shl 8) or L`
`X        = (16-Bits) Register X`
`Y        = (16-Bits) Register Y`
`[N+#nn]  =  (8-Bits) Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]     =  (8-Bits) Memory: (I shl 16) or HL`

`; DEC Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds - 1`

### Description

"Destination" is decremented by 1.

### Conditions

Zero: Set when result is 0

Carry, Overflow and Sign remain unchanged

### Examples

`; A = 0x55`
**`DEC`` ``A`**
`; A = 0x54 (0x55 - 1 = 0x54)`
`; F = (Zero=0)`

`; [N+0x88] = 0xFF`
**`DEC`` ``[N+$88]`**
`; [N+0x88] = 0xFE (0xFF - 1 = 0xFE)`
`; F = (Zero=0)`

`; BA = 0x2997`
**`DEC`` ``BA`**
`; BA = 0x2996 (0x2997 - 1 = 0x2996)`
`; F = (Zero=0)`

`; X = 0xFFFF`
**`DEC`` ``X`**
`; X = 0xFFFE (0xFFFF - 1 = 0xFFFE)`
`; F = (Zero=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")