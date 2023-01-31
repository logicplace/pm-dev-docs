# POP = Pop Register from Stack

| Hex   | Mnemonic | Cycles | Regs stacked from top to bottom                  |
| ----- | -------- | ------ | --------------------------------------------     |
| A8    | POP BA   | 3      | B, A                                             |
| A9    | POP HL   | 3      | H, L                                             |
| AA    | POP IX   | 3      | IX(Hi), IX(Lo)                                   |
| AB    | POP IY   | 3      | IY(Hi), IY(Lo)                                   |
| AC    | POP BR   | 2      | BR                                               |
| AD    | POP EP   | 2      | EP                                               |
| AE    | POP IP   | 3      | XP, YP                                           |
| AF    | POP SC   | 2      | SC                                               |
| CF B4 | POP A    | 3      | A                                                |
| CF B5 | POP B    | 3      | B                                                |
| CF B6 | POP L    | 3      | L                                                |
| CF B7 | POP H    | 3      | H                                                |
| CF BC | POP ALL  | 44     | B, A, H, L, IX(Hi:Lo), IY(Hi:Lo), BR             |
| CF BD | POP ALE  | 56     | B, A, H, L, IX(Hi:Lo), IY(Hi:Lo), BR, EP, XP, YP |

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

### POP 16-bits

```
; POP r16
;
; r16 = 16-bits Register (BA, HL, IX or IY)

r16 = (Memory[SP+1] SLL 8) OR Memory[SP]
SP = SP + 2
```

### POP 8-bits

```
; POP r8
;
; r8  =  8-bits Register (A, B, L, H, BR, EP and SC)

r8 = Memory[SP]
SP = SP + 1
```

### POP IP

```
; POP IP

XP = Memory[SP+1]
YP = Memory[SP]
SP = SP + 2
```

### POP ALL

```
; POP ALL

B = Memory[SP+8] = B
A = Memory[SP+7] = A
H = Memory[SP+6] = H
L = Memory[SP+5] = L
IX = (Memory[SP+4] SLL 8) OR Memory[SP+3]
IY = (Memory[SP+2] SLL 8) OR Memory[SP+1]
BR = Memory[SP]
SP = SP + 9
```

### POP ALE

```
; POP ALE

B = Memory[SP+11]
A = Memory[SP+10]
H = Memory[SP+9]
L = Memory[SP+8]
IX = (Memory[SP+7] SLL 8) OR Memory[SP+6]
IY = (Memory[SP+5] SLL 8) OR Memory[SP+4]
BR = Memory[SP+3]
EP = Memory[SP+2]
XP = Memory[SP+1]
YP = Memory[SP]
SP = SP + 12
```

## Description

Pop register(s) from the stack.

## Conditions

None

## Examples

```
; BA = 0x1337
; SP = 0x2000
PUSH BA
; BA = 0x1337
; SP = 0x1FFE
LD A, 0x80
; BA = 0x1380
; SP = 0x1FFE
INC B
; BA = 0x1480
; SP = 0x1FFE
POP BA
; BA = 0x1337
; SP = 0x2000
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
