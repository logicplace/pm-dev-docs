# SEP = Expand Register

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE A8 | SEP      | 3      |

## Execute

```
A  = (8-bits) Register A
BA = (16-bits) Register BA: (B shl 8) or A
```

```
; SEP
;
; BA = Destination
; A  = Source

IF (A AND 0x80) THEN  ; Check for sign
  B = 0xFF
ELSE
  B = 0x00
ENDIF
```

## Description

SEP expands register A into BA, turning a signed 8-bits value into 16-bits.

## Conditions

None

## Examples

```
; A = 0x05 (5)
SEP BA, A
; BA = 0x0005 (5)
```

```
; A = 0xF9 (-7)
SEP BA, A
; BA = 0xFFF9 (-7)
```

```
; A = 0x00 (0)
SEP BA, A
; BA = 0x0000 (0)
```

```
; A = 0x7F (127)
SEP BA, A
; BA = 0x007F (127)
```

```
; A = 0x80 (-128)
SEP BA, A
; BA = 0xFF80 (-128)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
