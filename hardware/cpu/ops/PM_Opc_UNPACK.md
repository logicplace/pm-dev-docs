# UPCK = Unpack Nibbles

| Hex | Mnemonic | Cycles |
| --- | -------- | ------ |
| DF  | UPCK     | 2      |

## Execute

```
A = (8-bits) Register A
B = (8-bits) Register B
```

```
; UPCK

B = A SRL 4
A = A AND 0x0F
```

## Description

Unpack byte in register A into 2 nibbles, storing them into register A and B.

Register A receive the lower nibble and register B receive the higher nibble.

## Conditions

None

## Examples

```
; A = 0x21
UPCK
; A = 0x01
; B = 0x02
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
