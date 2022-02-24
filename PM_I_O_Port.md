## Pokémon mini I/O Port Overview

The Pokémon mini provides a tri-state 8-bit I/O port. Each bit is mapped to a different pin, and each has it's own configurable direction, providing a relatively powerful interface to external hardware.

The I/O interface is shared among various parts of hardware, so care must be taken when altering the direction and data as not to disturb other processes.

| Pin | Function                                |
| --- | --------------------------------------- |
| 0   | IR Receiver                             |
| 1   | IR Transmitter                          |
| 2   | EEPROM Data                             |
| 3   | EEPROM Clk                              |
| 4   | Rumble Motor                            |
| 5   | IR Disable                              |
| 6   | Always 1 (Pull-Up?)                     |
| 7   | (IR Transmitter? Used to double power?) |

**Pin Mapping**

## How the I/O Port Works

The I/O Port is configured using 2 8-bit registers. IO_DIR selects the data direction of the respective pin. Reset is an input bit, Set is an output pin. IO_DATA provides both a input read value as well as the latch to drive output, the value read back from this port depends on the state of IO_DIR.

When a pin is set to input, and there is no data being externally driven on the pin, the state is left undetermined as that bit is defined as floating.

## Hardware

The EEPROM is a [24xx64](http://ww1.microchip.com/downloads/en/devicedoc/21189f.pdf) alike 64 kbit serial EEPROM using an I2C interface.

Rumble is simply a pin used to drive a motor, which is likely driven through an amplifier. For rumble to be active, the rumble pin must be set for output with a logical 1 driving the pin.

IR is a unmodulated diode transceiver. Setting the IR Disable to output and setting data to logical 1, disables the receiver.
