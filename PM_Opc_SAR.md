\== SAR = Shift Arithmetic Right ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 88    | SAR A          | 12     |
| CE 89    | SAR B          | 12     |
| CE 8A nn | SAR \[N+\#nn\] | 20     |
| CE 8B    | SAR \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; SAR Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds AND 0x80) OR (Ds SHR 1)`

### Description

"8-Bits Destination" bits are arithmetically shifted right by 1.

NOTE: This instruction can be used as an signed integer division by 2.

### Conditions

Zero: Set when result is 0

Carry: Set when the old bit 0 was 1

Overflow: Always Reset (there's never a overflow)

Sign: Set when bit 7 of the result is 1

### Examples

`; A = 0x04 (4)`
**`SAR`` ``A`**
`; A = 0x02 (2)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; A = 0xFD (-4)`
**`SAR`` ``A`**
`; A = 0xFE (-2)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=1)`

`; B = 0x45 (69)`
**`SAR`` ``B`**
`; B = 0x22 (34)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=0)`

`; B = 0x84 (-124)`
**`SAR`` ``B`**
`; B = 0xC2 (-62)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=1)`

`; [HL] = 0x01 (1)`
**`SAR`` ``[HL]`**
`; [HL] = 0x00 (0)`
`; F = (Zero=1):(Carry=1):(Overflow=0):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")