\== RORC = Rotate Right through Carry ==

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| CE 98    | RORC A          | 12     |
| CE 99    | RORC B          | 12     |
| CE 9A nn | RORC \[N+\#nn\] | 20     |
| CE 9B    | RORC \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; RORC Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds SHR 1) OR (Carry SHL 7)`

### Description

"8-Bits Destination" bits are rotated right by 1 through Carry.

### Conditions

Zero: Set when result is 0

Carry: Set when old bit 0 is 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04`
`; F = (Carry=0)`
**`RORC`` ``A`**
`; A = 0x02`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45`
`; F = (Carry=1)`
**`RORC`` ``B`**
`; B = 0xA2`
`; F = (Zero=0):(Carry=1):(Sign=0)`

`; B = 0x84`
`; F = (Carry=0)`
**`RORC`` ``B`**
`; B = 0x42`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; [HL] = 0x01`
`; F = (Carry=0)`
**`RORC`` ``[HL]`**
`; [HL] = 0x00`
`; F = (Zero=1):(Carry=1):(Sign=0)`

`; [HL] = 0x01`
`; F = (Carry=1)`
**`RORC`` ``[HL]`**
`; [HL] = 0x80`
`; F = (Zero=0):(Carry=1):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
