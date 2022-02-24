\== NEG = Negate ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE A4    | NEG A          | 12     |
| CE A5    | NEG B          | 12     |
| CE A6 nn | NEG \[N+\#nn\] | 20     |
| CE A7    | NEG \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; NEG Ds`
`;`
`; Ds = Source/Destination`

`Ds = 0 - Ds`

### Description

8-Bits Destination is negated.

### Conditions

Zero: Set when result is 0

Carry: Set when result is not 0

Overflow: Set when result is 0x80

Sign: Set when bit 7 of the result is 1

### Examples

`; A = 0x01`
**`NEG`` ``A`**
`; A = 0xFF (0 - 0x01 = 0xFF)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

`; B = 0x00`
**`NEG`` ``B`**
`; B = 0x00 (0 - 0x00 = 0x00)`
`; F = (Zero=1):(Carry=0):(Overflow=0):(Sign=0)`

`; [HL] = 0x80`
**`NEG`` ``[HL]`**
`; [HL] = 0x80 (0 - 0x80 = 0x80)`
`; F = (Zero=0):(Carry=1):(Overflow=1):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
