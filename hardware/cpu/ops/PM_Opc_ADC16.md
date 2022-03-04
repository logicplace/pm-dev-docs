\== ADC = Addition with Carry (16-Bits) ==

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| CF 04       | ADC BA, BA     | 16     |
| CF 05       | ADC BA, HL     | 16     |
| CF 06       | ADC BA, X      | 16     |
| CF 07       | ADC BA, Y      | 16     |
| CF 24       | ADC HL, BA     | 16     |
| CF 25       | ADC HL, HL     | 16     |
| CF 26       | ADC HL, X      | 16     |
| CF 27       | ADC HL, Y      | 16     |
| CF 60 nn nn | ADC BA, \#nnnn | 16     |
| CF 61 nn nn | ADC HL, \#nnnn | 16     |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`

`; ADC Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds + Sc + Carry`

### Description

16-Bits Source and Carry adds to the 16-Bits Destination.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \>= 65536

Overflow: Set when result overflow 16-bits signed range (\< -32768 OR \>
32767)

Sign: Set when bit 15 of the result is 1

### Examples

`; BA = 0x0EF0`
`; F = (Carry=1)`
**`ADC`` ``BA,`` ``$1337`**
`; BA = 0x2228 (0x0EF0 + 0x1337 + 0x0001 = 0x(0)2228)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; HL = 0xBB7E`
`; BA = 0xCF12`
`; F = (Carry=0)`
**`ADC`` ``BA,`` ``HL`**
`; HL = 0xBB7E`
`; BA = 0x8A90 (0xCF12 + 0xBB7E + 0x0000 = 0x(1)8A90)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

`; X = 0xBEEF`
`; BA = 0xDEAD`
`; F = (Carry=1)`
**`ADC`` ``BA,`` ``X`**
`; X = 0xBEEF`
`; BA = 0x9D9D (0xDEAD + 0xBEEF + 0x0001 = 0x(1)9D9D)`
`; F = (Zero=0):(Carry=1):(Overflow=1):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
