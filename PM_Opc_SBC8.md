\== SBC = Subtraction with Carry (8-Bits) ==

| Hex      | Mnemonic          | Cycles |
| -------- | ----------------- | ------ |
| 18       | SBC A, A          | 8      |
| 19       | SBC A, B          | 8      |
| 1A nn    | SBC A, \#nn       | 8      |
| 1B       | SBC A, \[HL\]     | 8      |
| 1C nn    | SBC A, \[N+\#nn\] | 12     |
| 1D nn nn | SBC A, \[\#nnnn\] | 16     |
| 1E       | SBC A, \[X\]      | 8      |
| 1F       | SBC A, \[Y\]      | 8      |
| CE 18 ss | SBC A, \[X+\#ss\] | 16     |
| CE 19 ss | SBC A, \[Y+\#ss\] | 16     |
| CE 1A    | SBC A, \[X+L\]    | 16     |
| CE 1B    | SBC A, \[Y+L\]    | 16     |
| CE 1C    | SBC \[HL\], A     | 16     |
| CE 1D nn | SBC \[HL\], \#nn  | 20     |
| CE 1E    | SBC \[HL\], \[X\] | 20     |
| CE 1F    | SBC \[HL\], \[Y\] | 20     |

### Execute

`#nn     = Immediate unsigned 8-Bits`
`#ss     = Immediate signed 8-Bits`
`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`
`[X]     = Memory: (XI shl 16) or X`
`[Y]     = Memory: (YI shl 16) or Y`
`[#nnnn] = Memory: (I shl 16) or #nnnn`
`[X+#ss] = Memory: (XI shl 16) or (X + #ss)`
`[Y+#ss] = Memory: (YI shl 16) or (Y + #ss)`
`[X+L]   = Memory: (XI shl 16) or (X + signed(L))`
`[Y+L]   = Memory: (YI shl 16) or (Y + signed(L))`

`; SBC Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`; (If flags BCD=0 and NIBBLE=0)`
`Ds = Ds - Sc - Carry`

`;------------------------------------------------ `

`; (If flags BCD=0 and NIBBLE=1)`
`Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=0)`
`IF (((Ds & 15) - (Sc & 15) - Carry) >= 10) THEN    ; Note: Should be an unsigned check`
`  Ds = Ds - Sc - Carry - 6`
`ELSE`
`  Ds = Ds - Sc - Carry`
`ENDIF`
`IF (Ds >= 0xA0) Ds = Ds - 0x60`
`; NOTE: This isn't accurate, there's some weird effect on a strange condition`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=1)`
`IF (((Ds & 15) - (Sc & 15) - Carry) >= 10) THEN    ; Note: Should be an unsigned check`
`  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry - 6`
`ELSE`
`  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry`
`ENDIF`

### Description

8-Bits Source and Carry subtracts to the 8-Bits Destination.

### Conditions

\==== If flags BCD=0 and NIBBLE=0 ====

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 8-bits signed range (\< -128 OR \>
127)

Sign: Set when bit 7 of the result is 1

\==== If flags BCD=0 and NIBBLE=1 ====

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 4-bits signed range (\< -16 OR \> 15)

Sign: Set when bit 3 of the result is 1

\==== If flags BCD=1 and NIBBLE=0 ====

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Always Reset

Sign: Always Reset

\==== If flags BCD=1 and NIBBLE=1 ====

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Always Reset

Sign: Always Reset

### Examples

`; A = 0x55`
`; F = (Carry=1)`
**`SBC`` ``A,`` ``$80`**
`; A = 0xD4 (0x55 - 0x80 - 0x01 = 0x(1)D4)`
`; F = (Zero=0):(Carry=0):(Overflow=1):(Sign=1)`

`; B = 0x31`
`; A = 0xCF`
`; F = (Carry=0)`
**`SBC`` ``A,`` ``B`**
`; B = 0x31`
`; A = 0x9E (0xCF - 0x31 - 0x00 = 0x(0)9E)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; ( BCD = 1, NIBBLE = 0 )`
`; A = 0x10`
`; F = (Carry=1)`
**`SBC`` ``A,``
``$01`**
`; A = 0x08 (10 - 01 - 01 = 08)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; ( BCD = 0, NIBBLE = 1 )`
`; A = 0x3F (Note, in "nibble mode" the high nibble is always discarded)`
`; F = (Carry=1)`
**`SBC`` ``A,`` ``$01`**
`; A = 0x0D (0xF - 0x1 - 0x1 = 0x(0)D)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
