# AND = Logical AND

| Hex      | Mnemonic         | Cycles |
| -------- | ---------------- | ------ |
| 20       | AND A,A          | 2      |
| 21       | AND A,B          | 2      |
| 22 nn    | AND A,#nn        | 2      |
| 23       | AND A,\[HL]      | 2      |
| 24 ll    | AND A,\[BR:ll]   | 3      |
| 25 ll hh | AND A,\[hhll]    | 4      |
| 26       | AND A,\[IX]      | 2      |
| 27       | AND A,\[IY]      | 2      |
| 9C nn    | AND SC,#nn       | 3      |
| CE B0 nn | AND B,#nn        | 3      |
| CE B1 nn | AND L,#nn        | 3      |
| CE B2 nn | AND H,#nn        | 3      |
| D8 ll nn | AND \[BR:ll],#nn | 5      |
| CE 20 dd | AND A,\[IX+dd]   | 4      |
| CE 21 dd | AND A,\[IY+dd]   | 4      |
| CE 22    | AND A,\[IX+L]    | 4      |
| CE 23    | AND A,\[IY+L]    | 4      |
| CE 24    | AND \[HL],A      | 4      |
| CE 25 nn | AND \[HL],#nn    | 5      |
| CE 26    | AND \[HL],\[IX]  | 5      |
| CE 27    | AND \[HL],\[IY]  | 5      |

## Execute

```
#nn     = Immediate unsigned 8-bits
A       = Register A
B       = Register B
L       = Register L
H       = Register H
SC      = Register SC
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
; AND Ds, Sc
;
; Ds = Destination
; Sc = Source

Ds = Ds AND Sc
```

## Description

"8-bits Destination" Logical AND with "8-bits Source".

```
Truth table:

& 0 1
0 0 0
1 0 1
```

Can be used to reset (clear) one or multiple bits via what's referred to as masking. Below is a table of bytes to AND with in order to reset certain bits:

| Reset bits | Mask to use |
| ---------- | ----------- |
| Bit 0      | $FE         |
| Bit 1      | $FD         |
| Bit 2      | $FB         |
| Bit 3      | $F7         |
| Bit 4      | $EF         |
| Bit 5      | $DF         |
| Bit 6      | $BF         |
| Bit 7      | $7F         |
| All bits   | $00         |

## Conditions

* Zero: Set when result is 0
* Negative: Set when bit 7 of the result is 1

Carry and Overflow remain unchanged

## Examples

```
; A = 0x85
AND A, $80
; A = 0x80
; SC = (Zero=0):(Negative=1)
```

```
; B = 0xF0
AND B, $04
; B = 0x00
; SC = (Zero=1):(Negative=0)
```

```
; A = 0xF0
AND A, $55
; A = 0x50
; SC = (Zero=0):(Negative=0)
```

[**« Back to Instruction set**](../S1C88_InstructionSet.md)
