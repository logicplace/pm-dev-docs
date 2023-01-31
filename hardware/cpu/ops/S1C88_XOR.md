# XOR = Logical Exclusive-OR

| Hex      | Mnemonic             | Cycles |
| -------- | -------------------- | ------ |
| 38       | XOR A,A              | 2      |
| 39       | XOR A,B              | 2      |
| 3A nn    | XOR A,#nn            | 2      |
| 3B       | XOR A,\[HL]          | 2      |
| 3C ll    | XOR A,\[BR:ll]       | 3      |
| 3D ll hh | XOR A,\[hhll]        | 4      |
| 3E       | XOR A,\[IX]          | 2      |
| 3F       | XOR A,\[IY]          | 2      |
| 9E nn    | XOR SC,#nn           | 3      |
| CE B8 nn | XOR B,#nn            | 3      |
| CE B9 nn | XOR L,#nn            | 3      |
| CE BA nn | XOR H,#nn            | 3      |
| DA ll nn | XOR \[BR:ll],#nn     | 5      |
| CE 38 dd | XOR A,\[IX+dd]       | 4      |
| CE 39 dd | XOR A,\[IY+dd]       | 4      |
| CE 3A    | XOR A,\[IX+L]        | 4      |
| CE 3B    | XOR A,\[IY+L]        | 4      |
| CE 3C    | XOR \[HL],A          | 4      |
| CE 3D nn | XOR \[HL],#nn        | 5      |
| CE 3E    | XOR \[HL],\[IX]      | 5      |
| CE 3F    | XOR \[HL],\[IY]      | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
A       = Register A
B       = Register B
L       = Register L
H       = Register H
SC      = Register SC
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]    = Memory: (XP shl 16) or IX
[IY]    = Memory: (YP shl 16) or IY
[hhll]  = Memory: hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]  = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]  = Memory: (YP shl 16) or (IY + signed(L))
```

```
; XOR Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds XOR Sc
```

## Description

"8-bits Destination" Logical XOR (Exclusive-OR) with "8-bits Source".

Can be used to toggle one or multiple bits. Below is a table of bytes to XOR with in order to toggle certain bits:

| Toggle bits | Mask to use |
| ----------- | ----------- |
| Bit 0       | $01         |
| Bit 1       | $02         |
| Bit 2       | $04         |
| Bit 3       | $08         |
| Bit 4       | $10         |
| Bit 5       | $20         |
| Bit 6       | $40         |
| Bit 7       | $80         |
| All bits    | $FF         |

## Conditions

* Zero: Set when result is 0
* Negative: Set when 7th bit of the result is 1

Carry and Overflow remain unchanged

## Examples

```
; A = 0x45
XOR A, $40
; A = 0x05
; SC = (Zero=0):(Negative=0)
```

```
; B = 0xF0
XOR B, $04
; B = 0xF4
; SC = (Zero=0):(Negative=1)
```

```
; A = 0xF0
XOR A, $55
; A = 0xA5
; SC = (Zero=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
