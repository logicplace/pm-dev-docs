\== POP = Pop Register from Stack
==

| Hex   | Mnemonic | Cycles | Regs stacked from top to bottom              |
| ----- | -------- | ------ | -------------------------------------------- |
| A8    | POP BA   | 12     | B, A                                         |
| A9    | POP HL   | 12     | H, L                                         |
| AA    | POP X    | 12     | X(Hi), X(Lo)                                 |
| AB    | POP Y    | 12     | Y(Hi), Y(Lo)                                 |
| AC    | POP N    | 8      | N                                            |
| AD    | POP I    | 8      | I                                            |
| AE    | POPX     | 12     | XI, YI                                       |
| AF    | POP F    | 8      | F                                            |
| CF B4 | POP A    | 12     | A                                            |
| CF B5 | POP B    | 12     | B                                            |
| CF B6 | POP L    | 12     | L                                            |
| CF B7 | POP H    | 12     | H                                            |
| CF BC | POPA     | 44     | B, A, H, L, X(Hi:Lo), Y(Hi:Lo), N            |
| CF BD | POPAX    | 56     | B, A, H, L, X(Hi:Lo), Y(Hi:Lo), N, I, XI, YI |

### Execute

`A        = Register A`
`B        = Register B`
`L        = Register L`
`H        = Register H`
`N        = Register N`
`F        = Register F`
`I        = Register I`
`XI       = Register XI`
`YI       = Register YI`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`
`SP       = Register SP (Stack Pointer)`

`; POP r16`
`;`
`; r16 = 16-Bits Register (BA, HL, X or Y)`

`r16 = (Memory[SP+1] SHL 8) OR Memory[SP]`
`SP = SP + 2`

`; POP r8`
`;`
`; r8  =  8-Bits Register (A, B, L, H, N, I and F)`

`r8 = Memory[SP]`
`SP = SP + 1`

`; POPX`

`XI = Memory[SP+1]`
`YI = Memory[SP]`
`SP = SP + 2`

`; POPA`

`B = Memory[SP+8] = B`
`A = Memory[SP+7] = A`
`H = Memory[SP+6] = H`
`L = Memory[SP+5] = L`
`X = (Memory[SP+4] SHL 8) OR Memory[SP+3]`
`Y = (Memory[SP+2] SHL 8) OR Memory[SP+1]`
`N = Memory[SP]`
`SP = SP + 9`

`; POPAX`

`B = Memory[SP+11]`
`A = Memory[SP+10]`
`H = Memory[SP+9]`
`L = Memory[SP+8]`
`X = (Memory[SP+7] SHL 8) OR Memory[SP+6]`
`Y = (Memory[SP+5] SHL 8) OR Memory[SP+4]`
`N = Memory[SP+3]`
`I = Memory[SP+2]`
`XI = Memory[SP+1]`
`YI = Memory[SP]`
`SP = SP + 12`

### Description

Pop register(s) from the stack.

### Conditions

None

### Examples

`; BA = 0x1337`
`; SP = 0x2000`
[`PUSH`` ``BA`](PM_Opc_PUSH.md "wikilink")
`; BA = 0x1337`
`; SP = 0x1FFE`
[`MOV`` ``A,`` ``0x80`](PM_Opc_MOV8.md "wikilink")
`; BA = 0x1380`
`; SP = 0x1FFE`
[`INC`` ``B`](PM_Opc_INC.md "wikilink")
`; BA = 0x1480`
`; SP = 0x1FFE`
**`POP`` ``BA`**
`; BA = 0x1337`
`; SP = 0x2000`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
