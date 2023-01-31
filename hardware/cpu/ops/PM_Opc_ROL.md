# RLC = Rotate Left

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 94    | RLC A          | 3      |
| CE 95    | RLC B          | 3      |
| CE 96 ll | RLC \[BR:ll]   | 5      |
| CE 97    | RLC \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; RLC Ds
;
; Ds = Source/Destination

Ds = (Ds SLL 1) OR (Ds SRL 7)
```

## Description

"8-bits Destination" bits are rotated left by 1.

## Conditions

* Zero: Set when result is 0
* Carry: Set when bit 0 of the result is 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04
RLC A
; A = 0x08
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45
RLC B
; B = 0x8A
; SC = (Zero=0):(Carry=0):(Negative=1)
```

```
; B = 0x84
RLC B
; B = 0x15
; SC = (Zero=0):(Carry=1):(Negative=0)
```

```
; [HL] = 0x80
RLC [HL]
; [HL] = 0x01
; SC = (Zero=0):(Carry=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
