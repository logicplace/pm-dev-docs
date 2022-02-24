\== CMP = Compare (16-Bits) ==

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| D4 nn nn    | CMP BA, \#nnnn | 12     |
| D5 nn nn    | CMP HL, \#nnnn | 12     |
| D6 nn nn    | CMP X, \#nnnn  | 12     |
| D7 nn nn    | CMP Y, \#nnnn  | 12     |
| CF 6C nn nn | CMP SP, \#nnnn | 16     |
| CF 18       | CMP BA, BA     | 16     |
| CF 19       | CMP BA, HL     | 16     |
| CF 1A       | CMP BA, X      | 16     |
| CF 1B       | CMP BA, Y      | 16     |
| CF 38       | CMP HL, BA     | 16     |
| CF 39       | CMP HL, HL     | 16     |
| CF 3A       | CMP HL, X      | 16     |
| CF 3B       | CMP HL, Y      | 16     |
| CF 5C       | CMP SP, BA     | 16     |
| CF 5D       | CMP SP, HL     | 16     |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`
`SP       = Register SP (Stack Pointer)`

`; CMP Sc2, Sc`
`;`
`; Sc2 = Source 2`
`; Sc  = Source`

`(discarded) = Sc2 - Sc`

### Description

"16-Bits Source 2" subtracts with "16-Bits Source", result is discarded.

This instruction is used to compare values.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 16-bits signed range (\< -32768 OR \>
32767)

Sign: Set when bit 15 of the result is 1

### Examples

`; BA = 0x2EF0`
**`CMP`` ``BA,`` ``$1337`**
`; BA = 0x2EF0`
`;      0x1BB9 (0x2EF0 - 0x1337 = 0x(0)1BB9)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; HL = 0xBB7E`
`; BA = 0xCF12`
**`CMP`` ``BA,`` ``HL`**
`; HL = 0xBB7E`
`; BA = 0xCF12`
`;     0xEC6C (0xCF12 - 0xBB7E = 0x(1)EC6C)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
