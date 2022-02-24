\== NOT = Logical NOT ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE A0    | NOT A          | 12     |
| CE A1    | NOT B          | 12     |
| CE A2 nn | NOT \[N+\#nn\] | 20     |
| CE A3    | NOT \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; NOT Ds`
`;`
`; Ds = Source/Destination`

`Ds = Ds XOR $FF`

### Description

8-Bits Destination is inverted (all bits).

### Conditions

Zero: Set when result is 0

Sign: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

### Examples

`; A = 0x01`
**`NOT`` ``A`**
`; A = 0xFE`
`; F = (Zero=0):(Sign=1)`

`; B = 0x85`
**`NOT`` ``B`**
`; B = 0x7A`
`; F = (Zero=0):(Sign=0)`

`; [HL] = 0xFF`
**`NOT`` ``[HL]`**
`; [HL] = 0x00`
`; F = (Zero=1):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")