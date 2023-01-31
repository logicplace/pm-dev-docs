# Calling routines

| Hex      | Mnemonic     | Cycles,True | or False | Condition                                   |
| -------- | ------------ | ----------- | -------- | ---------------------------------------     |
| E0 rr    | CARS C,rr    | 5           | 2        | Carry=1                                     |
| E1 rr    | CARS NC,rr   | 5           | 2        | Carry=0                                     |
| E2 rr    | CARS Z,rr    | 5           | 2        | Zero=1                                      |
| E3 rr    | CARS NZ,rr   | 5           | 2        | Zero=0                                      |
| E8 rr qq | CARL C,qqrr  | 6           | 3        | Carry=1                                     |
| E9 rr qq | CARL NC,qqrr | 6           | 3        | Carry=0                                     |
| EA rr qq | CARL Z,qqrr  | 6           | 3        | Zero=1                                      |
| EB rr qq | CARL NZ,qqrr | 6           | 3        | Zero=0                                      |
| F0 rr    | CARS rr      | 5           | n/a      | n/a                                         |
| F2 rr qq | CARL qqrr    | 6           | n/a      | n/a                                         |
| FB ll hh | CALL \[hhll] | 5           | n/a      | n/a                                         |
| FC kk    | INT \[kk]    | 5           | n/a      | n/a                                         |
| CE F0 rr | CARS LT,rr   | 6           | 3        | (Overflow=1) != (Negative=1)                |
| CE F1 rr | CARS LE,rr   | 6           | 3        | ((Overflow=0) != (Negative=0)) OR (Zero=1)  |
| CE F2 rr | CARS GT,rr   | 6           | 3        | ((Overflow=1) == (Negative=1)) AND (Zero=0) |
| CE F3 rr | CARS GE,rr   | 6           | 3        | (Overflow=0) == (Negative=0)                |
| CE F4 rr | CARS V,rr    | 6           | 3        | Overflow=1                                  |
| CE F5 rr | CARS NV,rr   | 6           | 3        | Overflow=0                                  |
| CE F6 rr | CARS P,rr    | 6           | 3        | Negative=0                                  |
| CE F7 rr | CARS M,rr    | 6           | 3        | Negative=1                                  |
| CE F8 rr | CARS F0,rr   | 6           | 3        | F0=1<sup>*</sup>                            |
| CE F9 rr | CARS F1,rr   | 6           | 3        | F1=1 (unused flag)                          |
| CE FA rr | CARS F2,rr   | 6           | 3        | F2=1 (unused flag)                          |
| CE FB rr | CARS F3,rr   | 6           | 3        | F3=1 (unused flag)                          |
| CE FC rr | CARS NF0,rr  | 6           | 3        | F0=0<sup>*</sup>                            |
| CE FD rr | CARS NF1,rr  | 6           | 3        | F1=0 (unused flag)                          |
| CE FE rr | CARS NF2,rr  | 6           | 3        | F2=0 (unused flag)                          |
| CE FF rr | CARS NF3,rr  | 6           | 3        | F3=0 (unused flag)                          |

\* _F0 is set on the Pokémon Channel emulator when the previous DIV had a denominator of 0._

## Execute

```
kk     = Lower 8 bits of a vector address
rr     = Immediate signed 8-bits
qqrr   = Immediate signed 16-bits
NB/CB  = Register NB or CB
SP     = Register SP (Stack Pointer)
PC     = Register PC (Program Counter)
[hhll] = Memory: (EP shl 16) or hhll
```

### Conditional CARS

```
; CARS *,rr

IF (Condition) THEN
  SP = SP - 3
  Memory[SP+2] = CB
  Memory[SP+1] = PC SRL 8
  Memory[SP]   = PC AND 0x00FF
  CB = NB
  PC = PC + rr - 1
ENDIF
```

### Conditional CARL

```
; CARL *,qqrr

IF (Condition) THEN
  SP = SP - 3
  Memory[SP+2] = CB
  Memory[SP+1] = PC SRL 8
  Memory[SP]   = PC AND 0x00FF
  CB = NB
  PC = PC + qqrr - 1
ENDIF
```

### CARS

```
; CARS rr

SP = SP - 3
Memory[SP+2] = CB
Memory[SP+1] = PC SRL 8
Memory[SP]   = PC AND 0x00FF
CB = NB
PC = PC + rr - 1
```

### CARL

```
; CARL qqrr

SP = SP - 3
Memory[SP+2] = CB
Memory[SP+1] = PC SRL 8
Memory[SP]   = PC AND 0x00FF
CB = NB
PC = PC + qqrr - 1
```

### CALL

```
; CALL [hhll]

SP = SP - 3
Memory[SP+2] = CB
Memory[SP+1] = PC SRL 8
Memory[SP]   = PC AND 0x00FF
CB = NB
PC = Memory16[(EP SLL 16) + hhll]
```

### INT

```
; INT [kk]  ;; (not fully tested)

SP = SP - 4
Memory[SP+3] = CB
Memory[SP+2] = PC SRL 8
Memory[SP+1] = PC AND 0x00FF
Memory[SP]   = SC
CB = NB
PC = Memory16[kk]
```

## Description

Call a subroutine (CARS/CARL/CALL) or a interrupt vector (INT).

Use [RET](PM_Opc_RET.md#ret) to return from a subroutine and [RETE](PM_Opc_RET.md#rete) from a interrupt.

NOTE: All non-branch instructions do "NB = CB" causing NB to be restored, any branch that requires banking needs "LD NB, A" or "LD NB, #nn" directly before any call.

## Conditions

None

## Examples

```
; A = 0x10
; B = 0x10
CALL somefunction
; A = 0x11
; B = 0x0F
BIT B, #0x10
; SC = (Zero=0):(Negative=0)
CARS Z,somefunction    ; Condition fails, call not taken
; A = 0x11
; B = 0x0F
; SC = (Zero=0):(Negative=0)
CARS NS,somefunction   ; Condition succeeds
; A = 0x12
; B = 0x0E

 (...)

somefunction:
  INC A
  DEC B
  RET                   ; Return from the call
```

```
; Calling a subroutine in different bank
LD NB, $0F
CALL function_at_bank_16
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
