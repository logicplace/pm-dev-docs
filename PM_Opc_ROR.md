\== ROR = Rotate Right ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 9C    | ROR A          | 12     |
| CE 9D    | ROR B          | 12     |
| CE 9E nn | ROR \[N+\#nn\] | 20     |
| CE 9F    | ROR \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; ROR Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds SHR 1) OR (Ds SHL 7)`

### Description

"8-Bits Destination" bits are rotated right by 1.

### Conditions

Zero: Set when result is 0

Carry: Set when bit 7 of the result is 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04`
**`ROR`` ``A`**
`; A = 0x02`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45`
**`ROR`` ``B`**
`; B = 0xA2`
`; F = (Zero=0):(Carry=1):(Sign=1)`

`; B = 0x84`
**`ROR`` ``B`**
`; B = 0x42`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; [HL] = 0x01`
**`ROR`` ``[HL]`**
`; [HL] = 0x80`
`; F = (Zero=0):(Carry=1):(Sign=1)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")