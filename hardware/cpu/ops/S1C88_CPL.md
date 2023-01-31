# CPL = Logical CPL

| Hex      | Mnemonic     | Cycles |
| -------- | ------------ | ------ |
| CE A0    | CPL A        | 3      |
| CE A1    | CPL B        | 3      |
| CE A2 ll | CPL \[BR:ll] | 5      |
| CE A3    | CPL \[HL]    | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; CPL Ds
;
; Ds = Source/Destination

Ds = Ds XOR $FF
```

## Description

8-bits Destination is inverted (all bits).

## Conditions

* Zero: Set when result is 0
* Negative: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

## Examples

```
; A = 0x01
CPL A
; A = 0xFE
; SC = (Zero=0):(Negative=1)
```

```
; B = 0x85
CPL B
; B = 0x7A
; SC = (Zero=0):(Negative=0)
```

```
; [HL] = 0xFF
CPL [HL]
; [HL] = 0x00
; SC = (Zero=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
