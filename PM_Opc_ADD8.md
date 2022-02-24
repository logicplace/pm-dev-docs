\== ADD = Addition (8-Bits) ==

| Hex      | Mnemonic          | Cycles |
| -------- | ----------------- | ------ |
| 00       | ADD A, A          | 8      |
| 01       | ADD A, B          | 8      |
| 02 nn    | ADD A, \#nn       | 8      |
| 03       | ADD A, \[HL\]     | 8      |
| 04 nn    | ADD A, \[N+\#nn\] | 12     |
| 05 nn nn | ADD A, \[\#nnnn\] | 16     |
| 06       | ADD A, \[X\]      | 8      |
| 07       | ADD A, \[Y\]      | 8      |
| CE 00 ss | ADD A, \[X+\#ss\] | 16     |
| CE 01 ss | ADD A, \[Y+\#ss\] | 16     |
| CE 02    | ADD A, \[X+L\]    | 16     |
| CE 03    | ADD A, \[Y+L\]    | 16     |
| CE 04    | ADD \[HL\], A     | 16     |
| CE 05 nn | ADD \[HL\], \#nn  | 20     |
| CE 06    | ADD \[HL\], \[X\] | 20     |
| CE 07    | ADD \[HL\], \[Y\] | 20     |

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

`; ADD Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`; (If flags BCD=0 and NIBBLE=0)`
`Ds = Ds + Sc`

`;------------------------------------------------ `

`; (If flags BCD=0 and NIBBLE=1)`
`Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F)`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=0)`
`IF (((Ds & 15) + (Sc & 15)) >= 10) THEN`
`  Ds = Ds + Sc + 6`
`ELSE`
`  Ds = Ds + Sc`
`ENDIF`
`IF (Ds >= 0xA0) Ds = Ds + 0x60`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=1)`
`IF (((Ds & 15) + (Sc & 15)) >= 10) THEN`
`  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F) + 6`
`ELSE`
`  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F)`
`ENDIF`

### Description

8-Bits Source adds to the 8-Bits Destination.

### Conditions

\==== If flags BCD=0 and NIBBLE=0 ====

Zero: Set when result is 0

Carry: Set when result is \>= 256

Overflow: Set when result overflow 8-bits signed range (\< -128 OR \>
127)

Sign: Set when bit 7 of the result is 1

\==== If flags BCD=0 and NIBBLE=1 ====

Zero: Set when result is 0

Carry: Set when result is \>= 16

Overflow: Set when result overflow 4-bits signed range (\< -16 OR \> 15)

Sign: Set when bit 3 of the result is 1

\==== If flags BCD=1 and NIBBLE=0 ====

Zero: Set when result is 0

Carry: Set when result is \>= 100

Overflow: Always Reset

Sign: Always Reset

\==== If flags BCD=1 and NIBBLE=1 ====

Zero: Set when result is 0

Carry: Set when result is \>= 10

Overflow: Always Reset

Sign: Always Reset

### Examples

`; A = 0x55`
**`ADD`` ``A,`` ``$80`**
`; A = 0xD5 (0x55 + 0x80 = 0x(0)D5)`
`; F = (Zero=0):(Carry=0):(Overflow=1):(Sign=1)`

`; B = 0x31`
`; A = 0xCF`
**`ADD`` ``A,`` ``B`**
`; B = 0x31`
`; A = 0x00 (0xCF + 0x31 = 0x(1)00)`
`; F = (Zero=1):(Carry=1):(Overflow=0):(Sign=0)`

`; [HL] = 0xDE`
`; A = 0xCF`
**`ADD`` ``A,`` ``[HL]`**
`; [HL] = 0xDE`
`; A = 0xAD (0xCF + 0xDE = 0x(1)AD)`
`; F = (Zero=0):(Carry=1):(Overflow=0):(Sign=1)`

`; ( BCD = 1, NIBBLE = 0 )`
`; A = 0x09`
**`ADD`` ``A,``
``$01`**
`; A = 0x10 (09 + 01 = 10)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; ( BCD = 0, NIBBLE = 1 )`
`; A = 0x3F (Note, in "nibble mode" the high nibble is always discarded)`
**`ADD`` ``A,`` ``$01`**
`; A = 0x00 (0xF + 0x1 = 0x(1)0)`
`; F = (Zero=1):(Carry=1):(Overflow=0):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")