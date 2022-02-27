# PMAS - Pika Macro ASsembler

Team PokeMe's second assembler, first developed by DarkFader. It was the product of reverse engineering the Pokémon Channel emulator.

## Installing

* A version is shipped with PokeMini emulator
* Download latest version [here](https://www.pokemon-mini.net/tools/pika-macro-assembler/)
* Source repository (abandoned) [here](https://github.com/darkfader/PokemonMini)

## Usage

TODO

## Mnemonics and registers

PMAS used mnemonics based on Intel x86 architectures since the official ones weren't known at the time.
For those who are adapting from it, reading old code, or are for some reason using this tool still, here is a list for converting the operations.

In the following lists, we use these symbols:

| Symbol             | Meaning                                       |
|:------------------:| --------------------------------------------- |
| `r`                | 8-bit register: e.g. A, B, L, or H            |
| `rp`               | 16-bit register: e.g. BA, HL, IX, IY, or SP   |
| `er`               | Indexing register: NB, EP, XP, or YP          |
| `nn` or `pp`       | Unsigned 8-bit immediate data                 |
| `dd` or `rr`       | Signed 8-bit immediate (offset, usually)      |
| `mmnn` or `hhll`   | Unsigned 16-bit immediate                     |
| `qqrr`             | Signed 16-bit immediate (offset)              |
| `x` or `y`         | Any valid register or immediate               |
| `t`                | Any valid 8-bit target (register or indirect) |
| `tt`               | Any valid 16-bit target                       |
| `s`                | Any valid 8-bit source (target or immediate)  |
| `ss`               | Any valid 16-bit source                       |
| `$`                | Flag name (incl. N$) in a conditional branch  |

Valid means "forms a defined operation".
S1C88 code requires immediate data be prefixed with `#` while PMAS does not. So keep this in mind when looking at variables like `x` in the operations lists below.

### Registers

Registers marked as `n/a` in the PMAS column did not have any equivalent.
Note that S1C88 does not allow access to the CB register and any operation which used in in PMAS will use NB in S1C88 tools.
Additionally, the CC register cannot be directly accessed by software and can only be used as a branch condition.

| PMAS register | S1C88 register | Description                                |
| ------------- | -------------- | ------------------------------------------ |
| A             | A              | data register A, the Accumulator           |
| B             | B              | data register B                            |
| BA            | BA             | BA pair register                           |
| H             | H              | data register H                            |
| L             | L              | data register L                            |
| HL            | HL             | index register HL                          |
| X or X1       | IX             | Index register IX                          |
| Y or X2       | IY             | Index register IY                          |
| SP            | SP             | Stack Pointer                              |
| N             | BR             | Base Register                              |
| F             | SC             | System Condition flags                     |
| n/a           | CC             | Custom Condition flags                     |
| PC            | PC             | Program Counter                            |
| U             | NB             | New code Bank register                     |
| V             | CB             | current Code Bank register                 |
| I             | EP             | Expand Page register                       |
| XI            | XP             | IX's expand Page register                  |
| YI            | YP             | IY's expand Page register                  |
| n/a           | IP             | Index Page pair register composed of YP:XP |

For brevity purposes, the few times X or Y are mentioned explicitly in the operations lists below, they will also imply the ability to use X1/X2 instead, respectively.

### Short list

A list with only the differences, combining aliases into one row and ignoring b/w suffixed ops.

| PMAS mnemonic           | S1C88 mnemonic |
| ----------------------- | -------------- |
| ADDC x,y / ADC x,y      | ADC x,y        |
| BCDD / UNPACK           | UPCK           |
| BCDE / PACK             | PACK           |
| BCDX t / SWAP t         | SWAP t         |
| CALL rr / CALR rr       | CARS rr        |
| CALL qqrr / CALR qqrr   | CARL qqrr      |
| CALL$ rr / CALR$ rr     | CARS $,rr      | 
| CALL$ qqrr / CALR$ qqrr | CARL $,qqrr    | 
| CMP x,y                 | CP x,y         |
| CMPN BA,mmnn            | ADC BA,#mmnn   |
| CMPN HL,mmnn            | ADC HL,#mmnn   |
| CMPN X,mmnn             | SBC BA,#mmnn   |
| CMPN Y,mmnn             | SBC HL,#mmnn   |
| DIV HL, A               | DIV            |
| EX BA,A / EXTS BA,A     | SEP            |
| INT kk                  | INT \[kk]      |
| J$ rr                   | JRS $,rr       |
| J$ qqrr                 | JRL $,qqrr     |
| JDBNZ rr / DJNZ rr      | DJR NZ,rr      |
| JINT kk                 | JP \[kk]       |
| JMP HL / JP HL          | JP HL          |
| JMP rr / JP rr          | JRS rr         |
| JMP qqrr / JP qqrr      | JRL qqrr       |
| MOV x,y / LD x,y        | LD x,y         |
| MOVX A,rp / LX A,rp     | LD A,er        |
| MOVX rp,x / LX rp,x     | LD er,x        |
| MUL L,A                 | MLT            |
| NOT t / CPL t           | CPL t          |
| POPA                    | POP ALL        |
| POPAX                   | POP ALE        |
| POPX                    | POP IP         |
| POPX HL                 | POP EP         |
| POPXXX                  | POP IP         |
| PUSHA                   | PUSH ALL       |
| PUSHAX                  | PUSH ALE       |
| PUSHX                   | PUSH IP        |
| PUSHX HL                | PUSH EP        |
| PUSHXXX                 | PUSH IP        |
| RETI                    | RETE           |
| RETSKIP                 | RETS           |
| RL t / ROL t            | RLC t          |
| RLC t / ROLC t          | RL t           |
| RR t / ROR t            | RRC t          |
| RRC t / RORC t          | RR t           |
| SAL t / SLA t           | SLA t          |
| SAR t / SRA t           | SRA t          |
| SHL t                   | SLL t          |
| SHR t                   | SRL t          |
| STOP                    | SLP            |
| SUBC x,y / SBC x,y      | SBC x,y        |
| TEST t,s / TST t,x      | BIT t,s        |
| XCHG x,y / EX x,y       | EX x,y         |

### Full list

A list of the full operations.

| PMAS mnemonic | S1C88 mnemonic        | Operation                                                 |
| ------------- | --------------------- | --------------------------------------------------------- |
| ADC x,y       | ADC x,y               | ADd with Carry                                            |
| ADCb t,s      | ADC t,s               | ADd with Carry (byte)                                     |
| ADCw rp,ss    | ADC rp,ss             | ADd with Carry (word)                                     |
| ADD x,y       | ADD x,y               | ADD                                                       |
| ADDb t,s      | ADD t,s               | ADD (byte)                                                |
| ADDw rp,ss    | ADD rp,ss             | ADD (word)                                                |
| ADDC x,y      | ADD x,y               | ADD with Carry                                            |
| ADDCb t,s     | ADD t,s               | ADD with Carry (byte)                                     |
| ADDCw rp,ss   | ADD rp,ss             | ADD with Carry (word)                                     |
| AND t,s       | AND t,s               | bitwise AND                                               |
| ANDb t,s      | AND t,s               | bitwise AND (byte)                                        |
| BCDD          | UPCK                  | BCD Decode / UnPaCK                                       |
| BCDE          | PACK                  | BCD Encode / PACK                                         |
| BCDX t        | SWAP t                | BCD eXchange / SWAP nibbles                               |
| CALL \[hhll]  | CALL \[hhll]          | CALL subroutine indirectly                                |
| CALL rr       | CARS rr               | CALL Relative Short subroutine                            |
| CALL qqrr     | CARL qqrr             | CALL Relative Long subroutine                             |
| CALLb rr      | CARS rr               | CALL Relative Short subroutine (byte)                     |
| CALLw qqrr    | CARL qqrr             | CALL Relative Long subroutine (word)                      |
| CALLC x       | CARS x / CARL x       | CALL Relative Short/Long if Carried                       |
| CALLCb rr     | CARS rr               | CALL Relative Short if Carried (byte)                     |
| CALLCw qqrr   | CARL qqrr             | CALL Relative Long if Carried (word)                      |
| CALLG rr      | CARS GT,rr            | CALL Relative Short if was Greater Than                   |
| CALLGE rr     | CARS GE,rr            | CALL Relative Short if was Greater than or Equal to       |
| CALLL rr      | CARS LT,rr            | CALL Relative Short if was Less Than                      |
| CALLLE rr     | CARS LE,rr            | CALL Relative Short if was Less than or Equal to          |
| CALLNC x      | CARS NC,x / CARL NC,x | CALL Relative Short/Long if Not Carried                   |
| CALLNCb rr    | CARS NC,rr            | CALL Relative Short if Not Carried (byte)                 |
| CALLNCw qqrr  | CARL NC,qqrr          | CALL Relative Long if Not Carried (word)                  |
| CALLNO rr     | CARS NV,rr            | CALL Relative Short if did Not OVerflow                   |
| CALLNS rr     | CARS P,rr             | CALL Relative Short if No Sign (i.e. Positive)            |
| CALLNZ x      | CARS NZ,x / CARL NZ,x | CALL Relative Short/Long if was Not Zero                  |
| CALLNZb rr    | CARS NZ,rr            | CALL Relative Short if was Not Zero (byte)                |
| CALLNZw qqrr  | CARL NZ,qqrr          | CALL Relative Long if was Not Zero (word)                 |
| CALLO rr      | CARS V,rr             | CALL Relative Short if OVerflowed                         |
| CALLS rr      | CARS M,rr             | CALL Relative Short if Minus Signed                       |
| CALLZ x       | CARS Z,x / CARL Z,x   | CALL Relative Short/Long if was Zero                      |
| CALLZb rr     | CARS Z,rr             | CALL Relative Short if was Zero (byte)                    |
| CALLZw qqrr   | CARL Z,qqrr           | CALL Relative Long if was Zero (word)                     |
| CALR \[hhll]  | CALL \[hhll]          | CALL Relative subroutine indirectly                       |
| CALR rr       | CARS rr               | CALL Relative Short subroutine                            |
| CALR qqrr     | CARL qqrr             | CALL Relative Long subroutine                             |
| CALRb rr      | CARS rr               | CALL Relative Short subroutine (byte)                     |
| CALRw qqrr    | CARL qqrr             | CALL Relative Long subroutine (word)                      |
| CALRC x       | CARS x / CARL x       | CALL Relative Short/Long if Carried                       |
| CALRCb rr     | CARS rr               | CALL Relative Short if Carried (byte)                     |
| CALRCw qqrr   | CARL qqrr             | CALL Relative Long if Carried (word)                      |
| CALRG rr      | CARS GT,rr            | CALL Relative Short if was Greater Than                   |
| CALRGE rr     | CARS GE,rr            | CALL Relative Short if was Greater than or Equal to       |
| CALRL rr      | CARS LT,rr            | CALL Relative Short if was Less Than                      |
| CALRLE rr     | CARS LE,rr            | CALL Relative Short if was Less than or Equal to          |
| CALRNC x      | CARS NC,x / CARL NC,x | CALL Relative Short/Long if Not Carried                   |
| CALRNCb rr    | CARS NC,rr            | CALL Relative Short if Not Carried (byte)                 |
| CALRNCw qqrr  | CARL NC,qqrr          | CALL Relative Long if Not Carried (word)                  |
| CALRNO rr     | CARS NV,rr            | CALL Relative Short if did Not OVerflow                   |
| CALRNS rr     | CARS P,rr             | CALL Relative Short if No Sign (i.e. Positive)            |
| CALRNZ x      | CARS NZ,x / CARL NZ,x | CALL Relative Short/Long if was Not Zero                  |
| CALRNZb rr    | CARS NZ,rr            | CALL Relative Short if was Not Zero (byte)                |
| CALRNZw qqrr  | CARL NZ,qqrr          | CALL Relative Long if was Not Zero (word)                 |
| CALRO rr      | CARS V,rr             | CALL Relative Short if OVerflowed                         |
| CALRS rr      | CARS M,rr             | CALL Relative Short if Minus Signed                       |
| CALRZ x       | CARS Z,x / CARL Z,x   | CALL Relative Short/Long if was Zero                      |
| CALRZb rr     | CARS Z,rr             | CALL Relative Short if was Zero (byte)                    |
| CALRZw qqrr   | CARL Z,qqrr           | CALL Relative Long if was Zero (word)                     |
| CINT kk       | INT \[kk]             | Call software INTerrupt                                   |
| CMP x,y       | CP x,y                | CoMPare and set flags                                     |
| CMPb t,s      | CP t,s                | CoMPare and set flags (byte)                              |
| CMPw rp,ss    | CP rp,ss              | CoMPare and set flags (word)                              |
| CMPN BA,mmnn  | ADC BA,#mmnn          | Some sort of bug?                                         |
| CMPN HL,mmnn  | ADC HL,#mmnn          | Some sort of bug?                                         |
| CMPN X,mmnn   | SBC BA,#mmnn          | Some sort of bug?                                         |
| CMPN Y,mmnn   | SBC HL,#mmnn          | Some sort of bug?                                         |
| CMPNw BA,mmnn | ADC BA,#mmnn          | Some sort of bug?                                         |
| CMPNw HL,mmnn | ADC HL,#mmnn          | Some sort of bug?                                         |
| CMPNw X,mmnn  | SBC BA,#mmnn          | Some sort of bug?                                         |
| CMPNw Y,mmnn  | SBC HL,#mmnn          | Some sort of bug?                                         |
| CPL t         | CPL t                 | 1s ComPLement                                             |
| CPLb t        | CPL t                 | 1s ComPLement (byte)                                      |
| DEC x         | DEC x                 | DECrement                                                 |
| DECb t        | DEC t                 | DECrement (byte)                                          |
| DECw rp       | DEC rp                | DECrement (word)                                          |
| DIV HL, A     | DIV                   | DIVide                                                    |
| DJNZ rr       | DJR NZ,rr             | Decrement b and Jump Relative if is Not Zero              |
| EX BA,A       | SEP                   | Sign EXpand to Pair register                              |
| EX x,y        | EX x,y                | EXchange                                                  |
| EXb A,s       | EX A,s                | EXchange (byte)                                           |
| EXw BA,rp     | EX BA,rp              | EXchange (word)                                           |
| EXTS BA,A     | SEP                   | Sign EXpand to Pair register                              |
| HALT          | HALT                  | set cpu to HALT mode                                      |
| INC x         | INC x                 | INCrement                                                 |
| INCb t        | INC t                 | INCrement (byte)                                          |
| INCw rp       | INC rp                | INCrement (word)                                          |
| INT kk        | INT \[kk]             | software INTerrupt                                        |
| JC x          | JRS C,x / JRL C,x     | Jump Relative Short/Long if Carried                       |
| JCb rr        | JRS C,rr              | Jump Relative Short if Carried (byte)                     |
| JCw qqrr      | JRL C,qqrr            | Jump Relative Long if Carried (word)                      |
| JDBNZ rr      | DJR NZ,rr             | Decrement B and Jump Relative if is Not Zero              |
| JG rr         | JRS GT,rr             | Jump Relative Short if was Greater Than                   |
| JGE rr        | JRS GE,rr             | Jump Relative Short if was Greater than or Equal to       |
| JINT kk       | JP \[kk]              | indirect JumP using INTerrupt vector                      |
| JL rr         | JRS LT,rr             | Jump Relative Short if was Less Than                      |
| JLE rr        | JRS LE,rr             | Jump Relative Short if was Less than or Equal to          |
| JMP HL        | JP HL                 | indirect JuMP using HL register                           |
| JMP x         | JRS x / JRL x         | JuMP Relative Short/Long                                  |
| JMPb rr       | JRS rr                | JuMP Relative Short (byte)                                |
| JMPw qqrr     | JRL qqrr              | JuMP Relative Long (word)                                 |
| JNC x         | JRS NC,x / JRL NC,x   | Jump Relative Short/Long if Not Carried                   |
| JNCb rr       | JRS NC,rr             | Jump Relative Short if Not Carried (byte)                 |
| JNCw qqrr     | JRL NC,qqrr           | Jump Relative Long if Not Carried (word)                  |
| JNO rr        | JRS NV,rr             | Jump Relative Short if did Not OVerflow                   |
| JNS rr        | JRS P,rr              | Jump Relative Short if No Sign (i.e. Positive)            |
| JNZ x         | JRS NZ,x / JRL NZ,x   | Jump Relative Short/Long if was Not Zero                  |
| JNZb rr       | JRS NZ,rr             | Jump Relative Short if was Not Zero (byte)                |
| JNZw qqrr     | JRL NZ,qqrr           | Jump Relative Long if was Not Zero (word)                 |
| JO rr         | JRS V,rr              | Jump Relative Short if OVerflowed                         |
| JP HL         | JP HL                 | indirect JumP using vector                                |
| JP x          | JRS x / JRL x         | JumP Relative Short/Long                                  |
| JPb rr        | JRS rr                | JumP Relative Short (byte)                                |
| JPw qqrr      | JRL qqrr              | JumP Relative Long (word)                                 |
| JS rr         | JRS M,rr              | Jump Relative Short if Minus Signed                       |
| JZ x          | JRS Z,x / JRL Z,x     | Jump Relative Short/Long if was Zero                      |
| JZb rr        | JRS Z,rr              | Jump Relative Short if was Zero (byte)                    |
| JZw qqrr      | JRL Z,qqrr            | Jump Relative Long if was Zero (word)                     |
| LD x,y        | LD x,y                | LoaD value into target                                    |
| LDb t,s       | LD t,s                | LoaD value into target                                    |
| LDw tt,ss     | LD tt,ss              | LoaD value into target                                    |
| LDX A,HL      | LD A,EP               | LoaD EXpand Page register for HL into A                   |
| LDX A,X       | LD A,XP               | LoaD eXpand Page register for IX into A                   |
| LDX A,Y       | LD A,YP               | LoaD eXpand Page register for IY into A                   |
| LDX HL,A      | LD EP,A               | LoaD A into EXpand Page register for HL                   |
| LDX HL,pp     | LD EP,#pp             | LoaD value into EXpand Page register for HL               |
| LDX X1,A      | LD XP,A               | LoaD A into eXpand Page register for IX                   |
| LDX X1,pp     | LD XP,#pp             | LoaD value into eXpand Page register for IX               |
| LDX X2,A      | LD YP,A               | LoaD A into eXpand Page register for IY                   |
| LDX X2,pp     | LD YP,#pp             | LoaD value into eXpand Page register for IY               |
| MOV x,y       | LD x,y                | MOVe/LoaD value into target                               |
| MOVb t,s      | LD t,s                | MOVe/LoaD value into target (byte)                        |
| MOVw tt,ss    | LD tt,ss              | MOVe/LoaD value into target (word)                        |
| MOVX A,HL     | LD A,EP               | MOVe/LoaD EXpand Page register for HL into A              |
| MOVX A,X1     | LD A,XP               | MOVe/LoaD eXpand Page register for IX into A              |
| MOVX A,X2     | LD A,YP               | MOVe/LoaD eXpand Page register for IY into A              |
| MOVX HL,A     | LD EP,A               | MOVe/LoaD A into EXpand Page register for HL              |
| MOVX HL,pp    | LD EP,#pp             | MOVe/LoaD value into EXpand Page register for HL          |
| MOVX X1,A     | LD XP,A               | MOVe/LoaD A into eXpand Page register for IX              |
| MOVX X1,pp    | LD XP,#pp             | MOVe/LoaD value into eXpand Page register for IX          |
| MOVX X2,A     | LD YP,A               | MOVe/LoaD A into eXpand Page register for IY              |
| MOVX X2,pp    | LD YP,#pp             | MOVe/LoaD value into eXpand Page register for IY          |
| MUL L,A       | MLT                   | MULTiply                                                  |
| NEG t         | NEG t                 | NEGate                                                    |
| NEGb t        | NEG t                 | NEGate                                                    |
| NOP           | NOP                   | No OPeration                                              |
| NOT t         | CPL t                 | bitwise NOT / 1s ComPLement                               |
| NOTb t        | CPL t                 | bitwise NOT / 1s ComPLement (byte)                        |
| OR t,s        | OR t,s                | bitwise OR                                                |
| ORb t,s       | OR t,s                | bitwise OR (byte)                                         |
| PACK          | PACK                  | PACK                                                      |
| POP x         | POP x                 | POP from stack                                            |
| POPb r        | POP r                 | POP from stack (byte)                                     |
| POPw rp       | POP rp                | POP from stack (word)                                     |
| POPA          | POP ALL               | POP ALL standard registers from stack                     |
| POPAX         | POP ALE               | POP ALl (incl. Expansion) registers from stack            |
| POPX          | POP IP                | POP eXpand Page registers for Indexers from stack         |
| POPX HL       | POP EP                | POP EXpand Page register for HL from stack                |
| POPXXX        | POP IP                | POP Indexers X1 and X2's eXpand Page registers from stack |
| PUSH x        | PUSH x                | PUSH to stack                                             |
| PUSHb r       | PUSH r                | PUSH to stack (byte)                                      |
| PUSHw rp      | PUSH rp               | PUSH to stack (word)                                      |
| PUSHA         | PUSH ALL              | PUSH ALL standard registers to stack                      |
| PUSHAX        | PUSH ALE              | PUSH ALl (incl. Expansion) registers to stack             |
| PUSHX         | PUSH IP               | PUSH eXpand Page registers for Indexers to stack          |
| PUSHX HL      | PUSH EP               | PUSH EXpand Page register for HL to stack                 |
| PUSHXXX       | PUSH IP               | PUSH Indexers X1 and X2's eXpand Page registers to stack  |
| RET           | RET                   | RETurn normally                                           |
| RETI          | RETE                  | RETurn from Interrupt / Exception                         |
| RETSKIP       | RETS                  | RETurn and SKIP 2 bytes ahead                             |
| RL t          | RLC t                 | Rotate Left _with**out**_ Carry                           |
| RLb t         | RLC t                 | Rotate Left _with**out**_ Carry (byte)                    |
| RLC t         | RL t                  | Rotate Left _with_ Carry                                  |
| RLCb t        | RL t                  | Rotate Left _with_ Carry (byte)                           |
| ROL t         | RLC t                 | ROtate Left _with**out**_ Carry                           |
| ROLb t        | RLC t                 | ROtate Left _with**out**_ Carry (byte)                    |
| ROLC t        | RL t                  | ROtate Left _with_ Carry                                  |
| ROLCb t       | RL t                  | ROtate Left _with_ Carry (byte)                           |
| ROR t         | RRC t                 | ROtate Right _with**out**_ Carry                          |
| RORb t        | RRC t                 | ROtate Right _with**out**_ Carry (byte)                   |
| RORC t        | RR t                  | ROtate Right _with_ Carry                                 |
| RORCb t       | RR t                  | ROtate Right _with_ Carry (byte)                          |
| RR t          | RRC t                 | Rotate Right _with**out**_ Carry                          |
| RRb t         | RRC t                 | Rotate Right _with**out**_ Carry (byte)                   |
| RRC t         | RR t                  | Rotate Right _with_ Carry                                 |
| RRCb t        | RR t                  | Rotate Right _with_ Carry (byte)                          |
| SAL t         | SLA t                 | Arithmetic Shift Left                                     |
| SALb t        | SLA t                 | Arithmetic Shift Left (byte)                              |
| SAR t         | SRA t                 | Arithmetic Shift Right                                    |
| SARb t        | SRA t                 | Arithmetic Shift Right (byte)                             |
| SBC x,y       | SBC x,y               | SuBtract with Carry                                       |
| SBCb t,s      | SBC t,s               | SuBtract with Carry (byte)                                |
| SBCw rp,ss    | SBC rp,ss             | SuBtract with Carry (word)                                |
| SHL t         | SLL t                 | Logical SHift Left                                        |
| SHLb t        | SLL t                 | Logical SHift Left (byte)                                 |
| SHR t         | SRL t                 | Logical SHift Right                                       |
| SHRb t        | SRL t                 | Logical SHift Right (byte)                                |
| SLA t         | SLA t                 | Arithmetic Shift Left                                     |
| SLAb t        | SLA t                 | Arithmetic Shift Left (byte)                              |
| SRA t         | SRA t                 | Arithmetic Shift Right                                    |
| SRAb t        | SRA t                 | Arithmetic Shift Right (byte)                             |
| STOP          | SLP                   | STOP everything and SLeeP                                 |
| SUB x,y       | SUB x,y               | SUBtract                                                  |
| SUBb t,s      | SUB t,s               | SUBtract (byte)                                           |
| SUBw rp,ss    | SUB rp,ss             | SUBtract (word)                                           |
| SUBC x,y      | SBC x,y               | SuBtract with Carry                                       |
| SUBCb t,s     | SBC t,s               | SuBtract with Carry (byte)                                |
| SUBCw rp,ss   | SBC rp,ss             | SuBtract with Carry (word)                                |
| SWAP t        | SWAP t                | SWAP nibbles                                              |
| TEST t,s      | BIT t,s               | TEST a BITmask                                            |
| TESTb t,s     | BIT t,s               | TEST a BITmask (byte)                                     |
| TST t,s       | BIT t,s               | TEST a BITmask                                            |
| TSTb t,s      | BIT t,s               | TEST a BITmask (byte)                                     |
| UNPACK        | UPCK                  | UNPACK                                                    |
| XCHG x,y      | EX x,y                | EXCHanGe bytes                                            |
| XCHGb t,s     | EX t,s                | EXCHanGe bytes                                            |
| XCHGw rp,rp   | EX rp,rp              | EXCHanGe bytes                                            |
| XOR t,s       | XOR t,s               | bitwise XOR                                               |
| XORb t,s      | XOR t,s               | bitwise XOR (byte)                                        |
