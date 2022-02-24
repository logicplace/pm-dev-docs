\== XOR = Logical Exclusive-OR ==

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 38       | XOR A, A             | 8      |
| 39       | XOR A, B             | 8      |
| 3A nn    | XOR A, \#nn          | 8      |
| 3B       | XOR A, \[HL\]        | 8      |
| 3C nn    | XOR A, \[N+\#nn\]    | 12     |
| 3D nn nn | XOR A, \[\#nnnn\]    | 16     |
| 3E       | XOR A, \[X\]         | 8      |
| 3F       | XOR A, \[Y\]         | 8      |
| 9E nn    | XOR F, \#nn          | 12     |
| CE B8 nn | XOR B, \#nn          | 12     |
| CE B9 nn | XOR L, \#nn          | 12     |
| CE BA nn | XOR H, \#nn          | 12     |
| DA nn nn | XOR \[N+\#nn\], \#nn | 20     |
| CE 38 ss | XOR A, \[X+\#ss\]    | 16     |
| CE 39 ss | XOR A, \[Y+\#ss\]    | 16     |
| CE 3A    | XOR A, \[X+L\]       | 16     |
| CE 3B    | XOR A, \[Y+L\]       | 16     |
| CE 3C    | XOR \[HL\], A        | 16     |
| CE 3D nn | XOR \[HL\], \#nn     | 20     |
| CE 3E    | XOR \[HL\], \[X\]    | 20     |
| CE 3F    | XOR \[HL\], \[Y\]    | 20     |

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

`; XOR Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Ds XOR Sc`

### Description

"8-Bits Destination" Logic XOR (Exclusive-OR) with "8-Bits Source".

`Can be used to toggle one or multiple bits.`

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

Sign: Set when 7th bit of the result is 1

Carry and Overflow remain unchanged

### Examples

`; A = 0x45`
**`XOR`` ``A,`` ``$40`**
`; A = 0x05`
`; F = (Zero=0):(Sign=0)`

`; B = 0xF0`
**`XOR`` ``B,`` ``$04`**
`; B = 0xF4`
`; F = (Zero=0):(Sign=1)`

`; A = 0xF0`
**`XOR`` ``A,`` ``$55`**
`; A = 0xA5`
`; F = (Zero=0):(Sign=1)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")