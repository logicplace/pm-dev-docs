# INC = Increase Register by 1

| Hex   | Mnemonic     | Cycles |
| ----- | ------------ | ------ |
| 80    | INC A        | 2      |
| 81    | INC B        | 2      |
| 82    | INC L        | 2      |
| 83    | INC H        | 2      |
| 84    | INC BR       | 2      |
| 85 ll | INC \[BR:ll] | 4      |
| 86    | INC \[HL]    | 3      |
| 87    | INC SP       | 2      |
| 90    | INC BA       | 2      |
| 91    | INC HL       | 2      |
| 92    | INC IX       | 2      |
| 93    | INC IY       | 2      |

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
; INC Ds
;
; Ds = Source/Destination

Ds = Ds + 1
```

## Description

"Destination" is incremented by 1.

## Conditions

* Zero: Set when result is 0

Carry, Overflow, and Sign remain unchanged

## Examples

```
; A = 0x55
INC A
; A = 0x56 (0x55 + 1 = 0x56)
; SC = (Zero=0)
```

```
; [BR+0x88] = 0xFF
INC [BR+$88]
; [BR+0x88] = 0x00 (0xFF + 1 = 0x00)
; SC = (Zero=1)
```

```
; BA = 0x2997
INC BA
; BA = 0x2998 (0x2997 + 1 = 0x2998)
; SC = (Zero=0)
```

```
; IX = 0xFFFF
INC IX
; IX = 0x0000 (0xFFFF + 1 = 0x0000)
; SC = (Zero=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
