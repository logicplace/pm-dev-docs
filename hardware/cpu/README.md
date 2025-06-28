# S1C88V20 Core

The S1C88V20 is an 8-bit microcontroller with 16-bit operations (designed by Timex, now Epson), part of the S1C88 processor family. The processor provides numerous addressing modes with a 24-bit addressing bus. In the PM's case, only 21 bits are mapped externally.

[Epson S1C88 Core manual](http://www.epsondevice.com/webapp/docs_ic/DownloadServlet?id=ID001149)

Additionally, the S1C88V20 provides the capability to handle up to 32 exception processing vectors with delayed response capability. Up to 128 interrupt vectors may be specified, allowing the remaining 96 for BIOS calls.

The CPU is clocked at 4.00 MHz, although the processor operates on a 4 cycle data access period, leaving the system with a theoretical limit of 1 MIPS.

- [Instruction Set](S1C88_InstructionSet.md)
- [The Memory Map](Memory.md)
  - [The Hardware Registers](Registers.md)
- [Internal BIOS](BIOS.md)
- [Interrupts](Interrupts.md)
- [Oscillators & Timers](../Timers.md)
- [I/O](IO.md)
- [Audio / Sound](Sound.md)
- [LCD Controller](LCD_Controller.md)
- [Standby modes](Standby.md)

## Registers

The S1C88V20 operates with a handful of registers. The CPU is an amalgamation of Z80 like paradigms combined with something similar to a typical 8-bit microcontroller bank system.

Here, _#hh_ and _#ll_ are immediate data used for addressing operations. _00_ is a fixed zero value and blank means the option is not available. Not having a page register means there is no method of using it for indirectly addressing data.

| Page | 16-bit | 8-bit Hi | 8-bit Lo | Description                    |
|:----:|:------:|:--------:|:--------:| ------------------------------ |
|      | `BA`   | `B`      | `A`      | Data register                  |
| `EP` | `HL`   | `H`      | `L`      | Index or data register         |
| `EP` |        | `BR`     | _#ll_    | Base register                  |
| `EP` |        | _#hh_    | _#ll_    | Absolute addressing            |
| `XP` | `IX`   |          |          | Index register                 |
| `YP` | `IY`   |          |          | Index register                 |
| `CB` | `PC`   |          |          | Code bank and program counter  |
| `NB` |        |          |          | New code bank                  |
| _00_ | `SP`   |          |          | Stack pointer                  |
|      |        |          | `SC`     | System condition flags         |
|      |        |          | `CC`     | Custom condition flags         |
|      | `IP`   | `XP`     | `YP`     | Index pages (only in PUSH/POP) |

### BA pair register

This is a general purpose data register which decomposes into the accumulator, A, and B. This register is most frequently used in arithmetic and data transfer. It cannot be used for indirect addressing.

### HL pair register

This is a general purpose indexing register which decomposes into the general purpose data registers H and L. L in particular as some special uses, such as acting as an offset in indirect addressing as well as its use in the MLT operation.

### BR register

BR-based addressing is most useful for accessing register memory quickly. BR provides the mid byte of a 24-bit addressing mode, and the _#ll_ is an 8-bit immediate. For example, `[BR:8Ah]` would point to $208A (VPU_CNT) if BR = 20h and EP = 00h. It is rare to see BR with any value other than 20h, but it is not entirely out of the question to change it.

### IX and IY registers

These are general-purpose registers intended for indirect addressing. They use XP and YP as their page registers, respectively.

### Page registers

In order to access 24-bit addresses using registers, separate page registers are available. IX and IY both provide 24-bit addresses using the XP and YP registers, respectively, as their uppermost 8 bits. HL, BR, and absolute addressing use the Expand Page register, EP, for selecting the page. It is generally good practice to maintain EP as 00h unless otherwise necessary.

### PC register

Since the program cursor is only 16 bits, it uses a special "delayed" register to account for the upper 8 bits of program access space. When PC has its [most significant bit](/Glossary.md#significant-bits) set, the register CB takes the place of the upper 8 bits, extending PC out to 23 bits in total. To prevent bank switch problems, CB is "delayed" by the means of register NB. After each branch instruction, the value of NB is copied to register CB implicitly, allowing for full 23 bit jumps without special programming tricks or special functions.

### SP register

The stack pointer, as the name implies, points to the top of the stack. It may point anywhere between $1EFF and $1FFF (the bottom of the RAM). The stack expands upwards from the bottom and the heap refers to whatever space is above SP, that is, the portion of the potential stack space which is not currently allocated by the stack.

### SC and CC registers

| Bit | SC | Description       | CC | Description |
| --- | -- | ----------------- | -- | ----------- |
| 0   | Z  | Zero              | F0 | Div by 0*   |
| 1   | C  | Carry             | F1 | ??          |
| 2   | V  | Overflow          | F2 | ??          |
| 3   | N  | Negative          | F3 | ??          |
| 4   | D  | Decimal mode      |    |             |
| 5   | U  | Unpack mode       |    |             |
| 6   | I0 | Interrupt bit 0   |    |             |
| 7   | I1 | Interrupt bit 1   |    |             |

While the SC register can, in some cases, be treated as a general purpose 8-bit register, the exception register however is not directly accessible by any conventional means. It is also to be noted that the exception trapping needs to be "enabled" by some means we've not discovered yet.

Division by zero causes the physical system to hard lock, but it is available in Pokémon Channel's emulator.

The lower 4 bits of both registers are used for branch conditions and C is used for carry chaining in certain arithmetic operations. The upper 4 bits control certain functionality.

While the below sections describe some generalities, not all operations will affect or use all flags. Check each operation's documentation for how it uses them.

#### Zero flag

If some arithmetic operation results in a 0, this flag is set to 1; otherwise, it's reset to 0. For example, if A=10 and we perform the operation `cp A,10` then Z=1, because 10 minus 10 is 0.

#### Carry flag

The carry flag has a different function for each arithmetic operation. See each one to understand how it works. For CP, the operation for which conditional jumps are most often used, carry is set when the signed result of the subtraction results in a negative number. That is, in `cp A,B` when A is less than B.

#### Overflow flag

The overflow flag is set when the signed value overflows, that is, loops around. For 8-bit registers this means if you subtract from -128, causing it to underflow back to (or past) 127; or if you add to 127 causing it to overflow the other way. For 16-bit registers this range is -32768~32767.

#### Negative flag

For most operations, this is a copy of the [most significant bit](/Glossary.md#significant-bits), which represents whether or not a signed value is negative. As expected, 0 is positive and 1 is negative.

#### Decimal mode

For operations which support this mode, it causes the operation to treat the operands as being in Binary Coded Decimal form. The exact mechanics of which are described in each supporting operator's documentation.

In this mode, only Z and C flags can be set. V and N are always reset to 0. 

#### Unpack mode

For operations which support this mode, it essentially reduces the register from being a signed 8-bit register to a signed 4-bit register. After performing the operation, the upper 4 bits are set to 0.

Setting flags works the same as normal, except that they too only consider the lower 4 bits.

#### Interrupt flags

These two bits describe the minimum priority level for interrupts to fire. Essentially, this compares the values you set to the interrupt priority registers (or a value of 3 for non-maskable interrupts) to this value. If the priority is strictly greater than this value, it will fire.

After an interrupt fires, this flag will represent the priority of the fired interrupt and must be changed for it to fire again.

For more information, see the [Interrupts](Interrupts.md) page.
