\== CALL = Call routine
==

| Hex      | Mnemonic                     | Cycles,True | or False | Condition                               |
| -------- | ---------------------------- | ----------- | -------- | --------------------------------------- |
| E0 ss    | CALLCB \#ss<sup>\*1</sup>    | 20          | 8        | Carry=1                                 |
| E1 ss    | CALLNCB \#ss<sup>\*1</sup>   | 20          | 8        | Carry=0                                 |
| E2 ss    | CALLZB \#ss<sup>\*1</sup>    | 20          | 8        | Zero=1                                  |
| E3 ss    | CALLNZB \#ss<sup>\*1</sup>   | 20          | 8        | Zero=0                                  |
| E8 ss ss | CALLCW \#ssss<sup>\*1</sup>  | 24          | 12       | Carry=1                                 |
| E9 ss ss | CALLNCW \#ssss<sup>\*1</sup> | 24          | 12       | Carry=0                                 |
| EA ss ss | CALLZW \#ssss<sup>\*1</sup>  | 24          | 12       | Zero=1                                  |
| EB ss ss | CALLNZW \#ssss<sup>\*1</sup> | 24          | 12       | Zero=0                                  |
| F0 ss    | CALLB \#ss<sup>\*1</sup>     | 20          | None     | None                                    |
| F2 ss ss | CALLW \#ssss<sup>\*1</sup>   | 24          | None     | None                                    |
| FB nn nn | CALL \[\#nnnn\]              | 20          | None     | None                                    |
| FC nn    | CINT \#nn                    | 20          | None     | None                                    |
| CE F0 ss | CALLL \#ss                   | 24          | 12       | (Overflow=1) \!= (Sign=1)               |
| CE F1 ss | CALLLE \#ss                  | 24          | 12       | ((Overflow=0) \!= (Sign=0)) OR (Zero=1) |
| CE F2 ss | CALLG \#ss                   | 24          | 12       | ((Overflow=1) == (Sign=1)) AND (Zero=0) |
| CE F3 ss | CALLGE \#ss                  | 24          | 12       | (Overflow=0) == (Sign=0)                |
| CE F4 ss | CALLO \#ss                   | 24          | 12       | Overflow=1                              |
| CE F5 ss | CALLNO \#ss                  | 24          | 12       | Overflow=0                              |
| CE F6 ss | CALLNS \#ss                  | 24          | 12       | Sign=0                                  |
| CE F7 ss | CALLS \#ss                   | 24          | 12       | Sign=1                                  |
| CE F8 ss | CALLNX0 \#ss                 | 24          | 12       | ??                                      |
| CE F9 ss | CALLNX1 \#ss                 | 24          | 12       | ??                                      |
| CE FA ss | CALLNX2 \#ss                 | 24          | 12       | ??                                      |
| CE FB ss | CALLNX3 \#ss                 | 24          | 12       | ??                                      |
| CE FC ss | CALLX0 \#ss                  | 24          | 12       | ??                                      |
| CE FD ss | CALLX1 \#ss                  | 24          | 12       | ??                                      |
| CE FE ss | CALLX2 \#ss                  | 24          | 12       | ??                                      |
| CE FF ss | CALLX3 \#ss                  | 24          | 12       | ??                                      |

**\*1**: CALL, CALLC, CALLNC, CALLZ and CALLNZ can be used in the
assembler to auto-detect the appropriate range.

### Execute

`#nn      = Immediate unsigned 8-Bits`
`#ss      = Immediate signed 8-Bits`
`#ssss    = Immediate signed 16-Bits`
`U/V      = Register U or V`
`SP       = Register SP (Stack Pointer)`
`PC       = Register PC (Program Counter)`
`[#nnnn]  = Memory: (I shl 16) or #nnnn`

`; CALL*B #ss`

`IF (Condition) THEN`
`  SP = SP - 3`
`  Memory[SP+2] = V`
`  Memory[SP+1] = PC SHR 8`
`  Memory[SP]   = PC AND 0x00FF`
`  V = U`
`  PC = PC + #ss - 1`
`ENDIF`

`; CALL*W #ssss`

`IF (Condition) THEN`
`  SP = SP - 3`
`  Memory[SP+2] = V`
`  Memory[SP+1] = PC SHR 8`
`  Memory[SP]   = PC AND 0x00FF`
`  V = U`
`  PC = PC + #ssss - 1`
`ENDIF`

`; CALLB #ss`

`SP = SP - 3`
`Memory[SP+2] = V`
`Memory[SP+1] = PC SHR 8`
`Memory[SP]   = PC AND 0x00FF`
`V = U`
`PC = PC + #ss - 1`

`; CALLW #ssss`

`SP = SP - 3`
`Memory[SP+2] = V`
`Memory[SP+1] = PC SHR 8`
`Memory[SP]   = PC AND 0x00FF`
`V = U`
`PC = PC + #ssss - 1`

`; CALL [#nnnn]`

`SP = SP - 3`
`Memory[SP+2] = V`
`Memory[SP+1] = PC SHR 8`
`Memory[SP]   = PC AND 0x00FF`
`V = U`
`PC = Memory16[(I SHL 16) + #nnnn]`

`; CINT #nn (`*`not`` ``fully`` ``tested`*`)`

`SP = SP - 4`
`Memory[SP+3] = V`
`Memory[SP+2] = PC SHR 8`
`Memory[SP+1] = PC AND 0x00FF`
`Memory[SP]   = F`
`V = U`
`PC = Memory16[#nn SHL 1]`

### Description

Call a subroutine (CALL\*) or a interrupt vector (CINT).

Use [RET](PM_Opc_RET.md "wikilink") to return from a subroutine and
[RETI](PM_Opc_RET.md "wikilink") from a interrupt.

NOTE: All non-branch instructions does "U = V" causing U to be restored,
any branch that require banking needs "MOV U, A" or "MOV U, \#nn" before
CALL...

### Conditions

None

### Examples

` ; A = 0x10`
` ; B = 0x10`
` `**`CALL`` ``somefunction`**
` ; A = 0x11`
` ; B = 0x0F`
` `[`TST`` ``B,`` ``#0x10`](PM_Opc_TST.md "wikilink")
` ; F = (Zero=0):(Sign=0)`
` `**`CALLZ`` ``somefunction`**`    ; Condition fail, call not taken`
` ; A = 0x11`
` ; B = 0x0F`
` ; F = (Zero=0):(Sign=0)`
` `**`CALLNS`` ``somefunction`**`   ; Condition succeed`
` ; A = 0x12`
` ; B = 0x0E`

` (...)`

`somefunction:`
` `[`INC`` ``A`](PM_Opc_INC.md "wikilink")
` `[`DEC``
``B`](PM_Opc_DEC.md "wikilink")
` `[`RET`](PM_Opc_RET.md "wikilink")`                   ; Return from the call`

`; Calling a subroutine at different bank`
[`MOV`` ``U,`` ``$0F`](PM_Opc_MOV8.md "wikilink")
**`CALL`` ``function_at_bank_16`**

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
