# Supply Voltage Detection circuit

The PM uses a SVD cicuit similar to the ones in the [S1C88649](../s1c88/649.md) and [S1C88848](../s1c88/848.md).

The procedure to use this can be taken from [the BIOS](../../../software/bios/disasm.md#user-content-check_voltage). A summary of the steps:

1. Set the criteria voltage (SVDS)
2. Set SVDON to 1
3. Wait ~200 cycles (with OSC3 clocking the CPU). This *should* be 100 µsec
4. Set SVDON to 0
5. Read SVDDT

The BIOS sets SVDS to 0b1000. It is unconfirmed what the criteria voltages are and the two chips above provide very different values for them. It's also unconfirmed what the minimum wait time after turning on the SVD is, but we can assume the BIOS is accurate.

Running the SVD increases current consumption and should not be run frequently. Developers should not ever need to run it manually as it's run by the BIOS during system startup.

## SVDDT

$2010 bit 5 is a read-only register.

SVD Detection data

The result of the SVD operation. A value of 0 indicates normal levels (supply voltage >= criteria voltage) and a value of 1 indicates that the supply voltage is low.

This register is read-only.

This is the official register name.

## SVDON

$2010 bit 4 is a R/W register.

SVD circuit on/off

Write 1 to turn the SVD on and 0 to turn it back off. You will only get an accurate reading in SVDDT if you wait long enough before turning it back off, presumably 100 µsec.

The state can be read back.

This is the official register name.

## SVDS

$2010 bits 3~0 is a R/W register.

SVD criteria voltage Setting

Although the criteria voltages are unconfirmed, the table from the [S1C88848](../s1c88/848.md) is reproduced here, as the wait time the PM uses matches the minimum wait time for this chip.

| SVDS3~SVDS0 | Criteria voltage (V) |
|:-----------:|:--------------------:|
|   1 1 1 1   | 4.35                 |
|   1 1 1 0   | 4.17                 |
|   1 1 0 1   | 4.00                 |
|   1 1 0 0   | 3.83                 |
|   1 0 1 1   | 3.67                 |
|   1 0 1 0   | 3.50                 |
|   1 0 0 1   | 3.33                 |
|   1 0 0 0   | 3.17                 |
|   0 1 1 1   | 3.00                 |
|   0 1 1 0   | 2.83                 |
|   0 1 0 1   | 2.67                 |
|   0 1 0 0   | 2.50                 |
|   0 0 1 1   | 2.33                 |
|   0 0 1 0   | 2.17                 |
|   0 0 0 1   | 2.00                 |
|   0 0 0 0   | 1.83                 |

This is the official register name.
