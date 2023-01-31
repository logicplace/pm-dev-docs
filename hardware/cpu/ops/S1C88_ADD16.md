# ADD = Addition (16-bits)

| Hex         | Mnemonic     | Cycles |
| ----------- | ------------ | ------ |
| C0 nn mm    | ADD BA,#mmnn | 3      |
| C1 nn mm    | ADD HL,#mmnn | 3      |
| C2 nn mm    | ADD IX,#mmnn | 3      |
| C3 nn mm    | ADD IY,#mmnn | 3      |
| CF 68 nn mm | ADD SP,#mmnn | 4      |
| CF 00       | ADD BA,BA    | 4      |
| CF 01       | ADD BA,HL    | 4      |
| CF 02       | ADD BA,IX    | 4      |
| CF 03       | ADD BA,IY    | 4      |
| CF 20       | ADD HL,BA    | 4      |
| CF 21       | ADD HL,HL    | 4      |
| CF 22       | ADD HL,IX    | 4      |
| CF 23       | ADD HL,IY    | 4      |
| CF 40       | ADD IX,BA    | 4      |
| CF 41       | ADD IX,HL    | 4      |
| CF 42       | ADD IY,BA    | 4      |
| CF 43       | ADD IY,HL    | 4      |
| CF 44       | ADD SP,BA    | 4      |
| CF 45       | ADD SP,HL    | 4      |

## Execute

```
#mmnn    = Immediate unsigned 16-bits
BA       = Register BA: (B shl 8) or A
HL       = Register HL: (H shl 8) or L
IX       = Register IX
IY       = Register IY
SP       = Register SP (Stack Pointer)
```

```
; ADD Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds + Sc
```

## Description

16-bits Source adds to the 16-bits Destination.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is >= 65536
* Overflow: Set when result exceeds 16-bits signed range (< -32768 OR > 32767)
* Negative: Set when bit 15 of the result is 1

## Examples

```
; BA = 0x0EF0
ADD BA, $1337
; BA = 0x2227 (0x0EF0 + 0x1337 = 0x(0)2227)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; HL = 0xBB7E
; BA = 0xCF12
ADD BA, HL
; HL = 0xBB7E
; BA = 0x8A90 (0xCF12 + 0xBB7E = 0x(1)8A90)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; IX = 0xBEEF
; BA = 0xDEAD
ADD BA, IX
; IX = 0xBEEF
; BA = 0x9D9C (0xDEAD + 0xBEEF = 0x(1)9D9C)
; SC = (Zero=0):(Carry=1):(Overflow=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
