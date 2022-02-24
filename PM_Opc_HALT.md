\== HALT = Halt CPU ==

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE AE | HALT     | 8      |

### Execute

`See description.`

### Description

Halt the CPU until a interrupt is requested.

Using this instruction will reduce energy consumption.

NOTE:
If no interrupts are enabled, the system will be unable to resume
operation.
Never call HALT in a middle of an interrupt.
Code will resume after HALT when the requested interrupt is completed.

### Conditions

None

### Examples

`; Make sure interrupts are enabled and configured correctly.`
**`HALT`**
`; Operation will resume once the interrupt finish.`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")