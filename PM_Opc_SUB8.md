\== SUB = Subtraction (8-Bits) ==

| Hex      | Mnemonic              | Cycles |
| -------- | --------------------- | ------ |
| 10       | SUB A, A              | 8      |
| 11       | SUB A, B              | 8      |
| 12 nn    | SUB A, \#nn           | 8      |
| 13       | SUB A, \[HL\]         | 8      |
| 14 nn    | SUB A, \[N+\#nn\]     | 12     |
| 15 nn nn | SUB A, \[\#nnnn\]\]\] | 16     |
| 16       | SUB A, \[X\]          | 8      |
| 17       | SUB A, \[Y\]          | 8      |
| CE 10 ss | SUB A, \[X+\#ss\]     | 16     |
| CE 11 ss | SUB A, \[Y+\#ss\]     | 16     |
| CE 12    | SUB A, \[X+L\]        | 16     |
| CE 13    | SUB A, \[Y+L\]        | 16     |
| CE 14    | SUB \[HL\], A         | 16     |
| CE 15 nn | SUB \[HL\], \#nn      | 20     |
| CE 16    | SUB \[HL\], \[X\]     | 20     |
| CE 17    | SUB \[HL\], \[Y\]     | 20     |

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

`; SUB Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`; (If flags BCD=0 and NIBBLE=0)`
`Ds = Ds - Sc`

`;------------------------------------------------ `

`; (If flags BCD=0 and NIBBLE=1)`
`Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F)`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=0)`
`IF (((Ds & 15) - (Sc & 15)) >= 10) THEN    ; Note: Should be an unsigned check`
`  Ds = Ds - Sc - 6`
`ELSE`
`  Ds = Ds - Sc`
`ENDIF`
`IF (Ds >= 0xA0) Ds = Ds - 0x60`
`; NOTE: This isn't accurate, there's some weird effect on a strange condition`

`;------------------------------------------------`

`; (If flags BCD=1 and NIBBLE=1)`
`IF (((Ds & 15) - (Sc & 15)) >= 10) THEN    ; Note: Should be an unsigned check`
`  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - 6`
`ELSE`
`  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F)`
`ENDIF`

### Description

8-Bits Source subtracts to the 8-Bits Destination.

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
**`SUB`` ``A,`` ``$80`**
`; A = 0xD5 (0x55 - 0x80 = 0x(1)D5)`
`; F = (Zero=0):(Carry=0):(Overflow=1):(Sign=1)`

`; B = 0x31`
`; A = 0xCF`
**`SUB`` ``A,`` ``B`**
`; B = 0x31`
`; A = 0x9E (0xCF - 0x31 = 0x(0)9E)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; ( BCD = 1, NIBBLE = 0 )`
`; A = 0x10`
**`SUB`` ``A,``
``$01`**
`; A = 0x09 (10 - 01 = 09)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; ( BCD = 0, NIBBLE = 1 )`
`; A = 0x3F (Note, in "nibble mode" the high nibble is always discarded)`
**`SUB`` ``A,`` ``$01`**
`; A = 0x0E (0xF - 0x1 = 0x(0)E)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")