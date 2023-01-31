# MUL = Multiply

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE D8 | MUL      | 48     |

## Execute

```
; MUL L, A
;
; L is the Factor/Multiplicand
; A is the Multiplier
; HL will be the Product

HL = L x A
```

## Description

Multiply "8-bits Register L" by "8-bits Register A", 16-bits result is
placed in "16-bits Register HL".

## Conditions

* Zero: Set when result is 0
* Carry: Always reset
* Overflow: Always reset
* Negative: Set when bit 15 of the result is 1

## Examples

```
; A = 0x03
; L = 0x03
MUL L, A
; A = 0x03
; HL = 0x0009 (0x03 * 0x03 = 0x0009)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; A = 0x00
; L = 0x03
MUL L, A
; A = 0x00
; HL = 0x0000 (0x03 * 0x00 = 0x0000)
; SC = (Zero=1):(Carry=0):(Overflow=0):(Negative=0)
```

```
; A = 0xFF
; L = 0xFF
MUL L, A
; A = 0xFF
; HL = 0xFE01 (0xFF * 0xFF = 0xFE01)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
