# RR = Rotate Right through Carry

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| CE 98    | RR A            | 3      |
| CE 99    | RR B            | 3      |
| CE 9A ll | RR \[BR:ll]     | 5      |
| CE 9B    | RR \[HL]        | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; RR Ds
;
; Ds = Source/Destination

Ds = (Ds SRL 1) OR (Carry SLL 7)
```

## Description

"8-bits Destination" bits are rotated right by 1 through Carry.

## Conditions

* Zero: Set when result is 0
* Carry: Set when old bit 0 is 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04
; SC = (Carry=0)
RR A
; A = 0x02
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45
; SC = (Carry=1)
RR B
; B = 0xA2
; SC = (Zero=0):(Carry=1):(Negative=0)
```

```
; B = 0x84
; SC = (Carry=0)
RR B
; B = 0x42
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; [HL] = 0x01
; SC = (Carry=0)
RR [HL]
; [HL] = 0x00
; SC = (Zero=1):(Carry=1):(Negative=0)
```

```
; [HL] = 0x01
; SC = (Carry=1)
RR [HL]
; [HL] = 0x80
; SC = (Zero=0):(Carry=1):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
