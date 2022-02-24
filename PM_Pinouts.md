## Cartridge Pinouts

| Conn. | Card  | TSOP   | Name    | Direction | Function                                                                                 |
| ----- | ----- | ------ | ------- | --------- | ---------------------------------------------------------------------------------------- |
| 1     | B1    | note 1 | VCC     | .         | Power supply.                                                                            |
| 2     | B1.5  | note 1 | VCC     | .         | Power supply.                                                                            |
| 3     | B2    | 2      | A20     | OUT       | Address bit 20.                                                                          |
| 4     | B2.5  | 3      | A9/A19  | OUT       | Address bit 9 is latched when LALH is high. Address bit 19 is latched when HALH is high. |
| 5     | B3    | 4      | A8/A18  | OUT       | Address bit 8 is latched when LALH is high. Address bit 18 is latched when HALH is high. |
| 6     | B3.5  | 5      | A7/A17  | OUT       | Address bit 7 is latched when LALH is high. Address bit 17 is latched when HALH is high. |
| 7     | B4    | 6      | A6/A16  | OUT       | Address bit 6 is latched when LALH is high. Address bit 16 is latched when HALH is high. |
| 8     | B4.5  | 7      | A5/A15  | OUT       | Address bit 5 is latched when LALH is high. Address bit 15 is latched when HALH is high. |
| 9     | B5    | 8      | A4/A14  | OUT       | Address bit 4 is latched when LALH is high. Address bit 14 is latched when HALH is high. |
| 10    | B5.5  | 9      | A3/A13  | OUT       | Address bit 3 is latched when LALH is high. Address bit 13 is latched when HALH is high. |
| 11    | B6    | 10     | A2/A12  | OUT       | Address bit 2 is latched when LALH is high. Address bit 12 is latched when HALH is high. |
| 12    | B6.5  | 11     | A1/A11  | OUT       | Address bit 1 is latched when LALH is high. Address bit 11 is latched when HALH is high. |
| 13    | B7    | 12     | A0/A10  | OUT       | Address bit 0 is latched when LALH is high. Address bit 10 is latched when HALH is high. |
| 14    | B7.5  | note 1 | VCC     | .         | Power supply.                                                                            |
| 15    | B8    | 14     | HALE    | OUT       | High address bits are latched when HALE is high.                                         |
| 16    | .     | .      | .       | .         | No pad on cartridge.                                                                     |
| 17    | B9/M1 | 15     | LALE    | OUT       | Low address bits are latched when LALE is high.                                          |
| 18    | B9.5  | note 2 | GND     | .         | Ground.                                                                                  |
| 19    | B10   | 31     | D0      | BIDIR     | Data bit 0 is output when OE is high.                                                    |
| 20    | B10.5 | 30     | D1      | BIDIR     | Data bit 1 is output when OE is high.                                                    |
| 21    | B11   | 29     | D2      | BIDIR     | Data bit 2 is output when OE is high.                                                    |
| 22    | B11.5 | 27     | D3      | BIDIR     | Data bit 3 is output when OE is high.                                                    |
| 23    | B12   | 26     | D4      | BIDIR     | Data bit 4 is output when OE is high.                                                    |
| 24    | B12.5 | 25     | D5      | BIDIR     | Data bit 5 is output when OE is high.                                                    |
| 25    | B13   | 23     | D6      | BIDIR     | Data bit 6 is output when OE is high.                                                    |
| 26    | B13.5 | 22     | D7      | BIDIR     | Data bit 7 is output when OE is high.                                                    |
| 27    | B14   | 20     | OE      | OUT       | Output Enable. Data bits are output when OE is high.                                     |
| 28    | B14.5 | .      | IRQ     | IN        | Cause "Cartridge IRQ" interrupt when IRQ go high.                                        |
| 29    | B15   | 19     | WE      | OUT       | Write Enable. Pulled down with 100K in cartridge.                                        |
| 30    | B15.5 | 18     | CS      | OUT       | Chip select. Enables chip control. Pulled down with 100K in cartridge.                   |
| 31    | B16   | .      | CARD_N  | IN        | Card detect. Active-low. It is connected to GND in the cartridge.                        |
| 32    | B16.5 | note 2 | GND     | .         | Ground.                                                                                  |
| 33    | B17   | note 2 | GND     | .         | Ground.                                                                                  |

**note 1:** VCC on pin 1,21,28,32. LVTTL.

**note 2:** GND on pin 13,16,17,24.

**note 3:** Directions are relative to the system

## Abbreviations

PM = Pokémon Mini

IN = Input

OUT = Output

BIDIR = Bi-Directional

TSOP = Thin Small Outline Package

LVTTL = Low Voltage Transistor-Transistor Level (3.3 Volt)

ROM = Read Only Memory

ALH = Address Latch High

OE = Output Enable

A? = Address signal

CS? = Chip Select

VCC = Power supply

GND = Signal ground

## TSOP Chip

```
   MX23L4004    TSOP package
.-------------/ /-------------.
|  1 VCC               VCC 32 |
|  2 A20               D0  31 |
|  3 A9/A19            D1  30 |
|  4 A8/A18            D2  29 |
|  5 A7/A17            VCC 28 |
|  6 A6/A16            D3  27 |
|  7 A5/A15            D4  26 |
|  8 A4/A14            D5  25 |
|  9 A3/A13            GND 24 |
| 10 A2/A12            D6  23 |
| 11 A1/A11            D7  22 |
| 12 A0/A10            VCC 21 |
| 13 GND               OE  20 |
| 14 HALE              WE  19 |
| 15 LALE              CS  18 |
| 16 GND               GND 17 |
`-------------/ /-------------'
```

## PCB silk screen text

"MIN-KCM1-01"

"4M MASKROM" (4 Mbit)

Pads B1 to B17 are labeled.

## IC U1

"MX23L4004-12A" (Macronix)

"MIN-MPBE-0 E" (Mini PinBall)

TSOP
