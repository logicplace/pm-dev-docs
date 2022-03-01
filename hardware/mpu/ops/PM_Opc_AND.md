\== AND = Logical AND ==

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 20       | AND A, A             | 8      |
| 21       | AND A, B             | 8      |
| 22 nn    | AND A, \#nn          | 8      |
| 23       | AND A, \[HL\]        | 8      |
| 24 nn    | AND A, \[N+\#nn\]    | 12     |
| 25 nn nn | AND A, \[\#nnnn\]    | 16     |
| 26       | AND A, \[X\]         | 8      |
| 27       | AND A, \[Y\]         | 8      |
| 9C nn    | AND F, \#nn          | 12     |
| CE B0 nn | AND B, \#nn          | 12     |
| CE B1 nn | AND L, \#nn          | 12     |
| CE B2 nn | AND H, \#nn          | 12     |
| D8 nn nn | AND \[N+\#nn\], \#nn | 20     |
| CE 20 ss | AND A, \[X+\#ss\]    | 16     |
| CE 21 ss | AND A, \[Y+\#ss\]    | 16     |
| CE 22    | AND A, \[X+L\]       | 16     |
| CE 23    | AND A, \[Y+L\]       | 16     |
| CE 24    | AND \[HL\], A        | 16     |
| CE 25 nn | AND \[HL\], \#nn     | 20     |
| CE 26    | AND \[HL\], \[X\]    | 20     |
| CE 27    | AND \[HL\], \[Y\]    | 20     |

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

`; AND Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds AND Sc`

### Description

"8-Bits Destination" Logic AND with "8-Bits Source".

`Can be used to reset (clear) one or multiple bits.`

`Bit 0 - Mask $FE`
`Bit 1 - Mask $FD`
`Bit 2 - Mask $FB`
`Bit 3 - Mask $F7`
`Bit 4 - Mask $EF`
`Bit 5 - Mask $DF`
`Bit 6 - Mask $BF`
`Bit 7 - Mask $7F`
`All   - Mask $00`

### Conditions

Zero: Set when result is 0

Sign: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

### Examples

`; A = 0x85`
**`AND`` ``A,`` ``$80`**
`; A = 0x80`
`; F = (Zero=0):(Sign=1)`

`; B = 0xF0`
**`AND`` ``B,`` ``$04`**
`; B = 0x00`
`; F = (Zero=1):(Sign=0)`

`; A = 0xF0`
**`AND`` ``A,`` ``$55`**
`; A = 0x50`
`; F = (Zero=0):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
