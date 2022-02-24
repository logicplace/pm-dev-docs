## RAM Overview

The memory used in the Pokemon Mini is general purpose static ram. It is
high speed and there is no performance hit for accessing it other than
the instruction processing speed. The biggest problem with the system is
that the ram is small, and also shared with the [picture rendering
chip](PM_PRC.md "wikilink"). Sections of this memory can be disabled, but
up to 1248 bytes of 4k can be re-purposed for video.

General purpose memory is considered unused and is safe for all use at
any time. Disabling various parts of the [picture rendering
chip](PM_PRC.md "wikilink") can free up additional memory.

## RAM Layout

<table>
<caption><strong>Memory layout schema's</strong></caption>
<tbody>
<tr class="odd">
<td><table>
<caption><strong>PRC rendering sprites with Tile Map 0, 1 or 2</strong></caption>
<thead>
<tr class="header">
<th><p>Start</p></th>
<th><p>End</p></th>
<th><p>Size</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$1000</p></td>
<td><p>$12FF</p></td>
<td><p>$0300 (768B)</p></td>
<td><p><a href="PM_PRC#Frame_Copy_Stage" title="wikilink">Frame Buffer</a></p></td>
</tr>
<tr class="even">
<td><p>$1300</p></td>
<td><p>$135F</p></td>
<td><p>$0060 (96B)</p></td>
<td><p><a href="PM_PRC#Sprite_Rendering_Stage" title="wikilink">Sprite Attributes</a></p></td>
</tr>
<tr class="odd">
<td><p>$1360</p></td>
<td><p>$141F</p></td>
<td><p>$00C0 (192B)</p></td>
<td><p><a href="PM_PRC#Map_Rendering_Stage" title="wikilink">Tile Map</a></p></td>
</tr>
<tr class="even">
<td><p>$1420</p></td>
<td><p>$1FFF</p></td>
<td><p>$0BE0 (3040B)</p></td>
<td><p>General Purpose Memory</p></td>
</tr>
</tbody>
</table>
<table>
<caption><strong>PRC rendering sprites with Tile Map 3</strong></caption>
<thead>
<tr class="header">
<th><p>Start</p></th>
<th><p>End</p></th>
<th><p>Size</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$1000</p></td>
<td><p>$12FF</p></td>
<td><p>$0300 (768B)</p></td>
<td><p><a href="PM_PRC#Frame_Copy_Stage" title="wikilink">Frame Buffer</a></p></td>
</tr>
<tr class="even">
<td><p>$1300</p></td>
<td><p>$135F</p></td>
<td><p>$0060 (96B)</p></td>
<td><p><a href="PM_PRC#Sprite_Rendering_Stage" title="wikilink">Sprite Attributes</a></p></td>
</tr>
<tr class="odd">
<td><p>$1360</p></td>
<td><p>$14DF</p></td>
<td><p>$0180 (384B)</p></td>
<td><p><a href="PM_PRC#Map_Rendering_Stage" title="wikilink">Tile Map</a></p></td>
</tr>
<tr class="even">
<td><p>$14E0</p></td>
<td><p>$1FFF</p></td>
<td><p>$0B20 (2848B)</p></td>
<td><p>General Purpose Memory</p></td>
</tr>
</tbody>
</table></td>
<td><table>
<caption><strong>PRC rendering only sprites</strong></caption>
<thead>
<tr class="header">
<th><p>Start</p></th>
<th><p>End</p></th>
<th><p>Size</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$1000</p></td>
<td><p>$12FF</p></td>
<td><p>$0300 (768B)</p></td>
<td><p><a href="PM_PRC#Frame_Copy_Stage" title="wikilink">Frame Buffer</a></p></td>
</tr>
<tr class="even">
<td><p>$1300</p></td>
<td><p>$135F</p></td>
<td><p>$0060 (96B)</p></td>
<td><p><a href="PM_PRC#Sprite_Rendering_Stage" title="wikilink">Sprite Attributes</a></p></td>
</tr>
<tr class="odd">
<td><p>$1360</p></td>
<td><p>$1FFF</p></td>
<td><p>$0CA0 (3232B)</p></td>
<td><p>General Purpose Memory</p></td>
</tr>
</tbody>
</table>
<table>
<caption><strong>PRC blitting directly from frame buffer</strong></caption>
<thead>
<tr class="header">
<th><p>Start</p></th>
<th><p>End</p></th>
<th><p>Size</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$1000</p></td>
<td><p>$12FF</p></td>
<td><p>$0300 (768B)</p></td>
<td><p><a href="PM_PRC#Frame_Copy_Stage" title="wikilink">Frame Buffer</a></p></td>
</tr>
<tr class="even">
<td><p>$1300</p></td>
<td><p>$1FFF</p></td>
<td><p>$0D00 (3328B)</p></td>
<td><p>General Purpose Memory</p></td>
</tr>
</tbody>
</table>
<table>
<caption><strong>PRC off (no BG, Sprites or frame buffer)</strong></caption>
<thead>
<tr class="header">
<th><p>Start</p></th>
<th><p>End</p></th>
<th><p>Size</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$1000</p></td>
<td><p>$1FFF</p></td>
<td><p>$1000 (4096B)</p></td>
<td><p>General Purpose Memory</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>