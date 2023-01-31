# DEC = Decrease Register by 1

| Hex   | Mnemonic       | Cycles |
| ----- | -------------- | ------ |
| 88    | DEC A          | 2      |
| 89    | DEC B          | 2      |
| 8A    | DEC L          | 2      |
| 8B    | DEC H          | 2      |
| 8C    | DEC BR         | 2      |
| 8D ll | DEC \[BR:ll]   | 4      |
| 8E    | DEC \[HL]      | 3      |
| 8F    | DEC SP         | 2      |
| 98    | DEC BA         | 2      |
| 99    | DEC HL         | 2      |
| 9A    | DEC IX         | 2      |
| 9B    | DEC IY         | 2      |

## Execute

```
A       = (8-bits) Register A
B       = (8-bits) Register B
L       = (8-bits) Register L
H       = (8-bits) Register H
BR      = (8-bits) Register BR
SP      = (16-bits) Register SP (Stack Pointer)
BA      = (16-bits) Register BA: (B shl 8) or A
HL      = (16-bits) Register HL: (H shl 8) or L
IX      = (16-bits) Register IX
IY      = (16-bits) Register IY
[BR:ll] = (8-bits) Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = (8-bits) Memory: (EP shl 16) or HL
```

```
; DEC Ds
;
; Ds = Source/Destination

Ds = Ds - 1
```

## Description

"Destination" is decremented by 1.

## Conditions

* Zero: Set when result is 0

Carry, Overflow, and Sign remain unchanged

## Examples

```
; A = 0x55
DEC A
; A = 0x54 (0x55 - 1 = 0x54)
; SC = (Zero=0)
```

```
; [BR+0x88] = 0xFF
DEC [BR+$88]
; [BR+0x88] = 0xFE (0xFF - 1 = 0xFE)
; SC = (Zero=0)
```

```
; BA = 0x2997
DEC BA
; BA = 0x2996 (0x2997 - 1 = 0x2996)
; SC = (Zero=0)
```

```
; IX = 0xFFFF
DEC IX
; IX = 0xFFFE (0xFFFF - 1 = 0xFFFE)
; SC = (Zero=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
