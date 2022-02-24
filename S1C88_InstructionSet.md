# 8-bit arithmetic and logic operation

## **ADD**: Addition

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [ADD](S1C88_ADD.md "wikilink") | A,A          | 0           | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 1            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | 2,nn         | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | 3            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | 4,ll         | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | 5,ll,hh      | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | 6            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | 7            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE, 0,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE, 1,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE, 2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE, 3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [ADD](S1C88_ADD.md "wikilink") | \[HL\],A     | CE, 4       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE, 5,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE, 6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE, 7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |

## **ADC**: Addition with carry

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [ADC](S1C88_ADC.md "wikilink") | A,A          | 8           | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 9            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | A,nn         | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | B            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | C,ll         | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | D,ll,hh      | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | E            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | F            | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE, 8,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE, 9,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE, A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE, B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [ADC](S1C88_ADC.md "wikilink") | \[HL\],A     | CE, C       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE, D,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE, E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE, F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                             |              |             |             |         |    |

## **SUB**: Subtraction

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [SUB](S1C88_SUB.md "wikilink") | A,A          | 10          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 11           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | 12,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | 13           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | 14,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | 15,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | 16           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | 17           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE,10,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE,11,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE,12        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE,13        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [SUB](S1C88_SUB.md "wikilink") | \[HL\],A     | CE,14       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE,15,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE,16        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE,17        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |

## **SBC**: Subtraction with carry

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [SBC](S1C88_SBC.md "wikilink") | A,A          | 18          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 19           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | 1A,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | 1B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | 1C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | 1D,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | 1E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | 1F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE,18,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE,19,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE,1A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE,1B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [SBC](S1C88_SBC.md "wikilink") | \[HL\],A     | CE,1C       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE,1D,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE,1E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE,1F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                             |              |             |             |         |    |

## **AND**: Logical product

| Mnemonic                    | Machine Code   | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | -------------- | ----------- | ----------- | ------- | -- |
| I1                          | I0             | U           | D           | N       | V  |
| [AND](S1C88_AND.md "wikilink") | A,A            | 20          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 21             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | 22,nn          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | 23             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | 24,ll          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | 25,ll,hh       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | 26             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | 27             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE,20,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE,21,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE,22          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE,23          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [AND](S1C88_AND.md "wikilink") | B,\#nn         | CE,B0,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [AND](S1C88_AND.md "wikilink") | H,\#nn         | CE,B2,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [AND](S1C88_AND.md "wikilink") | \[BR:ll\],\#nn | D8,ll,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [AND](S1C88_AND.md "wikilink") | \[HL\],A       | CE,24       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE,25,nn       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE,26          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE,27          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [AND](S1C88_AND.md "wikilink") | L,\#nn         | CE,B1,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [AND](S1C88_AND.md "wikilink") | SC,\#nn        | 9C,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |                |             |             |         |    |

## **OR**: Logical sum

| Mnemonic                  | Machine Code   | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | -------------- | ----------- | ----------- | ------- | -- |
| I1                        | I0             | U           | D           | N       | V  |
| [OR](S1C88_OR.md "wikilink") | A,A            | 28          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                       | 29             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                    | 2A,nn          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                  | 2B             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]               | 2C,ll          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                | 2D,ll,hh       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                  | 2E             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                  | 2F             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]               | CE,28,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]               | CE,29,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                | CE,2A          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                | CE,2B          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [OR](S1C88_OR.md "wikilink") | B,\#nn         | CE,B4,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [OR](S1C88_OR.md "wikilink") | H,\#nn         | CE,B6,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [OR](S1C88_OR.md "wikilink") | \[BR:ll\],\#nn | D9,ll,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [OR](S1C88_OR.md "wikilink") | \[HL\],A       | CE,2C       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn               | CE,2D,nn       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]             | CE,2E          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]             | CE,2F          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [OR](S1C88_OR.md "wikilink") | L,\#nn         | CE,B5,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [OR](S1C88_OR.md "wikilink") | SC,\#nn        | 9D,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
|                           |                |             |             |         |    |

## **XOR**: Exclusive OR

| Mnemonic                    | Machine Code   | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | -------------- | ----------- | ----------- | ------- | -- |
| I1                          | I0             | U           | D           | N       | V  |
| [XOR](S1C88_XOR.md "wikilink") | A,A            | 38          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                         | 39             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                      | 3A,nn          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                    | 3B             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]                 | 3C,ll          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                  | 3D,ll,hh       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                    | 3E             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                    | 3F             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]                 | CE,38,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]                 | CE,39,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                  | CE,3A          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                  | CE,3B          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [XOR](S1C88_XOR.md "wikilink") | B,\#nn         | CE,B8,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [XOR](S1C88_XOR.md "wikilink") | H,\#nn         | CE,BA,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [XOR](S1C88_XOR.md "wikilink") | \[BR:ll\],\#nn | DA,ll,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [XOR](S1C88_XOR.md "wikilink") | \[HL\],A       | CE,3C       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn                 | CE,3D,nn       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]               | CE,3E          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]               | CE,3F          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [XOR](S1C88_XOR.md "wikilink") | L,\#nn         | CE,B9,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [XOR](S1C88_XOR.md "wikilink") | SC,\#nn        | 9E,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |                |             |             |         |    |

## **CP**: Comparison

| Mnemonic                  | Machine Code   | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | -------------- | ----------- | ----------- | ------- | -- |
| I1                        | I0             | U           | D           | N       | V  |
| [CP](S1C88_CP.md "wikilink") | A,A            | 30          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                       | 31             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                    | 32,nn          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                  | 33             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]               | 34,ll          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                | 35,ll,hh       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX\]                  | 36             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                  | 37             | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX+dd\]               | CE,30,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]               | CE,31,dd       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                | CE,32          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                | CE,33          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [CP](S1C88_CP.md "wikilink") | B,\#nn         | CE,BC,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | H,\#nn         | CE,BE,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | BR,\#hh        | CE,BF,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | \[BR:ll\],\#nn | DB,ll,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | \[HL\],A       | CE,34       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[HL\],\#nn               | CE,35,nn       | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX\]             | CE,36          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY\]             | CE,37          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [CP](S1C88_CP.md "wikilink") | L,\#nn         | CE,BD,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
|                           |                |             |             |         |    |

## **BIT**: Bit test

| Mnemonic                    | Machine Code   | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | -------------- | ----------- | ----------- | ------- | -- |
| I1                          | I0             | U           | D           | N       | V  |
| [BIT](S1C88_BIT.md "wikilink") | A,B            | 94          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,\#nn                      | 96,nn          | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [BIT](S1C88_BIT.md "wikilink") | B,\#nn         | 97,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
| [BIT](S1C88_BIT.md "wikilink") | \[HL\],\#nn    | 95,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
| [BIT](S1C88_BIT.md "wikilink") | \[BR:ll\],\#nn | DC,ll,nn    | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |                |             |             |         |    |

## **INC**: 1 increment

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [INC](S1C88_INC.md "wikilink") | A            | 80        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | B            | 81        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | H            | 83        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | \[BR:ll\]    | 85,ll     | ?PSEUDOCODE | ?CYCLES | 2  |
| [INC](S1C88_INC.md "wikilink") | \[HL\]       | 86        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | L            | 82        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | BR           | 84        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

## **DEC**: 1 decrement

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [DEC](S1C88_DEC.md "wikilink") | A            | 88        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | B            | 89        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | H            | 8B        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | \[BR:ll\]    | 8D,ll     | ?PSEUDOCODE | ?CYCLES | 2  |
| [DEC](S1C88_DEC.md "wikilink") | \[HL\]       | 8E        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | L            | 8A        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | BR           | 8C        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

## **MLT**: Multiplication

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [MLT](S1C88_MLT.md "wikilink") |              | CE,D8     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

## **DIV**: Division

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [DIV](S1C88_DIV.md "wikilink") |              | CE,D9     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

## **CPL**: Complement of 1

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [CPL](S1C88_CPL.md "wikilink") | A            | CE,A0     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CPL](S1C88_CPL.md "wikilink") | B            | CE,A1     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CPL](S1C88_CPL.md "wikilink") | \[HL\]       | CE,A3     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CPL](S1C88_CPL.md "wikilink") | \[BR:ll\]    | CE,A2,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **NEG**: Complement of 2

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [NEG](S1C88_NEG.md "wikilink") | A            | CE,A4     | ?PSEUDOCODE | ?CYCLES | 2  |
| [NEG](S1C88_NEG.md "wikilink") | B            | CE,A5     | ?PSEUDOCODE | ?CYCLES | 2  |
| [NEG](S1C88_NEG.md "wikilink") | \[HL\]       | CE,A7     | ?PSEUDOCODE | ?CYCLES | 2  |
| [NEG](S1C88_NEG.md "wikilink") | \[BR:ll\]    | CE,A6,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

# 8-bit transfer

## **LD**: Load

| Mnemonic                  | Machine Code | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                        | I0           | U           | D           | N       | V  |
| [LD](S1C88_LD.md "wikilink") | IY,\[hhll\]  | BB,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| IY,\#mmnn                 | C7,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IY,\[SP+dd\]              | CE,73,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IY,\[HL\]                 | CE,C3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,\[IX\]                 | CE,D3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,\[IY\]                 | CE,DB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,BA                     | CE,EC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,HL                     | CE,ED        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,IX                     | CE,EE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,IY                     | CE,EF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,SP                     | CE,FE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | SP,\#mmnn    | CE,6E,nn,mm | ?PSEUDOCODE | ?CYCLES | 4  |
| SP,\[hhll\]               | CE,78,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| SP,BA                     | CE,F0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,HL                     | CE,F1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,IX                     | CE,F2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,IY                     | CE,F3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | BA,\[hhll\]  | B8,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| BA,\#mmnn                 | C4,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| BA,\[SP+dd\]              | CE,70,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| BA,\[HL\]                 | CE,C0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\[IX\]                 | CE,D0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\[IY\]                 | CE,D8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,BA                     | CE,E0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,HL                     | CE,E1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                     | CE,E2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                     | CE,E3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,SP                     | CE,F8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,PC                     | CE,F9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | BR,\#hh      | B4,hh       | ?PSEUDOCODE | ?CYCLES | 2  |
| BR,A                      | CE,C2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX+L\],A   | CE,46       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[IX+L\],B                | CE,4E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX+L\],L                | CE,56        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX+L\],H                | CE,5E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | HL,\[hhll\]  | B9,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| HL,\#mmnn                 | C5,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| HL,\[SP+dd\]              | CE,71,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| HL,\[HL\]                 | CE,C1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\[IX\]                 | CE,D1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\[IY\]                 | CE,D9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,BA                     | CE,E4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,HL                     | CE,E5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                     | CE,E6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                     | CE,E7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,SP                     | CE,F4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,PC                     | CE,F5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY+L\],A   | CE,47       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[IY+L\],B                | CE,4F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY+L\],L                | CE,57        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY+L\],H                | CE,5F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | YP,\#pp      | CE,C7,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| YP,A                      | CE,CF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY\],A     | 70          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[IY\],B                  | 71           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],L                  | 72           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],H                  | 73           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[BR:ll\]          | 74,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[HL\]             | 75           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[IX\]             | 76           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[IY\]             | 77           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\#nn               | B7,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[IX+dd\]          | CE,78,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY\],\[IY+dd\]          | CE,79,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY\],\[IX+L\]           | CE,7A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[IY+L\]           | CE,7B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],BA                 | CE,DC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],HL                 | CE,DD        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],IX                 | CE,DE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],IY                 | CE,DF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[BR:ll\],A  | 78,ll       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[BR:ll\],B               | 79,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],L               | 7A,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],H               | 7B,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[HL\]          | 7D,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[IX\]          | 7E,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[IY\]          | 7F,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\#nn            | DD,ll,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | \[SP+dd\],BA | CE,74,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[SP+dd\],HL              | CE,75,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[SP+dd\],IX              | CE,76,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[SP+dd\],IY              | CE,77,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY+dd\],A  | CE,45,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[IY+dd\],B               | CE,4D,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY+dd\],L               | CE,55,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY+dd\],H               | CE,5D,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | A,A          | 40          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                       | 41           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,L                       | 42           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,H                       | 43           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]               | 44,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                  | 45           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX\]                  | 46           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                  | 47           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                    | B0,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IX+dd\]               | CE,40,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]               | CE,41,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                | CE,42        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                | CE,43        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,BR                      | CE,C0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,SC                      | CE,C1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,NB                      | CE,C8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,EP                      | CE,C9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,XP                      | CE,CA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,YP                      | CE,CB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                | CE,D0,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | IX,\[hhll\]  | BA,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| IX,\#mmnn                 | C6,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IX,\[SP+dd\]              | CE,72,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IX,\[HL\]                 | CE,C2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,\[IX\]                 | CE,D2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,\[IY\]                 | CE,DA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,BA                     | CE,E8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,HL                     | CE,E9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,IX                     | CE,EA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,IY                     | CE,EB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,SP                     | CE,FA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | B,A          | 48          | ?PSEUDOCODE | ?CYCLES | 1  |
| B,B                       | 49           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,L                       | 4A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,H                       | 4B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[BR:ll\]               | 4C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[HL\]                  | 4D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[IX\]                  | 4E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[IY\]                  | 4F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\#nn                    | B1,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[IX+dd\]               | CE,48,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| B,\[IY+dd\]               | CE,49,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| B,\[IX+L\]                | CE,4A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[IY+L\]                | CE,4B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[hhll\]                | CE,D1,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | H,A          | 58          | ?PSEUDOCODE | ?CYCLES | 1  |
| H,B                       | 59           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,L                       | 5A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,H                       | 5B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[BR:ll\]               | 5C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[HL\]                  | 5D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[IX\]                  | 5E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[IY\]                  | 5F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\#nn                    | B3,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[IX+dd\]               | CE,58,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| H,\[IY+dd\]               | CE,59,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| H,\[IX+L\]                | CE,5A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[IY+L\]                | CE,5B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[hhll\]                | CE,D3,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | \[HL\],A     | 68          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[HL\],B                  | 69           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],L                  | 6A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],H                  | 6B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[BR:ll\]          | 6C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[HL\]             | 6D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[IX\]             | 6E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[IY\]             | 6F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\#nn               | B5,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IX+dd\]          | CE,60,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IY+dd\]          | CE,61,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX+L\]           | CE,62        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY+L\]           | CE,63        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],BA                 | CE,C4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],HL                 | CE,C5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],IX                 | CE,C6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],IY                 | CE,C7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | L,A          | 50          | ?PSEUDOCODE | ?CYCLES | 1  |
| L,B                       | 51           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,L                       | 52           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,H                       | 53           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[BR:ll\]               | 54,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[HL\]                  | 55           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[IX\]                  | 56           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[IY\]                  | 57           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\#nn                    | B2,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[IX+dd\]               | CE,50,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| L,\[IY+dd\]               | CE,51,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| L,\[IX+L\]                | CE,52        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[IY+L\]                | CE,53        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[hhll\]                | CE,D2,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | \[hhll\],BA  | BC,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[hhll\],HL               | BD,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],IX               | BE,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],IY               | BF,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],A                | CE,D4,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],B                | CE,D5,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],L                | CE,D6,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],H                | CE,D7,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],SP               | CE,7C,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | XP,\#pp      | CE,C6,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| XP,A                      | CE,CE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | EP,\#pp      | CE,C5,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| EP,A                      | CE,CD        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX\],A     | 60          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[IX\],B                  | 61           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],L                  | 62           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],H                  | 63           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[BR:ll\]          | 64,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[HL\]             | 65           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[IX\]             | 66           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[IY\]             | 67           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\#nn               | B6,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[IX+dd\]          | CE,68,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX\],\[IY+dd\]          | CE,69,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX\],\[IX+L\]           | CE,6A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[IY+L\]           | CE,6B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],BA                 | CE,D4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],HL                 | CE,D5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],IX                 | CE,D6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],IY                 | CE,D7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX+dd\],A  | CE,44,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[IX+dd\],B               | CE,4C,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX+dd\],L               | CE,54,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX+dd\],H               | CE,5C,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | SC,\#nn      | 9F,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
| SC,A                      | CE,C3        | ?PSEUDOCODE | ?CYCLES     | 2       | ↕  |
| [LD](S1C88_LD.md "wikilink") | NB,\#bb      | CE,C4,bb    | ?PSEUDOCODE | ?CYCLES | 3  |
| NB,A                      | CE,CC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                           |              |             |             |         |    |

## **EX**: Byte exchange

| Mnemonic                  | Machine Code | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                        | I0           | U           | D           | N       | V  |
| [EX](S1C88_EX.md "wikilink") | A,B          | CC          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,\[HL\]                  | CD           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |

## **SWAP**: Nibble exchange

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [SWAP](S1C88_SWAP.md "wikilink") | A            | F6        | ?PSEUDOCODE | ?CYCLES | 1  |
| [SWAP](S1C88_SWAP.md "wikilink") | \[HL\]       | F7        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

# Rotate/shift

## **RL**: Rotate to left

| Mnemonic                  | Machine Code | Operation | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                        | I0           | U         | D           | N       | V  |
| [RL](S1C88_RL.md "wikilink") | A            | CE,90     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RL](S1C88_RL.md "wikilink") | B            | CE,91     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RL](S1C88_RL.md "wikilink") | \[HL\]       | CE,93     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RL](S1C88_RL.md "wikilink") | \[BR:ll\]    | CE,92,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                           |              |           |             |         |    |

## **RLC**: Rotate to left with carry

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [RLC](S1C88_RLC.md "wikilink") | A            | CE,94     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RLC](S1C88_RLC.md "wikilink") | B            | CE,95     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RLC](S1C88_RLC.md "wikilink") | \[HL\]       | CE,97     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RLC](S1C88_RLC.md "wikilink") | \[BR:ll\]    | CE,96,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **RR**: Rotate to right

| Mnemonic                  | Machine Code | Operation | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                        | I0           | U         | D           | N       | V  |
| [RR](S1C88_RR.md "wikilink") | A            | CE,98     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RR](S1C88_RR.md "wikilink") | B            | CE,99     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RR](S1C88_RR.md "wikilink") | \[HL\]       | CE,9B     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RR](S1C88_RR.md "wikilink") | \[BR:ll\]    | CE,9A,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                           |              |           |             |         |    |

## **RRC**: Rotate to right with carry

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [RRC](S1C88_RRC.md "wikilink") | A            | CE,9C     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RRC](S1C88_RRC.md "wikilink") | B            | CE,9D     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RRC](S1C88_RRC.md "wikilink") | \[HL\]       | CE,9F     | ?PSEUDOCODE | ?CYCLES | 2  |
| [RRC](S1C88_RRC.md "wikilink") | \[BR:ll\]    | CE,9E,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **SLA**: Arithmetic shift to left

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SLA](S1C88_SLA.md "wikilink") | A            | CE,80     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLA](S1C88_SLA.md "wikilink") | B            | CE,81     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLA](S1C88_SLA.md "wikilink") | \[HL\]       | CE,83     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLA](S1C88_SLA.md "wikilink") | \[BR:ll\]    | CE,82,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **SLL**: Logical shift to left

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SLL](S1C88_SLL.md "wikilink") | A            | CE,84     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLL](S1C88_SLL.md "wikilink") | B            | CE,85     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLL](S1C88_SLL.md "wikilink") | \[HL\]       | CE,87     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SLL](S1C88_SLL.md "wikilink") | \[BR:ll\]    | CE,86,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **SRA**: Arithmetic shift to right

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SRA](S1C88_SRA.md "wikilink") | A            | CE,88     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRA](S1C88_SRA.md "wikilink") | B            | CE,89     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRA](S1C88_SRA.md "wikilink") | \[HL\]       | CE,8B     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRA](S1C88_SRA.md "wikilink") | \[BR:ll\]    | CE,8A,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **SRL**: Logical shift to right

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SRL](S1C88_SRL.md "wikilink") | A            | CE,8C     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRL](S1C88_SRL.md "wikilink") | B            | CE,8D     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRL](S1C88_SRL.md "wikilink") | \[HL\]       | CE,8F     | ?PSEUDOCODE | ?CYCLES | 2  |
| [SRL](S1C88_SRL.md "wikilink") | \[BR:ll\]    | CE,8E,ll  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

# Auxiliary operation

## **PACK**: Pack

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [PACK](S1C88_PACK.md "wikilink") |              | DE        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

## **UPCK**: Unpack

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [UPCK](S1C88_UPCK.md "wikilink") |              | DF        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

## **SEP**: Code extension

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SEP](S1C88_SEP.md "wikilink") |              | CE,A8     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

# 16-bit arithmetic operation

## **ADD**: Addition

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [ADD](S1C88_ADD.md "wikilink") | IX,\#mmnn    | C2,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| IX,BA                       | CE,40        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,HL                       | CE,41        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [ADD](S1C88_ADD.md "wikilink") | BA,\#mmnn    | C0,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| BA,BA                       | CE, 0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,HL                       | CE, 1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                       | CE, 2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                       | CE, 3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [ADD](S1C88_ADD.md "wikilink") | SP,BA        | CE,44       | ?PSEUDOCODE | ?CYCLES | 2  |
| SP,HL                       | CE,45        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,\#mmnn                   | CE,68,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [ADD](S1C88_ADD.md "wikilink") | IY,\#mmnn    | C3,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| IY,BA                       | CE,42        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,HL                       | CE,43        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [ADD](S1C88_ADD.md "wikilink") | HL,\#mmnn    | C1,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| HL,BA                       | CE,20        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,HL                       | CE,21        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                       | CE,22        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                       | CE,23        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                             |              |             |             |         |    |

## **ADC**: Addition with carry

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [ADC](S1C88_ADC.md "wikilink") | BA,BA        | CE, 4       | ?PSEUDOCODE | ?CYCLES | 2  |
| BA,HL                       | CE, 5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                       | CE, 6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                       | CE, 7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\#mmnn                   | CE,60,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [ADC](S1C88_ADC.md "wikilink") | HL,BA        | CE,24       | ?PSEUDOCODE | ?CYCLES | 2  |
| HL,HL                       | CE,25        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                       | CE,26        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                       | CE,27        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\#mmnn                   | CE,61,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
|                             |              |             |             |         |    |

## **SUB**: Subtraction

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [SUB](S1C88_SUB.md "wikilink") | IX,\#mmnn    | D2,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| IX,BA                       | CE,48        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,HL                       | CE,49        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [SUB](S1C88_SUB.md "wikilink") | BA,\#mmnn    | D0,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| BA,BA                       | CE, 8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,HL                       | CE, 9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                       | CE, A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                       | CE, B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [SUB](S1C88_SUB.md "wikilink") | SP,BA        | CE,4C       | ?PSEUDOCODE | ?CYCLES | 2  |
| SP,HL                       | CE,4D        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,\#mmnn                   | CE,6A,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [SUB](S1C88_SUB.md "wikilink") | IY,\#mmnn    | D3,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| IY,BA                       | CE,4A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,HL                       | CE,4B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [SUB](S1C88_SUB.md "wikilink") | HL,\#mmnn    | D1,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| HL,BA                       | CE,28        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,HL                       | CE,29        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                       | CE,2A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                       | CE,2B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                             |              |             |             |         |    |

## **SBC**: Subtraction with carry

| Mnemonic                    | Machine Code | Operation   | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                          | I0           | U           | D           | N       | V  |
| [SBC](S1C88_SBC.md "wikilink") | BA,BA        | CE, C       | ?PSEUDOCODE | ?CYCLES | 2  |
| BA,HL                       | CE, D        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                       | CE, E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                       | CE, F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\#mmnn                   | CE,62,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [SBC](S1C88_SBC.md "wikilink") | HL,BA        | CE,2C       | ?PSEUDOCODE | ?CYCLES | 2  |
| HL,HL                       | CE,2D        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                       | CE,2E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                       | CE,2F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\#mmnn                   | CE,63,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
|                             |              |             |             |         |    |

## **CP**: Comparison

| Mnemonic                  | Machine Code | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                        | I0           | U           | D           | N       | V  |
| [CP](S1C88_CP.md "wikilink") | IX,\#mmnn    | D6,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | BA,\#mmnn    | D4,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| BA,BA                     | CE,18        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,HL                     | CE,19        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                     | CE,1A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                     | CE,1B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [CP](S1C88_CP.md "wikilink") | IY,\#mmnn    | D7,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| [CP](S1C88_CP.md "wikilink") | HL,\#mmnn    | D5,nn,mm    | ?PSEUDOCODE | ?CYCLES | 3  |
| HL,BA                     | CE,38        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,HL                     | CE,39        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                     | CE,3A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                     | CE,3B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [CP](S1C88_CP.md "wikilink") | SP,BA        | CE,5C       | ?PSEUDOCODE | ?CYCLES | 2  |
| SP,HL                     | CE,5D        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,\#mmnn                 | CE,6C,nn,mm  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
|                           |              |             |             |         |    |

## **INC**: 1 increment

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [INC](S1C88_INC.md "wikilink") | IX           | 92        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | BA           | 90        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | HL           | 91        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | IY           | 93        | ?PSEUDOCODE | ?CYCLES | 1  |
| [INC](S1C88_INC.md "wikilink") | SP           | 87        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

## **DEC**: 1 decrement

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [DEC](S1C88_DEC.md "wikilink") | IX           | 9A        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | BA           | 98        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | HL           | 99        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | IY           | 9B        | ?PSEUDOCODE | ?CYCLES | 1  |
| [DEC](S1C88_DEC.md "wikilink") | SP           | 8F        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

# 16-bit transfer

## **LD**: Load

| Mnemonic                  | Machine Code | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                        | I0           | U           | D           | N       | V  |
| [LD](S1C88_LD.md "wikilink") | IY,\[hhll\]  | BB,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| IY,\#mmnn                 | C7,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IY,\[SP+dd\]              | CE,73,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IY,\[HL\]                 | CE,C3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,\[IX\]                 | CE,D3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,\[IY\]                 | CE,DB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,BA                     | CE,EC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,HL                     | CE,ED        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,IX                     | CE,EE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,IY                     | CE,EF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IY,SP                     | CE,FE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | SP,\#mmnn    | CE,6E,nn,mm | ?PSEUDOCODE | ?CYCLES | 4  |
| SP,\[hhll\]               | CE,78,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| SP,BA                     | CE,F0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,HL                     | CE,F1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,IX                     | CE,F2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| SP,IY                     | CE,F3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | BA,\[hhll\]  | B8,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| BA,\#mmnn                 | C4,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| BA,\[SP+dd\]              | CE,70,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| BA,\[HL\]                 | CE,C0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\[IX\]                 | CE,D0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,\[IY\]                 | CE,D8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,BA                     | CE,E0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,HL                     | CE,E1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IX                     | CE,E2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,IY                     | CE,E3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,SP                     | CE,F8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| BA,PC                     | CE,F9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | BR,\#hh      | B4,hh       | ?PSEUDOCODE | ?CYCLES | 2  |
| BR,A                      | CE,C2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX+L\],A   | CE,46       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[IX+L\],B                | CE,4E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX+L\],L                | CE,56        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX+L\],H                | CE,5E        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | HL,\[hhll\]  | B9,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| HL,\#mmnn                 | C5,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| HL,\[SP+dd\]              | CE,71,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| HL,\[HL\]                 | CE,C1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\[IX\]                 | CE,D1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,\[IY\]                 | CE,D9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,BA                     | CE,E4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,HL                     | CE,E5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IX                     | CE,E6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,IY                     | CE,E7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,SP                     | CE,F4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| HL,PC                     | CE,F5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY+L\],A   | CE,47       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[IY+L\],B                | CE,4F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY+L\],L                | CE,57        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY+L\],H                | CE,5F        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | YP,\#pp      | CE,C7,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| YP,A                      | CE,CF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY\],A     | 70          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[IY\],B                  | 71           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],L                  | 72           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],H                  | 73           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[BR:ll\]          | 74,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[HL\]             | 75           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[IX\]             | 76           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\[IY\]             | 77           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IY\],\#nn               | B7,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[IX+dd\]          | CE,78,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY\],\[IY+dd\]          | CE,79,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY\],\[IX+L\]           | CE,7A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],\[IY+L\]           | CE,7B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],BA                 | CE,DC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],HL                 | CE,DD        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],IX                 | CE,DE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IY\],IY                 | CE,DF        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[BR:ll\],A  | 78,ll       | ?PSEUDOCODE | ?CYCLES | 2  |
| \[BR:ll\],B               | 79,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],L               | 7A,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],H               | 7B,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[HL\]          | 7D,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[IX\]          | 7E,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\[IY\]          | 7F,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[BR:ll\],\#nn            | DD,ll,nn     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | \[SP+dd\],BA | CE,74,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[SP+dd\],HL              | CE,75,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[SP+dd\],IX              | CE,76,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[SP+dd\],IY              | CE,77,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IY+dd\],A  | CE,45,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[IY+dd\],B               | CE,4D,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY+dd\],L               | CE,55,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IY+dd\],H               | CE,5D,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | A,A          | 40          | ?PSEUDOCODE | ?CYCLES | 1  |
| A,B                       | 41           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,L                       | 42           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,H                       | 43           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[BR:ll\]               | 44,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[HL\]                  | 45           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IX\]                  | 46           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\[IY\]                  | 47           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| A,\#nn                    | B0,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IX+dd\]               | CE,40,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IY+dd\]               | CE,41,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| A,\[IX+L\]                | CE,42        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[IY+L\]                | CE,43        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,BR                      | CE,C0        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,SC                      | CE,C1        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,NB                      | CE,C8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,EP                      | CE,C9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,XP                      | CE,CA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,YP                      | CE,CB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| A,\[hhll\]                | CE,D0,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | IX,\[hhll\]  | BA,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| IX,\#mmnn                 | C6,nn,mm     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IX,\[SP+dd\]              | CE,72,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| IX,\[HL\]                 | CE,C2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,\[IX\]                 | CE,D2        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,\[IY\]                 | CE,DA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,BA                     | CE,E8        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,HL                     | CE,E9        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,IX                     | CE,EA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,IY                     | CE,EB        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| IX,SP                     | CE,FA        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | B,A          | 48          | ?PSEUDOCODE | ?CYCLES | 1  |
| B,B                       | 49           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,L                       | 4A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,H                       | 4B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[BR:ll\]               | 4C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[HL\]                  | 4D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[IX\]                  | 4E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\[IY\]                  | 4F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| B,\#nn                    | B1,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[IX+dd\]               | CE,48,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| B,\[IY+dd\]               | CE,49,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| B,\[IX+L\]                | CE,4A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[IY+L\]                | CE,4B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| B,\[hhll\]                | CE,D1,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | H,A          | 58          | ?PSEUDOCODE | ?CYCLES | 1  |
| H,B                       | 59           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,L                       | 5A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,H                       | 5B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[BR:ll\]               | 5C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[HL\]                  | 5D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[IX\]                  | 5E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\[IY\]                  | 5F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| H,\#nn                    | B3,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[IX+dd\]               | CE,58,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| H,\[IY+dd\]               | CE,59,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| H,\[IX+L\]                | CE,5A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[IY+L\]                | CE,5B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| H,\[hhll\]                | CE,D3,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | \[HL\],A     | 68          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[HL\],B                  | 69           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],L                  | 6A           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],H                  | 6B           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[BR:ll\]          | 6C,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[HL\]             | 6D           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[IX\]             | 6E           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\[IY\]             | 6F           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[HL\],\#nn               | B5,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IX+dd\]          | CE,60,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IY+dd\]          | CE,61,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[HL\],\[IX+L\]           | CE,62        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],\[IY+L\]           | CE,63        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],BA                 | CE,C4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],HL                 | CE,C5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],IX                 | CE,C6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[HL\],IY                 | CE,C7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | L,A          | 50          | ?PSEUDOCODE | ?CYCLES | 1  |
| L,B                       | 51           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,L                       | 52           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,H                       | 53           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[BR:ll\]               | 54,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[HL\]                  | 55           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[IX\]                  | 56           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\[IY\]                  | 57           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| L,\#nn                    | B2,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[IX+dd\]               | CE,50,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| L,\[IY+dd\]               | CE,51,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| L,\[IX+L\]                | CE,52        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[IY+L\]                | CE,53        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| L,\[hhll\]                | CE,D2,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | \[hhll\],BA  | BC,ll,hh    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[hhll\],HL               | BD,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],IX               | BE,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],IY               | BF,ll,hh     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[hhll\],A                | CE,D4,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],B                | CE,D5,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],L                | CE,D6,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],H                | CE,D7,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| \[hhll\],SP               | CE,7C,ll,hh  | ?PSEUDOCODE | ?CYCLES     | 4       | –  |
| [LD](S1C88_LD.md "wikilink") | XP,\#pp      | CE,C6,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| XP,A                      | CE,CE        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | EP,\#pp      | CE,C5,pp    | ?PSEUDOCODE | ?CYCLES | 3  |
| EP,A                      | CE,CD        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX\],A     | 60          | ?PSEUDOCODE | ?CYCLES | 1  |
| \[IX\],B                  | 61           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],L                  | 62           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],H                  | 63           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[BR:ll\]          | 64,ll        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[HL\]             | 65           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[IX\]             | 66           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\[IY\]             | 67           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| \[IX\],\#nn               | B6,nn        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[IX+dd\]          | CE,68,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX\],\[IY+dd\]          | CE,69,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX\],\[IX+L\]           | CE,6A        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],\[IY+L\]           | CE,6B        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],BA                 | CE,D4        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],HL                 | CE,D5        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],IX                 | CE,D6        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| \[IX\],IY                 | CE,D7        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | \[IX+dd\],A  | CE,44,dd    | ?PSEUDOCODE | ?CYCLES | 3  |
| \[IX+dd\],B               | CE,4C,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX+dd\],L               | CE,54,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| \[IX+dd\],H               | CE,5C,dd     | ?PSEUDOCODE | ?CYCLES     | 3       | –  |
| [LD](S1C88_LD.md "wikilink") | SC,\#nn      | 9F,nn       | ?PSEUDOCODE | ?CYCLES | 2  |
| SC,A                      | CE,C3        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
| [LD](S1C88_LD.md "wikilink") | NB,\#bb      | CE,C4,bb    | ?PSEUDOCODE | ?CYCLES | 3  |
| NB,A                      | CE,CC        | ?PSEUDOCODE | ?CYCLES     | 2       | –  |
|                           |              |             |             |         |    |

## **EX**: Byte exchange

| Mnemonic                  | Machine Code | Operation   | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | ----------- | ----------- | ------- | -- |
| I1                        | I0           | U           | D           | N       | V  |
| [EX](S1C88_EX.md "wikilink") | BA,HL        | C8          | ?PSEUDOCODE | ?CYCLES | 1  |
| BA,IX                     | C9           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| BA,IY                     | CA           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
| BA,SP                     | CB           | ?PSEUDOCODE | ?CYCLES     | 1       | –  |
|                           |              |             |             |         |    |

# Stack Control

## **PUSH**: Push

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [PUSH](S1C88_PUSH.md "wikilink") | IY           | A3        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | IX           | A2        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | ALL          | CE,B8     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | B            | CE,B1     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | BA           | A0        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | IP           | A6        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | ALE          | CE,B9     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | L            | CE,B2     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | HL           | A1        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | A            | CE,B0     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | BR           | A4        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | H            | CE,B3     | ?PSEUDOCODE | ?CYCLES | 2  |
| [PUSH](S1C88_PUSH.md "wikilink") | SC           | A7        | ?PSEUDOCODE | ?CYCLES | 1  |
| [PUSH](S1C88_PUSH.md "wikilink") | EP           | A5        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

## **POP**: Pop

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [POP](S1C88_POP.md "wikilink") | IY           | AB        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | IX           | AA        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | ALL          | CE,BC     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | B            | CE,B5     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | BA           | A8        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | IP           | AE        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | ALE          | CE,BD     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | L            | CE,B6     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | HL           | A9        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | A            | CE,B4     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | BR           | AC        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | H            | CE,B7     | ?PSEUDOCODE | ?CYCLES | 2  |
| [POP](S1C88_POP.md "wikilink") | SC           | AF        | ?PSEUDOCODE | ?CYCLES | 1  |
| [POP](S1C88_POP.md "wikilink") | EP           | AD        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

# Branch

## **JRS**: Relative short jump

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [JRS](S1C88_JRS.md "wikilink") | F0,rr        | CE,E8,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | F1,rr        | CE,E9,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | C,rr         | E4,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JRS](S1C88_JRS.md "wikilink") | LE,rr        | CE,E1,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | GE,rr        | CE,E3,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | rr           | F1,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JRS](S1C88_JRS.md "wikilink") | NC,rr        | E5,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JRS](S1C88_JRS.md "wikilink") | M,rr         | CE,E7,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | LT,rr        | CE,E0,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | F3,rr        | CE,EB,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | P,rr         | CE,E6,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | NZ,rr        | E7,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JRS](S1C88_JRS.md "wikilink") | GT,rr        | CE,E2,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | NF3,rr       | CE,EF,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | NF2,rr       | CE,EE,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | NF1,rr       | CE,ED,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | V,rr         | CE,E4,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | F2,rr        | CE,EA,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | Z,rr         | E6,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JRS](S1C88_JRS.md "wikilink") | NF0,rr       | CE,EC,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRS](S1C88_JRS.md "wikilink") | NV,rr        | CE,E5,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **JRL**: Relative long jump

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [JRL](S1C88_JRL.md "wikilink") | C,qqrr       | EC,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRL](S1C88_JRL.md "wikilink") | NC,qqrr      | ED,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRL](S1C88_JRL.md "wikilink") | Z,qqrr       | EE,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRL](S1C88_JRL.md "wikilink") | NZ,qqrr      | EF,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [JRL](S1C88_JRL.md "wikilink") | qqrr         | F3,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
|                             |              |           |             |         |    |

## **JP**: Indirect jump

| Mnemonic                  | Machine Code | Operation | Cycles      | Bytes   | SC |
| ------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                        | I0           | U         | D           | N       | V  |
| [JP](S1C88_JP.md "wikilink") | \[kk\]       | FD,kk     | ?PSEUDOCODE | ?CYCLES | 2  |
| [JP](S1C88_JP.md "wikilink") | HL           | F4        | ?PSEUDOCODE | ?CYCLES | 1  |
|                           |              |           |             |         |    |

## **DJR**: Loop

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [DJR](S1C88_DJR.md "wikilink") | NZ,rr        | F5,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

## **CARS**: Relative short call

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [CARS](S1C88_CARS.md "wikilink") | F0,rr        | CE,F8,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | F1,rr        | CE,F9,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | C,rr         | E0,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CARS](S1C88_CARS.md "wikilink") | LE,rr        | CE,F1,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | GE,rr        | CE,F3,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | rr           | F0,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CARS](S1C88_CARS.md "wikilink") | NC,rr        | E1,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CARS](S1C88_CARS.md "wikilink") | M,rr         | CE,F7,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | LT,rr        | CE,F0,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | F3,rr        | CE,FB,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | P,rr         | CE,F6,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | NZ,rr        | E3,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CARS](S1C88_CARS.md "wikilink") | GT,rr        | CE,F2,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | NF3,rr       | CE,FF,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | NF2,rr       | CE,FE,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | NF1,rr       | CE,FD,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | V,rr         | CE,F4,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | F2,rr        | CE,FA,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | Z,rr         | E2,rr     | ?PSEUDOCODE | ?CYCLES | 2  |
| [CARS](S1C88_CARS.md "wikilink") | NF0,rr       | CE,FC,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARS](S1C88_CARS.md "wikilink") | NV,rr        | CE,F5,rr  | ?PSEUDOCODE | ?CYCLES | 3  |
|                               |              |           |             |         |    |

## **CARL**: Relative long call

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [CARL](S1C88_CARL.md "wikilink") | C,qqrr       | E8,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARL](S1C88_CARL.md "wikilink") | NC,qqrr      | E9,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARL](S1C88_CARL.md "wikilink") | Z,qqrr       | EA,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARL](S1C88_CARL.md "wikilink") | NZ,qqrr      | EB,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
| [CARL](S1C88_CARL.md "wikilink") | qqrr         | F2,rr,qq  | ?PSEUDOCODE | ?CYCLES | 3  |
|                               |              |           |             |         |    |

## **CALL**: Indirect call

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [CALL](S1C88_CALL.md "wikilink") | \[hhll\]     | FB,ll,hh  | ?PSEUDOCODE | ?CYCLES | 3  |
|                               |              |           |             |         |    |

## **RET**: Return

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [RET](S1C88_RET.md "wikilink") |              | F8        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

## **RETE**: Exception processing return

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [RETE](S1C88_RETE.md "wikilink") |              | F9        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

## **RETS**: Return and skip

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [RETS](S1C88_RETS.md "wikilink") |              | FA        | ?PSEUDOCODE | ?CYCLES | 1  |
|                               |              |           |             |         |    |

## **INT**: Software interrupt

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [INT](S1C88_INT.md "wikilink") | \[kk\]       | FC,kk     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

# System Control

## **NOP**: No operation

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [NOP](S1C88_NOP.md "wikilink") |              | FF        | ?PSEUDOCODE | ?CYCLES | 1  |
|                             |              |           |             |         |    |

## **HALT**: Shifts to HALT status

| Mnemonic                      | Machine Code | Operation | Cycles      | Bytes   | SC |
| ----------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                            | I0           | U         | D           | N       | V  |
| [HALT](S1C88_HALT.md "wikilink") |              | CE,AE     | ?PSEUDOCODE | ?CYCLES | 2  |
|                               |              |           |             |         |    |

## **SLP**: Shifts to SLEEP status

| Mnemonic                    | Machine Code | Operation | Cycles      | Bytes   | SC |
| --------------------------- | ------------ | --------- | ----------- | ------- | -- |
| I1                          | I0           | U         | D           | N       | V  |
| [SLP](S1C88_SLP.md "wikilink") |              | CE,AF     | ?PSEUDOCODE | ?CYCLES | 2  |
|                             |              |           |             |         |    |

# Operation Code Map

## 1st operation code

|    |                                       |                                       |                                       |                                       |                                            |                                         |                                         |                                         |                                            |                                          |                                            |                                          |                                            |                                            |                                            |                                            |
| -- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------------ | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------------ | ---------------------------------------- | ------------------------------------------ | ---------------------------------------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
|    | x0                                    | x1                                    | x2                                    | x3                                    | x4                                         | x5                                      | x6                                      | x7                                      | x8                                         | x9                                       | xA                                         | xB                                       | xC                                         | xD                                         | xE                                         | xF                                         |
| 0x | [ADD](S1C88_ADD.md "wikilink") A,A       | [ADD](S1C88_ADD.md "wikilink") A,B       | [ADD](S1C88_ADD.md "wikilink") A,\#nn    | [ADD](S1C88_ADD.md "wikilink") A,\[HL\]  | [ADD](S1C88_ADD.md "wikilink") A,\[BR:ll\]    | [ADD](S1C88_ADD.md "wikilink") A,\[hhll\]  | [ADD](S1C88_ADD.md "wikilink") A,\[IX\]    | [ADD](S1C88_ADD.md "wikilink") A,\[IY\]    | [ADC](S1C88_ADC.md "wikilink") A,A            | [ADC](S1C88_ADC.md "wikilink") A,B          | [ADC](S1C88_ADC.md "wikilink") A,\#nn         | [ADC](S1C88_ADC.md "wikilink") A,\[HL\]     | [ADC](S1C88_ADC.md "wikilink") A,\[BR:ll\]    | [ADC](S1C88_ADC.md "wikilink") A,\[hhll\]     | [ADC](S1C88_ADC.md "wikilink") A,\[IX\]       | [ADC](S1C88_ADC.md "wikilink") A,\[IY\]       |
| 1x | [SUB](S1C88_SUB.md "wikilink") A,A       | [SUB](S1C88_SUB.md "wikilink") A,B       | [SUB](S1C88_SUB.md "wikilink") A,\#nn    | [SUB](S1C88_SUB.md "wikilink") A,\[HL\]  | [SUB](S1C88_SUB.md "wikilink") A,\[BR:ll\]    | [SUB](S1C88_SUB.md "wikilink") A,\[hhll\]  | [SUB](S1C88_SUB.md "wikilink") A,\[IX\]    | [SUB](S1C88_SUB.md "wikilink") A,\[IY\]    | [SBC](S1C88_SBC.md "wikilink") A,A            | [SBC](S1C88_SBC.md "wikilink") A,B          | [SBC](S1C88_SBC.md "wikilink") A,\#nn         | [SBC](S1C88_SBC.md "wikilink") A,\[HL\]     | [SBC](S1C88_SBC.md "wikilink") A,\[BR:ll\]    | [SBC](S1C88_SBC.md "wikilink") A,\[hhll\]     | [SBC](S1C88_SBC.md "wikilink") A,\[IX\]       | [SBC](S1C88_SBC.md "wikilink") A,\[IY\]       |
| 2x | [AND](S1C88_AND.md "wikilink") A,A       | [AND](S1C88_AND.md "wikilink") A,B       | [AND](S1C88_AND.md "wikilink") A,\#nn    | [AND](S1C88_AND.md "wikilink") A,\[HL\]  | [AND](S1C88_AND.md "wikilink") A,\[BR:ll\]    | [AND](S1C88_AND.md "wikilink") A,\[hhll\]  | [AND](S1C88_AND.md "wikilink") A,\[IX\]    | [AND](S1C88_AND.md "wikilink") A,\[IY\]    | [OR](S1C88_OR.md "wikilink") A,A              | [OR](S1C88_OR.md "wikilink") A,B            | [OR](S1C88_OR.md "wikilink") A,\#nn           | [OR](S1C88_OR.md "wikilink") A,\[HL\]       | [OR](S1C88_OR.md "wikilink") A,\[BR:ll\]      | [OR](S1C88_OR.md "wikilink") A,\[hhll\]       | [OR](S1C88_OR.md "wikilink") A,\[IX\]         | [OR](S1C88_OR.md "wikilink") A,\[IY\]         |
| 3x | [CP](S1C88_CP.md "wikilink") A,A         | [CP](S1C88_CP.md "wikilink") A,B         | [CP](S1C88_CP.md "wikilink") A,\#nn      | [CP](S1C88_CP.md "wikilink") A,\[HL\]    | [CP](S1C88_CP.md "wikilink") A,\[BR:ll\]      | [CP](S1C88_CP.md "wikilink") A,\[hhll\]    | [CP](S1C88_CP.md "wikilink") A,\[IX\]      | [CP](S1C88_CP.md "wikilink") A,\[IY\]      | [XOR](S1C88_XOR.md "wikilink") A,A            | [XOR](S1C88_XOR.md "wikilink") A,B          | [XOR](S1C88_XOR.md "wikilink") A,\#nn         | [XOR](S1C88_XOR.md "wikilink") A,\[HL\]     | [XOR](S1C88_XOR.md "wikilink") A,\[BR:ll\]    | [XOR](S1C88_XOR.md "wikilink") A,\[hhll\]     | [XOR](S1C88_XOR.md "wikilink") A,\[IX\]       | [XOR](S1C88_XOR.md "wikilink") A,\[IY\]       |
| 4x | [LD](S1C88_LD.md "wikilink") A,A         | [LD](S1C88_LD.md "wikilink") A,B         | [LD](S1C88_LD.md "wikilink") A,L         | [LD](S1C88_LD.md "wikilink") A,H         | [LD](S1C88_LD.md "wikilink") A,\[BR:ll\]      | [LD](S1C88_LD.md "wikilink") A,\[HL\]      | [LD](S1C88_LD.md "wikilink") A,\[IX\]      | [LD](S1C88_LD.md "wikilink") A,\[IY\]      | [LD](S1C88_LD.md "wikilink") B,A              | [LD](S1C88_LD.md "wikilink") B,B            | [LD](S1C88_LD.md "wikilink") B,L              | [LD](S1C88_LD.md "wikilink") B,H            | [LD](S1C88_LD.md "wikilink") B,\[BR:ll\]      | [LD](S1C88_LD.md "wikilink") B,\[HL\]         | [LD](S1C88_LD.md "wikilink") B,\[IX\]         | [LD](S1C88_LD.md "wikilink") B,\[IY\]         |
| 5x | [LD](S1C88_LD.md "wikilink") L,A         | [LD](S1C88_LD.md "wikilink") L,B         | [LD](S1C88_LD.md "wikilink") L,L         | [LD](S1C88_LD.md "wikilink") L,H         | [LD](S1C88_LD.md "wikilink") L,\[BR:ll\]      | [LD](S1C88_LD.md "wikilink") L,\[HL\]      | [LD](S1C88_LD.md "wikilink") L,\[IX\]      | [LD](S1C88_LD.md "wikilink") L,\[IY\]      | [LD](S1C88_LD.md "wikilink") H,A              | [LD](S1C88_LD.md "wikilink") H,B            | [LD](S1C88_LD.md "wikilink") H,L              | [LD](S1C88_LD.md "wikilink") H,H            | [LD](S1C88_LD.md "wikilink") H,\[BR:ll\]      | [LD](S1C88_LD.md "wikilink") H,\[HL\]         | [LD](S1C88_LD.md "wikilink") H,\[IX\]         | [LD](S1C88_LD.md "wikilink") H,\[IY\]         |
| 6x | [LD](S1C88_LD.md "wikilink") \[IX\],A    | [LD](S1C88_LD.md "wikilink") \[IX\],B    | [LD](S1C88_LD.md "wikilink") \[IX\],L    | [LD](S1C88_LD.md "wikilink") \[IX\],H    | [LD](S1C88_LD.md "wikilink") \[IX\],\[BR:ll\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[HL\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[IX\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[IY\] | [LD](S1C88_LD.md "wikilink") \[HL\],A         | [LD](S1C88_LD.md "wikilink") \[HL\],B       | [LD](S1C88_LD.md "wikilink") \[HL\],L         | [LD](S1C88_LD.md "wikilink") \[HL\],H       | [LD](S1C88_LD.md "wikilink") \[HL\],\[BR:ll\] | [LD](S1C88_LD.md "wikilink") \[HL\],\[HL\]    | [LD](S1C88_LD.md "wikilink") \[HL\],\[IX\]    | [LD](S1C88_LD.md "wikilink") \[HL\],\[IY\]    |
| 7x | [LD](S1C88_LD.md "wikilink") \[IY\],A    | [LD](S1C88_LD.md "wikilink") \[IY\],B    | [LD](S1C88_LD.md "wikilink") \[IY\],L    | [LD](S1C88_LD.md "wikilink") \[IY\],H    | [LD](S1C88_LD.md "wikilink") \[IY\],\[BR:ll\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[HL\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[IX\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[IY\] | [LD](S1C88_LD.md "wikilink") \[BR:ll\],A      | [LD](S1C88_LD.md "wikilink") \[BR:ll\],B    | [LD](S1C88_LD.md "wikilink") \[BR:ll\],L      | [LD](S1C88_LD.md "wikilink") \[BR:ll\],H    |                                            | [LD](S1C88_LD.md "wikilink") \[BR:ll\],\[HL\] | [LD](S1C88_LD.md "wikilink") \[BR:ll\],\[IX\] | [LD](S1C88_LD.md "wikilink") \[BR:ll\],\[IY\] |
| 8x | [INC](S1C88_INC.md "wikilink") A         | [INC](S1C88_INC.md "wikilink") B         | [INC](S1C88_INC.md "wikilink") L         | [INC](S1C88_INC.md "wikilink") H         | [INC](S1C88_INC.md "wikilink") BR             | [INC](S1C88_INC.md "wikilink") \[BR:ll\]   | [INC](S1C88_INC.md "wikilink") \[HL\]      | [INC](S1C88_INC.md "wikilink") SP          | [DEC](S1C88_DEC.md "wikilink") A              | [DEC](S1C88_DEC.md "wikilink") B            | [DEC](S1C88_DEC.md "wikilink") L              | [DEC](S1C88_DEC.md "wikilink") H            | [DEC](S1C88_DEC.md "wikilink") BR             | [DEC](S1C88_DEC.md "wikilink") \[BR:ll\]      | [DEC](S1C88_DEC.md "wikilink") \[HL\]         | [DEC](S1C88_DEC.md "wikilink") SP             |
| 9x | [INC](S1C88_INC.md "wikilink") BA        | [INC](S1C88_INC.md "wikilink") HL        | [INC](S1C88_INC.md "wikilink") IX        | [INC](S1C88_INC.md "wikilink") IY        | [BIT](S1C88_BIT.md "wikilink") A,B            | [BIT](S1C88_BIT.md "wikilink") \[HL\],\#nn | [BIT](S1C88_BIT.md "wikilink") A,\#nn      | [BIT](S1C88_BIT.md "wikilink") B,\#nn      | [DEC](S1C88_DEC.md "wikilink") BA             | [DEC](S1C88_DEC.md "wikilink") HL           | [DEC](S1C88_DEC.md "wikilink") IX             | [DEC](S1C88_DEC.md "wikilink") IY           | [AND](S1C88_AND.md "wikilink") SC,\#nn        | [OR](S1C88_OR.md "wikilink") SC,\#nn          | [XOR](S1C88_XOR.md "wikilink") SC,\#nn        | [LD](S1C88_LD.md "wikilink") SC,\#nn          |
| Ax | [PUSH](S1C88_PUSH.md "wikilink") BA      | [PUSH](S1C88_PUSH.md "wikilink") HL      | [PUSH](S1C88_PUSH.md "wikilink") IX      | [PUSH](S1C88_PUSH.md "wikilink") IY      | [PUSH](S1C88_PUSH.md "wikilink") BR           | [PUSH](S1C88_PUSH.md "wikilink") EP        | [PUSH](S1C88_PUSH.md "wikilink") IP        | [PUSH](S1C88_PUSH.md "wikilink") SC        | [POP](S1C88_POP.md "wikilink") BA             | [POP](S1C88_POP.md "wikilink") HL           | [POP](S1C88_POP.md "wikilink") IX             | [POP](S1C88_POP.md "wikilink") IY           | [POP](S1C88_POP.md "wikilink") BR             | [POP](S1C88_POP.md "wikilink") EP             | [POP](S1C88_POP.md "wikilink") IP             | [POP](S1C88_POP.md "wikilink") SC             |
| Bx | [LD](S1C88_LD.md "wikilink") A,\#nn      | [LD](S1C88_LD.md "wikilink") B,\#nn      | [LD](S1C88_LD.md "wikilink") L,\#nn      | [LD](S1C88_LD.md "wikilink") H,\#nn      | [LD](S1C88_LD.md "wikilink") BR,\#hh          | [LD](S1C88_LD.md "wikilink") \[HL\],\#nn   | [LD](S1C88_LD.md "wikilink") \[IX\],\#nn   | [LD](S1C88_LD.md "wikilink") \[IY\],\#nn   | [LD](S1C88_LD.md "wikilink") BA,\[hhll\]      | [LD](S1C88_LD.md "wikilink") HL,\[hhll\]    | [LD](S1C88_LD.md "wikilink") IX,\[hhll\]      | [LD](S1C88_LD.md "wikilink") IY,\[hhll\]    | [LD](S1C88_LD.md "wikilink") \[hhll\],BA      | [LD](S1C88_LD.md "wikilink") \[hhll\],HL      | [LD](S1C88_LD.md "wikilink") \[hhll\],IX      | [LD](S1C88_LD.md "wikilink") \[hhll\],IY      |
| Cx | [ADD](S1C88_ADD.md "wikilink") BA,\#mmnn | [ADD](S1C88_ADD.md "wikilink") HL,\#mmnn | [ADD](S1C88_ADD.md "wikilink") IX,\#mmnn | [ADD](S1C88_ADD.md "wikilink") IY,\#mmnn | [LD](S1C88_LD.md "wikilink") BA,\#mmnn        | [LD](S1C88_LD.md "wikilink") HL,\#mmnn     | [LD](S1C88_LD.md "wikilink") IX,\#mmnn     | [LD](S1C88_LD.md "wikilink") IY,\#mmnn     | [EX](S1C88_EX.md "wikilink") BA,HL            | [EX](S1C88_EX.md "wikilink") BA,IX          | [EX](S1C88_EX.md "wikilink") BA,IY            | [EX](S1C88_EX.md "wikilink") BA,SP          | [EX](S1C88_EX.md "wikilink") A,B              | [EX](S1C88_EX.md "wikilink") A,\[HL\]         | Expansion Code                             | Expansion Code                             |
| Dx | [SUB](S1C88_SUB.md "wikilink") BA,\#mmnn | [SUB](S1C88_SUB.md "wikilink") HL,\#mmnn | [SUB](S1C88_SUB.md "wikilink") IX,\#mmnn | [SUB](S1C88_SUB.md "wikilink") IY,\#mmnn | [CP](S1C88_CP.md "wikilink") BA,\#mmnn        | [CP](S1C88_CP.md "wikilink") HL,\#mmnn     | [CP](S1C88_CP.md "wikilink") IX,\#mmnn     | [CP](S1C88_CP.md "wikilink") IY,\#mmnn     | [AND](S1C88_AND.md "wikilink") \[BR:ll\],\#nn | [OR](S1C88_OR.md "wikilink") \[BR:ll\],\#nn | [XOR](S1C88_XOR.md "wikilink") \[BR:ll\],\#nn | [CP](S1C88_CP.md "wikilink") \[BR:ll\],\#nn | [BIT](S1C88_BIT.md "wikilink") \[BR:ll\],\#nn | [LD](S1C88_LD.md "wikilink") \[BR:ll\],\#nn   | [PACK](S1C88_PACK.md "wikilink")              | [UPCK](S1C88_UPCK.md "wikilink")              |
| Ex | [CARS](S1C88_CARS.md "wikilink") C,rr    | [CARS](S1C88_CARS.md "wikilink") NC,rr   | [CARS](S1C88_CARS.md "wikilink") Z,rr    | [CARS](S1C88_CARS.md "wikilink") NZ,rr   | [JRS](S1C88_JRS.md "wikilink") C,rr           | [JRS](S1C88_JRS.md "wikilink") NC,rr       | [JRS](S1C88_JRS.md "wikilink") Z,rr        | [JRS](S1C88_JRS.md "wikilink") NZ,rr       | [CARL](S1C88_CARL.md "wikilink") C,qqrr       | [CARL](S1C88_CARL.md "wikilink") NC,qqrr    | [CARL](S1C88_CARL.md "wikilink") Z,qqrr       | [CARL](S1C88_CARL.md "wikilink") NZ,qqrr    | [JRL](S1C88_JRL.md "wikilink") C,qqrr         | [JRL](S1C88_JRL.md "wikilink") NC,qqrr        | [JRL](S1C88_JRL.md "wikilink") Z,qqrr         | [JRL](S1C88_JRL.md "wikilink") NZ,qqrr        |
| Fx | [CARS](S1C88_CARS.md "wikilink") rr      | [JRS](S1C88_JRS.md "wikilink") rr        | [CARL](S1C88_CARL.md "wikilink") qqrr    | [JRL](S1C88_JRL.md "wikilink") qqrr      | [JP](S1C88_JP.md "wikilink") HL               | [DJR](S1C88_DJR.md "wikilink") NZ,rr       | [SWAP](S1C88_SWAP.md "wikilink") A         | [SWAP](S1C88_SWAP.md "wikilink") \[HL\]    | [RET](S1C88_RET.md "wikilink")                | [RETE](S1C88_RETE.md "wikilink")            | [RETS](S1C88_RETS.md "wikilink")              | [CALL](S1C88_CALL.md "wikilink") \[hhll\]   | [INT](S1C88_INT.md "wikilink") \[kk\]         | [JP](S1C88_JP.md "wikilink") \[kk\]           |                                            | [NOP](S1C88_NOP.md "wikilink")                |
|    |                                       |                                       |                                       |                                       |                                            |                                         |                                         |                                         |                                            |                                          |                                            |                                          |                                            |                                            |                                            |                                            |

\== 2nd operation code (1st operation code = CE)
==

|    |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           |
| -- | ------------------------------------------ | ------------------------------------------ | ----------------------------------------- | ----------------------------------------- | ------------------------------------- | --------------------------------------- | ----------------------------------------- | ----------------------------------------- | ------------------------------------------ | ------------------------------------------ | ----------------------------------------- | ----------------------------------------- | ------------------------------------- | --------------------------------------- | ----------------------------------------- | ----------------------------------------- |
|    | x0                                         | x1                                         | x2                                        | x3                                        | x4                                    | x5                                      | x6                                        | x7                                        | x8                                         | x9                                         | xA                                        | xB                                        | xC                                    | xD                                      | xE                                        | xF                                        |
| 0x | [ADD](S1C88_ADD.md "wikilink") A,\[IX+dd\]    | [ADD](S1C88_ADD.md "wikilink") A,\[IY+dd\]    | [ADD](S1C88_ADD.md "wikilink") A,\[IX+L\]    | [ADD](S1C88_ADD.md "wikilink") A,\[IY+L\]    | [ADD](S1C88_ADD.md "wikilink") \[HL\],A  | [ADD](S1C88_ADD.md "wikilink") \[HL\],\#nn | [ADD](S1C88_ADD.md "wikilink") \[HL\],\[IX\] | [ADD](S1C88_ADD.md "wikilink") \[HL\],\[IY\] | [ADC](S1C88_ADC.md "wikilink") A,\[IX+dd\]    | [ADC](S1C88_ADC.md "wikilink") A,\[IY+dd\]    | [ADC](S1C88_ADC.md "wikilink") A,\[IX+L\]    | [ADC](S1C88_ADC.md "wikilink") A,\[IY+L\]    | [ADC](S1C88_ADC.md "wikilink") \[HL\],A  | [ADC](S1C88_ADC.md "wikilink") \[HL\],\#nn | [ADC](S1C88_ADC.md "wikilink") \[HL\],\[IX\] | [ADC](S1C88_ADC.md "wikilink") \[HL\],\[IY\] |
| 1x | [SUB](S1C88_SUB.md "wikilink") A,\[IX+dd\]    | [SUB](S1C88_SUB.md "wikilink") A,\[IY+dd\]    | [SUB](S1C88_SUB.md "wikilink") A,\[IX+L\]    | [SUB](S1C88_SUB.md "wikilink") A,\[IY+L\]    | [SUB](S1C88_SUB.md "wikilink") \[HL\],A  | [SUB](S1C88_SUB.md "wikilink") \[HL\],\#nn | [SUB](S1C88_SUB.md "wikilink") \[HL\],\[IX\] | [SUB](S1C88_SUB.md "wikilink") \[HL\],\[IY\] | [SBC](S1C88_SBC.md "wikilink") A,\[IX+dd\]    | [SBC](S1C88_SBC.md "wikilink") A,\[IY+dd\]    | [SBC](S1C88_SBC.md "wikilink") A,\[IX+L\]    | [SBC](S1C88_SBC.md "wikilink") A,\[IY+L\]    | [SBC](S1C88_SBC.md "wikilink") \[HL\],A  | [SBC](S1C88_SBC.md "wikilink") \[HL\],\#nn | [SBC](S1C88_SBC.md "wikilink") \[HL\],\[IX\] | [SBC](S1C88_SBC.md "wikilink") \[HL\],\[IY\] |
| 2x | [AND](S1C88_AND.md "wikilink") A,\[IX+dd\]    | [AND](S1C88_AND.md "wikilink") A,\[IY+dd\]    | [AND](S1C88_AND.md "wikilink") A,\[IX+L\]    | [AND](S1C88_AND.md "wikilink") A,\[IY+L\]    | [AND](S1C88_AND.md "wikilink") \[HL\],A  | [AND](S1C88_AND.md "wikilink") \[HL\],\#nn | [AND](S1C88_AND.md "wikilink") \[HL\],\[IX\] | [AND](S1C88_AND.md "wikilink") \[HL\],\[IY\] | [OR](S1C88_OR.md "wikilink") A,\[IX+dd\]      | [OR](S1C88_OR.md "wikilink") A,\[IY+dd\]      | [OR](S1C88_OR.md "wikilink") A,\[IX+L\]      | [OR](S1C88_OR.md "wikilink") A,\[IY+L\]      | [OR](S1C88_OR.md "wikilink") \[HL\],A    | [OR](S1C88_OR.md "wikilink") \[HL\],\#nn   | [OR](S1C88_OR.md "wikilink") \[HL\],\[IX\]   | [OR](S1C88_OR.md "wikilink") \[HL\],\[IY\]   |
| 3x | [CP](S1C88_CP.md "wikilink") A,\[IX+dd\]      | [CP](S1C88_CP.md "wikilink") A,\[IY+dd\]      | [CP](S1C88_CP.md "wikilink") A,\[IX+L\]      | [CP](S1C88_CP.md "wikilink") A,\[IY+L\]      | [CP](S1C88_CP.md "wikilink") \[HL\],A    | [CP](S1C88_CP.md "wikilink") \[HL\],\#nn   | [CP](S1C88_CP.md "wikilink") \[HL\],\[IX\]   | [CP](S1C88_CP.md "wikilink") \[HL\],\[IY\]   | [XOR](S1C88_XOR.md "wikilink") A,\[IX+dd\]    | [XOR](S1C88_XOR.md "wikilink") A,\[IY+dd\]    | [XOR](S1C88_XOR.md "wikilink") A,\[IX+L\]    | [XOR](S1C88_XOR.md "wikilink") A,\[IY+L\]    | [XOR](S1C88_XOR.md "wikilink") \[HL\],A  | [XOR](S1C88_XOR.md "wikilink") \[HL\],\#nn | [XOR](S1C88_XOR.md "wikilink") \[HL\],\[IX\] | [XOR](S1C88_XOR.md "wikilink") \[HL\],\[IY\] |
| 4x | [LD](S1C88_LD.md "wikilink") A,\[IX+dd\]      | [LD](S1C88_LD.md "wikilink") A,\[IY+dd\]      | [LD](S1C88_LD.md "wikilink") A,\[IX+L\]      | [LD](S1C88_LD.md "wikilink") A,\[IY+L\]      | [LD](S1C88_LD.md "wikilink") \[IX+dd\],A | [LD](S1C88_LD.md "wikilink") \[IY+dd\],A   | [LD](S1C88_LD.md "wikilink") \[IX+L\],A      | [LD](S1C88_LD.md "wikilink") \[IY+L\],A      | [LD](S1C88_LD.md "wikilink") B,\[IX+dd\]      | [LD](S1C88_LD.md "wikilink") B,\[IY+dd\]      | [LD](S1C88_LD.md "wikilink") B,\[IX+L\]      | [LD](S1C88_LD.md "wikilink") B,\[IY+L\]      | [LD](S1C88_LD.md "wikilink") \[IX+dd\],B | [LD](S1C88_LD.md "wikilink") \[IY+dd\],B   | [LD](S1C88_LD.md "wikilink") \[IX+L\],B      | [LD](S1C88_LD.md "wikilink") \[IY+L\],B      |
| 5x | [LD](S1C88_LD.md "wikilink") L,\[IX+dd\]      | [LD](S1C88_LD.md "wikilink") L,\[IY+dd\]      | [LD](S1C88_LD.md "wikilink") L,\[IX+L\]      | [LD](S1C88_LD.md "wikilink") L,\[IY+L\]      | [LD](S1C88_LD.md "wikilink") \[IX+dd\],L | [LD](S1C88_LD.md "wikilink") \[IY+dd\],L   | [LD](S1C88_LD.md "wikilink") \[IX+L\],L      | [LD](S1C88_LD.md "wikilink") \[IY+L\],L      | [LD](S1C88_LD.md "wikilink") H,\[IX+dd\]      | [LD](S1C88_LD.md "wikilink") H,\[IY+dd\]      | [LD](S1C88_LD.md "wikilink") H,\[IX+L\]      | [LD](S1C88_LD.md "wikilink") H,\[IY+L\]      | [LD](S1C88_LD.md "wikilink") \[IX+dd\],H | [LD](S1C88_LD.md "wikilink") \[IY+dd\],H   | [LD](S1C88_LD.md "wikilink") \[IX+L\],H      | [LD](S1C88_LD.md "wikilink") \[IY+L\],H      |
| 6x | [LD](S1C88_LD.md "wikilink") \[HL\],\[IX+dd\] | [LD](S1C88_LD.md "wikilink") \[HL\],\[IY+dd\] | [LD](S1C88_LD.md "wikilink") \[HL\],\[IX+L\] | [LD](S1C88_LD.md "wikilink") \[HL\],\[IY+L\] |                                       |                                         |                                           |                                           | [LD](S1C88_LD.md "wikilink") \[IX\],\[IX+dd\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[IY+dd\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[IX+L\] | [LD](S1C88_LD.md "wikilink") \[IX\],\[IY+L\] |                                       |                                         |                                           |                                           |
| 7x |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           | [LD](S1C88_LD.md "wikilink") \[IY\],\[IX+dd\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[IY+dd\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[IX+L\] | [LD](S1C88_LD.md "wikilink") \[IY\],\[IY+L\] |                                       |                                         |                                           |                                           |
| 8x | [SLA](S1C88_SLA.md "wikilink") A              | [SLA](S1C88_SLA.md "wikilink") B              | [SLA](S1C88_SLA.md "wikilink") \[BR:ll\]     | [SLA](S1C88_SLA.md "wikilink") \[HL\]        | [SLL](S1C88_SLL.md "wikilink") A         | [SLL](S1C88_SLL.md "wikilink") B           | [SLL](S1C88_SLL.md "wikilink") \[BR:ll\]     | [SLL](S1C88_SLL.md "wikilink") \[HL\]        | [SRA](S1C88_SRA.md "wikilink") A              | [SRA](S1C88_SRA.md "wikilink") B              | [SRA](S1C88_SRA.md "wikilink") \[BR:ll\]     | [SRA](S1C88_SRA.md "wikilink") \[HL\]        | [SRL](S1C88_SRL.md "wikilink") A         | [SRL](S1C88_SRL.md "wikilink") B           | [SRL](S1C88_SRL.md "wikilink") \[BR:ll\]     | [SRL](S1C88_SRL.md "wikilink") \[HL\]        |
| 9x | [RL](S1C88_RL.md "wikilink") A                | [RL](S1C88_RL.md "wikilink") B                | [RL](S1C88_RL.md "wikilink") \[BR:ll\]       | [RL](S1C88_RL.md "wikilink") \[HL\]          | [RLC](S1C88_RLC.md "wikilink") A         | [RLC](S1C88_RLC.md "wikilink") B           | [RLC](S1C88_RLC.md "wikilink") \[BR:ll\]     | [RLC](S1C88_RLC.md "wikilink") \[HL\]        | [RR](S1C88_RR.md "wikilink") A                | [RR](S1C88_RR.md "wikilink") B                | [RR](S1C88_RR.md "wikilink") \[BR:ll\]       | [RR](S1C88_RR.md "wikilink") \[HL\]          | [RRC](S1C88_RRC.md "wikilink") A         | [RRC](S1C88_RRC.md "wikilink") B           | [RRC](S1C88_RRC.md "wikilink") \[BR:ll\]     | [RRC](S1C88_RRC.md "wikilink") \[HL\]        |
| Ax | [CPL](S1C88_CPL.md "wikilink") A              | [CPL](S1C88_CPL.md "wikilink") B              | [CPL](S1C88_CPL.md "wikilink") \[BR:ll\]     | [CPL](S1C88_CPL.md "wikilink") \[HL\]        | [NEG](S1C88_NEG.md "wikilink") A         | [NEG](S1C88_NEG.md "wikilink") B           | [NEG](S1C88_NEG.md "wikilink") \[BR:ll\]     | [NEG](S1C88_NEG.md "wikilink") \[HL\]        | [SEP](S1C88_SEP.md "wikilink")                |                                            |                                           |                                           |                                       |                                         | [HALT](S1C88_HALT.md "wikilink")             | [SLP](S1C88_SLP.md "wikilink")               |
| Bx | [AND](S1C88_AND.md "wikilink") B,\#nn         | [AND](S1C88_AND.md "wikilink") L,\#nn         | [AND](S1C88_AND.md "wikilink") H,\#nn        |                                           | [OR](S1C88_OR.md "wikilink") B,\#nn      | [OR](S1C88_OR.md "wikilink") L,\#nn        | [OR](S1C88_OR.md "wikilink") H,\#nn          |                                           | [XOR](S1C88_XOR.md "wikilink") B,\#nn         | [XOR](S1C88_XOR.md "wikilink") L,\#nn         | [XOR](S1C88_XOR.md "wikilink") H,\#nn        |                                           | [CP](S1C88_CP.md "wikilink") B,\#nn      | [CP](S1C88_CP.md "wikilink") L,\#nn        | [CP](S1C88_CP.md "wikilink") H,\#nn          | [CP](S1C88_CP.md "wikilink") BR,\#hh         |
| Cx | [LD](S1C88_LD.md "wikilink") A,BR             | [LD](S1C88_LD.md "wikilink") A,SC             | [LD](S1C88_LD.md "wikilink") BR,A            | [LD](S1C88_LD.md "wikilink") SC,A            | [LD](S1C88_LD.md "wikilink") NB,\#bb     | [LD](S1C88_LD.md "wikilink") EP,\#pp       | [LD](S1C88_LD.md "wikilink") XP,\#pp         | [LD](S1C88_LD.md "wikilink") YP,\#pp         | [LD](S1C88_LD.md "wikilink") A,NB             | [LD](S1C88_LD.md "wikilink") A,EP             | [LD](S1C88_LD.md "wikilink") A,XP            | [LD](S1C88_LD.md "wikilink") A,YP            | [LD](S1C88_LD.md "wikilink") NB,A        | [LD](S1C88_LD.md "wikilink") EP,A          | [LD](S1C88_LD.md "wikilink") XP,A            | [LD](S1C88_LD.md "wikilink") YP,A            |
| Dx | [LD](S1C88_LD.md "wikilink") A,\[hhll\]       | [LD](S1C88_LD.md "wikilink") B,\[hhll\]       | [LD](S1C88_LD.md "wikilink") L,\[hhll\]      | [LD](S1C88_LD.md "wikilink") H,\[hhll\]      | [LD](S1C88_LD.md "wikilink") \[hhll\],A  | [LD](S1C88_LD.md "wikilink") \[hhll\],B    | [LD](S1C88_LD.md "wikilink") \[hhll\],L      | [LD](S1C88_LD.md "wikilink") \[hhll\],H      | [MLT](S1C88_MLT.md "wikilink")                | [DIV](S1C88_DIV.md "wikilink")                |                                           |                                           |                                       |                                         |                                           |                                           |
| Ex | [JRS](S1C88_JRS.md "wikilink") LT,rr          | [JRS](S1C88_JRS.md "wikilink") LE,rr          | [JRS](S1C88_JRS.md "wikilink") GT,rr         | [JRS](S1C88_JRS.md "wikilink") GE,rr         | [JRS](S1C88_JRS.md "wikilink") V,rr      | [JRS](S1C88_JRS.md "wikilink") NV,rr       | [JRS](S1C88_JRS.md "wikilink") P,rr          | [JRS](S1C88_JRS.md "wikilink") M,rr          | [JRS](S1C88_JRS.md "wikilink") F0,rr          | [JRS](S1C88_JRS.md "wikilink") F1,rr          | [JRS](S1C88_JRS.md "wikilink") F2,rr         | [JRS](S1C88_JRS.md "wikilink") F3,rr         | [JRS](S1C88_JRS.md "wikilink") NF0,rr    | [JRS](S1C88_JRS.md "wikilink") NF1,rr      | [JRS](S1C88_JRS.md "wikilink") NF2,rr        | [JRS](S1C88_JRS.md "wikilink") NF3,rr        |
| Fx | [CARS](S1C88_CARS.md "wikilink") LT,rr        | [CARS](S1C88_CARS.md "wikilink") LE,rr        | [CARS](S1C88_CARS.md "wikilink") GT,rr       | [CARS](S1C88_CARS.md "wikilink") GE,rr       | [CARS](S1C88_CARS.md "wikilink") V,rr    | [CARS](S1C88_CARS.md "wikilink") NV,rr     | [CARS](S1C88_CARS.md "wikilink") P,rr        | [CARS](S1C88_CARS.md "wikilink") M,rr        | [CARS](S1C88_CARS.md "wikilink") F0,rr        | [CARS](S1C88_CARS.md "wikilink") F1,rr        | [CARS](S1C88_CARS.md "wikilink") F2,rr       | [CARS](S1C88_CARS.md "wikilink") F3,rr       | [CARS](S1C88_CARS.md "wikilink") NF0,rr  | [CARS](S1C88_CARS.md "wikilink") NF1,rr    | [CARS](S1C88_CARS.md "wikilink") NF2,rr      | [CARS](S1C88_CARS.md "wikilink") NF3,rr      |
|    |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           |

\== 3nd operation code (1st operation code = CF)
==

|    |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| -- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
|    | x0                                     | x1                                     | x2                                     | x3                                     | x4                                     | x5                                     | x6                                     | x7                                     | x8                                    | x9                                  | xA                                    | xB                                  | xC                                    | xD                                  | xE                                  | xF                                  |
| 0x | [ADD](S1C88_ADD.md "wikilink") BA,BA      | [ADD](S1C88_ADD.md "wikilink") BA,HL      | [ADD](S1C88_ADD.md "wikilink") BA,IX      | [ADD](S1C88_ADD.md "wikilink") BA,IY      | [ADC](S1C88_ADC.md "wikilink") BA,BA      | [ADC](S1C88_ADC.md "wikilink") BA,HL      | [ADC](S1C88_ADC.md "wikilink") BA,IX      | [ADC](S1C88_ADC.md "wikilink") BA,IY      | [SUB](S1C88_SUB.md "wikilink") BA,BA     | [SUB](S1C88_SUB.md "wikilink") BA,HL   | [SUB](S1C88_SUB.md "wikilink") BA,IX     | [SUB](S1C88_SUB.md "wikilink") BA,IY   | [SBC](S1C88_SBC.md "wikilink") BA,BA     | [SBC](S1C88_SBC.md "wikilink") BA,HL   | [SBC](S1C88_SBC.md "wikilink") BA,IX   | [SBC](S1C88_SBC.md "wikilink") BA,IY   |
| 1x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        | [CP](S1C88_CP.md "wikilink") BA,BA       | [CP](S1C88_CP.md "wikilink") BA,HL     | [CP](S1C88_CP.md "wikilink") BA,IX       | [CP](S1C88_CP.md "wikilink") BA,IY     |                                       |                                     |                                     |                                     |
| 2x | [ADD](S1C88_ADD.md "wikilink") HL,BA      | [ADD](S1C88_ADD.md "wikilink") HL,HL      | [ADD](S1C88_ADD.md "wikilink") HL,IX      | [ADD](S1C88_ADD.md "wikilink") HL,IY      | [ADC](S1C88_ADC.md "wikilink") HL,BA      | [ADC](S1C88_ADC.md "wikilink") HL,HL      | [ADC](S1C88_ADC.md "wikilink") HL,IX      | [ADC](S1C88_ADC.md "wikilink") HL,IY      | [SUB](S1C88_SUB.md "wikilink") HL,BA     | [SUB](S1C88_SUB.md "wikilink") HL,HL   | [SUB](S1C88_SUB.md "wikilink") HL,IX     | [SUB](S1C88_SUB.md "wikilink") HL,IY   | [SBC](S1C88_SBC.md "wikilink") HL,BA     | [SBC](S1C88_SBC.md "wikilink") HL,HL   | [SBC](S1C88_SBC.md "wikilink") HL,IX   | [SBC](S1C88_SBC.md "wikilink") HL,IY   |
| 3x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        | [CP](S1C88_CP.md "wikilink") HL,BA       | [CP](S1C88_CP.md "wikilink") HL,HL     | [CP](S1C88_CP.md "wikilink") HL,IX       | [CP](S1C88_CP.md "wikilink") HL,IY     |                                       |                                     |                                     |                                     |
| 4x | [ADD](S1C88_ADD.md "wikilink") IX,BA      | [ADD](S1C88_ADD.md "wikilink") IX,HL      | [ADD](S1C88_ADD.md "wikilink") IY,BA      | [ADD](S1C88_ADD.md "wikilink") IY,HL      | [ADD](S1C88_ADD.md "wikilink") SP,BA      | [ADD](S1C88_ADD.md "wikilink") SP,HL      |                                        |                                        | [SUB](S1C88_SUB.md "wikilink") IX,BA     | [SUB](S1C88_SUB.md "wikilink") IX,HL   | [SUB](S1C88_SUB.md "wikilink") IY,BA     | [SUB](S1C88_SUB.md "wikilink") IY,HL   | [SUB](S1C88_SUB.md "wikilink") SP,BA     | [SUB](S1C88_SUB.md "wikilink") SP,HL   |                                     |                                     |
| 5x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     | [CP](S1C88_CP.md "wikilink") SP,BA       | [CP](S1C88_CP.md "wikilink") SP,HL     |                                     |                                     |
| 6x | [ADC](S1C88_ADC.md "wikilink") BA,\#mmnn  | [ADC](S1C88_ADC.md "wikilink") HL,\#mmnn  | [SBC](S1C88_SBC.md "wikilink") BA,\#mmnn  | [SBC](S1C88_SBC.md "wikilink") HL,\#mmnn  |                                        |                                        |                                        |                                        | [ADD](S1C88_ADD.md "wikilink") SP,\#mmnn |                                     | [SUB](S1C88_SUB.md "wikilink") SP,\#mmnn |                                     | [CP](S1C88_CP.md "wikilink") SP,\#mmnn   |                                     | [LD](S1C88_LD.md "wikilink") SP,\#mmnn |                                     |
| 7x | [LD](S1C88_LD.md "wikilink") BA,\[SP+dd\] | [LD](S1C88_LD.md "wikilink") HL,\[SP+dd\] | [LD](S1C88_LD.md "wikilink") IX,\[SP+dd\] | [LD](S1C88_LD.md "wikilink") IY,\[SP+dd\] | [LD](S1C88_LD.md "wikilink") \[SP+dd\],BA | [LD](S1C88_LD.md "wikilink") \[SP+dd\],HL | [LD](S1C88_LD.md "wikilink") \[SP+dd\],IX | [LD](S1C88_LD.md "wikilink") \[SP+dd\],IY | [LD](S1C88_LD.md "wikilink") SP,\[hhll\] |                                     |                                       |                                     | [LD](S1C88_LD.md "wikilink") \[hhll\],SP |                                     |                                     |                                     |
| 8x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| 9x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Ax |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Bx | [PUSH](S1C88_PUSH.md "wikilink") A        | [PUSH](S1C88_PUSH.md "wikilink") B        | [PUSH](S1C88_PUSH.md "wikilink") L        | [PUSH](S1C88_PUSH.md "wikilink") H        | [POP](S1C88_POP.md "wikilink") A          | [POP](S1C88_POP.md "wikilink") B          | [POP](S1C88_POP.md "wikilink") L          | [POP](S1C88_POP.md "wikilink") H          | [PUSH](S1C88_PUSH.md "wikilink") ALL     | [PUSH](S1C88_PUSH.md "wikilink") ALE   |                                       |                                     | [POP](S1C88_POP.md "wikilink") ALL       | [POP](S1C88_POP.md "wikilink") ALE     |                                     |                                     |
| Cx | [LD](S1C88_LD.md "wikilink") BA,\[HL\]    | [LD](S1C88_LD.md "wikilink") HL,\[HL\]    | [LD](S1C88_LD.md "wikilink") IX,\[HL\]    | [LD](S1C88_LD.md "wikilink") IY,\[HL\]    | [LD](S1C88_LD.md "wikilink") \[HL\],BA    | [LD](S1C88_LD.md "wikilink") \[HL\],HL    | [LD](S1C88_LD.md "wikilink") \[HL\],IX    | [LD](S1C88_LD.md "wikilink") \[HL\],IY    |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Dx | [LD](S1C88_LD.md "wikilink") BA,\[IX\]    | [LD](S1C88_LD.md "wikilink") HL,\[IX\]    | [LD](S1C88_LD.md "wikilink") IX,\[IX\]    | [LD](S1C88_LD.md "wikilink") IY,\[IX\]    | [LD](S1C88_LD.md "wikilink") \[IX\],BA    | [LD](S1C88_LD.md "wikilink") \[IX\],HL    | [LD](S1C88_LD.md "wikilink") \[IX\],IX    | [LD](S1C88_LD.md "wikilink") \[IX\],IY    | [LD](S1C88_LD.md "wikilink") BA,\[IY\]   | [LD](S1C88_LD.md "wikilink") HL,\[IY\] | [LD](S1C88_LD.md "wikilink") IX,\[IY\]   | [LD](S1C88_LD.md "wikilink") IY,\[IY\] | [LD](S1C88_LD.md "wikilink") \[IY\],BA   | [LD](S1C88_LD.md "wikilink") \[IY\],HL | [LD](S1C88_LD.md "wikilink") \[IY\],IX | [LD](S1C88_LD.md "wikilink") \[IY\],IY |
| Ex | [LD](S1C88_LD.md "wikilink") BA,BA        | [LD](S1C88_LD.md "wikilink") BA,HL        | [LD](S1C88_LD.md "wikilink") BA,IX        | [LD](S1C88_LD.md "wikilink") BA,IY        | [LD](S1C88_LD.md "wikilink") HL,BA        | [LD](S1C88_LD.md "wikilink") HL,HL        | [LD](S1C88_LD.md "wikilink") HL,IX        | [LD](S1C88_LD.md "wikilink") HL,IY        | [LD](S1C88_LD.md "wikilink") IX,BA       | [LD](S1C88_LD.md "wikilink") IX,HL     | [LD](S1C88_LD.md "wikilink") IX,IX       | [LD](S1C88_LD.md "wikilink") IX,IY     | [LD](S1C88_LD.md "wikilink") IY,BA       | [LD](S1C88_LD.md "wikilink") IY,HL     | [LD](S1C88_LD.md "wikilink") IY,IX     | [LD](S1C88_LD.md "wikilink") IY,IY     |
| Fx | [LD](S1C88_LD.md "wikilink") SP,BA        | [LD](S1C88_LD.md "wikilink") SP,HL        | [LD](S1C88_LD.md "wikilink") SP,IX        | [LD](S1C88_LD.md "wikilink") SP,IY        | [LD](S1C88_LD.md "wikilink") HL,SP        | [LD](S1C88_LD.md "wikilink") HL,PC        |                                        |                                        | [LD](S1C88_LD.md "wikilink") BA,SP       | [LD](S1C88_LD.md "wikilink") BA,PC     | [LD](S1C88_LD.md "wikilink") IX,SP       |                                     |                                       |                                     | [LD](S1C88_LD.md "wikilink") IY,SP     |                                     |
|    |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |

# Illegal Instructions

**NOTE: This document is now out of date, as should be updated to the
new mnemonic and register naming**

The entire opcode table has been evaluated on Pokemon Mini units and new
and exotic illegal opcodes have been found.

These opcodes are not officially supported (they are not used by
commercial games and not even found in the Pokemon Channel emulator) and
can produce random results or crashes in some cases. The illegal opcodes
have been documented on [this page's Discussion
page](Talk:PM_InstructionList.md "wikilink"). ''' THIS PAGE IS IN PROCESS
'''