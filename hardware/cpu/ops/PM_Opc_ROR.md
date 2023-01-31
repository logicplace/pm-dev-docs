# RRC = Rotate Right

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 9C    | RRC A          | 3      |
| CE 9D    | RRC B          | 3      |
| CE 9E ll | RRC \[BR:ll]   | 5      |
| CE 9F    | RRC \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; RRC Ds
;
; Ds = Source/Destination

Ds = (Ds SRL 1) OR (Ds SLL 7)
```

## Description

"8-bits Destination" bits are rotated right by 1.

## Conditions

* Zero: Set when result is 0
* Carry: Set when bit 7 of the result is 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04
RRC A
; A = 0x02
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45
RRC B
; B = 0xA2
; SC = (Zero=0):(Carry=1):(Negative=1)
```

```
; B = 0x84
RRC B
; B = 0x42
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; [HL] = 0x01
RRC [HL]
; [HL] = 0x80
; SC = (Zero=0):(Carry=1):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
