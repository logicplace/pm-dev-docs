\== SBC = Subtract with Carry (16-Bits) ==

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| CF 0C       | SBC BA, BA     | 16     |
| CF 0D       | SBC BA, HL     | 16     |
| CF 0E       | SBC BA, X      | 16     |
| CF 0F       | SBC BA, Y      | 16     |
| CF 2C       | SBC HL, BA     | 16     |
| CF 2D       | SBC HL, HL     | 16     |
| CF 2E       | SBC HL, X      | 16     |
| CF 2F       | SBC HL, Y      | 16     |
| CF 62 nn nn | SBC BA, \#nnnn | 16     |
| CF 63 nn nn | SBC HL, \#nnnn | 16     |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`

`; SBC Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds - Sc - Carry`

### Description

16-Bits Source and Carry subtracts to the 16-Bits Destination.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 16-bits signed range (\< -32768 OR \>
32767)

Sign: Set when bit 15 of the result is 1

### Examples

`; BA = 0x2EF0`
`; F = (Carry=1)`
**`SBC`` ``BA,`` ``$1337`**
`; BA = 0x1BB8 (0x2EF0 - 0x1337 - 0x0001 = 0x(0)1BB8)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; HL = 0xBB7E`
`; BA = 0xCF12`
`; F = (Carry=0)`
**`SBC`` ``BA,`` ``HL`**
`; HL = 0xBB7E`
`; BA = 0xEC6C (0xCF12 - 0xBB7E - 0x0000 = 0x(1)EC6C)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
