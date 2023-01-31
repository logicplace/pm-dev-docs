# SUB = Subtraction (8-bits)

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| 10       | SUB A,A         | 2      |
| 11       | SUB A,B         | 2      |
| 12 nn    | SUB A,#nn       | 2      |
| 13       | SUB A,\[HL]     | 2      |
| 14 ll    | SUB A,\[BR:ll]  | 3      |
| 15 ll hh | SUB A,\[hhll]]] | 4      |
| 16       | SUB A,\[IX]     | 2      |
| 17       | SUB A,\[IY]     | 2      |
| CE 10 dd | SUB A,\[IX+dd]  | 4      |
| CE 11 dd | SUB A,\[IY+dd]  | 4      |
| CE 12    | SUB A,\[IX+L]   | 4      |
| CE 13    | SUB A,\[IY+L]   | 4      |
| CE 14    | SUB \[HL],A     | 4      |
| CE 15 nn | SUB \[HL],#nn   | 5      |
| CE 16    | SUB \[HL],\[IX] | 5      |
| CE 17    | SUB \[HL],\[IY] | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd     = Immediate signed 8-bits
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]     = Memory: (XP shl 16) or IX
[IY]     = Memory: (YP shl 16) or IY
[hhll] = Memory: (EP shl 16) or hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]   = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]   = Memory: (YP shl 16) or (IY + signed(L))
```

```
; SUB Ds, Sc
;
; Ds = Destination
; Sc = Source

; (If flags D=0 and U=0)
Ds = Ds - Sc

;------------------------------------------------

; (If flags D=0 and U=1)
Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F)

;------------------------------------------------

; (If flags D=1 and U=0)
IF (((Ds & 15) - (Sc & 15)) >= 10) THEN    ; Note: Should be an unsigned check
  Ds = Ds - Sc - 6
ELSE
  Ds = Ds - Sc
ENDIF
IF (Ds >= 0xA0) Ds = Ds - 0x60
; NOTE: This isn't accurate, there's some weird effect on a strange condition

;------------------------------------------------

; (If flags D=1 and U=1)
IF (((Ds & 15) - (Sc & 15)) >= 10) THEN    ; Note: Should be an unsigned check
  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F) - 6
ELSE
  Ds & 0x0F = (Ds & 0x0F) - (Sc & 0x0F)
ENDIF
```

## Description

Subtracts 8-bits Source from the 8-bits Destination.

## Conditions

### If flags D=0 and U=0

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result exceeds 8-bits signed range (< -128 OR > 127)
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
SUB A, $80
; A = 0xD5 (0x55 - 0x80 = 0x(1)D5)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x31
; A = 0xCF
SUB A, B
; B = 0x31
; A = 0x9E (0xCF - 0x31 = 0x(0)9E)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 1, Unpack = 0 )
; A = 0x10
SUB A,``
``$01
; A = 0x09 (10 - 01 = 09)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 0, Unpack = 1 )
; A = 0x3F (Note, in "unpack mode" the high nibble is always discarded)
SUB A, $01
; A = 0x0E (0xF - 0x1 = 0x(0)E)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
