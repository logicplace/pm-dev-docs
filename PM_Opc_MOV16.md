\== MOV = Move Register (16-Bits) ==

<table>
<tbody>
<tr class="odd">
<td><table>
<thead>
<tr class="header">
<th><p>Hex</p></th>
<th><p>Mnemonic</p></th>
<th><p>Cycles</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>B8 nn nn</p></td>
<td><p>MOV BA, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>B9 nn nn</p></td>
<td><p>MOV HL, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>BA nn nn</p></td>
<td><p>MOV X, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>BB nn nn</p></td>
<td><p>MOV Y, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF 78 nn nn</p></td>
<td><p>MOV SP, [#nnnn]</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>BC nn nn</p></td>
<td><p>MOV [#nnnn], BA</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>BD nn nn</p></td>
<td><p>MOV [#nnnn], HL</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>BE nn nn</p></td>
<td><p>MOV [#nnnn], X</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>BF nn nn</p></td>
<td><p>MOV [#nnnn], Y</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF 7C nn nn</p></td>
<td><p>MOV [#nnnn], SP</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>C4 nn nn</p></td>
<td><p>MOV BA, #nnnn</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>C5 nn nn</p></td>
<td><p>MOV HL, #nnnn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>C6 nn nn</p></td>
<td><p>MOV X, #nnnn</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>C7 nn nn</p></td>
<td><p>MOV Y, #nnnn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>CF 6E nn nn</p></td>
<td><p>MOV SP, #nnnn</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>CF 70 ss</p></td>
<td><p>MOV BA, [SP+#ss]</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>CF 71 ss</p></td>
<td><p>MOV HL, [SP+#ss]</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>CF 72 ss</p></td>
<td><p>MOV X, [SP+#ss]</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>CF 73 ss</p></td>
<td><p>MOV Y, [SP+#ss]</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>CF 74 ss</p></td>
<td><p>MOV [SP+#ss], BA</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>CF 75 ss</p></td>
<td><p>MOV [SP+#ss], HL</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>CF 76 ss</p></td>
<td><p>MOV [SP+#ss], X</p></td>
<td><p>24</p></td>
</tr>
<tr class="even">
<td><p>CF 77 ss</p></td>
<td><p>MOV [SP+#ss], Y</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>CF C0</p></td>
<td><p>MOV BA, [HL]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF C1</p></td>
<td><p>MOV HL, [HL]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF C2</p></td>
<td><p>MOV X, [HL]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF C3</p></td>
<td><p>MOV Y, [HL]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF D0</p></td>
<td><p>MOV BA, [X]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF D1</p></td>
<td><p>MOV HL, [X]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF D2</p></td>
<td><p>MOV X, [X]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF D3</p></td>
<td><p>MOV Y, [X]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF D8</p></td>
<td><p>MOV BA, [Y]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF D9</p></td>
<td><p>MOV HL, [Y]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF DA</p></td>
<td><p>MOV X, [Y]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF DB</p></td>
<td><p>MOV Y, [Y]</p></td>
<td><p>20</p></td>
</tr>
</tbody>
</table></td>
<td><table>
<thead>
<tr class="header">
<th><p>Hex</p></th>
<th><p>Mnemonic</p></th>
<th><p>Cycles</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CF C4</p></td>
<td><p>MOV [HL], BA</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF C5</p></td>
<td><p>MOV [HL], HL</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF C6</p></td>
<td><p>MOV [HL], X</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF C7</p></td>
<td><p>MOV [HL], Y</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF D4</p></td>
<td><p>MOV [X], BA</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF D5</p></td>
<td><p>MOV [X], HL</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF D6</p></td>
<td><p>MOV [X], X</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF D7</p></td>
<td><p>MOV [X], Y</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF DC</p></td>
<td><p>MOV [Y], BA</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF DD</p></td>
<td><p>MOV [Y], HL</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF DE</p></td>
<td><p>MOV [Y], X</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CF DF</p></td>
<td><p>MOV [Y], Y</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CF E0</p></td>
<td><p>MOV BA, BA</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF E1</p></td>
<td><p>MOV BA, HL</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF E2</p></td>
<td><p>MOV BA, X</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF E3</p></td>
<td><p>MOV BA, Y</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF E4</p></td>
<td><p>MOV HL, BA</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF E5</p></td>
<td><p>MOV HL, HL</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF E6</p></td>
<td><p>MOV HL, X</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF E7</p></td>
<td><p>MOV HL, Y</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF E8</p></td>
<td><p>MOV X, BA</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF E9</p></td>
<td><p>MOV X, HL</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF EA</p></td>
<td><p>MOV X, X</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF EB</p></td>
<td><p>MOV X, Y</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF EC</p></td>
<td><p>MOV Y, BA</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF ED</p></td>
<td><p>MOV Y, HL</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF EE</p></td>
<td><p>MOV Y, X</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF EF</p></td>
<td><p>MOV Y, Y</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF F0</p></td>
<td><p>MOV SP, BA</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF F1</p></td>
<td><p>MOV SP, HL</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF F2</p></td>
<td><p>MOV SP, X</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF F3</p></td>
<td><p>MOV SP, Y</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF F4</p></td>
<td><p>MOV HL, SP</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF F5</p></td>
<td><p>MOV HL, PC</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF F8</p></td>
<td><p>MOV BA, SP</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF F9</p></td>
<td><p>MOV BA, PC</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CF FA</p></td>
<td><p>MOV X, SP</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CF FE</p></td>
<td><p>MOV Y, SP</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

**Source as the column, and Destination as the
row:**

|             | \#nnnn      | BA       | HL       | X        | Y        | SP          | PC    | \[HL\] | \[X\] | \[Y\] | \[\#nnnn\]  | \[SP+\#ss\] |
| ----------- | ----------- | -------- | -------- | -------- | -------- | ----------- | ----- | ------ | ----- | ----- | ----------- | ----------- |
| BA          | C4 nn nn    | CF E0    | CF E1    | CF E2    | CF E3    | CF F8       | CF F9 | CF C0  | CF D0 | CF D8 | B8 nn nn    | CF 70 ss    |
| HL          | C5 nn nn    | CF E4    | CF E5    | CF E6    | CF E7    | CF F4       | CF F5 | CF C1  | CF D1 | CF D9 | B9 nn nn    | CF 71 ss    |
| X           | C6 nn nn    | CF E8    | CF E9    | CF EA    | CF EB    | CF FA       |       | CF C2  | CF D2 | CF DA | BA nn nn    | CF 72 ss    |
| Y           | C7 nn nn    | CF EC    | CF ED    | CF EE    | CF EF    | CF FE       |       | CF C3  | CF D3 | CF DB | BB nn nn    | CF 73 ss    |
| SP          | CF 6E nn nn | CF F0    | CF F1    | CF F2    | CF F3    |             |       |        |       |       | CF 78 nn nn |             |
| \[HL\]      |             | CF C4    | CF C5    | CF C6    | CF C7    |             |       |        |       |       |             |             |
| \[X\]       |             | CF D4    | CF D5    | CF D6    | CF D7    |             |       |        |       |       |             |             |
| \[Y\]       |             | CF DC    | CF DD    | CF DE    | CF DF    |             |       |        |       |       |             |             |
| \[\#nnnn\]  |             | BC nn nn | BD nn nn | BE nn nn | BF nn nn | CF 6E nn nn |       |        |       |       |             |             |
| \[SP+\#ss\] |             | CF 74 ss | CF 75 ss | CF 76 ss | CF 77    |             |       |        |       |       |             |             |

### Execute

`#nnnn    = Immediate unsigned 16-Bits`
`#ss      = Immediate signed 8-Bits`
`BA       = Register BA: (B shl 8) or A`
`HL       = Register HL: (H shl 8) or L`
`X        = Register X`
`Y        = Register Y`
`SP       = Register SP (Stack Pointer)`
`PC       = Register PC (Program Counter)`
`[HL]     = Memory: (I shl 16) or HL`
`[X]      = Memory: (XI shl 16) or X`
`[Y]      = Memory: (YI shl 16) or Y`
`[#nnnn]  = Memory: (I shl 16) or #nnnn`
`[SP+#ss] = Memory: SP + #ss`

`; MOV Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Sc`

### Description

16-Bits Source gets copied to the 16-Bits Destination.

### Conditions

None

### Examples

`; A = 0xF0`
`; B = 0x0E`
**`MOV`` ``BA,`` ``$1337`**
`; A = 0x37`
`; B = 0x13`

`; A = 0x12`
`; B = 0xCF`
`; L = 0x7E`
`; H = 0xAB`
**`MOV`` ``BA,`` ``HL`**
`; A = 0x7E`
`; B = 0xAB`
`; L = 0x7E`
`; H = 0xAB`

`; [HL] = 0xBEEF`
`; A = 0xAD`
`; B = 0xDE`
**`MOV`` ``BA,`` ``[HL]`**
`; [HL] = 0xBEEF`
`; A = 0xEF`
`; B = 0xBE`

[**« Back to Instruction set**](PM_InstructionList.md "wikilink")