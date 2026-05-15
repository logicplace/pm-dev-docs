# Cartridge

*For the cartridge header used for software, see [here](./cpu/memory.md#cartridge-memory)*

A commercial Pokémon mini cartridge is a 512 KiB ROM with a staggered 32-pin connector. The pins as well as an unnecessary border around the top have an ENIG finish.

To open the case, there are two Y1 tri-wing screws on the back. Once removed, slide the front half of the case downward then it's free to remove. The board will just fall out.

When in its case, much of the front of the board is covered by the sticker; only the ROM chip is visible. The back is in full view, and is a silk-screen containing a logo, copyright, and cartridge code: MIN-KCM1-01.

TODO: board scans

The board is approximately:

* Width: 27.7 mm (generally)
* Screw hole cutouts diameter: 4.5 mm
* Height: 23 mm
* Thickness: 1 mm thick

## Shells

The ornamental design patent is [USD478127](https://patents.google.com/patent/USD478127S1/en?oq=USD478127).

The case is approximately:

* Width: 33.5 mm
* Height: 26.5 mm (back), 33 mm (arc of the rounded part)
* Thickness: 1 mm (most of the plastic), 5.1 mm (back to sticker), 8.2 mm (thickest)

There are a handful of shell designs which fit commercial game PCBs and [flash carts](./flash_carts) which are compatible with it.

* By [Ksanto](https://www.thingiverse.com/thing:3592237), designed for [DITTO mini][] but also works for [PokeCard 512 rev 2+][]
  * Based on Ksanto's, by [4thAxisDesign](https://www.thingiverse.com/thing:6660072), offers a version with a hole (positioned for the [PokeCard 512 rev 2+][] and [DITTO mini][]) and one without, as well as using the notch on the bottom shell by [AlexiG](https://www.thingiverse.com/thing:5894655) to support the [PokMini][] PCBs.
* By [cyborg_ar](/assets/img/cart/aftermarket/cyborg_ar_2018-12-03.png) which was intended for [DITTO mini][] but never got a hole. STLs were never released nor was the shell finished.
* By [Pikpol](/assets/img/cart/aftermarket/pikpol_shell_clear.jpg), also in [yellow](/assets/img/cart/aftermarket/pikpol_shell_yellow.jpg), which was intended for [DITTO mini][]. STLs were never released.

[DITTO mini]: ./flash_carts/ditto.md
[PokeCard 512 rev 2+]: ./flash_carts/pokecard.md
[PokMini]: ./flash_carts/pokmini.md

## Using this document

On this board, all chips are on one side. We describe locations using the following abbreviations: top-left (TL), top-right (TR), middle-left (ML), middle-right (MR), bottom-left (BL), and bottom-right (BR).

For our purposes, bottom refers to where the pins are, such that `CN1` can be read correctly.

## Legend

The purpose of the circled I mark is possibly the board manufacturer.

There's a single digit printed on the right side, above B1, with unclear purpose. On my JP Party mini it's a 6. Possibly a 1-digit serial.

An `M 1` is printed between the CN1 text and the pins, which is possibly the board revision, as the sample cart has `F 0` here instead. This is from the code printed on the back, MIN-KC**M1**-01 or MIN-KC**F0**-01.

There is a 01 printed under the TSOP diagram which likely reflects the 01 from the product code printed on the back (MIN-KCM1-**01**). It does not appear to be a board revision as the sample cart, which has a different layout, also uses 01. It's possible that it refers to the year, 2001. However, no 02 release is known.

There is a graphic masked onto the board which looks like a rectangle with 0 or more dots inside and the corners marked 1 (TL), 6 (TR), 7 (BL), 12 (BR). It does not correspond with the ROM pins and is unclear what else it might refer to.

* C - Capacitor
* CN - Connector
* R - Resistor
* U - Unit: ROM

## Capacitors

All capacitors are surface mounted (SMD) multilayer ceramic capacitors (MLCC).

| Label        | Populated? | Location           | Capacitance |
| ------------ | ---------- | ------------------ | ----------- |
| <a id="user-content-c1">C1</a>  | yes        | MR, left of [C3][] | ?           |
| <a id="user-content-c2">C2</a>  | yes        | middle             | ?           |
| <a id="user-content-c3">C3</a>  | yes        | MR                 | ?           |
| <a id="user-content-c4">C4</a>  | yes        | ML                 | ?           |

[C1]: #user-content-c1
[C2]: #user-content-c2
[C3]: #user-content-c3
[C4]: #user-content-c4

## CN1

This refers to the pins. The top row is labeled B1 (on the right) and B17 (on the left). The community has had two methods of referring to the other row of pins: the right-most being either B1.5 or A1. Here, we prefer A1.

The pitch between two pins on the same row is 1 mm, making the pitch between two pins on opposite rows 0.5 mm. B1 and B17 are shaped like MissingNo. All the A pins are rounded on top and have through-holes on the top, they are slightly taller and narrower than the B pins. All the B pins except 1, 16, and 17 are rounded on top and have traces connecting upward. B16 is rectangular, but otherwise the same dimensions as the other B pins.

Pin A1 is attached to the large B1 contact and pin A16 is attached to the large B17 contact.

I/O listed from the perspective of [U1][]. PS = Power Supply.

TODO: confirm voltage, is it really 3.3v ??

<table>
<thead>
<tr>
<th align="center">Contact</th>
<th align="center"><a href="./board.md#cn4">CN4</a> pin</th>
<th>Name</th>
<th align="center">I/O</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><a id="user-content-b1">B1</a></td>
<td align="center">1</td>
<td>V<span style="font-size:smaller">DD</span></td>
<td align="center">PS</td>
<td>Stepped down from V<span style="font-size:smaller">CC</span></td>
</tr>
<tr>
<td align="center"><a id="user-content-a1">A1</a></td>
<td align="center">2</td>
<td>V<span style="font-size:smaller">DD</span></td>
<td align="center">PS</td>
<td>Stepped down from V<span style="font-size:smaller">CC</span></td>
</tr>
<tr>
<td align="center"><a id="user-content-b2">B2</a></td>
<td align="center">3</td>
<td>A20</td>
<td align="center">I</td>
<td>Address bit 20</td>
</tr>
<tr>
<td align="center"><a id="user-content-a2">A2</a></td>
<td align="center">4</td>
<td>A9</td>
<td align="center">I</td>
<td>Address bit 9 when LALE=high, 19 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b3">B3</a></td>
<td align="center">5</td>
<td>A8</td>
<td align="center">I</td>
<td>Address bit 8 when LALE=high, 18 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a3">A3</a></td>
<td align="center">6</td>
<td>A7</td>
<td align="center">I</td>
<td>Address bit 7 when LALE=high, 17 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b4">B4</a></td>
<td align="center">7</td>
<td>A6</td>
<td align="center">I</td>
<td>Address bit 6 when LALE=high, 16 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a4">A4</a></td>
<td align="center">8</td>
<td>A5</td>
<td align="center">I</td>
<td>Address bit 5 when LALE=high, 15 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b5">B5</a></td>
<td align="center">9</td>
<td>A4</td>
<td align="center">I</td>
<td>Address bit 4 when LALE=high, 14 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a5">A5</a></td>
<td align="center">10</td>
<td>A3</td>
<td align="center">I</td>
<td>Address bit 3 when LALE=high, 13 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b6">B6</a></td>
<td align="center">11</td>
<td>A2</td>
<td align="center">I</td>
<td>Address bit 2 when LALE=high, 12 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a6">A6</a></td>
<td align="center">12</td>
<td>A1</td>
<td align="center">I</td>
<td>Address bit 1 when LALE=high, 11 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b7">B7</a></td>
<td align="center">13</td>
<td>A0</td>
<td align="center">I</td>
<td>Address bit 0 when LALE=high, 10 when HALE=high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a7">A7</a></td>
<td align="center">14</td>
<td>V<span style="font-size:smaller">DD</span></td>
<td align="center">PS</td>
<td>Stepped down from V<span style="font-size:smaller">CC</span></td>
</tr>
<tr>
<td align="center"><a id="user-content-b8">B8</a></td>
<td align="center">15</td>
<td>HALE</td>
<td align="center">I</td>
<td>High address bits are latched when HALE is high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a8">A8</a></td>
<td align="center">16</td>
<td>-</td>
<td align="center">-</td>
<td>No pad</td>
</tr>
<tr>
<td align="center"><a id="user-content-b9">B9</a></td>
<td align="center">17</td>
<td>LALE</td>
<td align="center">I</td>
<td>Low address bits are latched when LALE is high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a9">A9</a></td>
<td align="center">18</td>
<td>GND</td>
<td align="center">PS</td>
<td>Ground</td>
</tr>
<tr>
<td align="center"><a id="user-content-b10">B10</a></td>
<td align="center">19</td>
<td>D0</td>
<td align="center">I/O</td>
<td>Data bit 0</td>
</tr>
<tr>
<td align="center"><a id="user-content-a10">A10</a></td>
<td align="center">20</td>
<td>D1</td>
<td align="center">I/O</td>
<td>Data bit 1</td>
</tr>
<tr>
<td align="center"><a id="user-content-b11">B11</a></td>
<td align="center">21</td>
<td>D2</td>
<td align="center">I/O</td>
<td>Data bit 2</td>
</tr>
<tr>
<td align="center"><a id="user-content-a11">A11</a></td>
<td align="center">22</td>
<td>D3</td>
<td align="center">I/O</td>
<td>Data bit 3</td>
</tr>
<tr>
<td align="center"><a id="user-content-b12">B12</a></td>
<td align="center">23</td>
<td>D4</td>
<td align="center">I/O</td>
<td>Data bit 4</td>
</tr>
<tr>
<td align="center"><a id="user-content-a12">A12</a></td>
<td align="center">24</td>
<td>D5</td>
<td align="center">I/O</td>
<td>Data bit 5</td>
</tr>
<tr>
<td align="center"><a id="user-content-b13">B13</a></td>
<td align="center">25</td>
<td>D6</td>
<td align="center">I/O</td>
<td>Data bit 6</td>
</tr>
<tr>
<td align="center"><a id="user-content-a13">A13</a></td>
<td align="center">26</td>
<td>D7</td>
<td align="center">I/O</td>
<td>Data bit 7</td>
</tr>
<tr>
<td align="center"><a id="user-content-b14">B14</a></td>
<td align="center">27</td>
<td>OE</td>
<td align="center">I</td>
<td>Output Enable. CPU reading data when OE is high</td>
</tr>
<tr>
<td align="center"><a id="user-content-a14">A14</a></td>
<td align="center">28</td>
<td>IRQ</td>
<td align="center">O</td>
<td>Causes [Cartridge IRQ][] when IRQ is high</td>
</tr>
<tr>
<td align="center"><a id="user-content-b15">B15</a></td>
<td align="center">29</td>
<td>WE</td>
<td align="center">I</td>
<td>Write Enable</td>
</tr>
<tr>
<td align="center"><a id="user-content-a15">A15</a></td>
<td align="center">30</td>
<td>CS</td>
<td align="center">I</td>
<td>Chip Select</td>
</tr>
<tr>
<td align="center"><a id="user-content-b16">B16</a></td>
<td align="center">31</td>
<td>CARD_N</td>
<td align="center">O</td>
<td>Card detect. Active-low. Connected to GND</td>
</tr>
<tr>
<td align="center"><a id="user-content-a16">A16</a></td>
<td align="center">32</td>
<td>GND</td>
<td align="center">PS</td>
<td>Ground</td>
</tr>
<tr>
<td align="center"><a id="user-content-b17">B17</a></td>
<td align="center">33</td>
<td>GND</td>
<td align="center">PS</td>
<td>Ground</td>
</tr>
</tbody>
</table>

## Resistors

| Label        | Populated? | Location            | Resistance |
| ------------ | ---------- | ------------------- | ---------- |
| <a id="user-content-r1">R1</a>  | yes        | ML, right of [C1][] | ?          |
| <a id="user-content-r2">R2</a>  | yes        | ML, right of [R1][] | ?          |

[R1]: #user-content-r1
[R2]: #user-content-r2

## U1

On commercial ROMs this is a MX23L4004-12A mask ROM chip. It's a 32-TSOP, 20 mm wide x 8 mm tall.

Seemingly no other Macronix chip uses this address demuxing scheme and the datasheet is not available.

* MX - Manufacturer (Macronix International Co., Ltd.)
* 23 - Type: Mask ROM
* L - Voltage: 2.7 ~ 3.6V
* 4 - Density: 4 Megabit (512 KiB)
* 004 - Options?? at least indicates 32-pin somehow
* 12 - Speed?: 120ns??
* A - Parallel

### Pins

There is a dot marking pin 1 on the ROM chip itself, and an arrow pointing to it on the board. It's located at the bottom-right of the chip.

Presumably pins 1 and 24 are the real power supply pins, unclear what the rest are doing. At most, other Macronix ROMs from around this time have two VSS pins, meaning either 13 or 16 might be real too.

I/O listed from the perspective of the ROM. PS = Power Supply.

|    Pin #    | Name   | I/O | Description               |
|:-----------:| ------ |:---:| ------------------------- |
| <a id="user-content-rom-1">1</a>  | VCC    | PS  | Power supply pin          |
| <a id="user-content-rom-2">2</a>  | A20    |  I  | Address input bit 20      |
| <a id="user-content-rom-3">3</a>  | A9/A19 |  I  | Address input bit 9/19    |
| <a id="user-content-rom-4">4</a>  | A8/A18 |  I  | Address input bit 8/18    |
| <a id="user-content-rom-5">5</a>  | A7/A17 |  I  | Address input bit 7/17    |
| <a id="user-content-rom-6">6</a>  | A6/A16 |  I  | Address input bit 6/16    |
| <a id="user-content-rom-7">7</a>  | A5/A15 |  I  | Address input bit 5/15    |
| <a id="user-content-rom-8">8</a>  | A4/A14 |  I  | Address input bit 4/14    |
| <a id="user-content-rom-9">9</a>  | A3/A13 |  I  | Address input bit 3/13    |
| <a id="user-content-rom-10">10</a> | A2/A12 |  I  | Address input bit 2/12    |
| <a id="user-content-rom-11">11</a> | A1/A11 |  I  | Address input bit 1/11    |
| <a id="user-content-rom-12">12</a> | A0/A10 |  I  | Address input bit 0/10    |
| <a id="user-content-rom-13">13</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-rom-14">14</a> | HALE   |  I  | High Address Latch Enable |
| <a id="user-content-rom-15">15</a> | LALE   |  I  | Low Address Latch Enable  |
| <a id="user-content-rom-16">16</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-rom-17">17</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-rom-18">18</a> | CE     |  I  | Chip Enable               |
| <a id="user-content-rom-19">19</a> | WE     |  I  | Probably not connected    |
| <a id="user-content-rom-20">20</a> | OE     |  I  | Output Enable input       |
| <a id="user-content-rom-21">21</a> | VCC    |  I  | Power supply pin          |
| <a id="user-content-rom-22">22</a> | D7     |  O  | Data output bit 7         |
| <a id="user-content-rom-23">23</a> | D6     |  O  | Data output bit 6         |
| <a id="user-content-rom-24">24</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-rom-25">25</a> | D5     |  O  | Data output bit 5         |
| <a id="user-content-rom-26">26</a> | D4     |  O  | Data output bit 4         |
| <a id="user-content-rom-27">27</a> | D3     |  O  | Data output bit 3         |
| <a id="user-content-rom-28">28</a> | VCC    |  I  | Power supply pin          |
| <a id="user-content-rom-29">29</a> | D2     |  O  | Data output bit 2         |
| <a id="user-content-rom-30">30</a> | D1     |  O  | Data output bit 1         |
| <a id="user-content-rom-31">31</a> | D0     |  O  | Data output bit 0         |
| <a id="user-content-rom-32">32</a> | VCC    |  I  | Power supply pin          |

## Sample cartridge

The sample cart is a flash cartridge distributed to (likely) reporters in Japan at the time. One sample cart (00954) has been dumped, which contained the full release version of Pokémon Party mini (JP). However the chip is 2 MiB and it has not had the full memory dumped.

![sample board photo front](/assets/img/cart/sample_front.jpg)
![sample board photo back](/assets/img/cart/sample_back.jpg)
![sample cart comparison](/assets/img/cart/sample_cart_compare.jpg)

The label on the cart says:

* SAMPLE
* 00954
* ポケモンミニ専用カートリッジ MIN-002
  * T/L: Pokémon mini Sample Cartridge
* Pokémon mini
* In the PM: 22
* © 2001 NINTENDO

The back silk-screen has a nintendo logo at the top on the console shape, a different font for the Pokémon mini text, and MIN-KCFO-01 next to the copyright where "Nintendo" would be on commercial carts.

The layout of the components is different, presumably due to the different width of U1. But they do seem to be the same components.

| Component | Location        |
| --------- | --------------- |
| [C1][]    | MR              |
| [C2][]    | middle          |
| [C3][]    | TR, above C1    |
| [C4][]    | TL, above R1    |
| [R1][]    | ML              |
| [R2][]    | ML, right of R1 |

### U1

This is a SST39VN016-120-4C-WH flash chip which is a 32-pin version of the typically 40-pin [SST39VF016](https://www.backoldgaming.com/data/medias/files/39vf016/SST39VF080_SiliconStorageTechnology.pdf). However it should be software compatible, so even if the BIOS does not refer to this chip, it should be mostly compatible with its dev cart functions.

* SST - Manufacturer (Silicon Storage Technology, Inc.)
* 39 - Product Series: Multi-Purpose Flash
* V - 2.7-3.6V
* N - ???
* 016 - Device Density: 16 Megabit (2 MiB)
* 120 - Read Access Speed: 120 ns
* 4 - Minimum Endurance: 10,000 cycles
* C - Temperature Range: Commercial (0⁰C to +70⁰C)
* W - Package Type: TSOP
* H - Package Modifier: 32 leads

#### Pins

Due to the expensive nature of this item, the board should not be disassembled, and the exact trace and pinout will likely remain unknown.

The chip has a dot indicating pin 1 and an arrow on the board, same as commercial boards.

|    Pin #    | Name   | I/O | Description               |
|:-----------:| ------ |:---:| ------------------------- |
| <a id="user-content-mpf-1">1</a>  | A20    |  I  | Address input bit 20      |
| <a id="user-content-mpf-2">2</a>  | A9/A19 |  I  | Address input bit 9/19    |
| <a id="user-content-mpf-3">3</a>  | ?      |  ?  |                           |
| <a id="user-content-mpf-4">4</a>  | ?      |  ?  |                           |
| <a id="user-content-mpf-5">5</a>  | ?      |  ?  |                           |
| <a id="user-content-mpf-6">6</a>  | ?      |  ?  |                           |
| <a id="user-content-mpf-7">7</a>  | VDD    | PS  | Power supply pin          |
| <a id="user-content-mpf-8">8</a>  | VSS    | PS  | Ground pin                |
| <a id="user-content-mpf-9">9</a>  | ?      |  ?  |                           |
| <a id="user-content-mpf-10">10</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-11">11</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-12">12</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-13">13</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-14">14</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-15">15</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-16">16</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-17">17</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-mpf-18">18</a> | VSS    | PS  | Ground pin                |
| <a id="user-content-mpf-19">19</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-20">20</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-21">21</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-22">22</a> | VSS    | PS  | Data output bit 7         |
| <a id="user-content-mpf-23">23</a> | VDD    | PS  | Power supply pin          |
| <a id="user-content-mpf-24">24</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-25">25</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-26">26</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-27">27</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-28">28</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-29">29</a> | VDD    | PS  | Power supply pin          |
| <a id="user-content-mpf-30">30</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-31">31</a> | ?      |  ?  |                           |
| <a id="user-content-mpf-32">32</a> | ?      |  ?  |                           |

## My JP Party mini markings

* On the inside face of the front part, each in rectangles: F >ABS< 1-8
* On the inside face of the back part, each in rectangles: B >ABS< 1-4
* On the outside face of the back, centered in a square:
  * Nintendo logo
  * MODEL NO.
  * MIN-002
  * PAT. PEND.
  * MADE IN JAPAN
* The rectangle: two circles in the bottom right of it
* Above B1: 6
* Under CN1: M 1
* Right of CN1: 01
* Back: ©2001 Nintendo  MIN-KCM1-01
* There are two circles on the edge of the right screw hole cutout and half of one on the left's
* U1, 4 lines:
  * J014220-M
  * MX23L4004-12A
  * MIN-MPTJ-0 E
  * 1R6601A1