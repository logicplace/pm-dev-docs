\== MUL = Multiply ==

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE D8 | MUL L, A | 48     |

### Execute

`; MUL L, A`
`;`
`; L is the Factor/Multiplicand`
`; A is the Multiplier`
`; HL will be the Product`

`HL = L x A`

### Description

"8-Bits Register L" multiply by "8-Bits Register A", 16-Bits result is
placed on "16-Bits Register HL".

### Conditions

Zero: Set when result is 0

Carry: Always Clear

Overflow: Always Clear

Sign: Set when bit 15 of the result is 1

### Examples

`; A = 0x03`
`; L = 0x03`
**`MUL`` ``L,`` ``A`**
`; A = 0x03`
`; HL = 0x0009 (0x03 * 0x03 = 0x0009)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=0)`

`; A = 0x00`
`; L = 0x03`
**`MUL`` ``L,`` ``A`**
`; A = 0x00`
`; HL = 0x0000 (0x03 * 0x00 = 0x0000)`
`; F = (Zero=1):(Carry=0):(Overflow=0):(Sign=0)`

`; A = 0xFF`
`; L = 0xFF`
**`MUL`` ``L,`` ``A`**
`; A = 0xFF`
`; HL = 0xFE01 (0xFF * 0xFF = 0xFE01)`
`; F = (Zero=0):(Carry=0):(Overflow=0):(Sign=1)`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
