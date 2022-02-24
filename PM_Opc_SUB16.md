\== SUB = Subtraction (16-Bits) ==

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| D0 nn nn    | SUB BA, \#nnnn | 12     |
| D1 nn nn    | SUB HL, \#nnnn | 12     |
| D2 nn nn    | SUB X, \#nnnn  | 12     |
| D3 nn nn    | SUB Y, \#nnnn  | 12     |
| CF 6A nn nn | SUB SP, \#nnnn | 16     |
| CF 08       | SUB BA, BA     | 16     |
| CF 09       | SUB BA, HL     | 16     |
| CF 0A       | SUB BA, X      | 16     |
| CF 0B       | SUB BA, Y      | 16     |
| CF 28       | SUB HL, BA     | 16     |
| CF 29       | SUB HL, HL     | 16     |
| CF 2A       | SUB HL, X      | 16     |
| CF 2B       | SUB HL, Y      | 16     |
| CF 48       | SUB X, BA      | 16     |
| CF 49       | SUB X, HL      | 16     |
| CF 4A       | SUB Y, BA      | 16     |
| CF 4B       | SUB Y, HL      | 16     |
| CF 4C       | SUB SP, BA     | 16     |
| CF 4D       | SUB SP, HL     | 16     |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`
`SP       = Register SP (Stack Pointer)`

`; SUB Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds - Sc`

### Description

16-Bits Source subtracts to the 16-Bits Destination.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 16-bits signed range (\< -32768 OR \>
32767)

Sign: Set when bit 15 of the result is 1

### Examples

`; BA = 0x2EF0`
**`SUB`` ``BA,`` ``$1337`**
`; BA = 0x1BB9 (0x2EF0 - 0x1337 = 0x(0)1BB9)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; HL = 0xBB7E`
`; BA = 0xCF12`
**`SUB`` ``BA,`` ``HL`**
`; HL = 0xBB7E`
`; BA = 0xEC6C (0xCF12 - 0xBB7E = 0x(1)EC6C)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
