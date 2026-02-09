# LCD and LCD Driver

## LCD screen

* Dimensions:
  * Glass: 35mm x 32mm\* x 2mm
    * \* ~7mm of the top is for the driver chip and FPC connection and otherwise "empty" glass
  * Display area: approx. 28mm x 19.5mm
  * Reflector panel: approx. 34.8mm x 24.7mm
* Pixels: 96 x 64
* Markings on glass (display side):
  * Upper left: `A` centered over `F11`
  * Upper right: `7680`
  * A `+` on either side
  * Dots around where the FPC connects with lines above them that match to etched lines on the FPC
* Marking on FPC: `1012-90`

Taped to the plastic front with clear, double-sided 3 mm wide tape in a hollow rectangle shape, the rectangle being approx. 35.4mm x 27.6mm on the outside

The reflector is taped to the board with approx. 28mm (l) x 4mm (w) x 3.6mm (h) black foam tape

## S1D15xxx LCD driver

[S1D15000 Series Technical Manual](https://www.crystalfontz.com/controllers/uploaded/Epson%20S1D15605_SED1565_577706%20Tech%20Manual%20v1.1.pdf)

* Part number: S1D15605?xxxx??
  * S1 - Seiko Epson, previously SE
  * D - Model name: Driver
  * 15605 - Model number
  * ? - Shape (unknown)
  * xxxx - Specifications (unknown)
  * ?? - Packing specification (unknown)
* Supply voltage range: 1.8 to 5.5 V
* LCD voltage range: 4.5 to 16 V
* Duty: 1/65 (1/7, 1/9 bias)
* Segments: 132
* Commons: 65
* Display RAM: 132x65 = 8580 bits
* Microprocessor interface: 8-bit parallel
* Frequency: 33 KHz
* Package: Chip on Glass (COG)
* Built-in power circuit for LCD (DC/DCx4)

The driver runs in parallel mode (P/S = HIGH), master operation (M/S = HIGH), with the internal oscillator circuit disabled (C/S = LOW). Thus the CL line takes input from the MCU via OSC1 and the FR line switching resets register $8A to 1 and increases $81's frame counter by 1 (see page 8-29 for a diagram).

### Commands

To simplify interaction with the LCD, try [libpmdd](https://github.com/logicplace/libpmdd) instead of direct access.

LCD_CTRL is primarily used for sending commands to the LCD driver and is accessible through register $FE on the PM.

LCD_DATA is primarily used for sending display data to the LCD driver and is accessible through register $FF on the PM.

LCD_CTRL and LCD_DATA both write and read over the D0-D7 lines, it determines what operation is happening and whether CTRL or DATA is being read/written by the status of the A0, <u style="text-decoration:overline">RD</u>, & <u style="text-decoration:overline">WR</u> lines.

| A0 | <u style="text-decoration:overline">RD</u> | <u style="text-decoration:overline">WR</u> | R/W | CTRL/DATA |
|---|---|---| ----- | ---- |
| 0 | 0 | 1 | Read  | CTRL |
| 0 | 1 | 0 | Write | CTRL |
| 1 | 0 | 1 | Read  | DATA |
| 1 | 1 | 0 | Write | DATA |

#### Command list

Listed below are the commands, written to CTRL.

| Cmd #     | Command            | Command Code    | Hex range |
|----------:| ------------------ | --------------- | --------- |
| [1][]     | Display ON/OFF     | 1 0 1 0 1 1 1 x | $AE - $AF |
| [2][]     | Display start line | 0 1 a a a a a a | $40 - $7F |
| [3][]     | Set Page           | 1 0 1 1 a a a a | $B0 - $BF |
| [4a][4]   | Set Column HI      | 0 0 0 1 h h h h | $10 - $1F |
| [4b][4]   | Set Column LO      | 0 0 0 0 l l l l | $00 - $0F |
| [8][]     | ADC select         | 1 0 1 0 0 0 0 x | $A0 - $A1 |
| [9][]     | Invert             | 1 0 1 0 0 1 1 x | $A6 - $A7 |
| [10][]    | All on             | 1 0 1 0 0 1 0 x | $A4 - $A5 |
| [11][]    | LCD bias           | 1 0 1 0 0 0 1 x | $A2 - $A3 |
| [12][]    | Start RMW          | 1 1 1 0 0 0 0 0 | $E0       |
| [13][12]  | End RMW            | 1 1 1 0 1 1 1 0 | $EE       |
| [14][]    | Reset              | 1 1 1 0 0 0 1 0 | $E2       |
| [15][]    | Row direction      | 1 1 0 0 x - - - | $C0 - $CF |
| [16][]    | Power control      | 0 0 1 0 1 m m m | $28 - $2F |
| [17][]    | V5 resistor ratio  | 0 0 1 0 0 r r r | $20 - $27 |
| [18a][18] | Contrast           | 1 0 0 0 0 0 0 1 | $81       |
| [18b][18] | Contrast           | - - v v v v v v | $00 - $FF |
| [19a][19] | Static indicator   | 1 0 1 0 1 1 0 x | $AC - $AD |
| [19b][19] | Static indicator   | - - - - - - m m | $00 - $FF |
| [20][]    | Power saver        |                 |           |
| [21][]    | NOP                | 1 1 1 0 0 0 1 1 | $E3       |
| [22][]    | Test               | 1 1 1 1 - - - - | $F0 - $FF |

[1]: cmd/1.md
[2]: cmd/2.md
[3]: cmd/3.md
[4]: cmd/4.md
[5]: cmd/5.md
[6]: cmd/6.md
[7]: cmd/7.md
[8]: cmd/8.md
[9]: cmd/9.md
[10]: cmd/10.md
[11]: cmd/11.md
[12]: cmd/12.md
[14]: cmd/14.md
[15]: cmd/15.md
[16]: cmd/16.md
[17]: cmd/17.md
[18]: cmd/18.md
[19]: cmd/19.md
[20]: cmd/20.md
[21]: cmd/21.md
[22]: cmd/22.md

#### Writing to display RAM

Writes the byte to display RAM at the current cursor location then increments the cursor by 1. When the cursor reaches the end of the current page, it *does not* wrap around to the next page, you must do this manually.

The data sent is displayed in a column of the current page formed as 0bABCDEFGH being (when rows are...)

| Normal | Reversed |
|:------:|:--------:|
|   H    |    A     |
|   G    |    B     |
|   F    |    C     |
|   E    |    D     |
|   D    |    E     |
|   C    |    F     |
|   B    |    G     |
|   A    |    H     |

Then moves one column to the right (if ADC is normal) or left (if ADC is reversed).

#### Reading display RAM

TODO: how to read reliably

Reading from LCD_DATA reads the byte in display RAM where the cursor is currently. If the driver is currently operating in RMW mode, the cursor is not incremented after reading. Otherwise, it is incremented.

TODO: does ADC reverse reading direction?

#### Reading display status

Read from LCD_CTRL. TODO: how to read reliably

The returned byte contains status information in the upper nibble:

* D7 - BUSY - 1 = busy, 0 = not busy
  * "Busy" means doing some sort of internal process or reset, during which it cannot accept commands.
  * There's no need to check the busy signal.
* D6 - ADC - 0 = reverse, 1 = normal
  * This is opposite to the assignment command.
  * The command $A0 will cause this status bit to be 1.
  * The command $A1 will cause this status bit to be 0.
* D5 - ON/OFF - 0 = ON 1 = OFF
  * This is opposite to the assignment command.
  * The command $AE will cause this status bit to be 0.
  * The command $AF will cause this status bit to be 1.
* D4 - RESET - 1 = reset in progress

## FPC board connector pinout

TODO: orientation

1. VRS
2. V5
3. V4
4. V3
5. V2
6. V1
7. CAP2-
8. CAP2+
9. CAP1-
10. CAP1+
11. CAP3- (mislabled as CAP3+ in the block diagram)
12. VOUT
13. VSS (GND)
14. VDD (VCC)
15. D7
16. D6
17. D5
18. D4
19. D3
20. D2
21. D1
22. D0
23. <u style="text-decoration:overline">RD</u>
24. <u style="text-decoration:overline">WR</u>
25. A0
26. <u style="text-decoration:overline">RES</u>
27. CS
28. CL
29. FR
