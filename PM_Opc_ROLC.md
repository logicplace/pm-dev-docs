\== ROLC = Rotate Left through Carry ==

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| CE 90    | ROLC A          | 12     |
| CE 91    | ROLC B          | 12     |
| CE 92 nn | ROLC \[N+\#nn\] | 20     |
| CE 93    | ROLC \[HL\]     | 16     |

### Execute

`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; ROLC Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds SHL 1) OR Carry`

### Description

"8-Bits Destination" bits are rotated left by 1 through Carry.

### Conditions

Zero: Set when result is 0

Carry: Set when old bit 7 is 1

Sign: Set when bit 7 of the result is 1

Overflow remain unchanged

### Examples

`; A = 0x04`
`; F = (Carry=0)`
**`ROLC`` ``A`**
`; A = 0x08`
`; F = (Zero=0):(Carry=0):(Sign=0)`

`; B = 0x45`
`; F = (Carry=1)`
**`ROLC`` ``B`**
`; B = 0x8B`
`; F = (Zero=0):(Carry=0):(Sign=1)`

`; B = 0x84`
`; F = (Carry=0)`
**`ROLC`` ``B`**
`; B = 0x08`
`; F = (Zero=0):(Carry=1):(Sign=0)`

`; [HL] = 0x80`
`; F = (Carry=0)`
**`ROLC`` ``[HL]`**
`; [HL] = 0x00`
`; F = (Zero=1):(Carry=1):(Sign=0)`

`; [HL] = 0x80`
`; F = (Carry=1)`
**`ROLC`` ``[HL]`**
`; [HL] = 0x01`
`; F = (Zero=0):(Carry=1):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
