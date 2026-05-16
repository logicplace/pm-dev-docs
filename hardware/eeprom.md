# EEPROM

TODO: this is largely written based on existing documentation and code samples, the code hasn't been tested yet, so execise caution.

The EEPROM is a [24xx64](http://ww1.microchip.com/downloads/en/devicedoc/21189f.pdf) alike 64 Kbit (8 KiB) serial EEPROM using an I²C interface.

It's unknown the exact chip used, so it's very possible it's something produced in-house for this board by Seiko (not necessarily that it wasn't sold commercially, but that it's not marked for it).

The EEPROM is used for storing game saves on-device instead of on the cartridge like most consoles. It has 6 game slots of storage (each slot is 1298 bytes) along with some additional information and a timestamp for tracking the <abbr title="Real Time Clock">RTC</abbr>. If a game saves persistent data, it had an icon of a PM with a book showing the number of slots it takes up. Race mini uses 2, Zany cards does not save, and every other commercial game uses 1.

TODO: icons

Due to being near the battery terminals, it can suffer issues from corrosion and become unusable. However, it's possible to continue playing the official games without being able to save.

## I²C

You can communicate with the EEPROM via the standard [I²C two-wire serial communication protocol](https://www.ti.com/lit/an/sbaa565/sbaa565.pdf) over the I/O ports [P02](./cpu/registers/io.md#p02) for <abbr title="Serial Data">SDA</abbr> and [P03](./cpu/registers/io.md#p02) for <abbr title="Serial Clock">SCL</abbr>. The address of the device is 0b1010_000.

I²C is a protocol for communicating with multiple devices on the same bus. As such, it's possible to attach other devices to this bus. So far, this has only been done by [Lupin](https://web.archive.org/web/20080412185344/http://lupin.shizzle.it/?p=55) with a [DS1621 digital thermometer](https://www.analog.com/media/en/technical-documentation/data-sheets/DS1621.pdf). Details on this mod [here](./mods/ds1621.md).

### Bit-level protocol

There are specific START and STOP signals for bounding [a packet](#communication-frames), signals for writing a single bit value, and signals for acknowledging a communication. They look like the following:

```s1c88
DEFINE READ_SDA   'BIT [BR:61h], #04h'
DEFINE SDA_OUTPUT 'OR  [BR:60h], #04h'
DEFINE SCL_OUTPUT 'OR  [BR:60h], #08h'
DEFINE Sxx_OUTPUT 'OR  [BR:60h], #0Ch'
DEFINE SDA_INPUT  'AND [BR:60h], #~04h'
DEFINE SCL_INPUT  'AND [BR:60h], #~08h'
DEFINE Sxx_INPUT  'AND [BR:60h], #~0Ch'
DEFINE SDA_HIGH   'OR  [BR:61h], #04h'
DEFINE SCL_HIGH   'OR  [BR:61h], #08h'
DEFINE SDA_LOW    'AND [BR:61h], #~04h'
DEFINE SCL_LOW    'AND [BR:61h], #~08h'

; SDA high to low while SCL is high
_i2c_start:
	; Disable interrupts
	PUSH SC
	LD  SC, 0C0h

	Sxx_OUTPUT  ; Clock/data to output
	SCL_HIGH    ; Clock/data goes high (order doesn't seem to matter)
	SDA_HIGH    ; TODO: can these be combined?
	SDA_LOW     ; Data goes low,
	SCL_LOW     ; then clock goes low
	RET

; SDA low to high while SCL is high
_i2c_stop:
	Sxx_OUTPUT  ; Set to output
	SDA_LOW     ; and set data low
	SCL_HIGH    ; Set clock high
	SDA_HIGH    ; Data goes high
	SCL_LOW     ; Then set clock low
	; TODO: Lupin claims a need to wait for "a while" (9000 cycles)
	; before being able to send START again, need to confirm
	RETI        ; Restore SC

; SCL low -> high -> low while SDA is high
_i2c_write_1bit:
	; presuming Sxx_OUTPUT and SCL_LOW
	SDA_HIGH    ; Set data high
	SCL_HIGH    ; Pulse clock
	SCL_LOW
	SDA_LOW     ; Set data low
	RET

; SCL low -> high -> low while SDA is low
_i2c_write_0bit:
	; presuming Sxx_OUTPUT and SCL_LOW
	SDA_LOW     ; Set data low
	SCL_HIGH    ; Pulse clock
	SCL_LOW
	RET

; This is the same as reading a bit of data
; but normal reads don't need to error obviously.
_i2c_recv_ack:
	; presuming SCL_OUTPUT
	SDA_INPUT
	SCL_HIGH
	READ_SDA    ; Read acknowledgement into Z flag
	SDA_OUTPUT
	JRS Z, ira__end
	; Error out
	CARS _i2c_stop
	Sxx_INPUT
ira__end:
	RET

; Essentially switch out of read and write a 0
_i2c_send_ack:
	SDA_OUTPUT
	CARS _i2c_write_0bit
	SDA_INPUT

; Essentially switch out of read and write a 1
_i2c_send_nack:
	SDA_OUTPUT
	CARS _i2c_write_1bit
	SDA_INPUT
```

### Communication frames

A packet consists of a single address frame followed by one or more data frames.

* START
* Address frame
  * Send: 7 bit target address (1010_000 for the EEPROM)
    * 4 bits of device type
	* 3 bits of configurable address (A2~A0 pins)
  * Send: 1 bit R/<u style="text-decoration:overline">W</u>
    * That is; 1 = read, 0 = write
  * Recv: 1 bit ACK
    * 0 = success, 1 = failure
* Data frame
  * Send: 8 bits of data
  * Recv: 1 bit ACK
    * 0 = success, 1 = failure
* STOP

### Reading from EEPROM

1. START
2. Address frame + W: 0xA0 (recv ACK)
3. Write hi address byte (recv ACK)
4. Write lo address byte (recv ACK)
5. START
6. Address frame + R: 0xA1 (recv ACK)
7. Read data byte (send ACK)
8. CPL data byte
9. Repeat 7~8 as many times as you want
10. send NACK
11. STOP

### Writing to EEPROM

1. START
2. Address frame + W: 0xA0 (recv ACK)
3. Write hi address byte (recv ACK)
4. Write lo address byte (recv ACK)
5. Write data byte (recv ACK)
6. Repeat 5 as many* times as you want
7. STOP
8. Address frame + W: 0xA0 (recv N/ACK)
9. Repeat 8 up to 36 times until NACK is received
10. STOP

\* In [MINLIB][] it stops writing at 32 byte boundaries (when the address & 0x1F is zero) and continues to the polling step (8~9) before returning to writing (if anything is left).

[MINLIB]: /software/minlib.md

## Format

Since the EEPROM is shared, every software which intends to use it should be aware of the data structure stored on it, even if it's defined by [MINLIB][].

| Offset | Size | Description             |
|:------:| ----:| ----------------------- |
| $0000  |    4 | Magic bytes: `GBMN`     |
| $0004  |   18 | Slot 1 [header][]       |
| $0016  |   18 | Slot 2 [header][]       |
| $0028  |   18 | Slot 3 [header][]       |
| $003A  |   18 | Slot 4 [header][]       |
| $004C  |   18 | Slot 5 [header][]       |
| $005E  |   18 | Slot 6 [header][]       |
| $0070  |   18 | Unused [header][] space |
| $0082  | 1280 | Slot 1 [data][]         |
| $0582  | 1280 | Slot 2 [data][]         |
| $0A82  | 1280 | Slot 3 [data][]         |
| $0F82  | 1280 | Slot 4 [data][]         |
| $1482  | 1280 | Slot 5 [data][]         |
| $1982  | 1280 | Slot 6 [data][]         |
| $1E82  |  368 | Unused slot [data][]    |
| $1FF2  |    4 | [Default settings][]    |
| $1FF6  |   10 | [Timestamp][]           |

[header]: #slot-header-format
[data]: #slot-data-format
[Default settings]: #default-settings-format
[Timestamp]: #timestamp-format

### Slot header format

Offset is relative to the beginning of the slot.

| Offset | Size | Description    |
|:------:| ----:| -------------- |
| $0000  |    4 | [Game code][]  |
| $0004  |   12 | [Game title][] |
| $0010  |    2 | Checksum       |

The checksum is the sum of the other bytes in the header.

[Game code]: ./cpu/memory.md#game-code
[Game title]: ./cpu/memory.md#game-title

### Slot data format

Each game has its own save data format.

TODO: commonalities (there's probably a checksum)

### Default settings format

| Offset | Size | Description                 |
|:------:| ----:| --------------------------- |
| $1FF2  |    1 | Rumble (0=off, 1=on)        |
| $1FF3  |    1 | BGM volume (0~4)            |
| $1FF4  |    1 | SFX volume (0~2)            |
| $1FF5  |    1 | Contrast (0~63, 31 default) |

### Timestamp format

| Offset | Size | Description     |
|:------:| ----:| --------------- |
| $1FF6  |    3 | Seconds counter |
| $1FF9  |    1 | Year            |
| $1FFA  |    1 | Month           |
| $1FFB  |    1 | Day             |
| $1FFC  |    1 | Hour            |
| $1FFD  |    1 | Minute          |
| $1FFE  |    1 | Seconds         |
| $1FFF  |    1 | Checksum        |

The checksum is the sum of the other bytes in the timestamp.
