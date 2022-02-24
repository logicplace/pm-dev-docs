\== INC = Increase Register by 1 ==

| Hex   | Mnemonic       | Cycles |
| ----- | -------------- | ------ |
| 80    | INC A          | 8      |
| 81    | INC B          | 8      |
| 82    | INC L          | 8      |
| 83    | INC H          | 8      |
| 84    | INC N          | 8      |
| 85 nn | INC \[N+\#nn\] | 16     |
| 86    | INC \[HL\]     | 12     |
| 87    | INC SP         | 8      |
| 90    | INC BA         | 8      |
| 91    | INC HL         | 8      |
| 92    | INC X          | 8      |
| 93    | INC Y          | 8      |

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

`; INC Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds + 1`

### Description

"Destination" is incremented by 1.

### Conditions

Zero: Set when result is 0

Carry, Overflow and Sign remain unchanged

### Examples

`; A = 0x55`
**`INC`` ``A`**
`; A = 0x56 (0x55 + 1 = 0x56)`
`; F = (Zero=0)`

`; [N+0x88] = 0xFF`
**`INC`` ``[N+$88]`**
`; [N+0x88] = 0x00 (0xFF + 1 = 0x00)`
`; F = (Zero=1)`

`; BA = 0x2997`
**`INC`` ``BA`**
`; BA = 0x2998 (0x2997 + 1 = 0x2998)`
`; F = (Zero=0)`

`; X = 0xFFFF`
**`INC`` ``X`**
`; X = 0x0000 (0xFFFF + 1 = 0x0000)`
`; F = (Zero=1)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")