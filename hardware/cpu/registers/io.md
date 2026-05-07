# I/O Ports (P ports)

The PM offers 7 or 8 bits of P ports. It's unclear if P07 is hooked up to anything.

All P ports have two registers:

* IOC0x - controls port direction: 1=Output, 0=Input
* P0xD - port data bit, writable when the respective IOC register is set to output, readable when it's set to input.

It's possible register $2062 is also related, but it's not known what it does, just that it's set to 0 in [init_io](../../../software/bios/disasm.md#user-content-01C8).

Not all ports are usable as both input and output on the PM. Each port comes with a mask option of using a resistor (default) or a gate direct.

The names such as IOC01, P01D, and P01 (where 0 is the byte and 1 is the bit index) are official in a sense, however no other S1C88 chip has a P ports register layout which only uses one set (byte) of ports, so it's possible the real names may be more like IOC1, P1D, P1.

## P00

IR Rx

P00D connects to the [GPIO0](../../board.md#user-content-cpu-30) pin which connects through TP5(RXD) test point to the RXD pin on the IrDA component.

The BIOS configures this as an input pin [here](../../../software/bios/disasm.md#user-content-01C5).

This could send data to TP5 if configured as an output pin.

Although it's technically possible to read when an IR signal is received via this register, it would be incredibly unreliable. So in order to check for a signal being received, use the [xP0](irq.md#xp0) interrupt instead, either via a handler or by polling the factor flag (retail games do some combination of both). See the [IR](../../ir.md) page for more information on how to do this.

## P01

IR Tx

P01D connects to the [GPIO1](../../board.md#user-content-cpu-29) pin which connects through TP4(TXD) test point to the TXD pin on the IrDA component.

The BIOS configures this as an output pin [here](../../../software/bios/disasm.md#user-content-01C5).

This could receive data from TP4 if configured as an input pin, with the understanding that it would also be sent to the IrDA.

The P01D register is used to send data over infrared. See the [IR](../../ir.md) page for more information on how to use it.

## P02

EEPROM Data

P02D connects to the [GPIO2](../../board.md#user-content-cpu-28) pin which connects to the SDA pin on the EEPROM.

The BIOS initially configures this as an input pin [here](../../../software/bios/disasm.md#user-content-01C5), but it's intended to be switched as needed.

See the [EEPROM](../../eeprom.md) page for more information on how to use it.

## P03

EEPROM Clock

P03D connects to the [GPIO3](../../board.md#user-content-cpu-27) pin which connects to the SCL pin on the EEPROM.

The BIOS initially configures this as an input pin [here](../../../software/bios/disasm.md#user-content-01C5), but it's intended to be switched as needed. Input is used as disabling clocking, the EEPROM does not output anything on this line.

See the [EEPROM](../../eeprom.md) page for more information on how to use it.

## P04

Rumble

P04D connects to the [GPIO4](../../board.md#user-content-cpu-26) pin which connects to PAD1 on the board (the rumble motor connects to this pad when the case is closed).

The BIOS configures this as an output pin [here](../../../software/bios/disasm.md#user-content-01C5).

This cannot be used as an input port. Configuring it as one is a simple way to disable rumble.

## P05

IR Disable

P05D connects to the [GPIO5](../../board.md#user-content-cpu-25) pin which connects to the PWDOWN on the IrDA component.

The BIOS configures this as an output pin [here](../../../software/bios/disasm.md#user-content-01C5).

Writing a 1 to this register causes the IrDA component to power down, writing a 0 will cause it to resume normal operation. (TODO: confirm)

There's nothing stopping it from being configured as an input port, but there are no connections to it besides the PWDOWN pin. It would only be useful to do if the IrDA component was replaced with something else. Though, similar to rumble, setting it to input would be a simple way to prevent it from being disabled, if that's useful...

## P06

Shock sensor

P06D connects to the <u style="text-decoration:overline">[SHOCK](../../board.md#user-content-cpu-24)</u> pin which connects to the shock sensor's pad 1. The shock sensor itself is labeled SW2 on the board.

The BIOS configures this as an input pin [here](../../../software/bios/disasm.md#user-content-01C5).

When this is 1, the sensor's reed is not in contact; when it's 0, the reed is in contact. Because of how instantaneous this moment is, it's unreliable to poll this value. Software should instead use the [xP6](irq.md#xp6) interrupt instead. If polling is preferred, poll (and then reset) FP6 instead of P06D.
