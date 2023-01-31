# ADC = Addition with Carry (16-bits)

| Hex         | Mnemonic     | Cycles |
| ----------- | ------------ | ------ |
| CF 04       | ADC BA,BA    | 4      |
| CF 05       | ADC BA,HL    | 4      |
| CF 06       | ADC BA,IX    | 4      |
| CF 07       | ADC BA,IY    | 4      |
| CF 24       | ADC HL,BA    | 4      |
| CF 25       | ADC HL,HL    | 4      |
| CF 26       | ADC HL,IX    | 4      |
| CF 27       | ADC HL,IY    | 4      |
| CF 60 nn mm | ADC BA,#mmnn | 4      |
| CF 61 nn mm | ADC HL,#mmnn | 4      |

## Execute

```
#mmnn = Immediate unsigned 16-bits
BA    = Register BA: (B shl 8) or A
HL    = Register HL: (H shl 8) or L
IX    = Register IX
IY    = Register IY
```

```
; ADC Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds + Sc + Carry
```

## Description

16-bits Source and Carry adds to the 16-bits Destination.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is >= 65536
* Overflow: Set when result exceeds 16-bits signed range (< -32768 OR > 32767)
* Negative: Set when bit 15 of the result is 1

## Examples

```
; BA = 0x0EF0
; SC = (Carry=1)
ADC BA, $1337
; BA = 0x2228 (0x0EF0 + 0x1337 + 0x0001 = 0x(0)2228)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; HL = 0xBB7E
; BA = 0xCF12
; SC = (Carry=0)
ADC BA, HL
; HL = 0xBB7E
; BA = 0x8A90 (0xCF12 + 0xBB7E + 0x0000 = 0x(1)8A90)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; IX = 0xBEEF
; BA = 0xDEAD
; SC = (Carry=1)
ADC BA, IX
; IX = 0xBEEF
; BA = 0x9D9D (0xDEAD + 0xBEEF + 0x0001 = 0x(1)9D9D)
; SC = (Zero=0):(Carry=1):(Overflow=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
