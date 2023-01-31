# SRA = Shift Arithmetic Right

| Hex      | Mnemonic       | Cycles |
| -------- | -------------- | ------ |
| CE 88    | SRA A          | 3      |
| CE 89    | SRA B          | 3      |
| CE 8A ll | SRA \[BR:ll]   | 5      |
| CE 8B    | SRA \[HL]      | 4      |

## Execute

```
A       = Register A
B       = Register B
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
```

```
; SRA Ds
;
; Ds = Source/Destination

Ds = (Ds AND 0x80) OR (Ds SRL 1)
```

## Description

"8-bits Destination" bits are arithmetically shifted right by 1.

NOTE: This instruction can be used as an signed integer division by 2.

## Conditions

* Zero: Set when result is 0
* Carry: Set when the old bit 0 was 1
* Overflow: Always reset (there's never a overflow)
* Negative: Set when bit 7 of the result is 1

## Examples

```
; A = 0x04 (4)
SRA A
; A = 0x02 (2)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; A = 0xFD (-4)
SRA A
; A = 0xFE (-2)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=1)
```

```
; B = 0x45 (69)
SRA B
; B = 0x22 (34)
; SC = (Zero=0):(Carry=1):(Overflow=0):(Negative=0)
```

```
; B = 0x84 (-124)
SRA B
; B = 0xC2 (-62)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=1)
```

```
; [HL] = 0x01 (1)
SRA [HL]
; [HL] = 0x00 (0)
; SC = (Zero=1):(Carry=1):(Overflow=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
