## S1C88 Overview

**NOTE: WE NEED TO REFACTOR ALL OF THIS TO ACCOMIDATE THE ACTUAL CORE
USED**

The S1C88 is an 8-bit microcontroller with 16-bit operations (designed
by Timex, now Epson).The processor provides numerous addressing modes
with a 24bit addressing bus (with only 21bits mapped externally)

[Epson S1C88 Core
manual](http://www.epsondevice.com/webapp/docs_ic/DownloadServlet?id=ID001149)

Additionally, the Minx provides the capibility to handle up to 32
hardware enabled interrupts with delayed response capbility. Up to 128
interrupt vectors may be specified, allowing the remaining 96 for BIOS
calls.

The CPU is clocked at 4.00mhz, although the processor operates on a 4
cycle data access period, leaving the system with a theoretical limit of
1MIPS.

  - [Instruction Set](S1C88_InstructionSet.md "wikilink")
  - [Interrupt Hardware](PM_IRQs.md "wikilink")

## Minx Register Mapping

The Minx operates with a handful of registers. The CPU is an
amalgamation of Z80 like paradigms combined with an 8-bit
microcontroller like bank system.

<table>
<tbody>
<tr class="odd">
<td><table>
<caption><strong>General Purpose Registers</strong></caption>
<thead>
<tr class="header">
<th><p>8 Bit Registers (Low)</p></th>
<th><p>8 Bit Registers (Hi)</p></th>
<th><p>16 Bit Register</p></th>
<th><p>Index Register</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>A</p></td>
<td><p>B</p></td>
<td><p>BA</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>L</p></td>
<td><p>H</p></td>
<td><p>HL</p></td>
<td><p>I</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>N</p></td>
<td></td>
<td><p>I</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>X</p></td>
<td><p>Xi</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><p>Y</p></td>
<td><p>Yi</p></td>
</tr>
</tbody>
</table></td>
<td><p>  </p></td>
<td><table>
<caption><strong>Fixed Function Registers</strong></caption>
<thead>
<tr class="header">
<th><p>Register</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PC</p></td>
<td><p>Program Cursor</p></td>
</tr>
<tr class="even">
<td><p>V</p></td>
<td><p>PC Bank Register</p></td>
</tr>
<tr class="odd">
<td><p>U</p></td>
<td><p>V Delay Register</p></td>
</tr>
<tr class="even">
<td><p>SP</p></td>
<td><p>Stack Pointer</p></td>
</tr>
<tr class="odd">
<td><p>F</p></td>
<td><p>Flag Register</p></td>
</tr>
<tr class="even">
<td><p>E</p></td>
<td><p>Exception Register</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

Since the program cursor is only 16 bits, it uses a special "delayed"
register to account for the upper 8 bits of program access space. When
PC has it's [most significant bit](most_significant_bit.md "wikilink") set,
the register V takes the place of the upper 8 bits, extending PC out to
23 bits in total. To prevent bank switch problems, V is "delayed" by the
means of register U. After each branch instruction, the value of U is
copied to register V implicitly, allowing for full 23bit jumps without
special programming tricks or special functions.

The Minx also provides additional facilities to access 24bit addresses
using registers. X and Y both provide 24bit addresses using the Xi and
Yi register as their upper 8
bits.

## Flag and Exception Register

| Bit | Flag                                       | F. Mne. | Exception | E. Mne. |
| --- | ------------------------------------------ | ------- | --------- | ------- |
| 0   | Zero                                       | Z       | ??        | EX0     |
| 1   | Carry                                      | C       | ??        | EX1     |
| 2   | Overflow                                   | O       | ??        | EX2     |
| 3   | Sign                                       | S       | ??        | EX3     |
| 4   | Binary Coded Decimal Mode (8-bit add\\sub) | BCD     |           |         |
| 5   | Low-Mask Mode (8-bit add\\sub)             | NIBBLE  |           |         |
| 6   | Interrupt Disable                          | ID      |           |         |
| 7   | Interrupt Branch                           | IB      |           |         |

**Flag Mapping**

While the F register can, in some cases, be treated as a general purpose
8-bit register, the exception register however is not directly
accessible by any conventional means. It is also to be noted that the
exception trapping needs to be "enabled" by some means we've not
discovered yet. Division by zero causes the system to hard lock, and the
existence of this register is only known through the reverse engineering
of Pokemon Channel's internal emulator. The lower 4 bits of both
registers are used for branch conditions and carry chaining for
arithmetic. The upper 4 bits are "control" registers.

## The I register

Unlike X and Y, the upper 8 bits of the remaining addressing modes are
not unique. The register I provides a bank extension to the these
remaining 24 bit accesses: \[HL\], \[I+$nnnn\], and \[N+$nn\]. It is
generally good practice to maintain I as $00 unless otherwise necessary.

## The N indexed mode

The N Indexed mode is most useful for accessing register memory quickly.
N provides the mid byte of a 24 bit addressing mode, and the $nn is an
8-bit immediate. In example. \[N+$8A\] would point to $208A (VPU_CNT)
if N = $20 and I = $00. It is rare to see N with any value other than
$20, but it is not entirely out of the question to see it change.