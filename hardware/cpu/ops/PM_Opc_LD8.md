# LD = Move Register (8-bits)

| Hex         | Mnemonic         | Cycles |
| ----------- | ---------------- | ------ |
| 40          | LD A, A          | 1      |
| 41          | LD A, B          | 1      |
| 42          | LD A, L          | 1      |
| 43          | LD A, H          | 1      |
| 44 ll       | LD A, [BR:ll]    | 3      |
| 45          | LD A, [HL]       | 2      |
| 46          | LD A, [IX]       | 2      |
| 47          | LD A, [IY]       | 2      |
| 48          | LD B, A          | 1      |
| 49          | LD B, B          | 1      |
| 4A          | LD B, L          | 1      |
| 4B          | LD B, H          | 1      |
| 4C ll       | LD B, [BR:ll]    | 3      |
| 4D          | LD B, [HL]       | 2      |
| 4E          | LD B, [IX]       | 2      |
| 4F          | LD B, [IY]       | 2      |
| 50          | LD L, A          | 1      |
| 51          | LD L, B          | 1      |
| 52          | LD L, L          | 1      |
| 53          | LD L, H          | 1      |
| 54 ll       | LD L, [BR:ll]    | 3      |
| 55          | LD L, [HL]       | 2      |
| 56          | LD L, [IX]       | 2      |
| 57          | LD L, [IY]       | 2      |
| 58          | LD H, A          | 1      |
| 59          | LD H, B          | 1      |
| 5A          | LD H, L          | 1      |
| 5B          | LD H, H          | 1      |
| 5C ll       | LD H, [BR:ll]    | 3      |
| 5D          | LD H, [HL]       | 2      |
| 5E          | LD H, [IX]       | 2      |
| 5F          | LD H, [IY]       | 2      |
| 60          | LD [IX], A       | 2      |
| 61          | LD [IX], B       | 2      |
| 62          | LD [IX], L       | 2      |
| 63          | LD [IX], H       | 2      |
| 64 ll       | LD [IX], [BR:ll] | 4      |
| 65          | LD [IX], [HL]    | 3      |
| 66          | LD [IX], [IX]    | 3      |
| 67          | LD [IX], [IY]    | 3      |
| 68          | LD [HL], A       | 2      |
| 69          | LD [HL], B       | 2      |
| 6A          | LD [HL], L       | 2      |
| 6B          | LD [HL], H       | 2      |
| 6C ll       | LD [HL], [BR:ll] | 4      |
| 6D          | LD [HL], [HL]    | 3      |
| 6E          | LD [HL], [IX]    | 3      |
| 6F          | LD [HL], [IY]    | 3      |
| 70          | LD [IY], A       | 2      |
| 71          | LD [IY], B       | 2      |
| 72          | LD [IY], L       | 2      |
| 73          | LD [IY], H       | 2      |
| 74 ll       | LD [IY], [BR:ll] | 4      |
| 75          | LD [IY], [HL]    | 3      |
| 76          | LD [IY], [IX]    | 3      |
| 77          | LD [IY], [IY]    | 3      |
| 78 ll       | LD [BR:ll], A    | 3      |
| 79 ll       | LD [BR:ll], B    | 3      |
| 7A ll       | LD [BR:ll], L    | 3      |
| 7B ll       | LD [BR:ll], H    | 3      |
| 7D ll       | LD [BR:ll], [HL] | 4      |
| 7E ll       | LD [BR:ll], [IX] | 4      |
| 7F ll       | LD [BR:ll], [IY] | 4      |
| 9F nn       | LD SC, #nn       | 3      |
| B0 nn       | LD A, #nn        | 2      |
| B1 nn       | LD B, #nn        | 2      |
| B2 nn       | LD L, #nn        | 2      |
| B3 nn       | LD H, #nn        | 2      |
| B4 nn       | LD BR, #nn       | 2      |
| B5 nn       | LD [HL], #nn     | 3      |
| B6 nn       | LD [IX], #nn     | 3      |
| B7 nn       | LD [IY], #nn     | 3      |
| DD ll nn    | LD [BR:ll], #nn  | 4      |
| CE C4 nn    | LD NB, #nn       | 4      |
| CE C5 nn    | LD EP, #nn       | 3      |
| CE C6 nn    | LD XP, #nn       | 3      |
| CE C7 nn    | LD YP, #nn       | 3      |
| CE 40 dd    | LD A, [IX+dd]    | 4      |
| CE 41 dd    | LD A, [IY+dd]    | 4      |
| CE 42       | LD A, [IX+L]     | 4      |
| CE 43       | LD A, [IY+L]     | 4      |
| CE 48 dd    | LD B, [IX+dd]    | 4      |
| CE 49 dd    | LD B, [IY+dd]    | 4      |
| CE 4A       | LD B, [IX+L]     | 4      |
| CE 4B       | LD B, [IY+L]     | 4      |
| CE 50 dd    | LD L, [IX+dd]    | 4      |
| CE 51 dd    | LD L, [IY+dd]    | 4      |
| CE 52       | LD L, [IX+L]     | 4      |
| CE 53       | LD L, [IY+L]     | 4      |
| CE 58 dd    | LD H, [IX+dd]    | 4      |
| CE 59 dd    | LD H, [IY+dd]    | 4      |
| CE 5A       | LD H, [IX+L]     | 4      |
| CE 5B       | LD H, [IY+L]     | 4      |
| CE 44 dd    | LD [IX+dd], A    | 4      |
| CE 45 dd    | LD [IY+dd], A    | 4      |
| CE 46       | LD [IX+L], A     | 4      |
| CE 47       | LD [IY+L], A     | 4      |
| CE 4C dd    | LD [IX+dd], B    | 4      |
| CE 4D dd    | LD [IY+dd], B    | 4      |
| CE 4E       | LD [IX+L], B     | 4      |
| CE 4F       | LD [IY+L], B     | 4      |
| CE 54 dd    | LD [IX+dd], L    | 4      |
| CE 55 dd    | LD [IY+dd], L    | 4      |
| CE 56       | LD [IX+L], L     | 4      |
| CE 57       | LD [IY+L], L     | 4      |
| CE 5C dd    | LD [IX+dd], H    | 4      |
| CE 5D dd    | LD [IY+dd], H    | 4      |
| CE 5E       | LD [IX+L], H     | 4      |
| CE 5F       | LD [IY+L], H     | 4      |
| CE 60 dd    | LD [HL], [IX+dd] | 5      |
| CE 61 dd    | LD [HL], [IY+dd] | 5      |
| CE 62       | LD [HL], [IX+L]  | 5      |
| CE 63       | LD [HL], [IY+L]  | 5      |
| CE 68 dd    | LD [IX], [IX+dd] | 5      |
| CE 69 dd    | LD [IX], [IY+dd] | 5      |
| CE 6A       | LD [IX], [IX+L]  | 5      |
| CE 6B       | LD [IX], [IY+L]  | 5      |
| CE 78 dd    | LD [IY], [IX+dd] | 5      |
| CE 79 dd    | LD [IY], [IY+dd] | 5      |
| CE 7A       | LD [IY], [IX+L]  | 5      |
| CE 7B       | LD [IY], [IY+L]  | 5      |
| CE C0       | LD A, BR         | 2      |
| CE C1       | LD A, SC         | 2      |
| CE C8       | LD A, V          | 2      |
| CE C9       | LD A, EP         | 2      |
| CE CA       | LD A, XP         | 2      |
| CE CB       | LD A, YP         | 2      |
| CE C2       | LD BR, A         | 2      |
| CE C3       | LD SC, A         | 3      |
| CE CC       | LD NB, A         | 3      |
| CE CD       | LD EP, A         | 2      |
| CE CE       | LD XP, A         | 2      |
| CE CF       | LD YP, A         | 2      |
| CE D0 ll hh | LD A, [hhll]     | 5      |
| CE D1 ll hh | LD B, [hhll]     | 5      |
| CE D2 ll hh | LD L, [hhll]     | 5      |
| CE D3 ll hh | LD H, [hhll]     | 5      |
| CE D4 ll hh | LD [hhll], A     | 5      |
| CE D5 ll hh | LD [hhll], B     | 5      |
| CE D6 ll hh | LD [hhll], L     | 5      |
| CE D7 ll hh | LD [hhll], H     | 5      |

## Source as the column, and Destination as the row

|            | #nn        | A           | B           | L           | H           | BR         | SC         | V       | EP      | XP    | YP    |
| ---------- | ---------- | ----------- | ----------- | ----------- | ----------- | ---------- | ---------- | ------- | ------- | ----- | ----- |
| A          | B0 nn      | 40          | 41          | 42          | 43          | CE C0      | CE C1      | CE C8   | CE C9   | CE CA | CE CB |
| B          | B1 nn      | 48          | 49          | 4A          | 4B          |            |            |         |         |       |       |
| L          | B2 nn      | 50          | 51          | 52          | 53          |            |            |         |         |       |       |
| H          | B3 nn      | 58          | 59          | 5A          | 5B          |            |            |         |         |       |       |
| BR         | B4 nn      | CE C2       |             |             |             |            |            |         |         |       |       |
| SC         | 9F nn      | CE C3       |             |             |             |            |            |         |         |       |       |
| NB         | CE C4 nn   | CE CC       |             |             |             |            |            |         |         |       |       |
| EP         | CE C5 nn   | CE CD       |             |             |             |            |            |         |         |       |       |
| XP         | CE C6 nn   | CE CE       |             |             |             |            |            |         |         |       |       |
| YP         | CE C7 nn   | CE CF       |             |             |             |            |            |         |         |       |       |
| \[BR:ll]   | DD ll nn   | 78 nn       | 79 nn       | 7A nn       | 7B nn       |            |            |         |         |       |       |
| \[HL]      | B5 nn      | 68          | 69          | 6A          | 6B          |            |            |         |         |       |       |
| \[IX]      | B6 nn      | 60          | 61          | 62          | 63          |            |            |         |         |       |       |
| \[IY]      | B7 nn      | 70          | 71          | 72          | 73          |            |            |         |         |       |       |
| \[hhll]    |            | CE D4 ll hh | CE D5 ll hh | CE D6 ll hh | CE D7 ll hh |            |            |         |         |       |       |
| \[IX+dd]   |            | CE 44 dd    | CE 4C dd    | CE 54 dd    | CE 5C dd    |            |            |         |         |       |       |
| \[IY+dd]   |            | CE 45 dd    | CE 4D dd    | CE 55 dd    | CE 5D dd    |            |            |         |         |       |       |
| \[IX+L]    |            | CE 46       | CE 4E       | CE 56       | CE 5E       |            |            |         |         |       |       |
| \[IY+L]    |            | CE 47       | CE 4F       | CE 57       | CE 5F       |            |            |         |         |       |       |

|            | \[BR:ll]   | \[HL]       | \[IX]       | \[IY]       | \[hhll]     | \[IX+dd]   | \[IY+dd]   | \[IX+L] | \[IY+L] |       |       |
| ---------- | ---------- | ----------- | ----------- | ----------- | ----------- | ---------- | ---------- | ------- | ------- | ----- | ----- |
| A          | 44 ll      | 45          | 46          | 47          | CE D0 ll hh | CE 40 dd   | CE 41 dd   | CE 42   | CE 43   |       |       |
| B          | 4C ll      | 4D          | 4E          | 4F          | CE D1 ll hh | CE 48 dd   | CE 49 dd   | CE 4A   | CE 4B   |       |       |
| L          | 54 ll      | 55          | 56          | 57          | CE D2 ll hh | CE 50 dd   | CE 51 dd   | CE 52   | CE 53   |       |       |
| H          | 5C ll      | 5D          | 5E          | 5F          | CE D3 ll hh | CE 58 dd   | CE 59 dd   | CE 5A   | CE 5B   |       |       |
| BR         |            |             |             |             |             |            |            |         |         |       |       |
| SC         |            |             |             |             |             |            |            |         |         |       |       |
| NB         |            |             |             |             |             |            |            |         |         |       |       |
| EP         |            |             |             |             |             |            |            |         |         |       |       |
| XP         |            |             |             |             |             |            |            |         |         |       |       |
| YP         |            |             |             |             |             |            |            |         |         |       |       |
| \[BR:ll]   |            | 7D ll       | 7E ll       | 7F ll       |             |            |            |         |         |       |       |
| \[HL]      | 6C ll      | 6D          | 6E          | 6F          |             | CE 60 dd   | CE 61 dd   | CE 62   | CE 63   |       |       |
| \[IX]      | 64 ll      | 65          | 66          | 67          |             | CE 68 dd   | CE 69 dd   | CE 6A   | CE 6B   |       |       |
| \[IY]      | 74 ll      | 75          | 76          | 77          |             | CE 78 dd   | CE 79 dd   | CE 7A   | CE 7B   |       |       |
| \[hhll]    |            |             |             |             |             |            |            |         |         |       |       |
| \[IX+dd]   |            |             |             |             |             |            |            |         |         |       |       |
| \[IY+dd]   |            |             |             |             |             |            |            |         |         |       |       |
| \[IX+L]    |            |             |             |             |             |            |            |         |         |       |       |
| \[IY+L]    |            |             |             |             |             |            |            |         |         |       |       |

## Execute

```
#nn     = Immediate unsigned 8-bits
dd      = Immediate signed 8-bits
A       = Register A
B       = Register B
L       = Register L
H       = Register H
BR      = Register BR
SC      = Register SC
NB/CB   = Register NB or CB
EP      = Register EP
XP      = Register XP
YP      = Register YP
[BR:ll] = Memory: (EP shl 16) or (BR shl 8) or #nn
[HL]    = Memory: (EP shl 16) or HL
[IX]    = Memory: (XP shl 16) or IX
[IY]    = Memory: (YP shl 16) or IY
[hhll]  = Memory: hhll
[IX+dd] = Memory: (XP shl 16) or (IX + dd)
[IY+dd] = Memory: (YP shl 16) or (IY + dd)
[IX+L]  = Memory: (XP shl 16) or (IX + signed(L))
[IY+L]  = Memory: (YP shl 16) or (IY + signed(L))
```

```
; LD Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Sc
```

## Description

Copies 8-bits Source into the 8-bits Destination.

## Conditions

None

## Examples

```
; A = 0x55
LD A, $80
; A = 0x80
```

```
; A = 0x12
; B = 0xCF
LD B, A
; A = 0x12
; B = 0x12
```

```
; [HL] = 0xDE
; A = 0xCF
LD A, [HL]
; [HL] = 0xDE
; A = 0xDE
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
