# SLL = Shift Left

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 84    | SLL A          | 3      |
| CE 85    | SLL B          | 3      |
| CE 86 ll | SLL \[BR:ll]   | 5      |
| CE 87    | SLL \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; SLL Ds
;
; Ds = Source/Destination

Ds = Ds SLL 1
```

## Description

"8-bits Destination" bits are shifted left by 1.

NOTE: This instruction can be used as an unsigned integer multiplication by 2.

## Conditions

* Zero: Set when result is 0
* Carry: Set when the old bit 7 was 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04 (4)
SLL A
; A = 0x08 (8)
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45 (69)
SLL B
; B = 0x8A (138)
; SC = (Zero=0):(Carry=0):(Negative=1)
```

```
; B = 0x84 (138)
SLL B
; B = 0x14 (20)
; SC = (Zero=0):(Carry=1):(Negative=0)
```

```
; [HL] = 0x80 (128)
SLL [HL]
; [HL] = 0x00 (0)
; SC = (Zero=1):(Carry=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
