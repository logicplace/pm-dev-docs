\== STOP = Stop CPU ==

| Hex   | Mnemonic | Cycles |
| ----- | -------- | ------ |
| CE AF | STOP     | 8      |

### Execute

`See description.`

### Description

Halt or disable most hardware until a interrupt is requested.

Used by BIOS to set the system in standby mode.

NOTE:
Almost all hardware gets disabled (CPU, LCD, Sound...).
If no interrupts are enabled, the system will be unable to resume
operation.
Never call STOP directly, let BIOS to handle the shutdown by using
"[CINT $24](PM_Opc_CALL.md "wikilink")".

### Conditions

None

### Examples

`; STOP instruction isn't recommended to use.`
`; Use this code to shutdown your program:`
[`CINT`` ``$24`](PM_Opc_CALL.md "wikilink")

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")