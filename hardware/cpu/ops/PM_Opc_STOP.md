
| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE AF | SLP      | 2      |

## Execute

```
See description.
```

## Description

Halt or disable most hardware until a interrupt is requested.

Used by BIOS to set the system in standby mode.

NOTE:
Almost all hardware gets disabled (CPU, LCD, Sound...).
If no interrupts are enabled, the system will be unable to resume operation.
Never call SLP directly, let BIOS to handle the shutdown by using "[INT [48h]](PM_Opc_CALL.md#int)".

## Conditions

None

## Examples

```
; SLP instruction isn't recommended to use.
; Use this code to shutdown your program:
INT [48h]
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
