## Program Rendering Chip Overview

Since the Pokemon Mini does not drive a conventional display, it does
not operate like typical display driver. The PRC was created as a method
for driving a serial LCD display. It's entire purpose is to
[blit](Blitter.md "wikilink") images from various locations in memory to an
internal frame buffer, and then force it out to GDRAM in on the [LCD
Controller](LCD_Controller.md "wikilink"). This is all done transparently.

The PRC operates by monitoring a display counter that can be accessed by
reading [PRC_CNT (Reg $8A)](PM_Registers.md "wikilink"), which overflows
65 times a frame (each frame is approx. 72 Hz), and a PRC rate divider
[PRC_RATE (Reg $81)](PM_Registers.md "wikilink") that will trigger the PRC
rendering process. When the counter reaches specific values between the
matching rate divider, the PRC triggers various components. It can
operates in 2 modes, "Rendering + Frame Copy" and "Frame Copy Only".

During these various stages, the CPU is halted, and yields the bus to
the PRC. Depending on the enabled stages, the PRC will read various
locations from memory (cartridge and ram) and build a frame buffer to
$1000 \~ $12FF. Depending on the PRC rate divider and the enabled modes,
developers lose varying amounts of processor time.

Since all three display stages can be enabled or disabled independently,
users can perform a number of tricks such as multiplexing sprites (by
disabling frame copy on even frames, and map copy on odd frames,
changing the sprites each time), running in a pure frame-buffered mode,
or simply use the LCD controller manually by disabling the VPU all
together. (This effect is demonstrated in pokemon shock tetris)

The PRC shares ram with the CPU, so the more modes that are enabled, the
less ram is usable by the developer (see [PM RAM
Layout](PM_RAM#RAM_Layout.md "wikilink")).

Two IRQs are associated with the PRC, one associated with the Map and
Sprite stage, and one with the Frame Copy stage. After Frame Copy is
finished, a "PRC Render Done" IRQ fires. This event latches even if the
PRC has both the map and sprite renderer disabled, so this should be
taken into account. After the frame is copied to the LCD, the "PRC Frame
Copy" IRQ fires. It is not yet known if this fires if the frame copy is
disabled.

It is not uncommon for commercial games to disable the render done IRQ,
and simply probe the strobe manually. Shock tetris uses this to double
the number of on screen sprites.

## Map Rendering Stage

Stage 1 of the PRC is a map renderer. This stage can render a variable
size 8x8 tile based map to the frame buffer (located at $1000). This
mode operates by using a 24bit address [PRC_MAP_\* (Reg $82 to
$84)](PM_Registers.md "wikilink") as the base for the tile set, and a tile
map located at $1360. This stage is enabled by using bit 2 of [PRC_MODE
(Reg $80)](PM_Registers.md "wikilink").

| Mode | Size    |
| ---- | ------- |
| 0    | 12 x 16 |
| 1    | 16 x 12 |
| 2    | 24 x 8  |
| 3    | 24 x 16 |

**Map Modes**

Tile maps are arranged in left to right order, wrapping around to the
next
line.

|    |       |       |       |       |       |       |       |       |       |       |       |       |
| -- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|    | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | 11    |
| 0  | $1360 | $1361 | $1362 | $1363 | $1364 | $1365 | $1366 | $1367 | $1368 | $1369 | $136A | $136B |
| 1  | $136C | $136D | $136E | $136F | $1370 | $1371 | $1372 | $1373 | $1374 | $1375 | $1376 | $1377 |
| 2  | $1378 | $1379 | $137A | $137B | $137C | $137D | $137E | $137F | $1380 | $1381 | $1382 | $1383 |
| 3  | $1384 | $1385 | $1386 | $1387 | $1388 | $1389 | $138A | $138B | $138C | $138D | $138E | $138F |
| 4  | $1390 | $1391 | $1392 | $1393 | $1394 | $1395 | $1396 | $1397 | $1398 | $1399 | $139A | $139B |
| 5  | $139C | $139D | $139E | $139F | $13A0 | $13A1 | $13A2 | $13A3 | $13A4 | $13A5 | $13A6 | $13A7 |
| 6  | $13A8 | $13A9 | $13AA | $13AB | $13AC | $13AD | $13AE | $13AF | $13B0 | $13B1 | $13B2 | $13B3 |
| 7  | $13B4 | $13B5 | $13B6 | $13B7 | $13B8 | $13B9 | $13BA | $13BB | $13BC | $13BD | $13BE | $13BF |
| 8  | $13C0 | $13C1 | $13C2 | $13C3 | $13C4 | $13C5 | $13C6 | $13C7 | $13C8 | $13C9 | $13CA | $13CB |
| 9  | $13CC | $13CD | $13CE | $13CF | $13D0 | $13D1 | $13D2 | $13D3 | $13D4 | $13D5 | $13D6 | $13D7 |
| 10 | $13D8 | $13D9 | $13DA | $13DB | $13DC | $13DD | $13DE | $13DF | $13E0 | $13E1 | $13E2 | $13E3 |
| 11 | $13E4 | $13E5 | $13E6 | $13E7 | $13E8 | $13E9 | $13EA | $13EB | $13EC | $13ED | $13EE | $13EF |
| 12 | $13F0 | $13F1 | $13F2 | $13F3 | $13F4 | $13F5 | $13F6 | $13F7 | $13F8 | $13F9 | $13FA | $13FB |
| 13 | $13FC | $13FD | $13FE | $13FF | $1400 | $1401 | $1402 | $1403 | $1404 | $1405 | $1406 | $1407 |
| 14 | $1408 | $1409 | $140A | $140B | $140C | $140D | $140E | $140F | $1410 | $1411 | $1412 | $1413 |
| 15 | $1414 | $1415 | $1416 | $1417 | $1418 | $1419 | $141A | $141B | $141C | $141D | $141E | $141F |

'''Mapping of 12x16

The value in the tile map then points to an 8 byte tile. The location of
the tile is specified by (Tile \* 8 +
[PRC_MAP_\*](PM_Registers.md "wikilink")). The tiles are encoded in
vertical strips, each 8 pixel strip = 1 byte. The strips are encoded
with the least significant bit on the top, shifting by one bit right as
it scans vertically. The PRC can also invert the graphics as it renders
them by setting the appropriate bit in [PRC_MODE (Reg
$80)](PM_Registers.md "wikilink").

Maps can be offset up to 127 pixels vertically or horizontally
([PRC_SCROLL_X (Reg. $86)](PM_Registers.md "wikilink") and
[PRC_SCROLL_Y (Reg. $85)](PM_Registers.md "wikilink")), and is clamped to
the size of the map itself, writes to the scroll registers when the
value is out of bounds does not update the location in which rendering
begins, but the values of the registers themselves changes.
Interestingly, these values are only verified when the register is
written, and changing the tile map size will result in maps rendering
gibberish tiles.

Under no circumstances do the maps wrap. To create smooth scrolling, the
entire map must be rewritten to simulate wrap around.

## Sprite Rendering Stage

After the map rendering stage, the Sprite Rendering stage takes effect.
The PRC allows for 24 16x16 on screen sprites per frame, which can be
positioned anywhere on screen.

Sprites are controlled by 24, 4 byte attribute blocks located between
$1300 \~
$135F.

| Address | 7           | 6                 | 5            | 4             | 3               | 2 | 1 | 0 |
| ------- | ----------- | ----------------- | ------------ | ------------- | --------------- | - | - | - |
| 0       |             | Sprite X Position |              |               |                 |   |   |   |
| 1       |             | Sprite Y Position |              |               |                 |   |   |   |
| 2       | Sprite Tile |                   |              |               |                 |   |   |   |
| 3       |             | Enable            | Invert Color | Vertical Flip | Horizontal Flip |   |   |   |

**Sprite Attribute Blocks**

The Position operates on a virtual (128x128) screen, with is positioned
at (-16,-16) on the frame buffer. This allows for sprites to be
positioned partially off screen on all sides. The MSB of both coordinate
elements are ignored, so it can wrap around if care is not taken.

Sprite Tiles are loaded using [PRC_SPR_\* (Reg. $87 to
$89)](PM_Registers.md "wikilink") as the base address, with sprites tiles
being 64 bytes in length (making a full tile set 16kB).

Sprites are rendered by using 8 tiles, 4 mask and 4 graphic. The mask
tiles use a set pixel to signify which bits are to be left alone and
which bits are to be overwritten with the graphic bits. A set bit leaves
a pixel unchanged. The tiles are formatted in the same way as the Map
tiles.

The 8 tiles (in order) are: Mask (0,0) Mask (0,8) Graphic (0,0) Graphic
(0,8) Mask (8,0) Mask (8,8) Graphic (8,0) Graphic (8,8)

Here is a graphical representation <small>(taken from <em>The Unofficial
Poke Doc</em> as distributed with
<em>PoKeKaMini</em>)</small>:

<div style="text-align:center">

<div style="width:300px;margin:0px auto;border:1px solid #999;text-align:center;padding:12px;">

|                    |                    |
| ------------------ | ------------------ |
| **1<sup>st</sup>** | **5<sup>th</sup>** |
| **2<sup>nd</sup>** | **6<sup>th</sup>** |
| **3<sup>rd</sup>** | **7<sup>th</sup>** |
| **4<sup>th</sup>** | **8<sup>th</sup>** |

**Sprite**

<small style="line-height:1em"> White square = Draw
Dark square = Mask
<span style="line-height:2.4em">VRAM = (VRAM & MASK) | (DRAW &
\~MASK);</span> </small>

**DRAW**:
 0 = white (black if inverted)
 1 = black (white if inverted)

**MASK**:
 0 = opaque
 1 = transparent

</div>

</div>

Sprites are rendered in reverse order, so Sprite \#0 would always been
on top. This means internally sprite \#23 is drawn first, followed by
\#22 up to \#0 (painter's order)

## Frame Copy Stage

The third and final stage is the simplest of all the PRC functions. It
simply sequentially moves the $300 bytes from $1000\~$12FF to the GDRAM
of the [LCD Controller](LCD_Controller.md "wikilink"). This mode can be
disabled independently of all the other modes allowing for advanced
rendering techniques by sacrificing frame rate.

## PRC Timing Information

The PRC timing is controlled by two registers, the PRC counter [PRC_CNT
(Reg. $8A)](PM_Registers.md "wikilink"), and a frame divider. The frame
counter move between the values $01 to $41, and overflows approximately
72 times per second (4,000,000 / 55634). As previously mentioned, this
counter controls when the PRC fires the various display stages. These
stages do not fire every time, however. The PRC is configured to skip a
certain number of display cycles, only activating once every Nth frames
as configured by [PRC_RATE (Reg. $81)](PM_Registers.md "wikilink"). The
top four bits of [PRC_RATE (Reg. $81)](PM_Registers.md "wikilink") is the
current state of the divider, it counts up from 0, resetting when it
reaches the specified divider value. The PRC only renders and copies
when the PRC divider is at it's absolute maximum for the configured
divide rate.

| Rate | Divider |
| ---- | ------- |
| 0    | 3       |
| 1    | 6       |
| 2    | 9       |
| 3    | 12      |
| 4    | 2       |
| 5    | 4       |
| 6    | 6       |
| 7    | 8       |

**PRC Rate Values**

There is no known way to use the PRC to use the full 72hz update
frequency. This can be circumvented by directly accessing GDRAM through
the [LCD Controller](LCD_Controller.md "wikilink")

<table>
<caption><strong>The stages trigger based on <a href="PM_Registers" title="wikilink">PRC_CNT (Reg. $8A)</a> when rate divider match <a href="PM_Registers" title="wikilink">PRC_RATE (Reg. $81)</a>, CPU is stalled in the middle of the process.</strong></caption>
<thead>
<tr class="header">
<th><p>Mode</p></th>
<th><p><a href="PM_Registers" title="wikilink">PRC_MODE (Reg $8A)</a></p></th>
<th><p>PRC_CNT Start</p></th>
<th><p>PRC_CNT End</p></th>
<th><p>PRC_CNT Time</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Rendering + Frame Copy</p></td>
<td><p>(7:0) xxxx101x<br />
(7:0) xxxx110x<br />
(7:0) xxxx111x<br />
</p></td>
<td><p>$17</p></td>
<td><p>$03</p></td>
<td><p>44 (67.7% PRC, 32.3% Free)</p></td>
</tr>
<tr class="even">
<td><p>Frame Copy only</p></td>
<td><p>(7:0) xxxx100x</p></td>
<td><p>$38</p></td>
<td><p>$03</p></td>
<td><p>11 (16.9% PRC, 83.1% Free)</p></td>
</tr>
<tr class="odd">
<td><p>No Rendering</p></td>
<td><p>(7:0) xxxx0xxx</p></td>
<td><p>N/A</p></td>
<td><p>N/A</p></td>
<td><p>0 (0.0% PRC, 100.0% Free)</p></td>
</tr>
</tbody>
</table>

x - Not important

The time for each logical frame is 55634 cycles + a few (Determined by
time between Frame Copy interrupts) and the time between each PRC
counter increment is approximately between 867 Cycles and 839 Cycles
(855 Cycles Average).

The time was determined by:

`MOV BA, [0x2036]     ;  Read Timer`
`MOV [NN+0x30], $8F   ;  Reset Timer to FFFF`

The extra cycles is the amount of time between the \[0x2036\] read and
the \[NN+0x30\] write, which is either or 6 and 8 cycles. Since we are
operating off a /2 divider, the error is also divided by two.

My estimation is it is 55638, since it is the first closest value
divisible by $42