## Interrupt Overview

The Minx provides up to 32 hardware mapped interrupts and up to 96 software interrupts (for bios calls). The full list is defined in the [BIOS section](PM_Bios.md "wikilink") of the standard. Out of the 32 interrupts, three are not maskable, $00\~$02.

On startup, **IRQ 0 (reset)** fires. Since BIOS resets the processor state, it is unknown if this behaves like a normal IRQ.

## Interrupt Priority

The Minx interrupt hardware is impressive in it's configurability. The 29 maskable interrupts are divided into 9 groups. Each of these groups are then provided a 2 bit priority encoder. These encoders define the order in which IRQs are processed. IRQs are processed by priority first, then by the internal IRQ number. If an IRQ group is assigned a priority of 0, all the IRQs for the group are implicity disabled.

## Enabling Interrupts

All 29 of the maskable interrupts can be disabled in 3 ways. The first way is if the interrupt disable flag or interrupt branch flag is set in the Flag register. This will prevent all maskable IRQs from occuring. The 2nd is by setting the IRQ group priority to zero. Finally, you can reset the effective bit in the IRQ_ENA_\* register. If any of these three conditions occur, the IRQ is effectively disabled.

Note: If registers V and U are different, IRQ will not be called.

## When Interrupts Occur

IRQs are set to "pending" on the rising edge of an event. Since IRQs are not nessessarly processed immediately, they will remain in a waiting state. This is where the IRQ_ACT_\* registers come in. At any point an IRQ is enabled, and the respective bit in an IRQ_ACT_\* is set. The down side to this is the IRQ will continue to fire until software clears the bit by writing a logical '1' to the bit in IRQ_ACT_\*.

After an IRQ branch occurs, the interrupt branch flag is set, preventing IRQs from colliding with one another.

## What is Not Known

It is unknown which interrupts are masked by the interrupt disable flag. Additionally, there are aproximately 7 hardware interrupts which have not been mapped and as such we don't know entire know all the details of their behavior.
