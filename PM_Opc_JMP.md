\== JMP = Jump to routine
==

| Hex      | Mnemonic                  | Cycles | Condition                               |
| -------- | ------------------------- | ------ | --------------------------------------- |
| E4 ss    | JCB \#ss<sup>\*1</sup>    | 8      | Carry=1                                 |
| E5 ss    | JNCB \#ss<sup>\*1</sup>   | 8      | Carry=0                                 |
| E6 ss    | JZB \#ss<sup>\*1</sup>    | 8      | Zero=1                                  |
| E7 ss    | JNZB \#ss<sup>\*1</sup>   | 8      | Zero=0                                  |
| EC ss ss | JCW \#ssss<sup>\*1</sup>  | 12     | Carry=1                                 |
| ED ss ss | JNCW \#ssss<sup>\*1</sup> | 12     | Carry=0                                 |
| EE ss ss | JZW \#ssss<sup>\*1</sup>  | 12     | Zero=1                                  |
| EF ss ss | JNZW \#ssss<sup>\*1</sup> | 12     | Zero=0                                  |
| F1 ss    | JMPB \#ss<sup>\*1</sup>   | 8      | None                                    |
| F3 ss ss | JMPW \#ssss<sup>\*1</sup> | 12     | None                                    |
| F4       | JMP HL                    | 8      | None                                    |
| F5 ss    | JDBNZ \#ss                | 16     | B \<\> 0x00, decrement B before check   |
| FD nn    | JINT \#nn                 | 8      | None                                    |
| CE E0 ss | JL \#ss                   | 12     | (Overflow=1) \!= (Sign=1)               |
| CE E1 ss | JLE \#ss                  | 12     | ((Overflow=0) \!= (Sign=0)) OR (Zero=1) |
| CE E2 ss | JG \#ss                   | 12     | ((Overflow=1) == (Sign=1)) AND (Zero=0) |
| CE E3 ss | JGE \#ss                  | 12     | (Overflow=0) == (Sign=0)                |
| CE E4 ss | JO \#ss                   | 12     | Overflow=1                              |
| CE E5 ss | JNO \#ss                  | 12     | Overflow=0                              |
| CE E6 ss | JNS \#ss                  | 12     | Sign=0                                  |
| CE E7 ss | JS \#ss                   | 12     | Sign=1                                  |
| CE E8 ss | JNX0 \#ss                 | 12     | ??                                      |
| CE E9 ss | JNX1 \#ss                 | 12     | ??                                      |
| CE EA ss | JNX2 \#ss                 | 12     | ??                                      |
| CE EB ss | JNX3 \#ss                 | 12     | ??                                      |
| CE EC ss | JX0 \#ss                  | 12     | ??                                      |
| CE ED ss | JX1 \#ss                  | 12     | ??                                      |
| CE EE ss | JX2 \#ss                  | 12     | ??                                      |
| CE EF ss | JX3 \#ss                  | 12     | ??                                      |

**\*1**: JMP, JC, JNC, JZ and JNZ can be used in the assembler to
auto-detect the appropriate range.

### Execute

`#nn      = Immediate unsigned 8-Bits`
`#ss      = Immediate signed 8-Bits`
`#ssss    = Immediate signed 16-Bits`
`B        = Register B`
`U/V      = Register U or V`
`HL       = Register HL: (H shl 8) or L`
`SP       = Register SP (Stack Pointer)`
`PC       = Register PC (Program Counter)`
`[#nnnn]  = Memory: (I shl 16) or #nnnn`

`; J*B #ss`

`IF (Condition) THEN`
`  V = U`
`  PC = PC + #ss - 1`
`ENDIF`

`; J*W #ssss`

`IF (Condition) THEN`
`  V = U`
`  PC = PC + #ssss - 1`
`ENDIF`

`; JMPB #ss`

`V = U`
`PC = PC + #ss - 1`

`; JMPW #ssss`

`V = U`
`PC = PC + #ssss - 1`

`; JMP HL`

`V = U`
`PC = HL`

`; JDBNZ #ss`

`B = B - 1`
`IF (B <> 0) THEN`
`  V = U`
`  PC = PC + #ss - 1`
`ENDIF`

`; JINT #nn (`*`not`` ``fully`` ``tested`*`)`

`V = U`
`PC = Memory16[#nn SHL 1]`

### Description

Jump into a new position of the program.

NOTE: All non-branch instructions does "U = V" causing U to be restored,
any branch that require banking needs "MOV U, A" or "MOV U, \#nn" before
JMP/J\*...

### Conditions

'''0xF5 - JDBNZ \#ss '''

Zero: Set when result is 0

Carry, Overflow and Sign remain unchanged

**All others:**

None

### Examples

` ; A = 0x10`
` `[`CMP`` ``A,``
``0x10`](PM_Opc_CMP8.md "wikilink")`  ; Compare A with 0x10`
` ; F = (Zero=1):(Carry=0):(Overflow=0):(Sign=0)`
` `**`JZ`` ``val_is_16`**
` `[`MOV`` ``A,`` ``0x00`](PM_Opc_MOV8.md "wikilink")
`val_is_16:`
` ; A = 0x10`

`; Jump into a label located at a different bank`
[`MOV`` ``U,`` ``$0F`](PM_Opc_MOV8.md "wikilink")
**`JMP`` ``function_at_bank_15`**

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")