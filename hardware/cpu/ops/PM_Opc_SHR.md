\== SHR = Shift Right ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 8C    | SHR A          | 12     |
| CE 8D    | SHR B          | 12     |
| CE 8E nn | SHR \[N+\#nn\] | 20     |
| CE 8F    | SHR \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; SHR Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds SHR 1`

### Description

"8-Bits Destination" bits are shifted right by 1.

NOTE: This instruction can be used as an unsigned integer division by 2.

### Conditions

Zero: Set when result is 0

Carry: Set when the old bit 0 was 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04 (4)`
**`SHR`` ``A`**
`; A = 0x02 (2)`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45 (69)`
**`SHR`` ``B`**
`; B = 0x22 (34)`
`; F = (Zero=0):(Carry=1):(Sign=0)`

`; B = 0x84 (132)`
**`SHR`` ``B`**
`; B = 0x42 (66)`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; [HL] = 0x01 (1)`
**`SHR`` ``[HL]`**
`; [HL] = 0x00 (0)`
`; F = (Zero=1):(Carry=1):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
