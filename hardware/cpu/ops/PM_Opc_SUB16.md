# SUB = Subtraction (16-bits)

| Hex         | Mnemonic     | Cycles |
| ----------- | ------------ | ------ |
| D0 nn mm    | SUB BA,#mmnn | 3      |
| D1 nn mm    | SUB HL,#mmnn | 3      |
| D2 nn mm    | SUB IX,#mmnn | 3      |
| D3 nn mm    | SUB IY,#mmnn | 3      |
| CF 6A nn mm | SUB SP,#mmnn | 4      |
| CF 08       | SUB BA,BA    | 4      |
| CF 09       | SUB BA,HL    | 4      |
| CF 0A       | SUB BA,IX    | 4      |
| CF 0B       | SUB BA,IY    | 4      |
| CF 28       | SUB HL,BA    | 4      |
| CF 29       | SUB HL,HL    | 4      |
| CF 2A       | SUB HL,IX    | 4      |
| CF 2B       | SUB HL,IY    | 4      |
| CF 48       | SUB IX,BA    | 4      |
| CF 49       | SUB IX,HL    | 4      |
| CF 4A       | SUB IY,BA    | 4      |
| CF 4B       | SUB IY,HL    | 4      |
| CF 4C       | SUB SP,BA    | 4      |
| CF 4D       | SUB SP,HL    | 4      |

## Execute

```
hhll    = Immediate unsigned 16-bits
BA       = Register BA: (B shl 8) or A
HL       = Register HL: (H shl 8) or L
IX        = Register IX
IY        = Register IY
SP       = Register SP (Stack Pointer)
```

```
; SUB Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds - Sc
```

## Description

16-bits Source subtracts to the 16-bits Destination.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result exceeds 16-bits signed range (< -32768 OR > 32767)
* Negative: Set when bit 15 of the result is 1

## Examples

```
; BA = 0x2EF0
SUB BA, $1337
; BA = 0x1BB9 (0x2EF0 - 0x1337 = 0x(0)1BB9)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; HL = 0xBB7E
; BA = 0xCF12
SUB BA, HL
; HL = 0xBB7E
; BA = 0xEC6C (0xCF12 - 0xBB7E = 0x(1)EC6C)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
