\== SWAP = Swap Low and High Nibbles ==

| Hex | Mnemonic    | Cycles |
| --- | ----------- | ------ |
| F6  | SWAP A      | 8      |
| F7  | SWAP \[HL\] | 12     |

### Execute

`A        = (8-Bits) Register A`
`[HL]     = (8-Bits) Memory: (I shl 16) or HL`

`; SWAP Ds`
`;`
`; Ds = Source/Destination`

`Ds = (Ds SHL 4) OR (Ds SHR 4)`

### Description

Swap low and high nibbles of a given byte.

### Conditions

None

### Examples

`; A = 0x3A`
**`SWAP`` ``A`**
`; A = 0xA3`

`; [HL] = 0xF6`
**`SWAP`` ``[HL]`**
`; [HL] = 0x6F`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")