# Interrupt Vectors

Exception processing vectors

Software interrupts

## Interrupt overview

The S1C88V20 provides up to 32 exception processing interrupts and up to 96 software interrupts (for BIOS calls). The full list is defined in the [BIOS section](PM_Bios.md "wikilink") of the standard. Out of the 32 interrupts, three are not maskable, $00~$02.

On startup, **IRQ 0 (reset)** fires. Since the BIOS resets the processor state, it is unknown if this behaves like a normal interrupt.

## Interrupt priority

The S1C88V20 interrupt hardware is impressive in it's configurability. The 29 maskable interrupts are divided into 9 groups. Each of these groups are then provided a 2 bit priority encoder. These encoders define the order in which exception interrupts are processed. They're processed by priority first, then by the vector address (earlier = higher priority). If an interrupt group is assigned a priority of 0, all the interrupts for the group are implicity disabled.

## Enabling interrupts

All 29 of the maskable interrupts can be disabled in 3 ways. The first way is if the interrupt flag is set too high in the [SC register](./S1C88_Core.md#sc-and-cc-registers). Setting this to 3 will prevent _all_ maskable interrupts from occuring. The second is by setting the interrupt group priority to zero. Finally, you can reset the effective bit in the interrupt enable register. If any of these three conditions occur, the interrupt is effectively disabled.

Note: Any operation which changes NB or SC is uninterruptible, which means interrupts cannot fire between that operation and the operation following it.

## When interrupts occur

IRQs are set to "pending" on the rising edge of an event. Since IRQs are not nessessarly processed immediately, they will remain in a waiting state. This is where the IRQ_ACT_\* registers come in. At any point an IRQ is enabled, and the respective bit in an IRQ_ACT_\* is set. The down side to this is the IRQ will continue to fire until software clears the bit by writing a logical '1' to the bit in IRQ_ACT_\*.

After an IRQ branch occurs, the interrupt branch flag is set, preventing IRQs from colliding with one another.

TODO: flow chart

## Vector tables

### Exception processing interrupts

In this table, the vector is the address stored in this vector table in the official BIOS. It's a location in the BIOS which handles the exception. The Software column is what the BIOS's handler continues into, if anything and only if it's enabled, which is a handler stored in the software itself.

The priority, enable, and strobe registers are defined in the [Registers](PM_Registers.md) section. The priority registers are two bits each, and each covers a logical group of registers. The others are only one bit and are individual.

| Address   | Vector | Software | Priority register | Enable register | Hardware strobe | Description                                |
| --------- | ------ | -------- | ----------------- | --------------- | --------------- | ------------------------------------------ |
| [$00][00] | $009A  |          | Non-Maskable                                        ||| System Start-up / System Reset             |
| [$02][02] | $00AB  |          | Non-Maskable                                        ||| Divide by zero ?                           |
| [$04][04] | $00AB  |          | Non-Maskable                                        ||| Watchdog timer ?                           |
| [$06][06] | $01CF  | $2108    | $20\[7..6]        | $23\[7]         | $27\[7]         | [PRC Copy Complete][1]                     |
| [$08][08] | $01E0  | $210e    | $20\[7..6]        | $23\[6]         | $27\[6]         | [PRC Frame Divider Overflow][1]            |
| [$0A][0A] | $01F1  | $2114    | $20\[5..4]        | $23\[5]         | $27\[5]         | [Timer2 Upper-8 Underflow][2]              |
| [$0C][0C] | $0202  | $211a    | $20\[5..4]        | $23\[4]         | $27\[4]         | [Timer2 Lower-8 Underflow (8-bit only)][2] |
| [$0E][0E] | $0213  | $2120    | $20\[3..2]        | $23\[3]         | $27\[3]         | [Timer1 Upper-8 Underflow][2]              |
| [$10][10] | $0224  | $2126    | $20\[3..2]        | $23\[2]         | $27\[2]         | [Timer1 Lower-8 Underflow (8-bit only)][2] |
| [$12][12] | $0235  | $212c    | $20\[1..0]        | $23\[1]         | $27\[1]         | [Timer3 Upper-8 Underflow][2]              |
| [$14][14] | $0246  | $2132    | $20\[1..0]        | $23\[0]         | $27\[0]         | [Timer3 Pivot][2]                          |
| [$16][16] | $025A  | $2138    | $21\[7..6]        | $24\[5]         | $28\[5]         | 32Hz (From 256Hz Timer)                    |
| [$18][18] | $026B  | $213e    | $21\[7..6]        | $24\[4]         | $28\[4]         | 8Hz (From 256Hz Timer)                     |
| [$1A][1A] | $027C  | $2144    | $21\[7..6]        | $24\[3]         | $28\[3]         | 2Hz (From 256Hz Timer)                     |
| [$1C][1C] | $028D  | $214a    | $21\[7..6]        | $24\[2]         | $28\[2]         | 1Hz (From 256Hz Timer)                     |
| [$1E][1E] | $029E  | $2150    | $22\[1..0]        | $26\[7]         | $2A\[7]         | IR Receiver                                |
| [$20][20] | $02AF  | $2156    | $22\[1..0]        | $26\[6]         | $2A\[6]         | Shock Sensor                               |
| [$22][22] | $00AB  |          |                   | $26\[5]         | $2A\[5]         | Unused                                     |
| [$24][24] | $00AB  |          |                   | $26\[4]         | $2A\[4]         | Unused                                     |
| [$26][26] | $043E  |          | $21\[5..4]        | $24\[1]         | $28\[1]         | Cartridge Ejected                          |
| [$28][28] | $02C0  | $219e    | $21\[5..4]        | $24\[0]         | $28\[0]         | Cartridge IRQ                              |
| [$2A][2A] | $03BA  | $215c    | $21\[3..2]        | $29\[7]         | $29\[7]         | Power Key                                  |
| [$2C][2C] | $02D1  | $2162    | $21\[3..2]        | $25\[6]         | $29\[6]         | Right Key                                  |
| [$2E][2E] | $02E2  | $2168    | $21\[3..2]        | $25\[5]         | $29\[5]         | Left Key                                   |
| [$30][30] | $02F3  | $216e    | $21\[3..2]        | $25\[4]         | $29\[4]         | Down Key                                   |
| [$32][32] | $0304  | $2174    | $21\[3..2]        | $25\[3]         | $29\[3]         | Up Key                                     |
| [$34][34] | $0315  | $217a    | $21\[3..2]        | $25\[2]         | $29\[2]         | C Key                                      |
| [$36][36] | $0326  | $2180    | $21\[3..2]        | $25\[1]         | $29\[1]         | B Key                                      |
| [$38][38] | $0337  | $2186    | $21\[3..2]        | $25\[0]         | $29\[0]         | A Key                                      |
| [$3A][3A] | $0348  | $218c    |                   | $26\[2]         | $2A\[2]         |                                            |
| [$3C][3C] | $035C  | $2192    |                   | $26\[1]         | $2A\[1]         |                                            |
| [$3E][3E] | $036D  | $2198    |                   | $26\[0]         | $2A\[0]         |                                            |

[1]: PM_PRC.md
[2]: Timers.md
[00]: #exception-00
[02]: #exception-02--04
[04]: #exception-02--04
[06]: #exception-06
[08]: #exception-08
[0A]: #exception-0A
[0C]: #exception-0C
[0E]: #exception-0E
[10]: #exception-10
[12]: #exception-12
[14]: #exception-14
[16]: #exception-16
[18]: #exception-18
[1A]: #exception-1A
[1C]: #exception-1C
[1E]: #exception-1E
[20]: #exception-20
[22]: #exception-22
[24]: #exception-24
[26]: #exception-26
[28]: #exception-28
[2A]: #exception-2A
[2C]: #exception-2C
[2E]: #exception-2E
[30]: #exception-30
[32]: #exception-32
[34]: #exception-34
[36]: #exception-36
[38]: #exception-38
[3A]: #exception-3A
[3C]: #exception-3C
[3E]: #exception-3E

### Software interrupts

These are interrupts you can call manually with `JP [kk]` where `kk` is the address from the address column here, such as `48h`.

| Address   | Vector | Description                                                   |
| --------- | ------ | ------------------------------------------------------------- |
| [$40][40] | $FFF1  | Software-defined interrupt                                    |
| [$42][42] | $0713  | Suspend system                                                |
| [$44][44] | $077C  | Sleep ??                                                      |
| [$46][46] | $078B  | Sleep with display on ??                                      |
| [$48][48] | $079D  | Shutdown system                                               |
| [$4A][4A] | $07B1  | ?? (involves interrupt $26)                                   |
| [$4C][4C] | $07E9  | Set default contrast                                          |
| [$4E][4E] | $0802  | Adjust default contrast                                       |
| [$50][50] | $081B  | Apply default contrast                                        |
| [$52][52] | $0821  | Get default contrast                                          |
| [$54][54] | $0830  | Set temporary contrast                                        |
| [$56][56] | $084E  | Turn LCD on                                                   |
| [$58][58] | $0871  | Initialize LCD                                                |
| [$5A][5A] | $08CB  | Turn LCD off                                                  |
| [$5C][5C] | $08EC  | Enable RAM vector                                             |
| [$5E][5E] | $0904  | Disable RAM vector (abortable)                                |
| [$60][60] | $0923  | Disable interrupt $26 (abortable)                             |
| [$62][62] | $092E  | Enable interrupt $26 (abortable)                              |
| [$64][64] | $0949  | ?? (involves interrupt $26)                                   |
| [$66][66] | $0961  | ?? (involves interrupt $26)                                   |
| [$68][68] | $097D  | Nintendo dev card (??)                                        |
| [$6A][6A] | $09E4  | Nintendo dev card (??)                                        |
| [$6C][6C] | $0A4F  | ?? (involves interrupt $26)                                   |
| [$6E][6E] | $0A76  | Disable interrupt $26                                         |
| [$70][70] | $0A81  | ?? (involves interrupt $26)                                   |
| [$72][72] | $0AA6  | Rumored to speed up CPU?                                      |
| [$74][74] | $0ACD  | Recover from interrupt $72?                                   |
| [$76][76] | $0AE6  | Cart power off and update state                               |
| [$78][78] | $0AF9  | Cart power on and update state                                |
| [$7A][7A] | $0B20  | Cart detect                                                   |
| [$7C][7C] | $0B2E  | ??                                                            |
| [$7E][7E] | $0B8F  | Set PRC Rate                                                  |
| [$80][80] | $0BA3  | Get PRC Rate                                                  |
| [$82][82] | $0BB1  | Test cart type                                                |
| [$84][84] | $047A  | Nintendo dev card: Read IDs                                   |
| [$86][86] | $0493  | Nintendo dev card: Reset                                      |
| [$88][88] | $04A4  | Nintendo dev card: Program byte                               |
| [$8A][8A] | $04C8  | Nintendo dev card: Erase sector                               |
| [$8C][8C] | $04F5  | Nintendo dev card: Unlock flash page register                 |
| [$8E][8E] | $0506  | Nintendo dev card: Select flash bank                          |
| [$90][90] | $0517  | Nintendo dev card: Command 0xC9                               |
| [$92][92] | $0529  | Nintendo dev card: Prepare manufacturer and device ID readout |
| [$94][94] | $053A  | Nintendo dev card: Select flash game                          |
| [$96][96] | $0000  | Nintendo SDK                                                  |
| [$98][98] | $0BBD  | IR pulse                                                      |

[40]: #software-interrupt-40
[42]: #software-interrupt-42
[44]: #software-interrupt-44
[46]: #software-interrupt-46
[48]: #software-interrupt-48
[4A]: #software-interrupt-4A
[4C]: #software-interrupt-4C
[4E]: #software-interrupt-4E
[50]: #software-interrupt-50
[52]: #software-interrupt-52
[54]: #software-interrupt-54
[56]: #software-interrupt-56
[58]: #software-interrupt-58
[5A]: #software-interrupt-5A
[5C]: #software-interrupt-5C
[5E]: #software-interrupt-5E
[60]: #software-interrupt-60
[62]: #software-interrupt-62
[64]: #software-interrupt-64
[66]: #software-interrupt-66
[68]: #software-interrupt-68
[6A]: #software-interrupt-6A
[6C]: #software-interrupt-6C
[6E]: #software-interrupt-6E
[70]: #software-interrupt-70
[72]: #software-interrupt-72
[74]: #software-interrupt-74
[76]: #software-interrupt-76
[78]: #software-interrupt-78
[7A]: #software-interrupt-7A
[7C]: #software-interrupt-7C
[7E]: #software-interrupt-7E
[80]: #software-interrupt-80
[82]: #software-interrupt-82
[84]: #software-interrupt-84
[86]: #software-interrupt-86
[88]: #software-interrupt-88
[8A]: #software-interrupt-8A
[8C]: #software-interrupt-8C
[8E]: #software-interrupt-8E
[90]: #software-interrupt-90
[92]: #software-interrupt-92
[94]: #software-interrupt-94
[96]: #software-interrupt-96
[98]: #software-interrupt-98

## Interrupt list

In the pseudo-code below, the `set` method sets bits of a [register](PM_Registers.md) represented by names and the value assigned. The `remaining` or `all` arguments set all the bits that are not set by other named arguments in the call. If a 1-bit flag is set to 1 or 0, this is the raw number set by the BIOS; if it's set to True or False, this is the logical value set by the BIOS (regardless of whether that's 1 or 0). Ideally, these should all be converted to True/False, and only remain as 1 or 0 due to lack of knowledge. When a multi-bit flag is set, if it's an enumeration, a named representation of the value will be used, as named in `pm.h`; otherwise, a raw value is assigned, and is likely as intended.

Some registers will address a property or method directly, which represents only one flag being set at that time.

Registers which are split over multiple bytes are combined into one where possible.

### General purpose methods

Some methods called by multiple handlers.

```python
def init_io():
  SYS_BATT.set(
    battery_adc_control = DISABLED,
    battery_adc_threshold = 8,
  )
  TMR1_OSC.set(
    enable_osc1 = False,
    enable_osc2 = False,
  )

  IRQ_PRI.set(
    group_06_08 = 0,
    group_0A_0C = 0,
    group_0E_10 = 0,
    group_12_14 = 0,
    group_16_thru_1C = 0,
    group_26_28 = 3,
    group_2A_thru_38 = 0,
    group_1E_20 = 2,
    remaining = 0,
  )

  IRQ_ENA.set(
    int_26 = True,
    remaining = False,
  )

  TMR256_CTRL.set(
    reset = 0,  # no-op?
    enabled = False,
  )

  REG_44.set(all=0)
  REG_50.set(0xFF)
  REG_51.set(all=0)
  REG_54.set(
    bit_2 = 0,
    bit_1 = 0,
    bit_0 = 1,
  )
  REG_55.set(1)

  IO_DIR.set(
    eeprom_clock = OUTPUT,
    eeprom_data = OUTPUT,
  )
  IO_DATA.eeprom_data = 0
  IO_DATA.eeprom_clock = 1
  IO_DATA.eeprom_data = 1
  IO_DIR.set(
    ir_disable = True,  # IR power as output?
    rumble = OUTPUT,
    eeprom_clock = INPUT,
    eeprom_data = INPUT,
    ir_rx = 1,  # "IR TxD as output" ??
    ir_tx = 0,
    remaining = 0,
  )

  REG_62.set(all=0)
  AUD_CTRL.set(all=0)
  AUD_VOL.set(
    cart_power = ON,
    volumn = 0,
    remaining = 0
  )
```

### Exception $00

**Cold reset**

Will happen when battery is replaced, reset button is pressed, or when system crashes ?

- It resets the the seconds counter which is used as the real-time clock and signals that the time is invalid.
- Resets display contrast to the default contrast.
- Resets speed ?

BIOS-only. Should not be called directly from software.

Clobbers all registers.

```python
def cold_reset():
  SEC_CTRL.reset()  # Clears all flags and sets reset
  SEC_CTRL.enabled = True
  SYS_CTRL1.set(
    startup_contrast = 31,
    cartridge_io_enable = 0,
    lcd_io_enable = 0,
  )
  SYS_CTRL3.set(
    cart_power_state = 0,
    cart_power_required = 0,
    suspend_mode = 0,
    rtc_timer_valid = False,
    unknowns = 0,
  )
  warm_reset()
```

### Exception $02 / $04

**Warm reset**

Normally triggered by powering up from shutdown. This reset will not reset the real-time clock, so the 'date and time' is preserved.

Clobbers all registers.

```python
def warm_reset():
  SC.i = 3
  SP = 0x2000
  PRC_MODE.set(
    map_size = MAP_12X16,
    enable_copy = False,
    enable_sprite = False,
    enable_map = False,
    invert_map = False,
  )
  set_fast_speed()

  startup_buttons = KEY_PAD
  SYS_CTRL1.set(
    cartridge_io_enable = 1,
    lcd_io_enable = 1,
  )
  SYS_CTRL2.set(
    ram_vector = 1,
    interrupt_abort = 1,
    enable_cart_interrupts = 0,
    power_on_reset = 0,
    cart_type = 0,
  )
  SYS_CTRL3.set(
    cart_power_state = 1,
    cart_power_required = 1,
  )
  init_io()

  # TODO: `movb    [nn+$80],$02	;Enable Tile Map` and below
```

### Exception $06

**PRC Copy Complete**

### Exception $08

**PRC Frame Divider Overflow**

### Exception $0A
### Exception $0C
### Exception $0E
### Exception $10
### Exception $12
### Exception $14
### Exception $16
### Exception $18
### Exception $1A
### Exception $1C
### Exception $1E
### Exception $20
### Exception $22
### Exception $24
### Exception $26
### Exception $28
### Exception $2A
### Exception $2C
### Exception $2E
### Exception $30
### Exception $32
### Exception $34
### Exception $36
### Exception $38
### Exception $3A
### Exception $3C
### Exception $3E

### Software interrupt $48

Use this to shut down the system

### Software interrupt $4C

A = Contrast level 0x00 to 0x3F

### Software interrupt $4E

Increase or decrease Contrast based of Zero flag (0 = Increase, 1 = Decrease

Return A = 0x00 if succeed, 0xFF if not.

### Software interrupt $52

return A

### Software interrupt $54

A = Contrast level 0x00 to 0x3F

### Software interrupt $5C

Check if Register 0x01 Bit 7 is set, if not, it set bit 6 and 7

### Software interrupt $5E

Does not run if SYS_CTRL2.int_abort is 0

### Software interrupt $60

Does not run if SYS_CTRL2.int_abort is 0

### Software interrupt $62

Does not run if SYS_CTRL2.int_abort is 0

### Software interrupt $7A

Z: No cart, NZ: Cart inserted (Test Register 0x53 Bit 1 and invert Zero flag)

### Software interrupt $7C

Read structure, write 0xFF, compare values and optionally jump to subroutine

```c
struct {
  byte   type            // 0x01 = Call subroutine, 0x00 = Don't call subroutine
  triple write_0xFF_addr // Address that 0xFF will be written
  triple compare_addr    // Address to read for compare
  byte   compare_value   // Value that must match the compare
  triple subroutine      // Use byte POP to receive flag of the compare
};
```
if type is 0x00, register A return 0x01 if compare is equal

### Software interrupt $7E

A = 0 to 7

### Software interrupt $80

Return A

### Software interrupt $82

Returns Z: non multi cart, NZ: multi cart (Register 0x01 Bit 3)

### Software interrupt $8C

Command 0xD0

### Software interrupt $8E

A=bank Nr, X last address of flash page

### Software interrupt $92

Command 0xC0

### Software interrupt $94

A = game Nr. ([0x041048 + 96 * A] if 0x08 -&gt; Command 0xC9

### Software interrupt $98

MOV [Y], $02 ; wait B*16 Cycles ; MOV [Y], $00

## What is not known

There are aproximately 7 hardware interrupts which have not been mapped and as such we don't know all the details of their behavior.
