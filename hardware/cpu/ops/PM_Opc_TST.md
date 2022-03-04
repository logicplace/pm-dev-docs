\== TST = Test Bits ==

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 94       | TST A, B             | 8      |
| 95 nn    | TST \[HL\], \#nn     | 12     |
| 96 nn    | TST A, \#nn          | 8      |
| 97 nn    | TST B, \#nn          | 8      |
| DC nn nn | TST \[N+\#nn\], \#nn | 16     |

### Execute

`#nn     = Immediate unsigned 8-Bits`
`A       = Register A`
`B       = Register B`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`

`; TST Sc2, Sc`
`;`
`; Sc2 = Source 2`
`; Sc  = Source`

`(discarded) = Sc2 AND Sc`

### Description

"8-Bits Source 2" Logic AND with "8-Bits Source", result is discarded.

Source is usually a mask, Flag Z (Zero) return true if the result masked
bits are all 0.

`Common usage:`

`Check Bit 0 - Mask $01`
`Check Bit 1 - Mask $02`
`Check Bit 2 - Mask $04`
`Check Bit 3 - Mask $08`
`Check Bit 4 - Mask $10`
`Check Bit 5 - Mask $20`
`Check Bit 6 - Mask $40`
`Check Bit 7 - Mask $80`

`Zero result if Bit is 0.`
`Non-zero result if Bit is 1.`

### Conditions

Zero: Set when result is 0

Sign: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

### Examples

`; A = 0x85`
**`TST`` ``A,`` ``$80`**
`; F = (Zero=0):(Sign=1)`

`; B = 0xF0`
**`TST`` ``B,`` ``$04`**
`; F = (Zero=1):(Sign=0)`

`; A = 0x05`
**`TST`` ``A,`` ``$01`**
`; F = (Zero=0):(Sign=0)`
`JNZ OddAccu  ; Called when first bit is 1.`
`JZ EvenAccu`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
