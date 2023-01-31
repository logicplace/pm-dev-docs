# RL = Rotate Left through Carry

| Hex      | Mnemonic        | Cycles |
| -------- | --------------- | ------ |
| CE 90    | RL A            | 3      |
| CE 91    | RL B            | 3      |
| CE 92 ll | RL \[BR:ll]     | 5      |
| CE 93    | RL \[HL]        | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; RL Ds
;
; Ds = Source/Destination

Ds = (Ds SLL 1) OR Carry
```

## Description

"8-bits Destination" bits are rotated left by 1 through Carry.

## Conditions

* Zero: Set when result is 0
* Carry: Set when old bit 7 is 1
* Negative: Set when bit 7 of the result is 1

Overflow remains unchanged

## Examples

```
; A = 0x04
; SC = (Carry=0)
RL A
; A = 0x08
; SC = (Zero=0):(Carry=0):(Negative=0)
```

```
; B = 0x45
; SC = (Carry=1)
RL B
; B = 0x8B
; SC = (Zero=0):(Carry=0):(Negative=1)
```

```
; B = 0x84
; SC = (Carry=0)
RL B
; B = 0x08
; SC = (Zero=0):(Carry=1):(Negative=0)
```

```
; [HL] = 0x80
; SC = (Carry=0)
RL [HL]
; [HL] = 0x00
; SC = (Zero=1):(Carry=1):(Negative=0)
```

```
; [HL] = 0x80
; SC = (Carry=1)
RL [HL]
; [HL] = 0x01
; SC = (Zero=0):(Carry=1):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
