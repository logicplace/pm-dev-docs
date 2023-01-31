# LD = Move Register (16-bits)


| Hex         | Mnemonic       | Cycles |
| ----------- | -------------- | ------ |
| B8 ll hh    | LD BA, [hhll]  | 5      |
| B9 ll hh    | LD HL, [hhll]  | 5      |
| BA ll hh    | LD IX, [hhll]  | 5      |
| BB ll hh    | LD IY, [hhll]  | 5      |
| CF 78 ll hh | LD SP, [hhll]  | 6      |
| BC ll hh    | LD [hhll], BA  | 5      |
| BD ll hh    | LD [hhll], HL  | 5      |
| BE ll hh    | LD [hhll], IX  | 5      |
| BF ll hh    | LD [hhll], IY  | 5      |
| CF 7C ll hh | LD [hhll], SP  | 6      |
| C4 ll hh    | LD BA, hhll    | 3      |
| C5 ll hh    | LD HL, hhll    | 3      |
| C6 ll hh    | LD IX, hhll    | 3      |
| C7 ll hh    | LD IY, hhll    | 3      |
| CF 6E ll hh | LD SP, hhll    | 4      |
| CF 70 dd    | LD BA, [SP+dd] | 6      |
| CF 71 dd    | LD HL, [SP+dd] | 6      |
| CF 72 dd    | LD IX, [SP+dd] | 6      |
| CF 73 dd    | LD IY, [SP+dd] | 6      |
| CF 74 dd    | LD [SP+dd], BA | 6      |
| CF 75 dd    | LD [SP+dd], HL | 6      |
| CF 76 dd    | LD [SP+dd], IX | 6      |
| CF 77 dd    | LD [SP+dd], IY | 6      |
| CF C0       | LD BA, [HL]    | 5      |
| CF C1       | LD HL, [HL]    | 5      |
| CF C2       | LD IX, [HL]    | 5      |
| CF C3       | LD IY, [HL]    | 5      |
| CF D0       | LD BA, [IX]    | 5      |
| CF D1       | LD HL, [IX]    | 5      |
| CF D2       | LD IX, [IX]    | 5      |
| CF D3       | LD IY, [IX]    | 5      |
| CF D8       | LD BA, [IY]    | 5      |
| CF D9       | LD HL, [IY]    | 5      |
| CF DA       | LD IX, [IY]    | 5      |
| CF DB       | LD IY, [IY]    | 5      |
| CF C4       | LD [HL], BA    | 5      |
| CF C5       | LD [HL], HL    | 5      |
| CF C6       | LD [HL], IX    | 5      |
| CF C7       | LD [HL], IY    | 5      |
| CF D4       | LD [IX], BA    | 5      |
| CF D5       | LD [IX], HL    | 5      |
| CF D6       | LD [IX], IX    | 5      |
| CF D7       | LD [IX], IY    | 5      |
| CF DC       | LD [IY], BA    | 5      |
| CF DD       | LD [IY], HL    | 5      |
| CF DE       | LD [IY], IX    | 5      |
| CF DF       | LD [IY], IY    | 5      |
| CF E0       | LD BA, BA      | 2      |
| CF E1       | LD BA, HL      | 2      |
| CF E2       | LD BA, IX      | 2      |
| CF E3       | LD BA, IY      | 2      |
| CF E4       | LD HL, BA      | 2      |
| CF E5       | LD HL, HL      | 2      |
| CF E6       | LD HL, IX      | 2      |
| CF E7       | LD HL, IY      | 2      |
| CF E8       | LD IX, BA      | 2      |
| CF E9       | LD IX, HL      | 2      |
| CF EA       | LD IX, IX      | 2      |
| CF EB       | LD IX, IY      | 2      |
| CF EC       | LD IY, BA      | 2      |
| CF ED       | LD IY, HL      | 2      |
| CF EE       | LD IY, IX      | 2      |
| CF EF       | LD IY, IY      | 2      |
| CF F0       | LD SP, BA      | 2      |
| CF F1       | LD SP, HL      | 2      |
| CF F2       | LD SP, IX      | 2      |
| CF F3       | LD SP, IY      | 2      |
| CF F4       | LD HL, SP      | 2      |
| CF F5       | LD HL, PC      | 2      |
| CF F8       | LD BA, SP      | 2      |
| CF F9       | LD BA, PC      | 2      |
| CF FA       | LD IX, SP      | 2      |
| CF FE       | LD IY, SP      | 2      |

## Source as the column, and Destination as the row

|             | hhll        | BA       | HL       | IX       | IY       | SP          | PC    | \[HL]  | \[IX] | \[IY] | \[hhll]     | \[SP+dd]    |
| ----------- | ----------- | -------- | -------- | -------- | -------- | ----------- | ----- | ------ | ----- | ----- | ----------- | ----------- |
| BA          | C4 ll hh    | CF E0    | CF E1    | CF E2    | CF E3    | CF F8       | CF F9 | CF C0  | CF D0 | CF D8 | B8 ll hh    | CF 70 dd    |
| HL          | C5 ll hh    | CF E4    | CF E5    | CF E6    | CF E7    | CF F4       | CF F5 | CF C1  | CF D1 | CF D9 | B9 ll hh    | CF 71 dd    |
| IX          | C6 ll hh    | CF E8    | CF E9    | CF EA    | CF EB    | CF FA       |       | CF C2  | CF D2 | CF DA | BA ll hh    | CF 72 dd    |
| IY          | C7 ll hh    | CF EC    | CF ED    | CF EE    | CF EF    | CF FE       |       | CF C3  | CF D3 | CF DB | BB ll hh    | CF 73 dd    |
| SP          | CF 6E ll hh | CF F0    | CF F1    | CF F2    | CF F3    |             |       |        |       |       | CF 78 ll hh |             |
| \[HL]       |             | CF C4    | CF C5    | CF C6    | CF C7    |             |       |        |       |       |             |             |
| \[IX]       |             | CF D4    | CF D5    | CF D6    | CF D7    |             |       |        |       |       |             |             |
| \[IY]       |             | CF DC    | CF DD    | CF DE    | CF DF    |             |       |        |       |       |             |             |
| \[hhll]     |             | BC ll hh | BD ll hh | BE ll hh | BF ll hh | CF 6E ll hh |       |        |       |       |             |             |
| \[SP+dd]    |             | CF 74 dd | CF 75 dd | CF 76 dd | CF 77 dd |             |       |        |       |       |             |             |

## Execute

```
hhll    = Immediate unsigned 16-bits
dd      = Immediate signed 8-bits
BA      = Register BA: (B shl 8) or A
HL      = Register HL: (H shl 8) or L
IX      = Register IX
IY      = Register IY
SP      = Register SP (Stack Pointer)
PC      = Register PC (Program Counter)
[HL]    = Memory: (EP shl 16) or HL
[IX]    = Memory: (XP shl 16) or IX
[IY]    = Memory: (YP shl 16) or IY
[hhll]  = Memory: (EP shl 16) or hhll
[SP+dd] = Memory: SP + dd
```

```
; LD Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Sc
```

## Description

Copies 16-bits Source into the 16-bits Destination.

## Conditions

None

## Examples

```
; A = 0xF0
; B = 0x0E
LD BA, $1337
; A = 0x37
; B = 0x13
```

```
; A = 0x12
; B = 0xCF
; L = 0x7E
; H = 0xAB
LD BA, HL
; A = 0x7E
; B = 0xAB
; L = 0x7E
; H = 0xAB
```

```
; [HL] = 0xBEEF
; A = 0xAD
; B = 0xDE
LD BA, [HL]
; [HL] = 0xBEEF
; A = 0xEF
; B = 0xBE
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
