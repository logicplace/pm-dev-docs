# ADD = Addition (8-bits)

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| 00       | ADD A,A         | 2      |
| 01       | ADD A,B         | 2      |
| 02 nn    | ADD A,#nn       | 2      |
| 03       | ADD A,\[HL]     | 2      |
| 04 ll    | ADD A,\[BR:ll]  | 3      |
| 05 ll hh | ADD A,\[hhll]   | 4      |
| 06       | ADD A,\[IX]     | 2      |
| 07       | ADD A,\[IY]     | 2      |
| CE 00 dd | ADD A,\[IX+dd]  | 4      |
| CE 01 dd | ADD A,\[IY+dd]  | 4      |
| CE 02    | ADD A,\[IX+L]   | 4      |
| CE 03    | ADD A,\[IY+L]   | 4      |
| CE 04    | ADD \[HL],A     | 4      |
| CE 05 nn | ADD \[HL],#nn   | 5      |
| CE 06    | ADD \[HL],\[IX] | 5      |
| CE 07    | ADD \[HL],\[IY] | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd      = Immediate signed 8-bits
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]     = Memory: (XP shl 16) or IX
[IY]     = Memory: (YP shl 16) or IY
[hhll]  = Memory: (EP shl 16) or hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]  = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]  = Memory: (YP shl 16) or (IY + signed(L))
```

```
; ADD Ds, Sc
;
; Ds = Destination
; Sc = Source

; (If flags D=0 and U=0)
Ds = Ds + Sc

;------------------------------------------------

; (If flags D=0 and U=1)
Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F)

;------------------------------------------------

; (If flags D=1 and U=0)
IF (((Ds & 15) + (Sc & 15)) >= 10) THEN
  Ds = Ds + Sc + 6
ELSE
  Ds = Ds + Sc
ENDIF
IF (Ds >= 0xA0) Ds = Ds + 0x60

;------------------------------------------------

; (If flags D=1 and U=1)
IF (((Ds & 15) + (Sc & 15)) >= 10) THEN
  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F) + 6
ELSE
  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F)
ENDIF
```

## Description

8-bits Source adds to the 8-bits Destination.

## Conditions

### If flags D=0 and U=0

* Zero: Set when result is 0
* Carry: Set when result is >= 256
* Overflow: Set when result exceeds 8-bits signed range (< -128 OR >127)
* Negative: Set when bit 7 of the result is 1

### If flags D=0 and U=1

* Zero: Set when result is 0
* Carry: Set when result is >= 16
* Overflow: Set when result exceeds 4-bits signed range (< -16 OR > 15)
* Negative: Set when bit 3 of the result is 1

### If flags D=1 and U=0

* Zero: Set when result is 0
* Carry: Set when result is >= 100
* Overflow: Always reset
* Negative: Always reset

### If flags D=1 and U=1

* Zero: Set when result is 0
* Carry: Set when result is >= 10
* Overflow: Always reset
* Negative: Always reset

## Examples

```
; A = 0x55
ADD A, $80
; A = 0xD5 (0x55 + 0x80 = 0x(0)D5)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x31
; A = 0xCF
ADD A, B
; B = 0x31
; A = 0x00 (0xCF + 0x31 = 0x(1)00)
; SC = (Zero=1):(Carry=1):(Overflow=0):(Negative=0)
```

```
; [HL] = 0xDE
; A = 0xCF
ADD A, [HL]
; [HL] = 0xDE
; A = 0xAD (0xCF + 0xDE = 0x(1)AD)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; ( Decimal = 1, Unpack = 0 )
; A = 0x09
ADD A,``
``$01
; A = 0x10 (09 + 01 = 10)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 0, Unpack = 1 )
; A = 0x3F (Note, in "unpack mode" the high nibble is always discarded)
ADD A, $01
; A = 0x00 (0xF + 0x1 = 0x(1)0)
; SC = (Zero=1):(Carry=1):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
