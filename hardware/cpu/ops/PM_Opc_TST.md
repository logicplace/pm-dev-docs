# BIT = Test Bits

| Hex      | Mnemonic         | Cycles |
| -------- | ---------------- | ------ |
| 94       | BIT A,B          | 2      |
| 95 nn    | BIT \[HL],#nn    | 3      |
| 96 nn    | BIT A,#nn        | 2      |
| 97 nn    | BIT B,#nn        | 2      |
| DC ll nn | BIT \[BR:ll],#nn | 4      |

## Execute

```
#nn     = Immediate unsigned 8-bits
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; BIT Sc2, Sc
;
; Sc2 = Source 2
; Sc  = Source

(discarded) = Sc2 AND Sc
```

## Description

"8-bits Source 2" Logical AND with "8-bits Source", result is discarded.

Source is usually a mask, Flag Z (Zero) is set if all the masked bits are 0.
Below is a table of bytes to check against for testing single bits.

| Check bit | Mask |
| --------- | ---- |
| Bit 0     | $01  |
| Bit 1     | $02  |
| Bit 2     | $04  |
| Bit 3     | $08  |
| Bit 4     | $10  |
| Bit 5     | $20  |
| Bit 6     | $40  |
| Bit 7     | $80  |
| All bits  | $FF  |

Zero result if Bit is 0.
Non-zero result if Bit is 1.

## Conditions

* Zero: Set when result is 0
* Negative: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

## Examples

```
; A = 0x85
BIT A, $80
; SC = (Zero=0):(Negative=1)
```

```
; B = 0xF0
BIT B, $04
; SC = (Zero=1):(Negative=0)
```

```
; A = 0x05
BIT A, $01
; SC = (Zero=0):(Negative=0)
JNZ OddAccu  ; Called when first bit is 1.
JZ EvenAccu
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
