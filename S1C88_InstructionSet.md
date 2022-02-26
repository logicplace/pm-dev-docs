# S1C88 Instruction Set

## 8-bit arithmetic and logic operation

### **ADD**: Addition

| Mnemonic              | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [ADD][+] A,A          | 00           | A ← A + A             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,B          | 01           | A ← A + B             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,#nn        | 02,nn        | A ← A + nn            |      2 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[HL]      | 03           | A ← A + \[HL]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[BR:ll]   | 04,ll        | A ← A + \[BR:ll]      |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[hhll]    | 05,ll,hh     | A ← A + \[hhll]       |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IX]      | 06           | A ← A + \[IX]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IY]      | 07           | A ← A + \[IY]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IX+dd]   | CE,00,dd     | A ← A + \[IX+dd]      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IY+dd]   | CE,01,dd     | A ← A + \[IY+dd]      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IX+L]    | CE,02        | A ← A + \[IX+L]       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] A,\[IY+L]    | CE,03        | A ← A + \[IY+L]       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] \[HL],A      | CE,04        | \[HL] ← \[HL] + A     |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] \[HL],#nn    | CE,05,nn     | \[HL] ← \[HL] + nn    |      5 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] \[HL],\[IX]  | CE,06        | \[HL] ← \[HL] + \[IX] |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADD][+] \[HL],\[IY]  | CE,07        | \[HL] ← \[HL] + \[IY] |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |

[+]: S1C88_ADD.md "wikilink"

### **ADC**: Addition with carry

| Mnemonic               | Machine Code | Operation                 | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------------------- | ------------ | ------------------------- | ------:| -----:|:------------------------:|
| [ADC][+c] A,A          | 08           | A ← A + A + C             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,B          | 09           | A ← A + B + C             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,#nn        | 0A,nn        | A ← A + nn + C            |      2 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[HL]      | 0B           | A ← A + \[HL] + C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[BR:ll]   | 0C,ll        | A ← A + \[BR:ll] + C      |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[hhll]    | 0D,ll,hh     | A ← A + \[hhll] + C       |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IX]      | 0E           | A ← A + \[IX] + C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IY]      | 0F           | A ← A + \[IY] + C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IX+dd]   | CE,08,dd     | A ← A + \[IX+dd] + C      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IY+dd]   | CE,09,dd     | A ← A + \[IY+dd] + C      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IX+L]    | CE,0A        | A ← A + \[IX+L] + C       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] A,\[IY+L]    | CE,0B        | A ← A + \[IY+L] + C       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] \[HL],A      | CE,0C        | \[HL] ← \[HL] + A + C     |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] \[HL],#nn    | CE,0D,nn     | \[HL] ← \[HL] + nn + C    |      5 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] \[HL],\[IX]  | CE,0E        | \[HL] ← \[HL] + \[IX] + C |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [ADC][+c] \[HL],\[IY]  | CE,0F        | \[HL] ← \[HL] + \[IY] + C |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |

[+c]: S1C88_ADC.md "wikilink"

### **SUB**: Subtraction

| Mnemonic                | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [SUB][-] A,A          | 10           | A ← A - A             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,B          | 11           | A ← A - B             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,#nn        | 12,nn        | A ← A - nn            |      2 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[HL]      | 13           | A ← A - \[HL]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[BR:ll]   | 14,ll        | A ← A - \[BR:ll]      |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[hhll]    | 15,ll,hh     | A ← A - \[hhll]       |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IX]      | 16           | A ← A - \[IX]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IY]      | 17           | A ← A - \[IY]         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IX+dd]   | CE,10,dd     | A ← A - \[IX+dd]      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IY+dd]   | CE,11,dd     | A ← A - \[IY+dd]      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IX+L]    | CE,12        | A ← A - \[IX+L]       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] A,\[IY+L]    | CE,13        | A ← A - \[IY+L]       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] \[HL],A      | CE,14        | \[HL] ← \[HL] - A     |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] \[HL],#nn    | CE,15,nn     | \[HL] ← \[HL] - nn    |      5 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] \[HL],\[IX]  | CE,16        | \[HL] ← \[HL] - \[IX] |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SUB][-] \[HL],\[IY]  | CE,17        | \[HL] ← \[HL] - \[IY] |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |

[-]: S1C88_SUB.md "wikilink"

### **SBC**: Subtraction with carry

| Mnemonic                | Machine Code | Operation                 | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------------- | ------------ | ------------------------- | ------:| -----:|:------------------------:|
| [SBC][-c] A,A          | 18           | A ← A - A - C             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,B          | 19           | A ← A - B - C             |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,#nn        | 1A,nn        | A ← A - nn - C            |      2 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[HL]      | 1B           | A ← A - \[HL] - C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[BR:ll]   | 1C,ll        | A ← A - \[BR:ll] - C      |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[hhll]    | 1D,ll,hh     | A ← A - \[hhll] - C       |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IX]      | 1E           | A ← A - \[IX] - C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IY]      | 1F           | A ← A - \[IY] - C         |      2 |     1 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IX+dd]   | CE,18,dd     | A ← A - \[IX+dd] - C      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IY+dd]   | CE,19,dd     | A ← A - \[IY+dd] - C      |      4 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IX+L]    | CE,1A        | A ← A - \[IX+L] - C       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] A,\[IY+L]    | CE,1B        | A ← A - \[IY+L] - C       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] \[HL],A      | CE,1C        | \[HL] ← \[HL] - A - C     |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] \[HL],#nn    | CE,1D,nn     | \[HL] ← \[HL] - nn - C    |      5 |     3 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] \[HL],\[IX]  | CE,1E        | \[HL] ← \[HL] - \[IX] - C |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [SBC][-c] \[HL],\[IY]  | CE,1F        | \[HL] ← \[HL] - \[IY] - C |      5 |     2 |        `– – * * ↕ ↕ ↕ ↕` |

[-c]: S1C88_SBC.md "wikilink"

### **AND**: Logical product

| Mnemonic              | Machine Code | Operation                | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | ------------------------ | ------:| -----:|:------------------------:|
| [AND][&] A,A          | 20           | A ← A & A                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [AND][&] A,B          | 21           | A ← A & B                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [AND][&] A,#nn        | 22,nn        | A ← A & nn               |      2 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[HL]      | 23           | A ← A & \[HL]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[BR:ll]   | 24,ll        | A ← A & \[BR:ll]         |      3 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[hhll]    | 25,ll,hh     | A ← A & \[hhll]          |      4 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IX]      | 26           | A ← A & \[IX]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IY]      | 27           | A ← A & \[IY]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IX+dd]   | CE,20,dd     | A ← A & \[IX+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IY+dd]   | CE,21,dd     | A ← A & \[IY+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IX+L]    | CE,22        | A ← A & \[IX+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] A,\[IY+L]    | CE,23        | A ← A & \[IY+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] B,#nn        | CE,B0,nn     | B ← B & nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] H,#nn        | CE,B2,nn     | H ← H & nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] \[BR:ll],#nn | D8,ll,nn     | \[BR:ll] ← \[BR:ll] & nn |      5 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] \[HL],A      | CE,24        | \[HL] ← \[HL] & A        |      4 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] \[HL],#nn    | CE,25,nn     | \[HL] ← \[HL] & nn       |      5 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] \[HL],\[IX]  | CE,26        | \[HL] ← \[HL] & \[IX]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] \[HL],\[IY]  | CE,27        | \[HL] ← \[HL] & \[IY]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [AND][&] L,#nn        | CE,B1,nn     | L ← L & nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [AND][&] SC,#nn       | 9C,nn        | SC ← SC & nn             |      3 |     2 |        `↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓` |

[&]: S1C88_AND.md "wikilink"

### **OR**: Logical sum

| Mnemonic               | Machine Code | Operation                 | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------------------- | ------------ | ------------------------- | ------:| -----:|:------------------------:|
| [OR][or] A,A           | 28           | A ← A \| A                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [OR][or] A,B           | 29           | A ← A \| B                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [OR][or] A,#nn         | 2A,nn        | A ← A \| nn               |      2 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[HL]       | 2B           | A ← A \| \[HL]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[BR:ll]    | 2C,ll        | A ← A \| \[BR:ll]         |      3 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[hhll]     | 2D,ll,hh     | A ← A \| \[hhll]          |      4 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IX]       | 2E           | A ← A \| \[IX]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IY]       | 2F           | A ← A \| \[IY]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IX+dd]    | CE,28,dd     | A ← A \| \[IX+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IY+dd]    | CE,29,dd     | A ← A \| \[IY+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IX+L]     | CE,2A        | A ← A \| \[IX+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] A,\[IY+L]     | CE,2B        | A ← A \| \[IY+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] B,#nn         | CE,B4,nn     | B ← B \| nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] H,#nn         | CE,B6,nn     | H ← H \| nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] \[BR:ll],#nn  | D9,ll,nn     | \[BR:ll] ← \[BR:ll] \| nn |      5 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] \[HL],A       | CE,2C        | \[HL] ← \[HL] \| A        |      4 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] \[HL],#nn     | CE,2D,nn     | \[HL] ← \[HL] \| nn       |      5 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] \[HL],\[IX]   | CE,2E        | \[HL] ← \[HL] \| \[IX]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] \[HL],\[IY]   | CE,2F        | \[HL] ← \[HL] \| \[IY]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [OR][or] L,#nn         | CE,B5,nn     | L ← L \| nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [OR][or] SC,#nn        | 9D,nn        | SC ← SC \| nn             |      3 |     2 |        `↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑` |

[or]: S1C88_OR.md "wikilink"

### **XOR**: Exclusive OR

| Mnemonic               | Machine Code | Operation                | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------------------- | ------------ | ------------------------ | ------:| -----:|:------------------------:|
| [XOR][^] A,A           | 38           | A ← A ^ A                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,B           | 39           | A ← A ^ B                |      2 |     1 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,#nn         | 3A,nn        | A ← A ^ nn               |      2 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[HL]       | 3B           | A ← A ^ \[HL]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[BR:ll]    | 3C,ll        | A ← A ^ \[BR:ll]         |      3 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[hhll]     | 3D,ll,hh     | A ← A ^ \[hhll]          |      4 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IX]       | 3E           | A ← A ^ \[IX]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IY]       | 3F           | A ← A ^ \[IY]            |      2 |     1 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IX+dd]    | CE,38,dd     | A ← A ^ \[IX+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IY+dd]    | CE,39,dd     | A ← A ^ \[IY+dd]         |      4 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IX+L]     | CE,3A        | A ← A ^ \[IX+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] A,\[IY+L]     | CE,3B        | A ← A ^ \[IY+L]          |      4 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] B,#nn         | CE,B8,nn     | B ← B ^ nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] H,#nn         | CE,BA,nn     | H ← H ^ nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] \[BR:ll],#nn  | DA,ll,nn     | \[BR:ll] ← \[BR:ll] ^ nn |      5 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] \[HL],A       | CE,3C        | \[HL] ← \[HL] ^ A        |      4 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] \[HL],#nn     | CE,3D,nn     | \[HL] ← \[HL] ^ nn       |      5 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] \[HL],\[IX]   | CE,3E        | \[HL] ← \[HL] ^ \[IX]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] \[HL],\[IY]   | CE,3F        | \[HL] ← \[HL] ^ \[IY]    |      5 |     2 |        `– – – – ↕ – – ↕` |
| [XOR][^] L,#nn         | CE,B9,nn     | L ← L ^ nn               |      3 |     3 |        `– – – – ↕ – – ↕` |
| [XOR][^] SC,#nn        | 9E,nn        | SC ← SC ^ nn             |      3 |     2 |        `↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕` |

[^]: S1C88_XOR.md "wikilink"

### **CP**: Comparison

| Mnemonic               | Machine Code | Operation     | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------------------- | ------------ | ------------- | ------:| -----:|:------------------------:|
| [CP][cp] A,A           | 30           | A - A         |      2 |     1 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,B           | 31           | A - B         |      2 |     1 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,#nn         | 32,nn        | A - nn        |      2 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[HL]       | 33           | A - \[HL]     |      2 |     1 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[BR:ll]    | 34,ll        | A - \[BR:ll]  |      3 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[hhll]     | 35,ll,hh     | A - \[hhll]   |      4 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IX]       | 36           | A - \[IX]     |      2 |     1 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IY]       | 37           | A - \[IY]     |      2 |     1 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IX+dd]    | CE,30,dd     | A - \[IX+dd]  |      4 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IY+dd]    | CE,31,dd     | A - \[IY+dd]  |      4 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IX+L]     | CE,32        | A - \[IX+L]   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] A,\[IY+L]     | CE,33        | A - \[IY+L]   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] B,#nn         | CE,BC,nn     | B - nn        |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] H,#nn         | CE,BE,nn     | H - nn        |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] BR,#hh        | CE,BF,hh     | BR - hh       |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] \[BR:ll],#nn  | DB,ll,nn     | \[BR:ll] - nn |      4 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] \[HL],A       | CE,34        | \[HL] - A     |      3 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] \[HL],#nn     | CE,35,nn     | \[HL] - nn    |      4 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] \[HL],\[IX]   | CE,36        | \[HL] - \[IX] |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] \[HL],\[IY]   | CE,37        | \[HL] - \[IY] |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] L,#nn         | CE,BD,nn     | L - nn        |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |

[cp]: S1C88_CP.md "wikilink"

### **BIT**: Bit test

| Mnemonic                | Machine Code | Operation     | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------------- | ------------ | ------------- | ------:| -----:|:------------------------:|
| [BIT][bt] A,B           | 94           | A & B         |      2 |     1 |        `– – – – ↕ – – ↕` |
| [BIT][bt] A,#nn         | 96,nn        | A & nn        |      2 |     2 |        `– – – – ↕ – – ↕` |
| [BIT][bt] B,#nn         | 97,nn        | B & nn        |      2 |     2 |        `– – – – ↕ – – ↕` |
| [BIT][bt] \[HL],#nn     | 95,nn        | \[HL] & nn    |      3 |     2 |        `– – – – ↕ – – ↕` |
| [BIT][bt] \[BR:ll],#nn  | DC,ll,nn     | \[BR:ll] & nn |      4 |     3 |        `– – – – ↕ – – ↕` |

[bt]: S1C88_BIT.md "wikilink"

### **INC**: Increment by 1

| Mnemonic            | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [INC][++] A         | 80           | A ← A + 1               |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] B         | 81           | B ← B + 1               |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] H         | 83           | H ← H + 1               |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] \[BR:ll]  | 85,ll        | \[BR:ll] ← \[BR:ll] + 1 |      4 |     2 |        `– – – – – – – ↕` |
| [INC][++] \[HL]     | 86           | \[HL] ← \[HL] + 1       |      3 |     1 |        `– – – – – – – ↕` |
| [INC][++] L         | 82           | L ← L + 1               |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] BR        | 84           | BR ← BR + 1             |      2 |     1 |        `– – – – – – – ↕` |

[++]: S1C88_INC.md "wikilink"

### **DEC**: Decrement by 1

| Mnemonic            | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [DEC][--] A         | 88           | A ← A - 1               |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] B         | 89           | B ← B - 1               |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] H         | 8B           | H ← H - 1               |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] \[BR:ll]  | 8D,ll        | \[BR:ll] ← \[BR:ll] - 1 |      4 |     2 |        `– – – – – – – ↕` |
| [DEC][--] \[HL]     | 8E           | \[HL] ← \[HL] - 1       |      3 |     1 |        `– – – – – – – ↕` |
| [DEC][--] L         | 8A           | L ← L - 1               |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] BR        | 8C           | BR ← BR - 1             |      2 |     1 |        `– – – – – – – ↕` |

[--]: S1C88_DEC.md "wikilink"

### **MLT**: Multiplication

| Mnemonic  | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [MLT][*]  | CE,D8        | HL ← L * A            |     12 |     2 |        `– – – – ↕ 0 0 ↕` |

[*]: S1C88_MLT.md "wikilink"

### **DIV**: Division

| Mnemonic  | Machine Code | Operation              | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------- | ------------ | ---------------------- | ------:| -----:|:------------------------:|
| [DIV][/]  | CE,D9        | L ← HL / A, H ← HL % A |     12 |     2 |        `– – – – ↕ ↕ 0 ↕` |

[/]: S1C88_DIV.md "wikilink"

### **CPL**: Complement of 1

| Mnemonic           | Machine Code | Operation            | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | -------------------- | ------:| -----:|:------------------------:|
| [CPL][~] A         | CE,A0        | A ← ~A               |      3 |     2 |        `– – – – ↕ – – ↕` |
| [CPL][~] B         | CE,A1        | B ← ~B               |      3 |     2 |        `– – – – ↕ – – ↕` |
| [CPL][~] \[HL]     | CE,A3        | \[HL] ← ~\[HL]       |      4 |     2 |        `– – – – ↕ – – ↕` |
| [CPL][~] \[BR:ll]  | CE,A2,ll     | \[BR:ll] ← ~\[BR:ll] |      5 |     3 |        `– – – – ↕ – – ↕` |

[~]: S1C88_CPL.md "wikilink"

### **NEG**: Complement of 2

| Mnemonic            | Machine Code | Operation            | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | -------------------- | ------:| -----:|:------------------------:|
| [NEG][ng] A         | CE,A4        | A ← -A               |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [NEG][ng] B         | CE,A5        | B ← -B               |      3 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [NEG][ng] \[HL]     | CE,A7        | \[HL] ← -\[HL]       |      4 |     2 |        `– – * * ↕ ↕ ↕ ↕` |
| [NEG][ng] \[BR:ll]  | CE,A6,ll     | \[BR:ll] ← -\[BR:ll] |      5 |     3 |        `– – * * ↕ ↕ ↕ ↕` |

[ng]: S1C88_NEG.md "wikilink"

## 8-bit transfer

### **LD**: Load

| Mnemonic                | Machine Code | Operation        | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------------- | ------------ | ---------------- | ------:| -----:|:------------------------:|
| [LD][=] A,A             | 40           | A ← A            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] A,B             | 41           | A ← B            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] A,L             | 42           | A ← L            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] A,H             | 43           | A ← H            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] A,\[BR:ll]      | 44,ll        | A ← \[BR:ll]     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] A,\[HL]         | 45           | A ← \[HL]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] A,\[IX]         | 46           | A ← \[IX]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] A,\[IY]         | 47           | A ← \[IY]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] A,#nn           | B0,nn        | A ← nn           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,\[IX+dd]      | CE,40,dd     | A ← \[IX+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] A,\[IY+dd]      | CE,41,dd     | A ← \[IY+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] A,\[IX+L]       | CE,42        | A ← \[IX+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] A,\[IY+L]       | CE,43        | A ← \[IY+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] A,BR            | CE,C0        | A ← BR           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,SC            | CE,C1        | A ← SC           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,NB            | CE,C8        | A ← NB           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,EP            | CE,C9        | A ← EP           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,XP            | CE,CA        | A ← XP           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,YP            | CE,CB        | A ← YP           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] A,\[hhll]       | CE,D0,ll,hh  | A ← \[hhll]      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] B,A             | 48           | B ← A            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] B,B             | 49           | B ← B            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] B,L             | 4A           | B ← L            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] B,H             | 4B           | B ← H            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] B,\[BR:ll]      | 4C,ll        | B ← \[BR:ll]     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] B,\[HL]         | 4D           | B ← \[HL]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] B,\[IX]         | 4E           | B ← \[IX]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] B,\[IY]         | 4F           | B ← \[IY]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] B,#nn           | B1,nn        | B ← nn           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] B,\[IX+dd]      | CE,48,dd     | B ← \[IX+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] B,\[IY+dd]      | CE,49,dd     | B ← \[IY+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] B,\[IX+L]       | CE,4A        | B ← \[IX+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] B,\[IY+L]       | CE,4B        | B ← \[IY+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] B,\[hhll]       | CE,D1,ll,hh  | B ← \[hhll]      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] L,A             | 50           | L ← A            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] L,B             | 51           | L ← B            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] L,L             | 52           | L ← L            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] L,H             | 53           | L ← H            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] L,\[BR:ll]      | 54,ll        | L ← \[BR:ll]     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] L,\[HL]         | 55           | L ← \[HL]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] L,\[IX]         | 56           | L ← \[IX]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] L,\[IY]         | 57           | L ← \[IY]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] L,#nn           | B2,nn        | L ← nn           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] L,\[IX+dd]      | CE,50,dd     | L ← \[IX+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] L,\[IY+dd]      | CE,51,dd     | L ← \[IY+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] L,\[IX+L]       | CE,52        | L ← \[IX+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] L,\[IY+L]       | CE,53        | L ← \[IY+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] L,\[hhll]       | CE,D2,ll,hh  | L ← \[hhll]      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] H,A             | 58           | H ← A            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] H,B             | 59           | H ← B            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] H,L             | 5A           | H ← L            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] H,H             | 5B           | H ← H            |      1 |     1 |        `– – – – – – – –` |
| [LD][=] H,\[BR:ll]      | 5C,ll        | H ← \[BR:ll]     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] H,\[HL]         | 5D           | H ← \[HL]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] H,\[IX]         | 5E           | H ← \[IX]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] H,\[IY]         | 5F           | H ← \[IY]        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] H,#nn           | B3,nn        | H ← nn           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] H,\[IX+dd]      | CE,58,dd     | H ← \[IX+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] H,\[IY+dd]      | CE,59,dd     | H ← \[IY+dd]     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] H,\[IX+L]       | CE,5A        | H ← \[IX+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] H,\[IY+L]       | CE,5B        | H ← \[IY+L]      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] H,\[hhll]       | CE,D3,ll,hh  | H ← \[hhll]      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] BR,#hh          | B4,hh        | BR ← hh          |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BR,A            | CE,C2        | BR ← A           |      2 |     2 |        `– – – – – – – –` |
| [LD][=] SC,#nn          | 9F,nn        | SC ← nn          |      3 |     2 |        `↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕` |
| [LD][=] SC,A            | CE,C3        | SC ← A           |      3 |     2 |        `↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕` |
| [LD][=] NB,#bb          | CE,C4,bb     | NB ← bb          |      3 |     3 |        `– – – – – – – –` |
| [LD][=] NB,A            | CE,CC        | NB ← A           |      4 |     2 |        `– – – – – – – –` |
| [LD][=] EP,#pp          | CE,C5,pp     | EP ← pp          |      2 |     3 |        `– – – – – – – –` |
| [LD][=] EP,A            | CE,CD        | EP ← A           |      3 |     2 |        `– – – – – – – –` |
| [LD][=] XP,#pp          | CE,C6,pp     | XP ← pp          |      2 |     3 |        `– – – – – – – –` |
| [LD][=] XP,A            | CE,CE        | XP ← A           |      3 |     2 |        `– – – – – – – –` |
| [LD][=] YP,#pp          | CE,C7,pp     | YP ← pp          |      2 |     3 |        `– – – – – – – –` |
| [LD][=] YP,A            | CE,CF        | YP ← A           |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],A      | 78,ll        | \[BR:ll] ← A     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],B      | 79,ll        | \[BR:ll] ← B     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],L      | 7A,ll        | \[BR:ll] ← L     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],H      | 7B,ll        | \[BR:ll] ← H     |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],\[HL]  | 7D,ll        | \[BR:ll] ← \[HL] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],\[IX]  | 7E,ll        | \[BR:ll] ← \[IX] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],\[IY]  | 7F,ll        | \[BR:ll] ← \[IY] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[BR:ll],#nn    | DD,ll,nn     | \[BR:ll] ← nn    |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[hhll],A       | CE,D4,ll,hh  | \[hhll] ← A      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] \[hhll],B       | CE,D5,ll,hh  | \[hhll] ← B      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] \[hhll],L       | CE,D6,ll,hh  | \[hhll] ← L      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] \[hhll],H       | CE,D7,ll,hh  | \[hhll] ← H      |      5 |     4 |        `– – – – – – – –` |
| [LD][=] \[HL],A         | 68           | \[HL] ← A        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],B         | 69           | \[HL] ← B        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],L         | 6A           | \[HL] ← L        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],H         | 6B           | \[HL] ← H        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],\[BR:ll]  | 6C,ll        | \[HL] ← \[BR:ll] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],\[HL]     | 6D           | \[HL] ← \[HL]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IX]     | 6E           | \[HL] ← \[IX]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IY]     | 6F           | \[HL] ← \[IY]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[HL],#nn       | B5,nn        | \[HL] ← nn       |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IX+dd]  | CE,60,dd     | \[HL] ← \[IX+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IY+dd]  | CE,61,dd     | \[HL] ← \[IY+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IX+L]   | CE,62        | \[HL] ← \[IX+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],\[IY+L]   | CE,63        | \[HL] ← \[IY+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],A         | 60           | \[IX] ← A        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],B         | 61           | \[IX] ← B        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],L         | 62           | \[IX] ← L        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],H         | 63           | \[IX] ← H        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],\[BR:ll]  | 64,ll        | \[IX] ← \[BR:ll] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],\[HL]     | 65           | \[IX] ← \[HL]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IX]     | 66           | \[IX] ← \[IX]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IY]     | 67           | \[IX] ← \[IY]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IX],#nn       | B6,nn        | \[IX] ← nn       |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IX+dd]  | CE,68,dd     | \[IX] ← \[IX+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IY+dd]  | CE,69,dd     | \[IX] ← \[IY+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IX+L]   | CE,6A        | \[IX] ← \[IX+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],\[IY+L]   | CE,6B        | \[IX] ← \[IY+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],A         | 70           | \[IY] ← A        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],B         | 71           | \[IY] ← B        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],L         | 72           | \[IY] ← L        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],H         | 73           | \[IY] ← H        |      2 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],\[BR:ll]  | 74,ll        | \[IY] ← \[BR:ll] |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],\[HL]     | 75           | \[IY] ← \[HL]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IX]     | 76           | \[IY] ← \[IX]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IY]     | 77           | \[IY] ← \[IY]    |      3 |     1 |        `– – – – – – – –` |
| [LD][=] \[IY],#nn       | B7,nn        | \[IY] ← nn       |      3 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IX+dd]  | CE,78,dd     | \[IY] ← \[IX+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IY+dd]  | CE,79,dd     | \[IY] ← \[IY+dd] |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IX+L]   | CE,7A        | \[IY] ← \[IX+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],\[IY+L]   | CE,7B        | \[IY] ← \[IY+L]  |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX+dd],A      | CE,44,dd     | \[IX+dd] ← A     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX+dd],B      | CE,4C,dd     | \[IX+dd] ← B     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX+dd],L      | CE,54,dd     | \[IX+dd] ← L     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX+dd],H      | CE,5C,dd     | \[IX+dd] ← H     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY+dd],A      | CE,45,dd     | \[IY+dd] ← A     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY+dd],B      | CE,4D,dd     | \[IY+dd] ← B     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY+dd],L      | CE,55,dd     | \[IY+dd] ← L     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IY+dd],H      | CE,5D,dd     | \[IY+dd] ← H     |      4 |     3 |        `– – – – – – – –` |
| [LD][=] \[IX+L],A       | CE,46        | \[IX+L] ← A      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX+L],B       | CE,4E        | \[IX+L] ← B      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX+L],L       | CE,56        | \[IX+L] ← L      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX+L],H       | CE,5E        | \[IX+L] ← H      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY+L],A       | CE,47        | \[IY+L] ← A      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY+L],B       | CE,4F        | \[IY+L] ← B      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY+L],L       | CE,57        | \[IY+L] ← L      |      4 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY+L],H       | CE,5F        | \[IY+L] ← H      |      4 |     2 |        `– – – – – – – –` |

[=]: S1C88_LD.md "wikilink"

### **EX**: Byte exchange

| Mnemonic          | Machine Code | Operation | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------- | ------------ | --------- | ------:| -----:|:------------------------:|
| [EX][ex] A,B      | CC           | A ↔ B     |      2 |     1 |        `– – – – – – – –` |
| [EX][ex] A,\[HL]  | CD           | A ↔ \[HL] |      3 |     1 |        `– – – – – – – –` |

[ex]: S1C88_EX.md "wikilink"

### **SWAP**: Nibble exchange

| Mnemonic          | Machine Code | Operation                    | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------- | ------------ | ---------------------------- | ------:| -----:|:------------------------:|
| [SWAP][sw] A      | F6           | ![swap nibbles in A][sw1]    |      2 |     1 |        `– – – – – – – –` |
| [SWAP][sw] \[HL]  | F7           | ![swap nibbles in [HL]][sw2] |      3 |     1 |        `– – – – – – – –` |

[sw]: S1C88_SWAP.md "wikilink"
[sw1]: /rsc/op-swap-a.svg "swap nibbles in A"
[sw2]: /rsc/op-swap-phl.svg "swap nibbles in \[HL\]"

## Rotate/shift

### **RL**: Rotate to left with carry

| Mnemonic          | Machine Code | Operation                         | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------- | ------------ | --------------------------------- | ------:| -----:|:------------------------:|
| [RL][(] A         | CE,90        | ![rotate A left thru C][(1]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RL][(] B         | CE,91        | ![rotate B left thru C][(2]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RL][(] \[HL]     | CE,93        | ![rotate [HL] left thru C][(3]    |      4 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RL][(] \[BR:ll]  | CE,92,ll     | ![rotate [BR:ll] left thru C][(4] |      5 |     3 |        `– – – – ↕ – ↕ ↕` |

[(]: S1C88_RL.md "wikilink"
[(1]: /rsc/op-rl-a.svg "rotate A left thru C"
[(2]: /rsc/op-rl-b.svg "rotate B left thru C"
[(3]: /rsc/op-rl-phl.svg "rotate [HL] left thru C"
[(4]: /rsc/op-rl-pbrll.svg "rotate [BR:ll] left thru C"

### **RLC**: Rotate to left

| Mnemonic            | Machine Code | Operation                             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ------------------------------------- | ------:| -----:|:------------------------:|
| [RLC][(c] A         | CE,94        | ![rotate A left and set C][(c1]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RLC][(c] B         | CE,95        | ![rotate B left and set C][(c2]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RLC][(c] \[HL]     | CE,97        | ![rotate [HL] left and set C][(c3]    |      4 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RLC][(c] \[BR:ll]  | CE,96,ll     | ![rotate [BR:ll] left and set C][(c4] |      5 |     3 |        `– – – – ↕ – ↕ ↕` |

[(c]: S1C88_RLC.md "wikilink"
[(c1]: /rsc/op-rlc-a.svg "rotate A left and set C"
[(c2]: /rsc/op-rlc-b.svg "rotate B left and set C"
[(c3]: /rsc/op-rlc-phl.svg "rotate [HL] left and set C"
[(c4]: /rsc/op-rlc-pbrll.svg "rotate [BR:ll] left and set C"

### **RR**: Rotate to right with carry

| Mnemonic          | Machine Code | Operation                          | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------- | ------------ | ---------------------------------- | ------:| -----:|:------------------------:|
| [RR][)] A         | CE,98        | ![rotate A right thru C][)1]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RR][)] B         | CE,99        | ![rotate B right thru C][)2]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RR][)] \[HL]     | CE,9B        | ![rotate [HL] right thru C][)3]    |      4 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RR][)] \[BR:ll]  | CE,9A,ll     | ![rotate [BR:ll] right thru C][)4] |      5 |     3 |        `– – – – ↕ – ↕ ↕` |

[)]: S1C88_RR.md "wikilink"
[)1]: /rsc/op-rr-a.svg "rotate A right thru C"
[)2]: /rsc/op-rr-b.svg "rotate B right thru C"
[)3]: /rsc/op-rr-phl.svg "rotate [HL] right thru C"
[)4]: /rsc/op-rr-pbrll.svg "rotate [BR:ll] right thru C"

### **RRC**: Rotate to right

| Mnemonic            | Machine Code | Operation                              | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | -------------------------------------- | ------:| -----:|:------------------------:|
| [RRC][)c] A         | CE,9C        | ![rotate A right and set C][)c1]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RRC][)c] B         | CE,9D        | ![rotate B right and set C][)c2]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RRC][)c] \[HL]     | CE,9F        | ![rotate [HL] right and set C][)c3]    |      4 |     2 |        `– – – – ↕ – ↕ ↕` |
| [RRC][)c] \[BR:ll]  | CE,9E,ll     | ![rotate [BR:ll] right and set C][)c4] |      5 |     3 |        `– – – – ↕ – ↕ ↕` |

[)c]: S1C88_RRC.md "wikilink"
[)c1]: /rsc/op-rrc-a.svg "rotate A right and set C"
[)c2]: /rsc/op-rrc-b.svg "rotate B right and set C"
[)c3]: /rsc/op-rrc-phl.svg "rotate [HL] right and set C"
[)c4]: /rsc/op-rrc-pbrll.svg "rotate [BR:ll] right and set C"

### **SLA**: Arithmetic shift to left

| Mnemonic            | Machine Code | Operation                             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ------------------------------------- | ------:| -----:|:------------------------:|
| [SLA][«<] A         | CE,80        | ![arithmetic shift A left][«<1]       |      3 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SLA][«<] B         | CE,81        | ![arithmetic shift B left][«<2]       |      3 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SLA][«<] \[HL]     | CE,83        | ![arithmetic shift [HL] left][«<3]    |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SLA][«<] \[BR:ll]  | CE,82,ll     | ![arithmetic shift [BR:ll] left][«<4] |      5 |     3 |        `– – – – ↕ ↕ ↕ ↕` |

[«<]: S1C88_SLA.md "wikilink"
[«<1]: /rsc/op-sll-a.svg "arithmetic shift A left"
[«<2]: /rsc/op-sll-b.svg "arithmetic shift B left"
[«<3]: /rsc/op-sll-phl.svg "arithmetic shift [HL] left"
[«<4]: /rsc/op-sll-pbrll.svg "arithmetic shift [BR:ll] left"

### **SLL**: Logical shift to left

| Mnemonic           | Machine Code | Operation                         | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | --------------------------------- | ------:| -----:|:------------------------:|
| [SLL][«] A         | CE,84        | ![logical shift A left][«1]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [SLL][«] B         | CE,85        | ![logical shift B left][«2]       |      3 |     2 |        `– – – – ↕ – ↕ ↕` |
| [SLL][«] \[HL]     | CE,87        | ![logical shift [HL] left][«3]    |      4 |     2 |        `– – – – ↕ – ↕ ↕` |
| [SLL][«] \[BR:ll]  | CE,86,ll     | ![logical shift [BR:ll] left][«4] |      5 |     3 |        `– – – – ↕ – ↕ ↕` |

[«]: S1C88_SLL.md "wikilink"
[«1]: /rsc/op-sll-a.svg "logical shift A left"
[«2]: /rsc/op-sll-b.svg "logical shift B left"
[«3]: /rsc/op-sll-phl.svg "logical shift [HL] left"
[«4]: /rsc/op-sll-pbrll.svg "logical shift [BR:ll] left"

### **SRA**: Arithmetic shift to right

| Mnemonic            | Machine Code | Operation                              | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | -------------------------------------- | ------:| -----:|:------------------------:|
| [SRA][»>] A         | CE,88        | ![arithmetic shift A right][»>1]       |      3 |     2 |        `– – – – ↕ 0 ↕ ↕` |
| [SRA][»>] B         | CE,89        | ![arithmetic shift B right][»>2]       |      3 |     2 |        `– – – – ↕ 0 ↕ ↕` |
| [SRA][»>] \[HL]     | CE,8B        | ![arithmetic shift [HL] right][»>3]    |      4 |     2 |        `– – – – ↕ 0 ↕ ↕` |
| [SRA][»>] \[BR:ll]  | CE,8A,ll     | ![arithmetic shift [BR:ll] right][»>4] |      5 |     3 |        `– – – – ↕ 0 ↕ ↕` |

[»>]: S1C88_SRA.md "wikilink"
[»>1]: /rsc/op-sra-a.svg "arithmetic shift A right"
[»>2]: /rsc/op-sra-b.svg "arithmetic shift B right"
[»>3]: /rsc/op-sra-phl.svg "arithmetic shift [HL] right"
[»>4]: /rsc/op-sra-pbrll.svg "arithmetic shift [BR:ll] right"

### **SRL**: Logical shift to right

| Mnemonic           | Machine Code | Operation                          | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | ---------------------------------- | ------:| -----:|:------------------------:|
| [SRL][»] A         | CE,8C        | ![logical shift A right][»1]       |      3 |     2 |        `– – – – 0 – ↕ ↕` |
| [SRL][»] B         | CE,8D        | ![logical shift B right][»2]       |      3 |     2 |        `– – – – 0 – ↕ ↕` |
| [SRL][»] \[HL]     | CE,8F        | ![logical shift [HL] right][»3]    |      4 |     2 |        `– – – – 0 – ↕ ↕` |
| [SRL][»] \[BR:ll]  | CE,8E,ll     | ![logical shift [BR:ll] right][»4] |      5 |     3 |        `– – – – 0 – ↕ ↕` |

[»]: S1C88_SRL.md "wikilink"
[»1]: /rsc/op-srl-a.svg "logical shift A right"
[»2]: /rsc/op-srl-b.svg "logical shift B right"
[»3]: /rsc/op-srl-phl.svg "logical shift [HL] right"
[»4]: /rsc/op-srl-pbrll.svg "logical shift [BR:ll] right"

## Auxiliary operation

### **PACK**: Pack

| Mnemonic    | Machine Code | Operation                     | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------- | ------------ | ----------------------------- | ------:| -----:|:------------------------:|
| [PACK][pk]  | DE           | ![B and A's LSNs into A][pk1] |      2 |     1 |        `– – – – – – – –` |

[pk]: S1C88_PACK.md "wikilink"
[pk1]: /rsc/op-pack.svg "B and A's least significant nibbles into A"

### **UPCK**: Unpack

| Mnemonic    | Machine Code | Operation                               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------- | ------------ | --------------------------------------- | ------:| -----:|:------------------------:|
| [UPCK][up]  | DF           | ![A's nibbles into B and A's LSNs][up1] |      2 |     1 |        `– – – – – – – –` |

[up]: S1C88_UPCK.md "wikilink"
[up1]: /rsc/op-upck.svg "A's nibbles into B and A's least significant nibbles, setting most significant nibbles to 0"

### **SEP**: Code extension

| Mnemonic   | Machine Code | Operation                    | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------- | ------------ | ---------------------------- | ------:| -----:|:------------------------:|
| [SEP][se]  | CE,A8        | ![sign extend A over B][se1] |      3 |     2 |        `– – – – – – – –` |

[se]: S1C88_SEP.md "wikilink"
[se1]: /rsc/op-sep.svg "sign extend A over B"

## 16-bit arithmetic operation

### **ADD**: Addition

| Mnemonic           | Machine Code | Operation      | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | -------------- | ------:| -----:|:------------------------:|
| [ADD][+] BA,#mmnn  | C0,nn,mm     | BA ← BA + mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] BA,BA     | CE,00        | BA ← BA + BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] BA,HL     | CE,01        | BA ← BA + HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] BA,IX     | CE,02        | BA ← BA + IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] BA,IY     | CE,03        | BA ← BA + IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] HL,#mmnn  | C1,nn,mm     | HL ← HL + mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] HL,BA     | CE,20        | HL ← HL + BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] HL,HL     | CE,21        | HL ← HL + HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] HL,IX     | CE,22        | HL ← HL + IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] HL,IY     | CE,23        | HL ← HL + IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IX,#mmnn  | C2,nn,mm     | IX ← IX + mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IX,BA     | CE,40        | IX ← IX + BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IX,HL     | CE,41        | IX ← IX + HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IY,#mmnn  | C3,nn,mm     | IY ← IY + mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IY,BA     | CE,42        | IY ← IY + BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] IY,HL     | CE,43        | IY ← IY + HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] SP,BA     | CE,44        | SP ← SP + BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] SP,HL     | CE,45        | SP ← SP + HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADD][+] SP,#mmnn  | CE,68,nn,mm  | SP ← SP + mmnn |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |

### **ADC**: Addition with carry

| Mnemonic            | Machine Code | Operation          | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ------------------ | ------:| -----:|:------------------------:|
| [ADC][+c] BA,BA     | CE,04        | BA ← BA + BA + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] BA,HL     | CE,05        | BA ← BA + HL + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] BA,IX     | CE,06        | BA ← BA + IX + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] BA,IY     | CE,07        | BA ← BA + IY + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] BA,#mmnn  | CE,60,nn,mm  | BA ← BA + mmnn + C |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] HL,BA     | CE,24        | HL ← HL + BA + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] HL,HL     | CE,25        | HL ← HL + HL + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] HL,IX     | CE,26        | HL ← HL + IX + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] HL,IY     | CE,27        | HL ← HL + IY + C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [ADC][+c] HL,#mmnn  | CE,61,nn,mm  | HL ← HL + mmnn + C |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |

### **SUB**: Subtraction

| Mnemonic           | Machine Code | Operation      | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | -------------- | ------:| -----:|:------------------------:|
| [SUB][-] BA,BA     | CE,08        | BA ← BA - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] BA,HL     | CE,09        | BA ← BA - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] BA,IX     | CE,0A        | BA ← BA - IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] BA,IY     | CE,0B        | BA ← BA - IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] BA,#mmnn  | D0,nn,mm     | BA ← BA - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] HL,BA     | CE,28        | HL ← HL - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] HL,HL     | CE,29        | HL ← HL - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] HL,IX     | CE,2A        | HL ← HL - IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] HL,IY     | CE,2B        | HL ← HL - IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] HL,#mmnn  | D1,nn,mm     | HL ← HL - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IX,BA     | CE,48        | IX ← IX - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IX,HL     | CE,49        | IX ← IX - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IX,#mmnn  | D2,nn,mm     | IX ← IX - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IY,BA     | CE,4A        | IY ← IY - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IY,HL     | CE,4B        | IY ← IY - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] IY,#mmnn  | D3,nn,mm     | IY ← IY - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] SP,BA     | CE,4C        | SP ← SP - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] SP,HL     | CE,4D        | SP ← SP - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SUB][-] SP,#mmnn  | CE,6A,nn,mm  | SP ← SP - mmnn |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |

### **SBC**: Subtraction with carry

| Mnemonic            | Machine Code | Operation          | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ------------------ | ------:| -----:|:------------------------:|
| [SBC][-c] BA,BA     | CE, C        | BA ← BA - BA - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] BA,HL     | CE, D        | BA ← BA - HL - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] BA,IX     | CE, E        | BA ← BA - IX - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] BA,IY     | CE, F        | BA ← BA - IY - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] BA,#mmnn  | CE,62,nn,mm  | BA ← BA - mmnn - C |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] HL,BA     | CE,2C        | HL ← HL - BA - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] HL,HL     | CE,2D        | HL ← HL - HL - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] HL,IX     | CE,2E        | HL ← HL - IX - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] HL,IY     | CE,2F        | HL ← HL - IY - C   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [SBC][-c] HL,#mmnn  | CE,63,nn,mm  | HL ← HL - mmnn - C |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |

### **CP**: Comparison

| Mnemonic           | Machine Code | Operation | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | --------- | ------:| -----:|:------------------------:|
| [CP][cp] BA,#mmnn  | D4,nn,mm     | BA - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] BA,BA     | CE,18        | BA - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] BA,HL     | CE,19        | BA - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] BA,IX     | CE,1A        | BA - IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] BA,IY     | CE,1B        | BA - IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] HL,#mmnn  | D5,nn,mm     | HL - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] HL,BA     | CE,38        | HL - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] HL,HL     | CE,39        | HL - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] HL,IX     | CE,3A        | HL - IX   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] HL,IY     | CE,3B        | HL - IY   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] IX,#mmnn  | D6,nn,mm     | IX - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] IY,#mmnn  | D7,nn,mm     | IY - mmnn |      3 |     3 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] SP,BA     | CE,5C        | SP - BA   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] SP,HL     | CE,5D        | SP - HL   |      4 |     2 |        `– – – – ↕ ↕ ↕ ↕` |
| [CP][cp] SP,#mmnn  | CE,6C,nn,mm  | SP - mmnn |      4 |     4 |        `– – – – ↕ ↕ ↕ ↕` |

### **INC**: Increment by 1

| Mnemonic      | Machine Code | Operation   | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------- | ------------ | ----------- | ------:| -----:|:------------------------:|
| [INC][++] SP  | 87           | SP ← SP + 1 |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] BA  | 90           | BA ← BA + 1 |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] HL  | 91           | HL ← HL + 1 |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] IX  | 92           | IX ← IX + 1 |      2 |     1 |        `– – – – – – – ↕` |
| [INC][++] IY  | 93           | IY ← IY + 1 |      2 |     1 |        `– – – – – – – ↕` |

### **DEC**: Decrement by 1

| Mnemonic      | Machine Code | Operation   | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------- | ------------ | ----------- | ------:| -----:|:------------------------:|
| [DEC][--] SP  | 8F           | SP ← SP - 1 |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] BA  | 98           | BA ← BA - 1 |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] HL  | 99           | HL ← HL - 1 |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] IX  | 9A           | IX ← IX - 1 |      2 |     1 |        `– – – – – – – ↕` |
| [DEC][--] IY  | 9B           | IY ← IY - 1 |      2 |     1 |        `– – – – – – – ↕` |

## 16-bit transfer

### **LD**: Load

For indirect loads, the number is treated as little-endian.
For example, in `LD BA,[hhll]` the byte _at_ hhll is loaded into A, and the following byte is loaded into B. 

| Mnemonic             | Machine Code | Operation     | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| -------------------- | ------------ | ------------- | ------:| -----:|:------------------------:|
| [LD][=] BA,\[hhll]   | B8,ll,hh     | BA ← \[hhll]  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] BA,#mmnn     | C4,nn,mm     | BA ← mmnn     |      3 |     3 |        `– – – – – – – –` |
| [LD][=] BA,\[SP+dd]  | CE,70,dd     | BA ← \[SP+dd] |      6 |     3 |        `– – – – – – – –` |
| [LD][=] BA,\[HL]     | CE,C0        | BA ← \[HL]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] BA,\[IX]     | CE,D0        | BA ← \[IX]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] BA,\[IY]     | CE,D8        | BA ← \[IY]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] BA,BA        | CE,E0        | BA ← BA       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BA,HL        | CE,E1        | BA ← HL       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BA,IX        | CE,E2        | BA ← IX       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BA,IY        | CE,E3        | BA ← IY       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BA,SP        | CE,F8        | BA ← SP       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] BA,PC        | CE,F9        | BA ← PC       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,\[hhll]   | B9,ll,hh     | HL ← \[hhll]  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] HL,#mmnn     | C5,nn,mm     | HL ← #mmnn    |      3 |     3 |        `– – – – – – – –` |
| [LD][=] HL,\[SP+dd]  | CE,71,dd     | HL ← \[SP+dd] |      6 |     3 |        `– – – – – – – –` |
| [LD][=] HL,\[HL]     | CE,C1        | HL ← \[HL]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] HL,\[IX]     | CE,D1        | HL ← \[IX]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] HL,\[IY]     | CE,D9        | HL ← \[IY]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] HL,BA        | CE,E4        | HL ← BA       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,HL        | CE,E5        | HL ← HL       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,IX        | CE,E6        | HL ← IX       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,IY        | CE,E7        | HL ← IY       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,SP        | CE,F4        | HL ← SP       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] HL,PC        | CE,F5        | HL ← PC       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IX,\[hhll]   | BA,ll,hh     | IX ← \[hhll]  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] IX,#mmnn     | C6,nn,mm     | IX ← mmnn     |      3 |     3 |        `– – – – – – – –` |
| [LD][=] IX,\[SP+dd]  | CE,72,dd     | IX ← \[SP+dd] |      6 |     3 |        `– – – – – – – –` |
| [LD][=] IX,\[HL]     | CE,C2        | IX ← \[HL]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IX,\[IX]     | CE,D2        | IX ← \[IX]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IX,\[IY]     | CE,DA        | IX ← \[IY]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IX,BA        | CE,E8        | IX ← BA       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IX,HL        | CE,E9        | IX ← HL       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IX,IX        | CE,EA        | IX ← IX       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IX,IY        | CE,EB        | IX ← IY       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IX,SP        | CE,FA        | IX ← SP       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IY,\[hhll]   | BB,ll,hh     | IY ← \[hhll]  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] IY,#mmnn     | C7,nn,mm     | IY ← mmnn     |      3 |     3 |        `– – – – – – – –` |
| [LD][=] IY,\[SP+dd]  | CE,73,dd     | IY ← \[SP+dd] |      6 |     3 |        `– – – – – – – –` |
| [LD][=] IY,\[HL]     | CE,C3        | IY ← \[HL]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IY,\[IX]     | CE,D3        | IY ← \[IX]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IY,\[IY]     | CE,DB        | IY ← \[IY]    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] IY,BA        | CE,EC        | IY ← BA       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IY,HL        | CE,ED        | IY ← HL       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IY,IX        | CE,EE        | IY ← IX       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IY,IY        | CE,EF        | IY ← IY       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] IY,SP        | CE,FE        | IY ← SP       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] SP,#mmnn     | CE,6E,nn,mm  | SP ← mmnn     |      4 |     4 |        `– – – – – – – –` |
| [LD][=] SP,\[hhll]   | CE,78,ll,hh  | SP ← \[hhll]  |      6 |     4 |        `– – – – – – – –` |
| [LD][=] SP,BA        | CE,F0        | SP ← BA       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] SP,HL        | CE,F1        | SP ← HL       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] SP,IX        | CE,F2        | SP ← IX       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] SP,IY        | CE,F3        | SP ← IY       |      2 |     2 |        `– – – – – – – –` |
| [LD][=] \[hhll],BA   | BC,ll,hh     | \[hhll] ← BA  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[hhll],HL   | BD,ll,hh     | \[hhll] ← HL  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[hhll],IX   | BE,ll,hh     | \[hhll] ← IX  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[hhll],IY   | BF,ll,hh     | \[hhll] ← IY  |      5 |     3 |        `– – – – – – – –` |
| [LD][=] \[hhll],SP   | CE,7C,ll,hh  | \[hhll] ← SP  |      6 |     4 |        `– – – – – – – –` |
| [LD][=] \[HL],BA     | CE,C4        | \[HL] ← BA    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],HL     | CE,C5        | \[HL] ← HL    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],IX     | CE,C6        | \[HL] ← IX    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[HL],IY     | CE,C7        | \[HL] ← IY    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],BA     | CE,D4        | \[IX] ← BA    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],HL     | CE,D5        | \[IX] ← HL    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],IX     | CE,D6        | \[IX] ← IX    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IX],IY     | CE,D7        | \[IX] ← IY    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],BA     | CE,DC        | \[IY] ← BA    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],HL     | CE,DD        | \[IY] ← HL    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],IX     | CE,DE        | \[IY] ← IX    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[IY],IY     | CE,DF        | \[IY] ← IY    |      5 |     2 |        `– – – – – – – –` |
| [LD][=] \[SP+dd],BA  | CE,74,dd     | \[SP+dd] ← BA |      6 |     3 |        `– – – – – – – –` |
| [LD][=] \[SP+dd],HL  | CE,75,dd     | \[SP+dd] ← HL |      6 |     3 |        `– – – – – – – –` |
| [LD][=] \[SP+dd],IX  | CE,76,dd     | \[SP+dd] ← IX |      6 |     3 |        `– – – – – – – –` |
| [LD][=] \[SP+dd],IY  | CE,77,dd     | \[SP+dd] ← IY |      6 |     3 |        `– – – – – – – –` |

### **EX**: Byte exchange

| Mnemonic        | Machine Code | Operation | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------- | ------------ | --------- | ------:| -----:|:------------------------:|
| [EX][ex] BA,HL  | C8           | BA ↔ HL   |      3 |     1 |        `– – – – – – – –` |
| [EX][ex] BA,IX  | C9           | BA ↔ IX   |      3 |     1 |        `– – – – – – – –` |
| [EX][ex] BA,IY  | CA           | BA ↔ IY   |      3 |     1 |        `– – – – – – – –` |
| [EX][ex] BA,SP  | CB           | BA ↔ SP   |      3 |     1 |        `– – – – – – – –` |

## Stack Control

### **PUSH**: Push

For 16-bit register pushes, the number is written as little-endian.
For example, in `PUSH BA`, after SP is adjusted, A is written to \[SP] and B is written to the following address.

| Mnemonic        | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [PUSH][ps] BA   | A0           | SP ← SP - 2; \[SP] ← BA |      4 |     1 |        `– – – – – – – –` |
| [PUSH][ps] HL   | A1           | SP ← SP - 2; \[SP] ← HL |      4 |     1 |        `– – – – – – – –` |
| [PUSH][ps] IX   | A2           | SP ← SP - 2; \[SP] ← IX |      4 |     1 |        `– – – – – – – –` |
| [PUSH][ps] IY   | A3           | SP ← SP - 2; \[SP] ← IY |      4 |     1 |        `– – – – – – – –` |
| [PUSH][ps] BR   | A4           | SP ← SP - 1; \[SP] ← BR |      3 |     1 |        `– – – – – – – –` |
| [PUSH][ps] EP   | A5           | SP ← SP - 1; \[SP] ← EP |      3 |     1 |        `– – – – – – – –` |
| [PUSH][ps] IP   | A6           | SP ← SP - 2; \[SP] ← IP |      4 |     1 |        `– – – – – – – –` |
| [PUSH][ps] SC   | A7           | SP ← SP - 1; \[SP] ← SC |      3 |     1 |        `– – – – – – – –` |
| [PUSH][ps] A    | CE,B0        | SP ← SP - 1; \[SP] ← A  |      3 |     2 |        `– – – – – – – –` |
| [PUSH][ps] B    | CE,B1        | SP ← SP - 1; \[SP] ← B  |      3 |     2 |        `– – – – – – – –` |
| [PUSH][ps] L    | CE,B2        | SP ← SP - 1; \[SP] ← L  |      3 |     2 |        `– – – – – – – –` |
| [PUSH][ps] H    | CE,B3        | SP ← SP - 1; \[SP] ← H  |      3 |     2 |        `– – – – – – – –` |
| [PUSH][ps] ALL  | CE,B8        | PUSH BA, HL, IX, IY, BR |     12 |     2 |        `– – – – – – – –` |
| [PUSH][ps] ALE  | CE,B9        | PUSH ALL, EP, IP        |     15 |     2 |        `– – – – – – – –` |

[ps]: S1C88_PUSH.md "wikilink"

### **POP**: Pop

For 16-bit register pops, the number is read as little-endian.
For example, in `POP BA`, the byte _at_ the top of the stack is written into A, and the following byte is written into B.

| Mnemonic       | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| -------------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [POP][pp] BA   | A8           | BA ← \[SP]; SP ← SP + 2 |      3 |     1 |        `– – – – – – – –` |
| [POP][pp] HL   | A9           | HL ← \[SP]; SP ← SP + 2 |      3 |     1 |        `– – – – – – – –` |
| [POP][pp] IX   | AA           | IX ← \[SP]; SP ← SP + 2 |      3 |     1 |        `– – – – – – – –` |
| [POP][pp] IY   | AB           | IY ← \[SP]; SP ← SP + 2 |      3 |     1 |        `– – – – – – – –` |
| [POP][pp] BR   | AC           | BR ← \[SP]; SP ← SP + 1 |      2 |     1 |        `– – – – – – – –` |
| [POP][pp] EP   | AD           | EP ← \[SP]; SP ← SP + 1 |      2 |     1 |        `– – – – – – – –` |
| [POP][pp] IP   | AE           | IP ← \[SP]; SP ← SP + 2 |      3 |     1 |        `– – – – – – – –` |
| [POP][pp] SC   | AF           | SC ← \[SP]; SP ← SP + 1 |      2 |     1 |        `↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕` |
| [POP][pp] A    | CE,B4        | A ← \[SP]; SP ← SP + 1  |      3 |     2 |        `– – – – – – – –` |
| [POP][pp] B    | CE,B5        | B ← \[SP]; SP ← SP + 1  |      3 |     2 |        `– – – – – – – –` |
| [POP][pp] L    | CE,B6        | L ← \[SP]; SP ← SP + 1  |      3 |     2 |        `– – – – – – – –` |
| [POP][pp] H    | CE,B7        | H ← \[SP]; SP ← SP + 1  |      3 |     2 |        `– – – – – – – –` |
| [POP][pp] ALL  | CE,BC        | POP BR, IY, IX, HL, BA  |     11 |     2 |        `– – – – – – – –` |
| [POP][pp] ALE  | CE,BD        | POP IP, EP, ALL         |     14 |     2 |        `– – – – – – – –` |

[pp]: S1C88_POP.md "wikilink"

## Branch

In this section's operations, we define the following functions:

```
skip:
  PC ← PC + Bytes
  NB ← CB

X ⇒ fun:
  if X then
    fun
  else
    skip
  end

PUSH CB:
  SP ← SP - 1
  [CB] ← CB

PUSH PC:
  SP ← SP - 2
  [SP] ← PC

POP CB:
  CB ← [SP]
  SP ← SP + 1

POP PC:
  PC ← [SP]
  SP ← SP + 2
```

Where `fun` is the name of some function and is defined in each section below
and the first operation of `skip` is the same as any execution, simply added for explicitness.

Cycles may be specified as `t : f`
where `t` is the cycle count for if the condition was true
and `f` is the cycle count for if the condition was false.

### **JRS**: Relative short jump

In the below operations, we define the following additional function:

```
jump:
  PC ← PC + rr + (Bytes - 1)
  CB ← NB
```

| Mnemonic          | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [JRS][js] C,rr    | E4,rr        | C ⇒ jump                |      2 | 2  |        `– – – – – – – –` |
| [JRS][js] NC,rr   | E5,rr        | !C ⇒ jump               |      2 | 2  |        `– – – – – – – –` |
| [JRS][js] Z,rr    | E6,rr        | Z ⇒ jump                |      2 | 2  |        `– – – – – – – –` |
| [JRS][js] NZ,rr   | E7,rr        | !Z ⇒ jump               |      2 | 2  |        `– – – – – – – –` |
| [JRS][js] rr      | F1,rr        | jump                    |      2 | 2  |        `– – – – – – – –` |
| [JRS][js] LT,rr   | CE,E0,rr     | (N ^^ V) ⇒ jump         |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] LE,rr   | CE,E1,rr     | (Z || (N ^^ V)) ⇒ jump  |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] GT,rr   | CE,E2,rr     | !(Z || (N ^^ V)) ⇒ jump |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] GE,rr   | CE,E3,rr     | !(N ^^ V) ⇒ jump        |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] V,rr    | CE,E4,rr     | V ⇒ jump                |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] NV,rr   | CE,E5,rr     | !V ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] P,rr    | CE,E6,rr     | !N ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] M,rr    | CE,E7,rr     | N ⇒ jump                |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] F0,rr   | CE,E8,rr     | F0 ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] F1,rr   | CE,E9,rr     | F1 ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] F2,rr   | CE,EA,rr     | F2 ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] F3,rr   | CE,EB,rr     | F3 ⇒ jump               |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] NF0,rr  | CE,EC,rr     | !F0 ⇒ jump              |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] NF1,rr  | CE,ED,rr     | !F1 ⇒ jump              |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] NF2,rr  | CE,EE,rr     | !F2 ⇒ jump              |      3 | 3  |        `– – – – – – – –` |
| [JRS][js] NF3,rr  | CE,EF,rr     | !F3 ⇒ jump              |      3 | 3  |        `– – – – – – – –` |

[js]: S1C88_JRS.md "wikilink"

### **JRL**: Relative long jump

In the below operations, we define the following additional function:

```
jump:
  PC ← PC + qqrr + 2
  CB ← NB
```

| Mnemonic           | Machine Code | Operation | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | --------- | ------:| -----:|:------------------------:|
| [JRL][jl] C,qqrr   | EC,rr,qq     | C ⇒ jump  |      3 |     3 |        `– – – – – – – –` |
| [JRL][jl] NC,qqrr  | ED,rr,qq     | !C ⇒ jump |      3 |     3 |        `– – – – – – – –` |
| [JRL][jl] Z,qqrr   | EE,rr,qq     | Z ⇒ jump  |      3 |     3 |        `– – – – – – – –` |
| [JRL][jl] NZ,qqrr  | EF,rr,qq     | !Z ⇒ jump |      3 |     3 |        `– – – – – – – –` |
| [JRL][jl] qqrr     | F3,rr,qq     | jump      |      3 |     3 |        `– – – – – – – –` |

[jl]: S1C88_JRL.md "wikilink"

### **JP**: Indirect jump

For indirect loads, the number is treated as little-endian.
For example, in `PC ← [00kk]` the byte _at_ 00kk is loaded into the low byte of PC, and the following byte is loaded into the high byte. 

| Mnemonic        | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [JP][jp] \[kk]  | FD,kk        | PC ← \[00kk]; CB ← NB | ?CYCLES | 2  |
| [JP][jp] HL     | F4           | PC ← HL; CB ← NB      | ?CYCLES | 1  |

[jp]: S1C88_JP.md "wikilink"

### **DJR**: Loop

In the below operations, we define the following additional function:

```
jump:
  PC ← PC + rr + 1
  CB ← NB
```

| Mnemonic         | Machine Code | Operation                | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------------- | ------------ | ------------------------ | ------:| -----:|:------------------------:|
| [DJR][dj] NZ,rr  | F5,rr        | B ← B - 1; B == 0 ⇒ jump |      4 |     2 |        `– – – – – – – ↕` |

[dj]: S1C88_DJR.md "wikilink"

### **CARS**: Relative short call

In the below operations, we define the following additional function:

```
call:
  PUSH CB, PC
  PC ← PC + rr + (Bytes - 1)
  CB ← NB
```

| Mnemonic           | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------ | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [CARS][cs] C,rr    | E0,rr        | C ⇒ call                |  5 : 2 |     2 |        `– – – – – – – –` |
| [CARS][cs] NC,rr   | E1,rr        | !C ⇒ call               |  5 : 2 |     2 |        `– – – – – – – –` |
| [CARS][cs] Z,rr    | E2,rr        | Z ⇒ call                |  5 : 2 |     2 |        `– – – – – – – –` |
| [CARS][cs] NZ,rr   | E3,rr        | !Z ⇒ call               |  5 : 2 |     2 |        `– – – – – – – –` |
| [CARS][cs] rr      | F0,rr        | call                    |      5 |     2 |        `– – – – – – – –` |
| [CARS][cs] LT,rr   | CE,F0,rr     | (N ^^ V) ⇒ call         |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] LE,rr   | CE,F1,rr     | (Z || (N ^^ V)) ⇒ call  |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] GT,rr   | CE,F2,rr     | !(Z || (N ^^ V)) ⇒ call |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] GE,rr   | CE,F3,rr     | !(N ^^ V) ⇒ call        |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] V,rr    | CE,F4,rr     | V ⇒ call                |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] NV,rr   | CE,F5,rr     | !V ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] P,rr    | CE,F6,rr     | !N ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] M,rr    | CE,F7,rr     | N ⇒ call                |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] F0,rr   | CE,F8,rr     | F0 ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] F1,rr   | CE,F9,rr     | F1 ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] F2,rr   | CE,FA,rr     | F2 ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] F3,rr   | CE,FB,rr     | F3 ⇒ call               |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] NF0,rr  | CE,FC,rr     | !F0 ⇒ call              |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] NF1,rr  | CE,FD,rr     | !F1 ⇒ call              |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] NF2,rr  | CE,FE,rr     | !F2 ⇒ call              |  6 : 3 |     3 |        `– – – – – – – –` |
| [CARS][cs] NF3,rr  | CE,FF,rr     | !F3 ⇒ call              |  6 : 3 |     3 |        `– – – – – – – –` |

[cs]: S1C88_CARS.md "wikilink"

### **CARL**: Relative long call

In the below operations, we define the following additional function:

```
call:
  PUSH CB, PC
  PC ← PC + qqrr + 2
  CB ← NB
```

| Mnemonic            | Machine Code | Operation | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | --------- | ------:| -----:|:------------------------:|
| [CARL][cl] C,qqrr   | E8,rr,qq     | C ⇒ call  |  6 : 3 |    3 |        `– – – – – – – –` |
| [CARL][cl] NC,qqrr  | E9,rr,qq     | !C ⇒ call |  6 : 3 |    3 |        `– – – – – – – –` |
| [CARL][cl] Z,qqrr   | EA,rr,qq     | Z ⇒ call  |  6 : 3 |    3 |        `– – – – – – – –` |
| [CARL][cl] NZ,qqrr  | EB,rr,qq     | !Z ⇒ call |  6 : 3 |    3 |        `– – – – – – – –` |
| [CARL][cl] qqrr     | F2,rr,qq     | call      |  6 : 3 |    3 |        `– – – – – – – –` |

[cl]: S1C88_CARL.md "wikilink"

### **CALL**: Indirect call

For indirect loads, the number is treated as little-endian.
For example, in `PC ← [hhll]` the byte _at_ hhll is loaded into the low byte of PC, and the following byte is loaded into the high byte. 

| Mnemonic            | Machine Code | Operation                          | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ------------------- | ------------ | ---------------------------------- | ------:| -----:|:------------------------:|
| [CALL][ca] \[hhll]  | FB,ll,hh     | PUSH CB, PC; PC ← [hhll]; CB ← NB  |      8 |     3 |        `– – – – – – – –` |

[ca]: S1C88_CALL.md "wikilink"

### **RET**: Return

| Mnemonic   | Machine Code | Operation           | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ---------- | ------------ | ------------------- | ------:| -----:|:------------------------:|
| [RET][rt]  | F8           | POP PC, CB; NB ← CB |      4 |     1 |        `– – – – – – – –` |

[rt]: S1C88_RET.md "wikilink"

### **RETE**: Exception processing return

| Mnemonic    | Machine Code | Operation               | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------- | ------------ | ----------------------- | ------:| -----:|:------------------------:|
| [RETE][re]  | F9           | POP SC, PC, CB; NB ← CB |      5 |     1 |        `↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕` |

[re]: S1C88_RETE.md "wikilink"

### **RETS**: Return and skip

| Mnemonic    | Machine Code | Operation                        | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| ----------- | ------------ | -------------------------------- | ------:| -----:|:------------------------:|
| [RETS][rs]  | FA           | POP PC, CB; NB ← CB; PC ← PC + 2 |      6 |     1 |        `– – – – – – – –` |

[rs]: S1C88_RETS.md "wikilink"

### **INT**: Software interrupt

For indirect loads, the number is treated as little-endian.
For example, in `PC ← [00kk]` the byte _at_ 00kk is loaded into the low byte of PC, and the following byte is loaded into the high byte. 

| Mnemonic              | Machine Code | Operation                              | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | -------------------------------------- | ------:| -----:|:------------------------:|
| [INT][it] \[kk]       | FC,kk        | PUSH CB, PC, SC; PC ← \[00kk]; CB ← NB |      8 |     2 |        `– – – – – – – –` |

[it]: S1C88_INT.md "wikilink"

<!--
## System Control

### **NOP**: No operation

| Mnemonic              | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [NOP][no]                    |              | FF        | ?PSEUDOCODE | ?CYCLES | 1  |

[no]: S1C88_NOP.md "wikilink"

### **HALT**: Shifts to HALT status

| Mnemonic              | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [HALT][ht]                     |              | CE,AE     | ?PSEUDOCODE | ?CYCLES | 2  |

[ht]: S1C88_HALT.md "wikilink"

### **SLP**: Shifts to SLEEP status

| Mnemonic              | Machine Code | Operation             | Cycles | Bytes | SC<br/>`1 0 U D N V C Z` |
| --------------------- | ------------ | --------------------- | ------:| -----:|:------------------------:|
| [SLP][zz]                    |              | CE,AF     | ?PSEUDOCODE | ?CYCLES | 2  |

[zz]: S1C88_SLP.md "wikilink"

## Operation Code Map

### 1st operation code

|    | x0                                    | x1                                    | x2                                    | x3                                    | x4                                         | x5                                      | x6                                      | x7                                      | x8                                         | x9                                       | xA                                         | xB                                       | xC                                         | xD                                         | xE                                         | xF                                         |
| ---| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------------ | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------------ | ---------------------------------------- | ------------------------------------------ | ---------------------------------------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| 0x | [ADD][+] A,A       | [ADD][+] A,B       | [ADD][+] A,#nn    | [ADD][+] A,\[HL]  | [ADD][+] A,\[BR:ll]    | [ADD][+] A,\[hhll]  | [ADD][+] A,\[IX]    | [ADD][+] A,\[IY]    | [ADC][+c] A,A            | [ADC][+c] A,B          | [ADC][+c] A,#nn         | [ADC][+c] A,\[HL]     | [ADC][+c] A,\[BR:ll]    | [ADC][+c] A,\[hhll]     | [ADC][+c] A,\[IX]       | [ADC][+c] A,\[IY]       |
| 1x | [SUB][-] A,A       | [SUB][-] A,B       | [SUB][-] A,#nn    | [SUB][-] A,\[HL]  | [SUB][-] A,\[BR:ll]    | [SUB][-] A,\[hhll]  | [SUB][-] A,\[IX]    | [SUB][-] A,\[IY]    | [SBC][-c] A,A            | [SBC][-c] A,B          | [SBC][-c] A,#nn         | [SBC][-c] A,\[HL]     | [SBC][-c] A,\[BR:ll]    | [SBC][-c] A,\[hhll]     | [SBC][-c] A,\[IX]       | [SBC][-c] A,\[IY]       |
| 2x | [AND][&] A,A       | [AND][&] A,B       | [AND][&] A,#nn    | [AND][&] A,\[HL]  | [AND][&] A,\[BR:ll]    | [AND][&] A,\[hhll]  | [AND][&] A,\[IX]    | [AND][&] A,\[IY]    | [OR][or] A,A              | [OR][or] A,B            | [OR][or] A,#nn           | [OR][or] A,\[HL]       | [OR][or] A,\[BR:ll]      | [OR][or] A,\[hhll]       | [OR][or] A,\[IX]         | [OR][or] A,\[IY]         |
| 3x | [CP][cp] A,A         | [CP][cp] A,B         | [CP][cp] A,#nn      | [CP][cp] A,\[HL]    | [CP][cp] A,\[BR:ll]      | [CP][cp] A,\[hhll]    | [CP][cp] A,\[IX]      | [CP][cp] A,\[IY]      | [XOR][^] A,A            | [XOR][^] A,B          | [XOR][^] A,#nn         | [XOR][^] A,\[HL]     | [XOR][^] A,\[BR:ll]    | [XOR][^] A,\[hhll]     | [XOR][^] A,\[IX]       | [XOR][^] A,\[IY]       |
| 4x | [LD][=] A,A         | [LD][=] A,B         | [LD][=] A,L         | [LD][=] A,H         | [LD][=] A,\[BR:ll]      | [LD][=] A,\[HL]      | [LD][=] A,\[IX]      | [LD][=] A,\[IY]      | [LD][=] B,A              | [LD][=] B,B            | [LD][=] B,L              | [LD][=] B,H            | [LD][=] B,\[BR:ll]      | [LD][=] B,\[HL]         | [LD][=] B,\[IX]         | [LD][=] B,\[IY]         |
| 5x | [LD][=] L,A         | [LD][=] L,B         | [LD][=] L,L         | [LD][=] L,H         | [LD][=] L,\[BR:ll]      | [LD][=] L,\[HL]      | [LD][=] L,\[IX]      | [LD][=] L,\[IY]      | [LD][=] H,A              | [LD][=] H,B            | [LD][=] H,L              | [LD][=] H,H            | [LD][=] H,\[BR:ll]      | [LD][=] H,\[HL]         | [LD][=] H,\[IX]         | [LD][=] H,\[IY]         |
| 6x | [LD][=] \[IX],A    | [LD][=] \[IX],B    | [LD][=] \[IX],L    | [LD][=] \[IX],H    | [LD][=] \[IX],\[BR:ll] | [LD][=] \[IX],\[HL] | [LD][=] \[IX],\[IX] | [LD][=] \[IX],\[IY] | [LD][=] \[HL],A         | [LD][=] \[HL],B       | [LD][=] \[HL],L         | [LD][=] \[HL],H       | [LD][=] \[HL],\[BR:ll] | [LD][=] \[HL],\[HL]    | [LD][=] \[HL],\[IX]    | [LD][=] \[HL],\[IY]    |
| 7x | [LD][=] \[IY],A    | [LD][=] \[IY],B    | [LD][=] \[IY],L    | [LD][=] \[IY],H    | [LD][=] \[IY],\[BR:ll] | [LD][=] \[IY],\[HL] | [LD][=] \[IY],\[IX] | [LD][=] \[IY],\[IY] | [LD][=] \[BR:ll],A      | [LD][=] \[BR:ll],B    | [LD][=] \[BR:ll],L      | [LD][=] \[BR:ll],H    |                                            | [LD][=] \[BR:ll],\[HL] | [LD][=] \[BR:ll],\[IX] | [LD][=] \[BR:ll],\[IY] |
| 8x | [INC][++] A         | [INC][++] B         | [INC][++] L         | [INC][++] H         | [INC][++] BR             | [INC][++] \[BR:ll]   | [INC][++] \[HL]      | [INC][++] SP          | [DEC][--] A              | [DEC][--] B            | [DEC][--] L              | [DEC][--] H            | [DEC][--] BR             | [DEC][--] \[BR:ll]      | [DEC][--] \[HL]         | [DEC][--] SP             |
| 9x | [INC][++] BA        | [INC][++] HL        | [INC][++] IX        | [INC][++] IY        | [BIT][bt] A,B            | [BIT][bt] \[HL],#nn | [BIT][bt] A,#nn      | [BIT][bt] B,#nn      | [DEC][--] BA             | [DEC][--] HL           | [DEC][--] IX             | [DEC][--] IY           | [AND][&] SC,#nn        | [OR][or] SC,#nn          | [XOR][^] SC,#nn        | [LD][=] SC,#nn          |
| Ax | [PUSH][ps] BA      | [PUSH][ps] HL      | [PUSH][ps] IX      | [PUSH][ps] IY      | [PUSH][ps] BR           | [PUSH][ps] EP        | [PUSH][ps] IP        | [PUSH][ps] SC        | [POP][pp] BA             | [POP][pp] HL           | [POP][pp] IX             | [POP][pp] IY           | [POP][pp] BR             | [POP][pp] EP             | [POP][pp] IP             | [POP][pp] SC             |
| Bx | [LD][=] A,#nn      | [LD][=] B,#nn      | [LD][=] L,#nn      | [LD][=] H,#nn      | [LD][=] BR,#hh          | [LD][=] \[HL],#nn   | [LD][=] \[IX],#nn   | [LD][=] \[IY],#nn   | [LD][=] BA,\[hhll]      | [LD][=] HL,\[hhll]    | [LD][=] IX,\[hhll]      | [LD][=] IY,\[hhll]    | [LD][=] \[hhll],BA      | [LD][=] \[hhll],HL      | [LD][=] \[hhll],IX      | [LD][=] \[hhll],IY      |
| Cx | [ADD][+] BA,#mmnn | [ADD][+] HL,#mmnn | [ADD][+] IX,#mmnn | [ADD][+] IY,#mmnn | [LD][=] BA,#mmnn        | [LD][=] HL,#mmnn     | [LD][=] IX,#mmnn     | [LD][=] IY,#mmnn     | [EX][ex] BA,HL            | [EX][ex] BA,IX          | [EX][ex] BA,IY            | [EX][ex] BA,SP          | [EX][ex] A,B              | [EX][ex] A,\[HL]         | Expansion Code                             | Expansion Code                             |
| Dx | [SUB][-] BA,#mmnn | [SUB][-] HL,#mmnn | [SUB][-] IX,#mmnn | [SUB][-] IY,#mmnn | [CP][cp] BA,#mmnn        | [CP][cp] HL,#mmnn     | [CP][cp] IX,#mmnn     | [CP][cp] IY,#mmnn     | [AND][&] \[BR:ll],#nn | [OR][or] \[BR:ll],#nn | [XOR][^] \[BR:ll],#nn | [CP][cp] \[BR:ll],#nn | [BIT][bt] \[BR:ll],#nn | [LD][=] \[BR:ll],#nn   | [PACK][pk]              | [UPCK][up]              |
| Ex | [CARS][cs] C,rr    | [CARS][cs] NC,rr   | [CARS][cs] Z,rr    | [CARS][cs] NZ,rr   | [JRS][js] C,rr           | [JRS][js] NC,rr       | [JRS][js] Z,rr        | [JRS][js] NZ,rr       | [CARL][cl] C,qqrr       | [CARL][cl] NC,qqrr    | [CARL][cl] Z,qqrr       | [CARL][cl] NZ,qqrr    | [JRL][jl] C,qqrr         | [JRL][jl] NC,qqrr        | [JRL][jl] Z,qqrr         | [JRL][jl] NZ,qqrr        |
| Fx | [CARS][cs] rr      | [JRS][js] rr        | [CARL][cl] qqrr    | [JRL][jl] qqrr      | [JP][jp] HL               | [DJR][dj] NZ,rr       | [SWAP][sw] A         | [SWAP][sw] \[HL]    | [RET][rt]                | [RETE][re]            | [RETS][rs]              | [CALL][ca] \[hhll]   | [INT][it] \[kk]         | [JP][jp] \[kk]           |                                            | [NOP][no]                |

\== 2nd operation code (1st operation code = CE)
==

|    | x0                                         | x1                                         | x2                                        | x3                                        | x4                                    | x5                                      | x6                                        | x7                                        | x8                                         | x9                                         | xA                                        | xB                                        | xC                                    | xD                                      | xE                                        | xF                                        |
| ---| ------------------------------------------ | ------------------------------------------ | ----------------------------------------- | ----------------------------------------- | ------------------------------------- | --------------------------------------- | ----------------------------------------- | ----------------------------------------- | ------------------------------------------ | ------------------------------------------ | ----------------------------------------- | ----------------------------------------- | ------------------------------------- | --------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| 0x | [ADD][+] A,\[IX+dd]    | [ADD][+] A,\[IY+dd]    | [ADD][+] A,\[IX+L]    | [ADD][+] A,\[IY+L]    | [ADD][+] \[HL],A  | [ADD][+] \[HL],#nn | [ADD][+] \[HL],\[IX] | [ADD][+] \[HL],\[IY] | [ADC][+c] A,\[IX+dd]    | [ADC][+c] A,\[IY+dd]    | [ADC][+c] A,\[IX+L]    | [ADC][+c] A,\[IY+L]    | [ADC][+c] \[HL],A  | [ADC][+c] \[HL],#nn | [ADC][+c] \[HL],\[IX] | [ADC][+c] \[HL],\[IY] |
| 1x | [SUB][-] A,\[IX+dd]    | [SUB][-] A,\[IY+dd]    | [SUB][-] A,\[IX+L]    | [SUB][-] A,\[IY+L]    | [SUB][-] \[HL],A  | [SUB][-] \[HL],#nn | [SUB][-] \[HL],\[IX] | [SUB][-] \[HL],\[IY] | [SBC][-c] A,\[IX+dd]    | [SBC][-c] A,\[IY+dd]    | [SBC][-c] A,\[IX+L]    | [SBC][-c] A,\[IY+L]    | [SBC][-c] \[HL],A  | [SBC][-c] \[HL],#nn | [SBC][-c] \[HL],\[IX] | [SBC][-c] \[HL],\[IY] |
| 2x | [AND][&] A,\[IX+dd]    | [AND][&] A,\[IY+dd]    | [AND][&] A,\[IX+L]    | [AND][&] A,\[IY+L]    | [AND][&] \[HL],A  | [AND][&] \[HL],#nn | [AND][&] \[HL],\[IX] | [AND][&] \[HL],\[IY] | [OR][or] A,\[IX+dd]      | [OR][or] A,\[IY+dd]      | [OR][or] A,\[IX+L]      | [OR][or] A,\[IY+L]      | [OR][or] \[HL],A    | [OR][or] \[HL],#nn   | [OR][or] \[HL],\[IX]   | [OR][or] \[HL],\[IY]   |
| 3x | [CP][cp] A,\[IX+dd]      | [CP][cp] A,\[IY+dd]      | [CP][cp] A,\[IX+L]      | [CP][cp] A,\[IY+L]      | [CP][cp] \[HL],A    | [CP][cp] \[HL],#nn   | [CP][cp] \[HL],\[IX]   | [CP][cp] \[HL],\[IY]   | [XOR][^] A,\[IX+dd]    | [XOR][^] A,\[IY+dd]    | [XOR][^] A,\[IX+L]    | [XOR][^] A,\[IY+L]    | [XOR][^] \[HL],A  | [XOR][^] \[HL],#nn | [XOR][^] \[HL],\[IX] | [XOR][^] \[HL],\[IY] |
| 4x | [LD][=] A,\[IX+dd]      | [LD][=] A,\[IY+dd]      | [LD][=] A,\[IX+L]      | [LD][=] A,\[IY+L]      | [LD][=] \[IX+dd],A | [LD][=] \[IY+dd],A   | [LD][=] \[IX+L],A      | [LD][=] \[IY+L],A      | [LD][=] B,\[IX+dd]      | [LD][=] B,\[IY+dd]      | [LD][=] B,\[IX+L]      | [LD][=] B,\[IY+L]      | [LD][=] \[IX+dd],B | [LD][=] \[IY+dd],B   | [LD][=] \[IX+L],B      | [LD][=] \[IY+L],B      |
| 5x | [LD][=] L,\[IX+dd]      | [LD][=] L,\[IY+dd]      | [LD][=] L,\[IX+L]      | [LD][=] L,\[IY+L]      | [LD][=] \[IX+dd],L | [LD][=] \[IY+dd],L   | [LD][=] \[IX+L],L      | [LD][=] \[IY+L],L      | [LD][=] H,\[IX+dd]      | [LD][=] H,\[IY+dd]      | [LD][=] H,\[IX+L]      | [LD][=] H,\[IY+L]      | [LD][=] \[IX+dd],H | [LD][=] \[IY+dd],H   | [LD][=] \[IX+L],H      | [LD][=] \[IY+L],H      |
| 6x | [LD][=] \[HL],\[IX+dd] | [LD][=] \[HL],\[IY+dd] | [LD][=] \[HL],\[IX+L] | [LD][=] \[HL],\[IY+L] |                                       |                                         |                                           |                                           | [LD][=] \[IX],\[IX+dd] | [LD][=] \[IX],\[IY+dd] | [LD][=] \[IX],\[IX+L] | [LD][=] \[IX],\[IY+L] |                                       |                                         |                                           |                                           |
| 7x |                                            |                                            |                                           |                                           |                                       |                                         |                                           |                                           | [LD][=] \[IY],\[IX+dd] | [LD][=] \[IY],\[IY+dd] | [LD][=] \[IY],\[IX+L] | [LD][=] \[IY],\[IY+L] |                                       |                                         |                                           |                                           |
| 8x | [SLA][«<] A              | [SLA][«<] B              | [SLA][«<] \[BR:ll]     | [SLA][«<] \[HL]        | [SLL][«] A         | [SLL][«] B           | [SLL][«] \[BR:ll]     | [SLL][«] \[HL]        | [SRA][»>] A              | [SRA][»>] B              | [SRA][»>] \[BR:ll]     | [SRA][»>] \[HL]        | [SRL][»] A         | [SRL][»] B           | [SRL][»] \[BR:ll]     | [SRL][»] \[HL]        |
| 9x | [RL][(] A                | [RL][(] B                | [RL][(] \[BR:ll]       | [RL][(] \[HL]          | [RLC][(c] A         | [RLC][(c] B           | [RLC][(c] \[BR:ll]     | [RLC][(c] \[HL]        | [RR][)] A                | [RR][)] B                | [RR][)] \[BR:ll]       | [RR][)] \[HL]          | [RRC][)c] A         | [RRC][)c] B           | [RRC][)c] \[BR:ll]     | [RRC][)c] \[HL]        |
| Ax | [CPL][~] A              | [CPL][~] B              | [CPL][~] \[BR:ll]     | [CPL][~] \[HL]        | [NEG][ng] A         | [NEG][ng] B           | [NEG][ng] \[BR:ll]     | [NEG][ng] \[HL]        | [SEP][se]                |                                            |                                           |                                           |                                       |                                         | [HALT][ht]             | [SLP][zz]               |
| Bx | [AND][&] B,#nn         | [AND][&] L,#nn         | [AND][&] H,#nn        |                                           | [OR][or] B,#nn      | [OR][or] L,#nn        | [OR][or] H,#nn          |                                           | [XOR][^] B,#nn         | [XOR][^] L,#nn         | [XOR][^] H,#nn        |                                           | [CP][cp] B,#nn      | [CP][cp] L,#nn        | [CP][cp] H,#nn          | [CP][cp] BR,#hh         |
| Cx | [LD][=] A,BR             | [LD][=] A,SC             | [LD][=] BR,A            | [LD][=] SC,A            | [LD][=] NB,#bb     | [LD][=] EP,#pp       | [LD][=] XP,#pp         | [LD][=] YP,#pp         | [LD][=] A,NB             | [LD][=] A,EP             | [LD][=] A,XP            | [LD][=] A,YP            | [LD][=] NB,A        | [LD][=] EP,A          | [LD][=] XP,A            | [LD][=] YP,A            |
| Dx | [LD][=] A,\[hhll]       | [LD][=] B,\[hhll]       | [LD][=] L,\[hhll]      | [LD][=] H,\[hhll]      | [LD][=] \[hhll],A  | [LD][=] \[hhll],B    | [LD][=] \[hhll],L      | [LD][=] \[hhll],H      | [MLT][*]                | [DIV][/]                |                                           |                                           |                                       |                                         |                                           |                                           |
| Ex | [JRS][js] LT,rr          | [JRS][js] LE,rr          | [JRS][js] GT,rr         | [JRS][js] GE,rr         | [JRS][js] V,rr      | [JRS][js] NV,rr       | [JRS][js] P,rr          | [JRS][js] M,rr          | [JRS][js] F0,rr          | [JRS][js] F1,rr          | [JRS][js] F2,rr         | [JRS][js] F3,rr         | [JRS][js] NF0,rr    | [JRS][js] NF1,rr      | [JRS][js] NF2,rr        | [JRS][js] NF3,rr        |
| Fx | [CARS][cs] LT,rr        | [CARS][cs] LE,rr        | [CARS][cs] GT,rr       | [CARS][cs] GE,rr       | [CARS][cs] V,rr    | [CARS][cs] NV,rr     | [CARS][cs] P,rr        | [CARS][cs] M,rr        | [CARS][cs] F0,rr        | [CARS][cs] F1,rr        | [CARS][cs] F2,rr       | [CARS][cs] F3,rr       | [CARS][cs] NF0,rr  | [CARS][cs] NF1,rr    | [CARS][cs] NF2,rr      | [CARS][cs] NF3,rr      |

\== 3nd operation code (1st operation code = CF)
==

|    | x0                                     | x1                                     | x2                                     | x3                                     | x4                                     | x5                                     | x6                                     | x7                                     | x8                                    | x9                                  | xA                                    | xB                                  | xC                                    | xD                                  | xE                                  | xF                                  |
| ---| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| 0x | [ADD][+] BA,BA      | [ADD][+] BA,HL      | [ADD][+] BA,IX      | [ADD][+] BA,IY      | [ADC][+c] BA,BA      | [ADC][+c] BA,HL      | [ADC][+c] BA,IX      | [ADC][+c] BA,IY      | [SUB][-] BA,BA     | [SUB][-] BA,HL   | [SUB][-] BA,IX     | [SUB][-] BA,IY   | [SBC][-c] BA,BA     | [SBC][-c] BA,HL   | [SBC][-c] BA,IX   | [SBC][-c] BA,IY   |
| 1x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        | [CP][cp] BA,BA       | [CP][cp] BA,HL     | [CP][cp] BA,IX       | [CP][cp] BA,IY     |                                       |                                     |                                     |                                     |
| 2x | [ADD][+] HL,BA      | [ADD][+] HL,HL      | [ADD][+] HL,IX      | [ADD][+] HL,IY      | [ADC][+c] HL,BA      | [ADC][+c] HL,HL      | [ADC][+c] HL,IX      | [ADC][+c] HL,IY      | [SUB][-] HL,BA     | [SUB][-] HL,HL   | [SUB][-] HL,IX     | [SUB][-] HL,IY   | [SBC][-c] HL,BA     | [SBC][-c] HL,HL   | [SBC][-c] HL,IX   | [SBC][-c] HL,IY   |
| 3x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        | [CP][cp] HL,BA       | [CP][cp] HL,HL     | [CP][cp] HL,IX       | [CP][cp] HL,IY     |                                       |                                     |                                     |                                     |
| 4x | [ADD][+] IX,BA      | [ADD][+] IX,HL      | [ADD][+] IY,BA      | [ADD][+] IY,HL      | [ADD][+] SP,BA      | [ADD][+] SP,HL      |                                        |                                        | [SUB][-] IX,BA     | [SUB][-] IX,HL   | [SUB][-] IY,BA     | [SUB][-] IY,HL   | [SUB][-] SP,BA     | [SUB][-] SP,HL   |                                     |                                     |
| 5x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     | [CP][cp] SP,BA       | [CP][cp] SP,HL     |                                     |                                     |
| 6x | [ADC][+c] BA,#mmnn  | [ADC][+c] HL,#mmnn  | [SBC][-c] BA,#mmnn  | [SBC][-c] HL,#mmnn  |                                        |                                        |                                        |                                        | [ADD][+] SP,#mmnn |                                     | [SUB][-] SP,#mmnn |                                     | [CP][cp] SP,#mmnn   |                                     | [LD][=] SP,#mmnn |                                     |
| 7x | [LD][=] BA,\[SP+dd] | [LD][=] HL,\[SP+dd] | [LD][=] IX,\[SP+dd] | [LD][=] IY,\[SP+dd] | [LD][=] \[SP+dd],BA | [LD][=] \[SP+dd],HL | [LD][=] \[SP+dd],IX | [LD][=] \[SP+dd],IY | [LD][=] SP,\[hhll] |                                     |                                       |                                     | [LD][=] \[hhll],SP |                                     |                                     |                                     |
| 8x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| 9x |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Ax |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Bx | [PUSH][ps] A        | [PUSH][ps] B        | [PUSH][ps] L        | [PUSH][ps] H        | [POP][pp] A          | [POP][pp] B          | [POP][pp] L          | [POP][pp] H          | [PUSH][ps] ALL     | [PUSH][ps] ALE   |                                       |                                     | [POP][pp] ALL       | [POP][pp] ALE     |                                     |                                     |
| Cx | [LD][=] BA,\[HL]    | [LD][=] HL,\[HL]    | [LD][=] IX,\[HL]    | [LD][=] IY,\[HL]    | [LD][=] \[HL],BA    | [LD][=] \[HL],HL    | [LD][=] \[HL],IX    | [LD][=] \[HL],IY    |                                       |                                     |                                       |                                     |                                       |                                     |                                     |                                     |
| Dx | [LD][=] BA,\[IX]    | [LD][=] HL,\[IX]    | [LD][=] IX,\[IX]    | [LD][=] IY,\[IX]    | [LD][=] \[IX],BA    | [LD][=] \[IX],HL    | [LD][=] \[IX],IX    | [LD][=] \[IX],IY    | [LD][=] BA,\[IY]   | [LD][=] HL,\[IY] | [LD][=] IX,\[IY]   | [LD][=] IY,\[IY] | [LD][=] \[IY],BA   | [LD][=] \[IY],HL | [LD][=] \[IY],IX | [LD][=] \[IY],IY |
| Ex | [LD][=] BA,BA        | [LD][=] BA,HL        | [LD][=] BA,IX        | [LD][=] BA,IY        | [LD][=] HL,BA        | [LD][=] HL,HL        | [LD][=] HL,IX        | [LD][=] HL,IY        | [LD][=] IX,BA       | [LD][=] IX,HL     | [LD][=] IX,IX       | [LD][=] IX,IY     | [LD][=] IY,BA       | [LD][=] IY,HL     | [LD][=] IY,IX     | [LD][=] IY,IY     |
| Fx | [LD][=] SP,BA        | [LD][=] SP,HL        | [LD][=] SP,IX        | [LD][=] SP,IY        | [LD][=] HL,SP        | [LD][=] HL,PC        |                                        |                                        | [LD][=] BA,SP       | [LD][=] BA,PC     | [LD][=] IX,SP       |                                     |                                       |                                     | [LD][=] IY,SP     |                                     |

## Illegal Instructions

**NOTE: This document is now out of date, as should be updated to the
new mnemonic and register naming**

The entire opcode table has been evaluated on Pokémon mini units and new
and exotic illegal opcodes have been found.

These opcodes are not officially supported (they are not used by
commercial games and not even found in the Pokemon Channel emulator) and
can produce random results or crashes in some cases. The illegal opcodes
have been documented on [this page's Discussion
page](Talk:S1C88_InstructionSet.md "wikilink"). ''' THIS PAGE IS IN PROCESS
'''
