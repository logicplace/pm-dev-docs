# NEG = Negate

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE A4    | NEG A          | 3      |
| CE A5    | NEG B          | 3      |
| CE A6 ll | NEG \[BR:ll]   | 5      |
| CE A7    | NEG \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; NEG Ds
;
; Ds = Source/Destination

Ds = 0 - Ds
```

## Description

8-bits Destination is negated.

## Conditions

* Zero: Set when result is 0
* Carry: Set when result is not 0
* Overflow: Set when result is 0x80
* Negative: Set when bit 7 of the result is 1

## Examples

```
; A = 0x01
NEG A
; A = 0xFF (0 - 0x01 = 0xFF)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=1)
```

```
; B = 0x00
NEG B
; B = 0x00 (0 - 0x00 = 0x00)
; SC = (Zero=1):(Carry=0):(Overflow=0):(Negative=0)
```

```
; [HL] = 0x80
NEG [HL]
; [HL] = 0x80 (0 - 0x80 = 0x80)
; SC = (Zero=0):(Carry=1):(Overflow=1):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
