# CP = Compare (8-bits)

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 30       | CP A,A               | 2      |
| 31       | CP A,B               | 2      |
| 32 nn    | CP A,#nn             | 2      |
| 33       | CP A,\[HL]           | 2      |
| 34 ll    | CP A,\[BR:ll]        | 3      |
| 35 ll hh | CP A,\[hhll]         | 4      |
| 36       | CP A,\[IX]           | 2      |
| 37       | CP A,\[IY]           | 2      |
| DB ll nn | CP \[BR:ll],#nn      | 4      |
| CE 30 dd | CP A,\[IX+dd]        | 4      |
| CE 31 dd | CP A,\[IY+dd]        | 4      |
| CE 32    | CP A,\[IX+L]         | 4      |
| CE 33    | CP A,\[IY+L]         | 4      |
| CE 34    | CP \[HL],A           | 4      |
| CE 35 nn | CP \[HL],#nn         | 5      |
| CE 36    | CP \[HL],\[IX]       | 5      |
| CE 37    | CP \[HL],\[IY]       | 5      |
| CE BC nn | CP B,#nn             | 3      |
| CE BD nn | CP L,#nn             | 3      |
| CE BE nn | CP H,#nn             | 3      |
| CE BF nn | CP BR,#nn            | 3      |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd      = Immediate signed 8-bits
A       = Register A
B       = Register B
BR      = Register BR
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]    = Memory: (XP shl 16) or IX
[IY]    = Memory: (YP shl 16) or IY
[hhll]  = Memory: (EP shl 16) or hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]  = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]  = Memory: (YP shl 16) or (IY + signed(L))
```

```
; CP Sc2, Sc
;
; Sc2 = Source 2
; Sc  = Source

(discarded) = Sc2 - Sc
```

## Description

Subtracts "8-bits Source 2" from "8-bits Source", result is discarded.

This instruction is used to compare values.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result overflow 8-bits signed range (< -128 OR > 127)
* Negative: Set when bit 7 of the result is 1

## Examples

```
; A = 0x55
CP A, $80
; A = 0x55
;     0xD5 (0x55 - 0x80 = 0x(1)D4)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x31
; A = 0xCF
CP A, B
; B = 0x31
; A = 0xCF
;     0x9E (0xCF - 0x31 = 0x(0)9E)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
