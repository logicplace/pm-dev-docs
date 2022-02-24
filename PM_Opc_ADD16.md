\== ADD = Addition (16-Bits) ==

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| C0 nn nn    | ADD BA, \#nnnn | 12     |
| C1 nn nn    | ADD HL, \#nnnn | 12     |
| C2 nn nn    | ADD X, \#nnnn  | 12     |
| C3 nn nn    | ADD Y, \#nnnn  | 12     |
| CF 68 nn nn | ADD SP, \#nnnn | 16     |
| CF 00       | ADD BA, BA     | 16     |
| CF 01       | ADD BA, HL     | 16     |
| CF 02       | ADD BA, X      | 16     |
| CF 03       | ADD BA, Y      | 16     |
| CF 20       | ADD HL, BA     | 16     |
| CF 21       | ADD HL, HL     | 16     |
| CF 22       | ADD HL, X      | 16     |
| CF 23       | ADD HL, Y      | 16     |
| CF 40       | ADD X, BA      | 16     |
| CF 41       | ADD X, HL      | 16     |
| CF 42       | ADD Y, BA      | 16     |
| CF 43       | ADD Y, HL      | 16     |
| CF 44       | ADD SP, BA     | 16     |
| CF 45       | ADD SP, HL     | 16     |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`
`SP       = Register SP (Stack Pointer)`

`; ADD Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds + Sc`

### Description

16-Bits Source adds to the 16-Bits Destination.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \>= 65536

Overflow: Set when result overflow 16-bits signed range (\< -32768 OR \>
32767)

Sign: Set when bit 15 of the result is 1

### Examples

`; BA = 0x0EF0`
**`ADD`` ``BA,`` ``$1337`**
`; BA = 0x2227 (0x0EF0 + 0x1337 = 0x(0)2227)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; HL = 0xBB7E`
`; BA = 0xCF12`
**`ADD`` ``BA,`` ``HL`**
`; HL = 0xBB7E`
`; BA = 0x8A90 (0xCF12 + 0xBB7E = 0x(1)8A90)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

`; X = 0xBEEF`
`; BA = 0xDEAD`
**`ADD`` ``BA,`` ``X`**
`; X = 0xBEEF`
`; BA = 0x9D9C (0xDEAD + 0xBEEF = 0x(1)9D9C)`
`; F = (Zero=0):(Carry=1):(Overflow=1):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")