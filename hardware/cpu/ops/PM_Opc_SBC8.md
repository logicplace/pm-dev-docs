# SBC = Subtraction with Carry (8-bits)

| Hex      | Mnemonic          | Cycles |
| -------- | ----------------- | ------ |
| 18       | SBC A,A           | 2      |
| 19       | SBC A,B           | 2      |
| 1A nn    | SBC A,#nn         | 2      |
| 1B       | SBC A,\[HL]       | 2      |
| 1C ll    | SBC A,\[BR:ll]    | 3      |
| 1D ll hh | SBC A,\[hhll]     | 4      |
| 1E       | SBC A,\[IX]       | 2      |
| 1F       | SBC A,\[IY]       | 2      |
| CE 18 dd | SBC A,\[IX+dd]    | 4      |
| CE 19 dd | SBC A,\[IY+dd]    | 4      |
| CE 1A    | SBC A,\[IX+L]     | 4      |
| CE 1B    | SBC A,\[IY+L]     | 4      |
| CE 1C    | SBC \[HL],A       | 4      |
| CE 1D nn | SBC \[HL],#nn     | 5      |
| CE 1E    | SBC \[HL],\[IX]   | 5      |
| CE 1F    | SBC \[HL],\[IY]   | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd      = Immediate signed 8-bits
A       = Register A
B       = Register B
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
; SBC Ds, Sc
;
; Ds = Destination
; Sc = Source

; (If flags D=0 and U=0)
Ds = Ds - Sc - Carry

;------------------------------------------------

; (If flags D=0 and U=1)
Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry

;------------------------------------------------

; (If flags D=1 and U=0)
IF (((Ds & 15) - (Sc & 15) - Carry) >= 10) THEN    ; Note: Should be an unsigned check
  Ds = Ds - Sc - Carry - 6
ELSE
  Ds = Ds - Sc - Carry
ENDIF
IF (Ds >= 0xA0) Ds = Ds - 0x60
; NOTE: This isn't accurate, there's some weird effect on a strange condition

;------------------------------------------------

; (If flags D=1 and U=1)
IF (((Ds & 15) - (Sc & 15) - Carry) >= 10) THEN    ; Note: Should be an unsigned check
  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry - 6
ELSE
  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - Carry
ENDIF
```

## Description

8-bits Source and Carry subtracts to the 8-bits Destination.

## Conditions

### If flags D=0 and U=0

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result overflow 8-bits signed range (< -128 OR > 127)
* Negative: Set when bit 7 of the result is 1

### If flags D=0 and U=1

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result exceeds 4-bits signed range (< -16 OR > 15)
* Negative: Set when bit 3 of the result is 1

### If flags D=1 and U=0

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Always reset
* Negative: Always reset

### If flags D=1 and U=1

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Always reset
* Negative: Always reset

## Examples

```
; A = 0x55
; SC = (Carry=1)
SBC A, $80
; A = 0xD4 (0x55 - 0x80 - 0x01 = 0x(1)D4)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x31
; A = 0xCF
; SC = (Carry=0)
SBC A, B
; B = 0x31
; A = 0x9E (0xCF - 0x31 - 0x00 = 0x(0)9E)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 1, Unpack = 0 )
; A = 0x10
; SC = (Carry=1)
SBC A,``
``$01
; A = 0x08 (10 - 01 - 01 = 08)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 0, Unpack = 1 )
; A = 0x3F (Note, in "unpack mode" the high nibble is always discarded)
; SC = (Carry=1)
SBC A, $01
; A = 0x0D (0xF - 0x1 - 0x1 = 0x(0)D)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
