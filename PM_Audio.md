## Sound

Single-channel square-wave with adjustable pulse-width.

3 Levels of volume: 0%, 50%, 100%

[Register 0x71, Bit 0 to 1](PM_Registers.md "wikilink")

| Bits | Decimal | Volume level |
|-----:|--------:|--------------|
|   00 |       0 | 0% (Silence) |
|   01 |       1 | 50%          |
|   10 |       2 | 50%          |
|   11 |       3 | 100% (Full)  |

Can read back timer values (since sound is assigned to [Timer 3](Timers.md "wikilink")).

To hear sound, you must:

- Enable Timer 3 (with [Registers 0x19, 0x1C, 0x1D, 0x48 and
  0x49](PM_Registers.md "wikilink"), check [Timers](Timers.md "wikilink"))
- Configure Timer 3 with the Preset & Pivot (Based of the frequency
  and pulse-width) (with [Registers 0x4A to
  0x4D](PM_Registers.md "wikilink"), check [Timers](Timers.md "wikilink"))
- Set volume to 50% or 100% (with [Register
  0x71](PM_Registers.md "wikilink"))
- NOTE: Pulse of 0% or 100% will not be audible

Some useful information:

- To generate Square-Wave, use Timer 3 Pivot with half the value of the Timer 3 Preset.
- Commercial games use very small Pulse-Width length to generate weak sounds (for example when Music Volume is 25%).

## Formulas

Timer3_Frequency = The Timer 3 counting speed in Hz (Check [Timers](Timers.md "wikilink"))

Sound_Frequency = The frequency of the note in Hz

Preset_Value = Timer 3 Preset value (to be written in [Registers 0x4A and 0x4B](PM_Registers.md "wikilink"))

Sound_Pivot = Timer 3 Pivot value (to be written in [Registers 0x4C and 0x4D](PM_Registers.md "wikilink"))

Pulse_Width = Pulse-Width from 0.0 to 1.0 (e.g. 0.0 = 0%, 0.5 = 50% (Square), 1.0 = 100%)

### Sound Frequency into Timer 3 Preset

Preset_Value = (Timer3_Frequency / Sound_Frequency) - 1

### Timer 3 Preset into Sound Frequency

Sound_Frequency = Timer3_Frequency / (Preset_Value + 1)

### Pulse-Width into Sound-Pivot

Sound_Pivot = Preset_Value \* Pulse_Width

### Sound-Pivot into Pulse-Width

Pulse_Width = Sound_Pivot / Preset_Value
