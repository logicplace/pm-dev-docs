\== OR = Logical Inclusive-OR ==

| Hex      | Mnemonic            | Cycles |
| -------- | ------------------- | ------ |
| 28       | OR A, A             | 8      |
| 29       | OR A, B             | 8      |
| 2A nn    | OR A, \#nn          | 8      |
| 2B       | OR A, \[HL\]        | 8      |
| 2C nn    | OR A, \[N+\#nn\]    | 12     |
| 2D nn nn | OR A, \[\#nnnn\]    | 16     |
| 2E       | OR A, \[X\]         | 8      |
| 2F       | OR A, \[Y\]         | 8      |
| 9D nn    | OR F, \#nn          | 12     |
| CE B4 nn | OR B, \#nn          | 12     |
| CE B5 nn | OR L, \#nn          | 12     |
| CE B6 nn | OR H, \#nn          | 12     |
| D9 nn nn | OR \[N+\#nn\], \#nn | 20     |
| CE 28 ss | OR A, \[X+\#ss\]    | 16     |
| CE 29 ss | OR A, \[Y+\#ss\]    | 16     |
| CE 2A    | OR A, \[X+L\]       | 16     |
| CE 2B    | OR A, \[Y+L\]       | 16     |
| CE 2C    | OR \[HL\], A        | 16     |
| CE 2D nn | OR \[HL\], \#nn     | 20     |
| CE 2E    | OR \[HL\], \[X\]    | 20     |
| CE 2F    | OR \[HL\], \[Y\]    | 20     |

### Execute

`#nn     = Immediate unsigned 8-Bits`
`A       = Register A`
`B       = Register B`
`L       = Register L`
`H       = Register H`
`F       = Register F`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`
`[X]     = Memory: (XI shl 16) or X`
`[Y]     = Memory: (YI shl 16) or Y`
`[#nnnn] = Memory: #nnnn`
`[X+#ss] = Memory: (XI shl 16) or (X + #ss)`
`[Y+#ss] = Memory: (YI shl 16) or (Y + #ss)`
`[X+L]   = Memory: (XI shl 16) or (X + signed(L))`
`[Y+L]   = Memory: (YI shl 16) or (Y + signed(L))`

`; OR Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds OR Sc`

### Description

"8-Bits Destination" Logic OR (Inclusive-OR) with "8-Bits Source".

`Can be used to set one or multiple bits.`

`Bit 0 - Mask $01`
`Bit 1 - Mask $02`
`Bit 2 - Mask $04`
`Bit 3 - Mask $08`
`Bit 4 - Mask $10`
`Bit 5 - Mask $20`
`Bit 6 - Mask $40`
`Bit 7 - Mask $80`
`All   - Mask $FF`

### Conditions

Zero: Set when result is 0

Sign: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

### Examples

`; A = 0x45`
**`OR`` ``A,`` ``$40`**
`; A = 0x45`
`; F = (Zero=0):(Sign=0)`

`; B = 0xF0`
**`OR`` ``B,`` ``$04`**
`; B = 0xF4`
`; F = (Zero=0):(Sign=1)`

`; A = 0xF0`
**`OR`` ``A,`` ``$55`**
`; A = 0xF5`
`; F = (Zero=0):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
