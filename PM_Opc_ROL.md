\== ROL = Rotate Left ==

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 94    | ROL A          | 12     |
| CE 95    | ROL B          | 12     |
| CE 96 nn | ROL \[N+\#nn\] | 20     |
| CE 97    | ROL \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; ROL Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds SHL 1) OR (Ds SHR 7)`

### Description

"8-Bits Destination" bits are rotated left by 1.

### Conditions

Zero: Set when result is 0

Carry: Set when bit 0 of the result is 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04`
**`ROL`` ``A`**
`; A = 0x08`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45`
**`ROL`` ``B`**
`; B = 0x8A`
`; F = (Zero=0):(Carry=0):(Sign=1)`

`; B = 0x84`
**`ROL`` ``B`**
`; B = 0x15`
`; F = (Zero=0):(Carry=1):(Sign=0)`

`; [HL] = 0x80`
**`ROL`` ``[HL]`**
`; [HL] = 0x01`
`; F = (Zero=0):(Carry=1):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
