# OR = Logical Inclusive-OR

| Hex      | Mnemonic            | Cycles |
| -------- | ------------------- | ------ |
| 28       | OR A,A              | 2      |
| 29       | OR A,B              | 2      |
| 2A nn    | OR A,#nn            | 2      |
| 2B       | OR A,\[HL]          | 2      |
| 2C ll    | OR A,\[BR:ll]       | 3      |
| 2D ll hh | OR A,\[hhll]        | 4      |
| 2E       | OR A,\[IX]          | 2      |
| 2F       | OR A,\[IY]          | 2      |
| 9D nn    | OR SC,#nn           | 3      |
| CE B4 nn | OR B,#nn            | 3      |
| CE B5 nn | OR L,#nn            | 3      |
| CE B6 nn | OR H,#nn            | 3      |
| D9 ll nn | OR \[BR:ll],#nn     | 5      |
| CE 28 dd | OR A,\[IX+dd]       | 4      |
| CE 29 dd | OR A,\[IY+dd]       | 4      |
| CE 2A    | OR A,\[IX+L]        | 4      |
| CE 2B    | OR A,\[IY+L]        | 4      |
| CE 2C    | OR \[HL],A          | 4      |
| CE 2D nn | OR \[HL],#nn        | 5      |
| CE 2E    | OR \[HL],\[IX]      | 5      |
| CE 2F    | OR \[HL],\[IY]      | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
A       = Register A
B       = Register B
L       = Register L
H       = Register H
SC       = Register SC
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]     = Memory: (XP shl 16) or IX
[IY]     = Memory: (YP shl 16) or IY
[hhll] = Memory: hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]   = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]   = Memory: (YP shl 16) or (IY + signed(L))
```

```
; OR Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds OR Sc
```

## Description

"8-bits Destination" Logical OR (Inclusive-OR) with "8-bits Source".

```
Truth table:

| 0 1
0 0 1
1 1 1
```

Can be used to set one or multiple bits. Below is a table of bytes to OR with in order to set certain bits:

| Set bits | Mask to use |
| -------- | ----------- |
| Bit 0    | $01         |
| Bit 1    | $02         |
| Bit 2    | $04         |
| Bit 3    | $08         |
| Bit 4    | $10         |
| Bit 5    | $20         |
| Bit 6    | $40         |
| Bit 7    | $80         |
| All bits | $FF         |

## Conditions

* Zero: Set when result is 0
* Negative: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

## Examples

```
; A = 0x45
OR A, $40
; A = 0x45
; SC = (Zero=0):(Negative=0)
```

```
; B = 0xF0
OR B, $04
; B = 0xF4
; SC = (Zero=0):(Negative=1)
```

```
; A = 0xF0
OR A, $55
; A = 0xF5
; SC = (Zero=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
