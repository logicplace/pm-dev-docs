# ADC = Addition with Carry (8-bits)

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| 08       | ADC A,A         | 2      |
| 09       | ADC A,B         | 2      |
| 0A nn    | ADC A,#nn       | 2      |
| 0B       | ADC A,\[HL]     | 2      |
| 0C ll    | ADC A,\[BR:ll]  | 3      |
| 0D ll hh | ADC A,\[hhll]   | 4      |
| 0E       | ADC A,\[IX]     | 2      |
| 0F       | ADC A,\[IY]     | 2      |
| CE 08 dd | ADC A,\[IX+dd]  | 4      |
| CE 09 dd | ADC A,\[IY+dd]  | 4      |
| CE 0A    | ADC A,\[IX+L]   | 4      |
| CE 0B    | ADC A,\[IY+L]   | 4      |
| CE 0C    | ADC \[HL],A     | 4      |
| CE 0D nn | ADC \[HL],#nn   | 5      |
| CE 0E    | ADC \[HL],\[IX] | 5      |
| CE 0F    | ADC \[HL],\[IY] | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd      = Immediate signed 8-bits
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or ll
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
; ADC Ds, Sc
;
; Ds = Destination
; Sc = Source

; (If flags D=0 and U=0)
Ds = Ds + Sc + Carry

;------------------------------------------------

; (If flags D=0 and U=1)
Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F) + Carry

;------------------------------------------------

; (If flags D=1 and U=0)
IF (((Ds & 15) + (Sc & 15) + Carry) >= 10) THEN
  Ds = Ds + Sc + Carry + 6
ELSE
  Ds = Ds + Sc + Carry
ENDIF
IF (Ds >= 0xA0) Ds = Ds + 0x60

;------------------------------------------------

; (If flags D=1 and U=1)
IF (((Ds & 15) + (Sc & 15) + Carry) >= 10) THEN
  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F) + Carry + 6
ELSE
  Ds & 0x0F = (Ds & 0x0F) + (Sc & 0x0F) + Carry
ENDIF
```

## Description

8-bits Source and Carry adds to the 8-bits Destination.

## Conditions

### If flags D=0 and U=0

* Zero: Set when result is 0
* Carry: Set when result is >= 256
* Overflow: Set when result exceeds 8-bits signed range (< -128 OR > 127)
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
; SC = (Carry=1)
ADC A,$80
; A = 0xD6 (0x55 + 0x80 + 0x01 = 0x(0)D6)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x31
; A = 0xCF
; SC = (Carry=0)
ADC A,B
; B = 0x31
; A = 0x00 (0xCF + 0x31 + 0x00 = 0x(1)00)
; SC = (Zero=1):(Carry=1):(Overflow=0):(Negative=0)
```

```
; [HL] = 0xDE
; A = 0xCF
; SC = (Carry=0)
ADC A,[HL]
; [HL] = 0xDE
; A = 0xAD (0xCF + 0xDE + 0x00 = 0x(1)AD)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; ( Decimal = 1, Unpack = 0 )
; A = 0x09
; SC = (Carry=1)
ADC A,$01
; A = 0x11 (09 + 01 + 01 = 11)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; ( Decimal = 0, Unpack = 1 )
; A = 0x3F (Note, in "unpack mode" the high nibble is always discarded)
; SC = (Carry=1)
ADC A,$01
; A = 0x01 (0xF + 0x1 + 0x1 = 0x(1)1)
; SC = (Zero=1):(Carry=1):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
