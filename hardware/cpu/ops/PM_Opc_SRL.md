# SRL = Shift Right

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 8C    | SRL A          | 3      |
| CE 8D    | SRL B          | 3      |
| CE 8E ll | SRL \[BR:ll]   | 5      |
| CE 8F    | SRL \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; SRL Ds
;
; Ds = Source/Destination

Ds = Ds SRL 1
```

## Description

"8-bits Destination" bits are shifted right by 1.

NOTE: This instruction can be used as an unsigned integer division by 2.

## Conditions

* Zero: Set when result is 0
* Carry: Set when the old bit 0 was 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04 (4)
SRL A
; A = 0x02 (2)
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45 (69)
SRL B
; B = 0x22 (34)
; SC = (Zero=0):(Carry=1):(Negative=0)
```

```
; B = 0x84 (132)
SRL B
; B = 0x42 (66)
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; [HL] = 0x01 (1)
SRL [HL]
; [HL] = 0x00 (0)
; SC = (Zero=1):(Carry=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
