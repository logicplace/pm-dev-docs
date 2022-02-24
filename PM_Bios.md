## The BIOS Overview

The internal BIOS consists of a 4kB program image built to initialize the system, bring it out of sleep and various other system specific tasks. Since the Pokémon mini is never technically off, only suspended, BIOS is used for tasks like enabling power to the system and responding to various at rest IRQs.

The BIOS image begins with a 256 byte IRQ vector table, consisting of 128 16-bit vectors (only first 76 are valid). The system reserves 32 vectors for hardware IRQs, the rest are used for software calls. It is worth noting that all IRQs are latched on the rising edge of an event, so button presses and IR receive is only latched when the IR receiver is active 1 or if a button has been press, but not released.

## The IRQ Vector Table

### Bios IRQ Vector Table

| IRQ | BIOS      | Cart IRQ | IRQ Group  | Hardware Strobe    | Description |
|-----|-----------|----------|------------|--------------------|-------------|
| $00 | 0000:009A | 0        <td colspan="2">Non-Maskable</td> | System Start-up / System Reset |
| $01 | 0002:00AB |          <td colspan="2">Non-Maskable</td> | Unused |
| $02 | 0004:00AB |          <td colspan="2">Non-Maskable</td> | Unused |
| $03 | 0006:01CF | 1        | $20\[7..6] | $27,7              | [PRC Copy Complete](PM_PRC.md "wikilink") |
| $04 | 0008:01E0 | 2        | $20\[7..6] | $27,6              | [PRC Frame Divider Overflow](PM_PRC.md "wikilink") |
| $05 | 000A:01F1 | 3        | $20\[5..4] | $27,5              | [Timer2 Upper-8 Underflow](Timers.md "wikilink") |
| $06 | 000C:0202 | 4        | $20\[5..4] | $27,4              | [Timer2 Lower-8 Underflow (8-bit only)](Timers.md "wikilink") |
| $07 | 000E:0213 | 5        | $20\[3..2] | $27,3              | [Timer1 Upper-8 Underflow](Timers.md "wikilink") |
| $08 | 0010:0224 | 6        | $20\[3..2] | $27,2              | [Timer1 Lower-8 Underflow (8-bit only)](Timers.md "wikilink") |
| $09 | 0012:0235 | 7        | $20\[1..0] | $27,1              | [Timer3 Upper-8 Underflow](Timers.md "wikilink") |
| $0A | 0014:0246 | 8        | $20\[1..0] | $27,0              | [Timer3 Pivot](Timers.md "wikilink") |
| $0B | 0016:025A | 9        | $21\[7..6] | $28,5              | 32Hz (From 256Hz Timer) |
| $0C | 0018:026B | 10       | $21\[7..6] | $28,4              | 8Hz (From 256Hz Timer) |
| $0D | 001A:027C | 11       | $21\[7..6] | $28,3              | 2Hz (From 256Hz Timer) |
| $0E | 001C:028D | 12       | $21\[7..6] | $28,2              | 1Hz (From 256Hz Timer) |
| $0F | 001E:029E | 13       | $22\[1..0] | $2A,7              | IR Receiver |
| $10 | 0020:02AF | 14       | $22\[1..0] | $2A,6              | Shock Sensor |
| $11 | 0022:00AB |          |            | $2A,5              | Unused |
| $12 | 0024:00AB |          |            | $2A,4              | Unused |
| $13 | 0026:043E |          | $21\[5..4] | $28,1              | Cartridge Ejected |
| $14 | 0028:02C0 | 26       | $21\[5..4] | $28,0              | Cartridge IRQ |
| $15 | 002A:03BA | 15       | $21\[3..2] | $29,7              | Power Key |
| $16 | 002C:02D1 | 16       | $21\[3..2] | $29,6              | Right Key |
| $17 | 002E:02E2 | 17       | $21\[3..2] | $29,5              | Left Key |
| $18 | 0030:02F3 | 18       | $21\[3..2] | $29,4              | Down Key |
| $19 | 0032:0304 | 19       | $21\[3..2] | $29,3              | Up Key |
| $1A | 0034:0315 | 20       | $21\[3..2] | $29,2              | C Key |
| $1B | 0036:0326 | 21       | $21\[3..2] | $29,1              | B Key |
| $1C | 0038:0337 | 22       | $21\[3..2] | $29,0              | A Key |
| $1D | 003A:0348 | 23       |            | $2A,2              | |
| $1E | 003C:035C | 24       |            | $2A,1              | |
| $1F | 003E:036D | 25       |            | $2A,0              | |

### Software-only IRQ Table

| IRQ | BIOS      | Description |
|-----|-----------|-------------|
| $20 | 0040:FFF1 | User IRQ Routine at PC 0xFFF1 |
| $21 | 0042:0713 | Suspend System |
| $22 | 0044:077C | Sleep ?? |
| $23 | 0046:078B | Sleep with display on ?? |
| $24 | 0048:079D | Shutdown System (Use this to exit your game!) |
| $25 | 004A:07B1 | ?? (Involves Cartridge Eject) |
| $26 | 004C:07E9 | Set default LCD Constrast (A = Contrast level 0x00 to 0x3F) |
| $27 | 004E:0802 | Increase or decrease Contrast based of Zero flag (0 = Increase, 1 = Decrease<br />Return A = 0x00 if succeed, 0xFF if not. |
| $28 | 0050:081B | Apply default LCD Constrast |
| $29 | 0052:0821 | Get default LCD Contrast (return A) |
| $2A | 0054:0830 | Set temporary LCD Constrast (A = Contrast level 0x00 to 0x3F) |
| $2B | 0056:084E | Turn LCD On |
| $2C | 0058:0871 | Initialize LCD |
| $2D | 005A:08CB | Turn LCD Off |
| $2E | 005C:08EC | Enable RAM vector. (Check if Register 0x01 Bit 7 is set, if not, it set bit 6 and 7) |
| $2F | 005E:0904 | Disable RAM vector |
| $30 | 0060:0923 | Disable Cart Eject IRQ 13 (with abort) |
| $31 | 0062:092E | Enable Cart Eject IRQ 13 (with abort) |
| $32 | 0064:0949 | ?? (Involves Cartridge Eject) |
| $33 | 0066:0961 | ?? (Involves Cartridge Eject) |
| $34 | 0068:097D | Nintendo Dev Card (??) |
| $35 | 006A:09E4 | Nintendo Dev Card (??) |
| $36 | 006C:0A4F | ?? (Involves Cartridge Eject) |
| $37 | 006E:0A76 | Disable Cartridge Eject IRQ (Reg 0x24, Bit 1 = 0) |
| $38 | 0070:0A81 | ?? (Involves Cartridge Eject) |
| $39 | 0072:0AA6 | Rumored to speed up CPU? |
| $3A | 0074:0ACD | Recover from IRQ $39? |
| $3B | 0076:0AE6 | Cart power off and update state |
| $3C | 0078:0AF9 | Cart power on and update state |
| $3D | 007A:0B20 | Cart detect. Z: No cart, NZ: Cart inserted (Test Register 0x53 Bit 1 and invert Zero flag) |
| $3E | 007C:0B2E | Read structure, write 0xFF, compare values and optionally jump to subroutine<br />See $3E structure below. |
| $3F | 007E:0B8F | Set PRC Rate (A = 0 to 7) |
| $40 | 0080:0BA3 | Get PRC Rate (return A) |
| $41 | 0082:0BB1 | Test cart type. Returns Z: non multi cart, NZ: multi cart (Register 0x01 Bit 3) |
| $42 | 0084:047A | Nintendo Dev Card (Read IDs) |
| $43 | 0086:0493 | Nintendo Dev Card (Reset) |
| $44 | 0088:04A4 | Nintendo Dev Card (Program Byte) |
| $45 | 008A:04C8 | Nintendo Dev Card (Erase Sector) |
| $46 | 008C:04F5 | Nintendo Dev Card (Unlock flash page register. Command 0xD0) |
| $47 | 008E:0506 | Nintendo Dev Card (Select flash bank. A=bank Nr, X last address of flash page) |
| $48 | 0090:0517 | Nintendo Dev Card (Command 0xC9) |
| $49 | 0092:0529 | Nintendo Dev Card (Prepare Manufacturer and device ID readout. Command 0xC0) |
| $4A | 0094:053A | Nintendo Dev Card (Select flash game. A = game Nr. ([0x041048 + 96 * A] if 0x08 -&gt; Command 0xC9) |
| $4B | 0096:0000 | Nintendo SDK |
| $4C | 0098:0BBD | IR pulse MOV [Y], $02 ; wait B*16 Cycles ; MOV [Y], $00 |

#### $3E Structure

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
