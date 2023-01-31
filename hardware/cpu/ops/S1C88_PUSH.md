# PUSH = Push Register into Stack

| Hex   | Mnemonic | Cycles | Regs stacked from top to bottom                  |
| ----- | -------- | ------ | --------------------------------------------     |
| A0    | PUSH BA  | 4      | B, A                                             |
| A1    | PUSH HL  | 4      | H, L                                             |
| A2    | PUSH IX  | 4      | IX(Hi), IX(Lo)                                   |
| A3    | PUSH IY  | 4      | IY(Hi), IY(Lo)                                   |
| A4    | PUSH BR  | 3      | BR                                               |
| A5    | PUSH EP  | 3      | EP                                               |
| A6    | PUSH IP  | 4      | XP, YP                                           |
| A7    | PUSH SC  | 3      | SC                                               |
| CF B0 | PUSH A   | 3      | A                                                |
| CF B1 | PUSH B   | 3      | B                                                |
| CF B2 | PUSH L   | 3      | L                                                |
| CF B3 | PUSH H   | 3      | H                                                |
| CF B8 | PUSH ALL | 48     | B, A, H, L, IX(Hi:Lo), IY(Hi:Lo), BR             |
| CF B9 | PUSH ALE | 60     | B, A, H, L, IX(Hi:Lo), IY(Hi:Lo), BR, EP, XP, YP |

## Execute

```
A  = Register A
B  = Register B
L  = Register L
H  = Register H
BR = Register BR
SC = Register SC
EP = Register EP
XP = Register XP
YP = Register YP
BA = Register BA: (B shl 8) or A
HL = Register HL: (H shl 8) or L
IX = Register IX
IY = Register IY
SP = Register SP (Stack Pointer)
```

### PUSH 16-bits

```
; PUSH r16
;
; r16 = 16-bits Register (BA, HL, IX or IY)

SP = SP - 2
Memory[SP+1] = r16 SRL 8      ; (High Byte)
Memory[SP]   = r16 AND 0x00FF ; (Low Byte)
```

### PUSH 8-bits

```
; PUSH r8
;
; r8  =  8-bits Register (A, B, L, H, BR, EP and SC)

SP = SP - 1
Memory[SP]   = r8
```

### PUSH IP

```
; PUSH IP

SP = SP - 2
Memory[SP+1] = XP
Memory[SP]   = YP
```

### PUSH ALL

```
; PUSH ALL

SP = SP - 9
Memory[SP+8] = B
Memory[SP+7] = A
Memory[SP+6] = H
Memory[SP+5] = L
Memory[SP+4] = IX SRL 8      ; IX(Hi)
Memory[SP+3] = IX AND 0x00FF ; IX(Lo)
Memory[SP+2] = IY SRL 8      ; IY(Hi)
Memory[SP+1] = IY AND 0x00FF ; IY(Lo)
Memory[SP]   = BR
```

### PUSH ALE

```
; PUSH ALE

SP = SP - 12
Memory[SP+11] = B
Memory[SP+10] = A
Memory[SP+9]  = H
Memory[SP+8]  = L
Memory[SP+7]  = IX SRL 8      ; IX(Hi)
Memory[SP+6]  = IX AND 0x00FF ; IX(Lo)
Memory[SP+5]  = IY SRL 8      ; IY(Hi)
Memory[SP+4]  = IY AND 0x00FF ; IY(Lo)
Memory[SP+3]  = BR
Memory[SP+2]  = EP
Memory[SP+1]  = XP
Memory[SP]    = YP
```

## Description

Push register(s) into the stack.

## Conditions

None

## Examples

```
; BA = 0x1337
; SP = 0x2000
PUSH BA
; BA = 0x1337
; SP = 0x1FFE
[`LD A, 0x80`](PM_Opc_MOV8.md)
; BA = 0x1380
; SP = 0x1FFE
[`INC B`](PM_Opc_INC.md)
; BA = 0x1480
; SP = 0x1FFE
[`POP BA`](PM_Opc_POP.md)
; BA = 0x1337
; SP = 0x2000
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
