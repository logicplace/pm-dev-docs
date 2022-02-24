\== SAL = Shift Arithmetic Left ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 80    | SAL A          | 12     |
| CE 81    | SAL B          | 12     |
| CE 82 nn | SAL \[N+\#nn\] | 20     |
| CE 83    | SAL \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; SAL Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds SHL 1`

### Description

"8-Bits Destination" bits are arithmetically shifted left by 1.

NOTE: This instruction can be used as an signed integer multiplication
by 2.

### Conditions

Zero: Set when result is 0

Carry: Set when the old bit 7 was 1

Overflow: Set when result overflow 8-bits signed range (\< -128 OR \>
127)

Sign: Set when bit 7 of the result is 1

### Examples

`; A = 0x04 (4)`
**`SAL`` ``A`**
`; A = 0x08 (8)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; A = 0xFE (-2)`
**`SAL`` ``A`**
`; A = 0xFC (-4)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

`; B = 0x45 (69)`
**`SAL`` ``B`**
`; B = 0x8A (-124)`
`; F = (Zero=0):(Carry=0):(Overflow=1):(Sign=1)`

`; B = 0x84 (-124)`
**`SAL`` ``B`**
`; B = 0x14 (20)`
`; F = (Zero=0):(Carry=1):(Overflow=1):(Sign=0)`

`; [HL] = 0x80 (-128)`
**`SAL`` ``[HL]`**
`; [HL] = 0x00 (0)`
`; F = (Zero=1):(Carry=1):(Overflow=1):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")