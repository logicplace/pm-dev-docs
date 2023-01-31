# EX = Exchange Registers

| Hex | Mnemonic       | Cycles |
| --- | -------------- | ------ |
| C8  | EX BA,HL       | 3      |
| C9  | EX BA,IX       | 3      |
| CA  | EX BA,IY       | 3      |
| CB  | EX BA,SP       | 3      |
| CC  | EX A,B         | 2      |
| CD  | EX A,\[HL]     | 3      |

## Execute

```
A    = (8-bits) Register A
B    = (8-bits) Register B
BA   = (16-bits) Register BA: (B shl 8) or A
HL   = (16-bits) Register HL: (H shl 8) or L
IX   = (16-bits) Register IX
IY   = (16-bits) Register IY
SP   = (16-bits) Register SP (Stack Pointer)
[HL] = (8-bits) Memory: (EP shl 16) or HL
```

```
; EX Sc2, Sc
;
; Sc2 = Source 2
; Sc  = Source
; Tr = Temporary Register

Sc2   Sc
   \ /
    x
   / \
Sc2   Sc
```

## Description

"Source" content is exchanged (swapped) with "Source 2".

## Conditions

None

## Examples

```
; BA = 0x1337
; HL = 0xC0D3
EX BA, HL
; BA = 0xC0D3
; HL = 0x1337
```

```
; A = 0x45
; B = 0x12
EX A, B
; A = 0x12
; B = 0x45
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
