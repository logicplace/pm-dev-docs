# DIV = Divide

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE D9 | DIV      | 12     |

## Execute

```
; DIV
;
; HL is the Dividend
; A is the Divisor
; L will be the Quotient
; H will be the Remainder

Ds = HL ÷ A
IF Ds < 256 THEN
  L = Ds          ; Quotient
  H = HL % A      ; Remainder
ENDIF
```

**Note:**

Can throw Division by Zero if Divisor is 0 (We need to research more
about this).

If Quotient can't fit in 8-bits range, Overflow flag will be set and the
result won't be saved.

## Description

"16-bits Register HL" divide by "8-bits Register A", Quotient will be
stored at "8-bits Register L" and Remainder will be stored at "8-bits
Register H".

## Conditions

* Zero: Set when result is 0
* Carry: Always reset
* Overflow: Set when Quotient can't fit in 8-bits range
* Negative: Set when bit 7 of Quotient is 1

## Examples

```
; A = 0x02
; HL = 0x0007
DIV HL, A
; L = 0x03 (0x0007 / 0x02 = 0x03 (with remainder 0x01))
; H = 0x01 (Remainder)
; SC = (Zero=0):(Carry=0):(Overflow=0):(Negative=0)
```

```
; A = 0x00
; HL = 0x0007
DIV HL, A
;          (0x0007 / 0x00 = Division by Zero)
; HL = 0x????  (Unpredictable result!?)
; SC = (Zero=?):(Carry=?):(Overflow=?):(Negative=?)
; - Throw Division by Zero Exception
```

```
; A = 0x02
; HL = 0xFFFD
DIV HL, A
;          (0xFFFD / 0x02 = 0x7FFE (with rest 0x01))
; HL = 0xFFFD  (Results are unchanged since Quotient exceed 8-bits range)
; SC = (Zero=0):(Carry=0):(Overflow=1):(Negative=1)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
