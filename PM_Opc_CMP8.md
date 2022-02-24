\== CMP = Compare (8-Bits) ==

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 30       | CMP A, A             | 8      |
| 31       | CMP A, B             | 8      |
| 32 nn    | CMP A, \#nn          | 8      |
| 33       | CMP A, \[HL\]        | 8      |
| 34 nn    | CMP A, \[N+\#nn\]    | 12     |
| 35 nn nn | CMP A, \[\#nnnn\]    | 16     |
| 36       | CMP A, \[X\]         | 8      |
| 37       | CMP A, \[Y\]         | 8      |
| DB nn nn | CMP \[N+\#nn\], \#nn | 16     |
| CE 30 ss | CMP A, \[X+\#ss\]    | 16     |
| CE 31 ss | CMP A, \[Y+\#ss\]    | 16     |
| CE 32    | CMP A, \[X+L\]       | 16     |
| CE 33    | CMP A, \[Y+L\]       | 16     |
| CE 34    | CMP \[HL\], A        | 16     |
| CE 35 nn | CMP \[HL\], \#nn     | 20     |
| CE 36    | CMP \[HL\], \[X\]    | 20     |
| CE 37    | CMP \[HL\], \[Y\]    | 20     |
| CE BC nn | CMP B, \#nn          | 12     |
| CE BD nn | CMP L, \#nn          | 12     |
| CE BE nn | CMP H, \#nn          | 12     |
| CE BF nn | CMP N, \#nn          | 12     |

### Execute

`#nn     = Immediate unsigned 8-Bits`
`#ss     = Immediate signed 8-Bits`
`A       = Register A`
`B       = Register B`
`N       = Register N`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`
`[X]     = Memory: (XI shl 16) or X`
`[Y]     = Memory: (YI shl 16) or Y`
`[#nnnn] = Memory: (I shl 16) or #nnnn`
`[X+#ss] = Memory: (XI shl 16) or (X + #ss)`
`[Y+#ss] = Memory: (YI shl 16) or (Y + #ss)`
`[X+L]   = Memory: (XI shl 16) or (X + signed(L))`
`[Y+L]   = Memory: (YI shl 16) or (Y + signed(L))`

`; CMP Sc2, Sc`
`;`
`; Sc2 = Source 2`
`; Sc  = Source`

`(discarded) = Sc2 - Sc`

### Description

"8-Bits Source 2" subtracts with "8-Bits Source", result is discarded.

This instruction is used to compare values.

### Conditions

Zero: Set when result is 0

Carry: Set when result is \< 0

Overflow: Set when result overflow 8-bits signed range (\< -128 OR \>
127)

Sign: Set when bit 7 of the result is 1

### Examples

`; A = 0x55`
**`CMP`` ``A,`` ``$80`**
`; A = 0x55`
`;     0xD5 (0x55 - 0x80 = 0x(1)D4)`
`; F = (Zero=0):(Carry=0):(Overflow=1):(Sign=1)`

`; B = 0x31`
`; A = 0xCF`
**`CMP`` ``A,`` ``B`**
`; B = 0x31`
`; A = 0xCF`
`;     0x9E (0xCF - 0x31 = 0x(0)9E)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
