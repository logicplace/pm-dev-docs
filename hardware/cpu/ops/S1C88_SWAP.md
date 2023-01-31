# SWAP = Swap Low and High Nibbles

| Hex | Mnemonic    | Cycles |
| --- | ----------- | ------ |
| F6  | SWAP A      | 2      |
| F7  | SWAP \[HL]  | 3      |

## Execute

```
A    = (8-bits) Register A
[HL] = (8-bits) Memory: (EP shl 16) or HL
```

```
; SWAP Ds
;
; Ds = Source/Destination

Ds = (Ds SLL 4) OR (Ds SRL 4)
```

## Description

Swap low and high nibbles of a given byte.

## Conditions

None

## Examples

```
; A = 0x3A
SWAP A
; A = 0xA3
```

```
; [HL] = 0xF6
SWAP [HL]
; [HL] = 0x6F
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
