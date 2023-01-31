# RET = Return from routine

| Hex | Mnemonic | Cycles |
| --- | -------- | ------ |
| F8  | RET      | 4      |
| F9  | RETE     | 5      |
| FA  | RETS     | 6      |

## Execute

```
SC    = Register SC
NB/CB = Register NB or CB
SP    = Register SP (Stack Pointer)
PC    = Register PC (Program Counter)
```

### RET

```
; RET (Return from a subroutine)

CB = Memory[SP+2]
PC = (Memory[SP+1] SLL 8) + Memory[SP]
SP = SP + 3
```

### RETE

```
; RETE (Return from an interrupt)

CB = Memory[SP+3]
PC = (Memory[SP+2] SLL 8) + Memory[SP+1]
SC = Memory[SP]
SP = SP + 4
```

### RETS

```
; RETS (Return from a subroutine and skip 2 bytes)

CB = Memory[SP+2]
PC = (Memory[SP+1] SLL 8) + Memory[SP] + 2
SP = SP + 3
```

## Description

Return from a subroutine or an interrupt.

## Conditions

None

## Examples

```
; A = 0x10
; B = 0x10
CALL somefunction
; A = 0x11
; B = 0x0F

(...)

somefunction:
  INC A
  DEC B
  RET
  INC A  ; Never executed
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
