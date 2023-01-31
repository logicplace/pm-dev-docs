# CP = Compare (16-bits)

| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| D4 nn mm    | CP BA,#mmnn    | 3      |
| D5 nn mm    | CP HL,#mmnn    | 3      |
| D6 nn mm    | CP IX,#mmnn    | 3      |
| D7 nn mm    | CP IY,#mmnn    | 3      |
| CF 6C nn mm | CP SP,#mmnn    | 4      |
| CF 18       | CP BA,BA       | 4      |
| CF 19       | CP BA,HL       | 4      |
| CF 1A       | CP BA,IX       | 4      |
| CF 1B       | CP BA,IY       | 4      |
| CF 38       | CP HL,BA       | 4      |
| CF 39       | CP HL,HL       | 4      |
| CF 3A       | CP HL,IX       | 4      |
| CF 3B       | CP HL,IY       | 4      |
| CF 5C       | CP SP,BA       | 4      |
| CF 5D       | CP SP,HL       | 4      |

## Execute

```
hhll = Immediate unsigned 16-bits
BA   = Register BA: (B shl 8) or A
HL   = Register HL: (H shl 8) or L
IX   = Register IX
IY   = Register IY
SP   = Register SP (Stack Pointer)
```

```
; CP Sc2, Sc
;
; Sc2 = Source 2
; Sc  = Source

(discarded) = Sc2 - Sc
```

## Description

Subtracts "16-bits Source 2" with "16-bits Source", result is discarded.

This instruction is used to compare values.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is < 0
* Overflow: Set when result overflow 16-bits signed range (< -32768 OR > 32767)
* Negative: Set when bit 15 of the result is 1

## Examples

```
; BA = 0x2EF0
CP BA, $1337
; BA = 0x2EF0
;      0x1BB9 (0x2EF0 - 0x1337 = 0x(0)1BB9)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; HL = 0xBB7E
; BA = 0xCF12
CP BA, HL
; HL = 0xBB7E
; BA = 0xCF12
;     0xEC6C (0xCF12 - 0xBB7E = 0x(1)EC6C)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
