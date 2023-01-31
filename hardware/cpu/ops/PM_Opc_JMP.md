# JMP = Jump to routine

| Hex      | Mnemonic     | Cycles | Condition                                   |
| -------- | ------------ | ------ | ---------------------------------------     |
| E4 dd    | JRS C,dd     | 2      | Carry=1                                     |
| E5 dd    | JRS NC,dd    | 2      | Carry=0                                     |
| E6 dd    | JRS Z,dd     | 2      | Zero=1                                      |
| E7 dd    | JRS NZ,dd    | 2      | Zero=0                                      |
| EC rr qq | JRL C,qqrr   | 3      | Carry=1                                     |
| ED rr qq | JRL NC,qqrr  | 3      | Carry=0                                     |
| EE rr qq | JRL Z,qqrr   | 3      | Zero=1                                      |
| EF rr qq | JRL NZ,qqrr  | 3      | Zero=0                                      |
| F1 dd    | JRS dd       | 2      | n/a                                         |
| F3 rr qq | JRL qqrr     | 3      | n/a                                         |
| F4       | JP HL        | 2      | n/a                                         |
| F5 dd    | DJR NZ,dd    | 4      | B != 0x00, decrement B before check         |
| FD kk    | JP \[kk]     | 2      | n/a                                         |
| CE E0 dd | JRS LT,dd    | 3      | (Overflow=1) != (Negative=1)                |
| CE E1 dd | JRS LE,dd    | 3      | ((Overflow=0) != (Negative=0)) OR (Zero=1)  |
| CE E2 dd | JRS GT,dd    | 3      | ((Overflow=1) == (Negative=1)) AND (Zero=0) |
| CE E3 dd | JRS GE,dd    | 3      | (Overflow=0) == (Negative=0)                |
| CE E4 dd | JRS V,dd     | 3      | Overflow=1                                  |
| CE E5 dd | JRS NV,dd    | 3      | Overflow=0                                  |
| CE E6 dd | JRS P,dd     | 3      | Negative=0                                  |
| CE E7 dd | JRS M,dd     | 3      | Negative=1                                  |
| CE E8 dd | JRS F0,dd    | 3      | F0=1<sup>*</sup>                            |
| CE E9 dd | JRS F1,dd    | 3      | F1=1 (unused flag)                          |
| CE EA dd | JRS F2,dd    | 3      | F2=1 (unused flag)                          |
| CE EB dd | JRS F3,dd    | 3      | F3=1 (unused flag)                          |
| CE EC dd | JRS NF0,dd   | 3      | F0=0<sup>*</sup>                            |
| CE ED dd | JRS NF1,dd   | 3      | F1=0 (unused flag)                          |
| CE EE dd | JRS NF2,dd   | 3      | F2=0 (unused flag)                          |
| CE EF dd | JRS NF3,dd   | 3      | F3=0 (unused flag)                          |

\* _F0 is set on the Pokémon Channel emulator when the previous DIV had a denominator of 0._

## Execute

```
kk     = Lower 8 bits of a vector address
dd     = Immediate signed 8-bits
qqrr   = Immediate signed 16-bits
B      = Register B
NB/CB  = Register NB or CB
HL     = Register HL: (H shl 8) or L
SP     = Register SP (Stack Pointer)
PC     = Register PC (Program Counter)
[hhll] = Memory: (EP shl 16) or hhll
```

### Conditional JRS

```
; JRS *,dd

IF (Condition) THEN
  CB = NB
  PC = PC + dd - 1
ENDIF
```

### Conditional JRL

```
; JRL *,ddss

IF (Condition) THEN
  CB = NB
  PC = PC + ddss - 1
ENDIF
```

### JRS

```
; JRS dd

CB = NB
PC = PC + dd - 1
```

### JRL

```
; JRL ddss

CB = NB
PC = PC + ddss - 1
```

### JP HL

```
; JP HL

CB = NB
PC = HL
```

### DJR

```
; DJR NZ,dd

B = B - 1
IF (B <> 0) THEN
  CB = NB
  PC = PC + dd - 1
ENDIF
```

### JP

```
; JP \[kk] (not fully tested)

CB = NB
PC = Memory16[kk SLL 1]
```

## Description

Jump into a new position of the program.

NOTE: All non-branch instructions do "NB = CB" causing NB to be restored, any branch that requires banking needs "LD NB, A" or "LD NB, #nn" directly before any jump.

## Conditions

**0xF5 - DJR NZ,dd**

* Zero: Set when result is 0

Carry, Overflow, and Sign remain unchanged

**All others:**

None

## Examples

```
; A = 0x10
CP A, 0x10  ; Compare A with 0x10`
; SC = (Zero=1):(Carry=0):(Overflow=0):(Negative=0)
JZ val_is_16
LD A, 0x00
val_is_16:
; A = 0x10
```

```
; Jump into a label located at a different bank
LD NB, $0F
JMP function_at_bank_15
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
