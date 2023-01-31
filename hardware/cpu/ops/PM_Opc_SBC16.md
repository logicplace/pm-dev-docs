# SBC = Subtract with Carry (16-bits)

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| CF 0C       | SBC BA,BA      | 4      |
| CF 0D       | SBC BA,HL      | 4      |
| CF 0E       | SBC BA,IX      | 4      |
| CF 0F       | SBC BA,IY      | 4      |
| CF 2C       | SBC HL,BA      | 4      |
| CF 2D       | SBC HL,HL      | 4      |
| CF 2E       | SBC HL,IX      | 4      |
| CF 2F       | SBC HL,IY      | 4      |
| CF 62 nn mm | SBC BA,#mmnn   | 4      |
| CF 63 nn mm | SBC HL,#mmnn   | 4      |

## Execute

```
hhll = Immediate unsigned 16-bits
BA   = Register BA: (B shl 8) or A
HL   = Register HL: (H shl 8) or L
IX   = Register IX
IY   = Register IY
```

```
; SBC Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds - Sc - Carry
```

## Description

Subtracts 16-bits Source and Carry from the 16-bits Destination.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result exceeds 16-bits signed range (< -32768 OR > 32767)
* Negative: Set when bit 15 of the result is 1

## Examples

```
; BA = 0x2EF0
; SC = (Carry=1)
SBC BA, $1337
; BA = 0x1BB8 (0x2EF0 - 0x1337 - 0x0001 = 0x(0)1BB8)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; HL = 0xBB7E
; BA = 0xCF12
; SC = (Carry=0)
SBC BA, HL
; HL = 0xBB7E
; BA = 0xEC6C (0xCF12 - 0xBB7E - 0x0000 = 0x(1)EC6C)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
