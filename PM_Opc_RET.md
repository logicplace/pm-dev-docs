\== RET = Return from routine ==

| Hex | Mnemonic | Cycles |
| --- | -------- | ------ |
| F8  | RET      | 16     |
| F9  | RETI     | 16     |
| FA  | RETSKIP  | 16     |

### Execute

`F        = Register F`
`U/V      = Register U or V`
`SP       = Register SP (Stack Pointer)`
`PC       = Register PC (Program Counter)`

`; RET (Return from a subroutine)`

`V = Memory[SP+2]`
`PC = (Memory[SP+1] SHL 8) + Memory[SP]`
`SP = SP + 3`

`; RETI (Return from an interrupt)`

`V = Memory[SP+3]`
`PC = (Memory[SP+2] SHL 8) + Memory[SP+1]`
`F = Memory[SP]`
`SP = SP + 4`

`; RETSKIP (Return from a subroutine and skip 2 bytes)`

`V = Memory[SP+2]`
`PC = (Memory[SP+1] SHL 8) + Memory[SP] + 2`
`SP = SP + 3`

### Description

Return from a subroutine or an interrupt.

### Conditions

None

### Examples

` ; A = 0x10`
` ; B = 0x10`
` `[`CALL`` ``somefunction`](PM_Opc_CALL.md "wikilink")
` ; A = 0x11`
` ; B = 0x0F`

` (...)`

`somefunction:`
` `[`INC`` ``A`](PM_Opc_INC.md "wikilink")
` `[`DEC`` ``B`](PM_Opc_DEC.md "wikilink")
` `**`RET`**
` `[`INC`` ``A`](PM_Opc_INC.md "wikilink")`  ; Never executed`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")