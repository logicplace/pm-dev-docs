\== EX = Expand Register ==

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE A8 | EX BA, A | 12     |

### Execute

`A       =  (8-Bits) Register A`
`BA      = (16-Bits) Register BA: (B shl 8) or A`

`; EX BA, A`
`;`
`; BA = Destination`
`; A  = Source`

`IF (A AND 0x80) THEN  ; Check for sign`
`  B = 0xFF`
`ELSE`
`  B = 0x00`
`ENDIF`

### Description

EX expands register A into BA, turning a signed 8-bits value into
16-bits.

### Conditions

None

### Examples

`; A = 0x05 (5)`
**`EX`` ``BA,`` ``A`**
`; BA = 0x0005 (5)`

`; A = 0xF9 (-7)`
**`EX`` ``BA,`` ``A`**
`; BA = 0xFFF9 (-7)`

`; A = 0x00 (0)`
**`EX`` ``BA,`` ``A`**
`; BA = 0x0000 (0)`

`; A = 0x7F (127)`
**`EX`` ``BA,`` ``A`**
`; BA = 0x007F (127)`

`; A = 0x80 (-128)`
**`EX`` ``BA,`` ``A`**
`; BA = 0xFF80 (-128)`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")