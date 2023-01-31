# SLA = Shift Arithmetic Left

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 80    | SLA A          | 3      |
| CE 81    | SLA B          | 3      |
| CE 82 ll | SLA \[BR:ll]   | 5      |
| CE 83    | SLA \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; SLA Ds
;
; Ds = Source/Destination

Ds = Ds SLL 1
```

## Description

"8-bits Destination" bits are arithmetically shifted left by 1.

NOTE: This instruction can be used as an signed integer multiplication by 2.

## Conditions

* Zero: Set when result is 0
* Carry: Set when the old bit 7 was 1
* Overflow: Set when result overflow 8-bits signed range (< -128 OR > 127)
* Negative: Set when bit 7 of the result is 1

## Examples

```
; A = 0x04 (4)
SLA A
; A = 0x08 (8)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; A = 0xFE (-2)
SLA A
; A = 0xFC (-4)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; B = 0x45 (69)
SLA B
; B = 0x8A (-124)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

```
; B = 0x84 (-124)
SLA B
; B = 0x14 (20)
; SC = (Zero=0):(Carry=1):(Overflow=1):(Negative=0)
```

```
; [HL] = 0x80 (-128)
SLA [HL]
; [HL] = 0x00 (0)
; SC = (Zero=1):(Carry=1):(Overflow=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
