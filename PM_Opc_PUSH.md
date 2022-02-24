\== PUSH = Push Register into Stack
==

| Hex   | Mnemonic | Cycles | Regs stacked from top to bottom              |
| ----- | -------- | ------ | -------------------------------------------- |
| A0    | PUSH BA  | 16     | B, A                                         |
| A1    | PUSH HL  | 16     | H, L                                         |
| A2    | PUSH X   | 16     | X(Hi), X(Lo)                                 |
| A3    | PUSH Y   | 16     | Y(Hi), Y(Lo)                                 |
| A4    | PUSH N   | 12     | N                                            |
| A5    | PUSH I   | 12     | I                                            |
| A6    | PUSHX    | 16     | XI, YI                                       |
| A7    | PUSH F   | 12     | F                                            |
| CF B0 | PUSH A   | 12     | A                                            |
| CF B1 | PUSH B   | 12     | B                                            |
| CF B2 | PUSH L   | 12     | L                                            |
| CF B3 | PUSH H   | 12     | H                                            |
| CF B8 | PUSHA    | 48     | B, A, H, L, X(Hi:Lo), Y(Hi:Lo), N            |
| CF B9 | PUSHAX   | 60     | B, A, H, L, X(Hi:Lo), Y(Hi:Lo), N, I, XI, YI |

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

`; PUSH r16`
`;`
`; r16 = 16-Bits Register (BA, HL, X or Y)`

`SP = SP - 2`
`Memory[SP+1] = r16 SHR 8      ; (High Byte)`
`Memory[SP]   = r16 AND 0x00FF ; (Low Byte)`

`; PUSH r8`
`;`
`; r8  =  8-Bits Register (A, B, L, H, N, I and F)`

`SP = SP - 1`
`Memory[SP]   = r8`

`; PUSHX`

`SP = SP - 2`
`Memory[SP+1] = XI`
`Memory[SP]   = YI`

`; PUSHA`

`SP = SP - 9`
`Memory[SP+8] = B`
`Memory[SP+7] = A`
`Memory[SP+6] = H`
`Memory[SP+5] = L`
`Memory[SP+4] = X SHR 8      ; X(Hi)`
`Memory[SP+3] = X AND 0x00FF ; X(Lo)`
`Memory[SP+2] = Y SHR 8      ; Y(Hi)`
`Memory[SP+1] = Y AND 0x00FF ; Y(Lo)`
`Memory[SP]   = N`

`; PUSHAX`

`SP = SP - 12`
`Memory[SP+11] = B`
`Memory[SP+10] = A`
`Memory[SP+9]  = H`
`Memory[SP+8]  = L`
`Memory[SP+7]  = X SHR 8      ; X(Hi)`
`Memory[SP+6]  = X AND 0x00FF ; X(Lo)`
`Memory[SP+5]  = Y SHR 8      ; Y(Hi)`
`Memory[SP+4]  = Y AND 0x00FF ; Y(Lo)`
`Memory[SP+3]  = N`
`Memory[SP+2]  = I`
`Memory[SP+1]  = XI`
`Memory[SP]    = YI`

### Description

Push register(s) into the stack.

### Conditions

None

### Examples

`; BA = 0x1337`
`; SP = 0x2000`
**`PUSH`` ``BA`**
`; BA = 0x1337`
`; SP = 0x1FFE`
[`MOV`` ``A,`` ``0x80`](PM_Opc_MOV8.md "wikilink")
`; BA = 0x1380`
`; SP = 0x1FFE`
[`INC`` ``B`](PM_Opc_INC.md "wikilink")
`; BA = 0x1480`
`; SP = 0x1FFE`
[`POP`` ``BA`](PM_Opc_POP.md "wikilink")
`; BA = 0x1337`
`; SP = 0x2000`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")