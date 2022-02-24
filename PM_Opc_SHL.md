\== SHL = Shift Left ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 84    | SHL A          | 12     |
| CE 85    | SHL B          | 12     |
| CE 86 nn | SHL \[N+\#nn\] | 20     |
| CE 87    | SHL \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; SHL Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds SHL 1`

### Description

"8-Bits Destination" bits are shifted left by 1.

NOTE: This instruction can be used as an unsigned integer multiplication
by 2.

### Conditions

Zero: Set when result is 0

Carry: Set when the old bit 7 was 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04 (4)`
**`SHL`` ``A`**
`; A = 0x08 (8)`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45 (69)`
**`SHL`` ``B`**
`; B = 0x8A (138)`
`; F = (Zero=0):(Carry=0):(Sign=1)`

`; B = 0x84 (138)`
**`SHL`` ``B`**
`; B = 0x14 (20)`
`; F = (Zero=0):(Carry=1):(Sign=0)`

`; [HL] = 0x80 (128)`
**`SHL`` ``[HL]`**
`; [HL] = 0x00 (0)`
`; F = (Zero=1):(Carry=1):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")