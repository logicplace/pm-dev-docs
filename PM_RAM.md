## RAM Overview

The memory used in the Pokémon mini is general purpose static ram. It is high speed and there is no performance hit for accessing it other than the instruction processing speed. The biggest problem with the system is that the ram is small, and also shared with the [picture rendering chip](PM_PRC.md "wikilink"). Sections of this memory can be disabled, but up to 1248 bytes of 4k can be re-purposed for video.

General purpose memory is considered unused and is safe for all use at any time. Disabling various parts of the [picture rendering chip](PM_PRC.md "wikilink") can free up additional memory.

## RAM Layout

### Memory layout schemas

#### PRC rendering sprites with Tile Map 0, 1, or 2

| Start | End   | Size          | Description            |
| ----- | ----- | ------------- | ---------------------- |
| $1000 | $12FF | $0300 (768B)  | [Frame Buffer][1]      |
| $1300 | $135F | $0060 (96B)   | [Sprite Attributes][2] |
| $1360 | $141F | $00C0 (192B)  | [Tile Map][3]          |
| $1420 | $1FFF | $0BE0 (3040B) | General Purpose Memory |

[1]: PM_PRC.md#Frame_Copy_Stage "wikilink"
[2]: PM_PRC.md#Sprite_Rendering_Stage "wikilink"
[3]: PM_PRC.md#Map_Rendering_Stage "wikilink"

#### PRC rendering sprites with Tile Map 3

| Start | End   | Size          | Description            |
| ----- | ----- | ------------- | ---------------------- |
| $1000 | $12FF | $0300 (768B)  | [Frame Buffer][1]      |
| $1300 | $135F | $0060 (96B)   | [Sprite Attributes][2] |
| $1360 | $14DF | $0180 (384B)  | [Tile Map][3]          |
| $14E0 | $1FFF | $0B20 (2848B) | General Purpose Memory |

[1]: PM_PRC.md#Frame_Copy_Stage "wikilink"
[2]: PM_PRC.md#Sprite_Rendering_Stage "wikilink"
[3]: PM_PRC.md#Map_Rendering_Stage "wikilink"

#### PRC rendering only sprites

| Start | End   | Size          | Description            |
| ----- | ----- | ------------- | ---------------------- |
| $1000 | $12FF | $0300 (768B)  | [Frame Buffer][1]      |
| $1300 | $135F | $0060 (96B)   | [Sprite Attributes][2] |
| $1360 | $1FFF | $0CA0 (3232B) | General Purpose Memory |

[1]: PM_PRC.md#Frame_Copy_Stage "wikilink"
[2]: PM_PRC.md#Sprite_Rendering_Stage "wikilink"

#### PRC blitting directly from frame buffer

| Start | End   | Size          | Description            |
| ----- | ----- | ------------- | ---------------------- |
| $1000 | $12FF | $0300 (768B)  | [Frame Buffer][1]      |
| $1300 | $1FFF | $0D00 (3328B) | General Purpose Memory |

[1]: PM_PRC.md#Frame_Copy_Stage "wikilink"

#### PRC off (no Tiles, Sprites, or frame buffer)

| Start | End   | Size          | Description            |
| ----- | ----- | ------------- | ---------------------- |
| $1000 | $1FFF | $1000 (4096B) | General Purpose Memory |
