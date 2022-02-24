## Register Overview

The Pokemon Mini maps $2000 \~ $20FF as hardware control registers. This
area is reserved for hardware related functions such as video, audio,
general purpose timers, hardware I/O and system control.

Much of this address space is mapped as [Open-Bus](Open-Bus.md "wikilink"),
leading us to beleive that this area is not used for any purpose. Other
areas respond to requests but their purpose is yet undetermined.

Registers tend to be controlled on a bit level, so for the sanity
purposes, they will be broken down to this level. At any point they are
shown spanning multiple columns, that indicates that it is a multi-bit
value and should be treated as if they were a number.

The bits themselves come in four flavors: Read-only, Write-Only,
Read-Write, and S-R Strobe. Write-Only registers typically return a zero
value, and are generally only used for things such as resetting timers.
S-R Strobes are used for clearing interrupt events, writting a logical
'1' to any bit that is set will result in a bit being cleared, where as
'0' leaves them unchanged. Unused bits always return '0'.

Any register not included on this list reads as
[Open-Bus](Open-Bus.md "wikilink") and will be excluded unless a function
has otherwise been
determined.

## Register Mapping

|        |            |           |            |            |                                  |                      |                 |                  |
| ------ | ---------- | --------- | ---------- | ---------- | -------------------------------- | -------------------- | --------------- | ---------------- |
| Unused | Read/Write | Read Only | Write Only | S-R Strobe | Read/Write (BIOS, Software only) | Unknown (Read/Write) | Unknown (Weird) | Unknown (Unused) |

**Register Map Legend**

<table>
<caption><strong>Registers ($2000 to $20FF)</strong></caption>
<thead>
<tr class="header">
<th><p>Address</p></th>
<th><p>Register</p></th>
<th><p>Const Name</p></th>
<th><p>&lt; Bit 7 &gt;</p></th>
<th><p>&lt; Bit 6 &gt;</p></th>
<th><p>&lt; Bit 5 &gt;</p></th>
<th><p>&lt; Bit 4 &gt;</p></th>
<th><p>&lt; Bit 3 &gt;</p></th>
<th><p>&lt; Bit 2 &gt;</p></th>
<th><p>&lt; Bit 1 &gt;</p></th>
<th><p>&lt; Bit 0 &gt;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>$00</p></td>
<td><p>System Control 1</p></td>
<td><p>SYS_CTRL1</p></td>
<td><p>Startup Contrast</p></td>
<td><p>Cartridge I/O<br />
Enable</p></td>
<td><p>LCD I/O<br />
Enable</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$01</p></td>
<td><p>System Control 2</p></td>
<td><p>SYS_CTRL2</p></td>
<td><p>Ram vector</p></td>
<td><p>Int abort</p></td>
<td><p>Enable cart interrupts</p></td>
<td><p>Power on reset</p></td>
<td><p>Cart type</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$02</p></td>
<td><p>System Control 3</p></td>
<td><p>SYS_CTRL3</p></td>
<td><p>Cart power state</p></td>
<td><p>Cart power required</p></td>
<td><p>Suspend mode</p></td>
<td><p>???</p></td>
<td><p>RTC Timer valid</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$08</p></td>
<td><p><a href="PM_Second_Counter" title="wikilink">Second Counter Control</a></p></td>
<td><p>SEC_CTRL</p></td>
<td></td>
<td><p>Reset</p></td>
<td><p>Enable</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$09</p></td>
<td><p><a href="PM_Second_Counter" title="wikilink">Second Counter Low</a></p></td>
<td><p>SEC_CNT_LO</p></td>
<td><p>Counter</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$0A</p></td>
<td><p><a href="PM_Second_Counter" title="wikilink">Second Counter Middle</a></p></td>
<td><p>SEC_CNT_MID</p></td>
<td><p>Counter</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$0B</p></td>
<td><p><a href="PM_Second_Counter" title="wikilink">Second Counter High</a></p></td>
<td><p>SEC_CNT_HI</p></td>
<td><p>Counter</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$10</p></td>
<td><p>Battery Sensor</p></td>
<td><p>SYS_BATT</p></td>
<td></td>
<td><p>Low Battery</p></td>
<td><p>Battery ADC control</p></td>
<td><p>Battery ADC threshold value</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$18</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Prescalars</a></p></td>
<td><p>TMR1_SCALE</p></td>
<td><p>Enable Hi</p></td>
<td><p>Hi Scalar</p></td>
<td><p>Enable Lo</p></td>
<td><p>Lo Scalar</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$19</p></td>
<td><p><a href="Timers" title="wikilink">Timers Osc. Enable<br />
Timer 1 Osc. Select</a></p></td>
<td><p>TMR1_ENA_OSC<br />
TMR1_OSC</p></td>
<td></td>
<td><p>Enable Osc. 1</p></td>
<td><p>Enable Osc. 2</p></td>
<td></td>
<td><p>2nd Osc. (Hi)</p></td>
<td><p>2nd Osc. (Lo)</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$1A</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Prescalars</a></p></td>
<td><p>TMR2_SCALE</p></td>
<td><p>Enable Hi</p></td>
<td><p>Hi Scalar</p></td>
<td><p>Enable Lo</p></td>
<td><p>Lo Scalar</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$1B</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Osc. Select</a></p></td>
<td><p>TMR2_OSC</p></td>
<td></td>
<td><p>2nd Osc. (Hi)</p></td>
<td><p>2nd Osc. (Lo)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$1C</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Prescalars</a></p></td>
<td><p>TMR3_SCALE</p></td>
<td><p>Enable Hi</p></td>
<td><p>Hi Scalar</p></td>
<td><p>Enable Lo</p></td>
<td><p>Lo Scalar</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$1D</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Osc. Select</a></p></td>
<td><p>TMR3_OSC</p></td>
<td></td>
<td><p>2nd Osc. (Hi)</p></td>
<td><p>2nd Osc. (Lo)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$20</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Priority 1</a></p></td>
<td><p>IRQ_PRI1</p></td>
<td><p>IRQ $03 ~ $04</p></td>
<td><p>IRQ $05 ~ $06</p></td>
<td><p>IRQ $07 ~ $08</p></td>
<td><p>IRQ $09 ~ $0A</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$21</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Priority 2</a></p></td>
<td><p>IRQ_PRI2</p></td>
<td><p>IRQ $0B ~ $0E</p></td>
<td><p>IRQ $13 ~ $14</p></td>
<td><p>IRQ $15 ~ $1C</p></td>
<td><p>IRQ ??? ($1D ~ $1F?)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$22</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Priority 3</a></p></td>
<td><p>IRQ_PRI3</p></td>
<td></td>
<td><p>IRQ $0F~$10</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$23</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Enable 1</a></p></td>
<td><p>IRQ_ENA1</p></td>
<td><p>IRQ $03</p></td>
<td><p>IRQ $04</p></td>
<td><p>IRQ $05</p></td>
<td><p>IRQ $06</p></td>
<td><p>IRQ $07</p></td>
<td><p>IRQ $08</p></td>
<td><p>IRQ $09</p></td>
<td><p>IRQ $0A</p></td>
</tr>
<tr class="odd">
<td><p>$24</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Enable 2</a></p></td>
<td><p>IRQ_ENA2</p></td>
<td></td>
<td><p>IRQ $0B</p></td>
<td><p>IRQ $0C</p></td>
<td><p>IRQ $0D</p></td>
<td><p>IRQ $0E</p></td>
<td><p>IRQ $13</p></td>
<td><p>IRQ $14</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>$25</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Enable 3</a></p></td>
<td><p>IRQ_ENA3</p></td>
<td><p>IRQ $15</p></td>
<td><p>IRQ $16</p></td>
<td><p>IRQ $17</p></td>
<td><p>IRQ $18</p></td>
<td><p>IRQ $19</p></td>
<td><p>IRQ $1A</p></td>
<td><p>IRQ $1B</p></td>
<td><p>IRQ $1C</p></td>
</tr>
<tr class="odd">
<td><p>$26</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Enable 4</a></p></td>
<td><p>IRQ_ENA4</p></td>
<td><p>IRQ $0F</p></td>
<td><p>IRQ $10</p></td>
<td><p>IRQ ???</p></td>
<td><p>IRQ ???</p></td>
<td></td>
<td><p>IRQ $1D</p></td>
<td><p>IRQ $1E</p></td>
<td><p>IRQ $1F</p></td>
</tr>
<tr class="even">
<td><p>$27</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Active 1</a></p></td>
<td><p>IRQ_ACT1</p></td>
<td><p>IRQ $03</p></td>
<td><p>IRQ $04</p></td>
<td><p>IRQ $05</p></td>
<td><p>IRQ $06</p></td>
<td><p>IRQ $07</p></td>
<td><p>IRQ $08</p></td>
<td><p>IRQ $09</p></td>
<td><p>IRQ $0A</p></td>
</tr>
<tr class="odd">
<td><p>$28</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Active 2</a></p></td>
<td><p>IRQ_ACT2</p></td>
<td></td>
<td><p>IRQ $0B</p></td>
<td><p>IRQ $0C</p></td>
<td><p>IRQ $0D</p></td>
<td><p>IRQ $0E</p></td>
<td><p>IRQ $13</p></td>
<td><p>IRQ $14</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>$29</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Active 3</a></p></td>
<td><p>IRQ_ACT3</p></td>
<td><p>IRQ $15</p></td>
<td><p>IRQ $16</p></td>
<td><p>IRQ $17</p></td>
<td><p>IRQ $18</p></td>
<td><p>IRQ $19</p></td>
<td><p>IRQ $1A</p></td>
<td><p>IRQ $1B</p></td>
<td><p>IRQ $1C</p></td>
</tr>
<tr class="odd">
<td><p>$2A</p></td>
<td><p><a href="PM_IRQs" title="wikilink">IRQ Active 4</a></p></td>
<td><p>IRQ_ACT4</p></td>
<td><p>IRQ $0F</p></td>
<td><p>IRQ $10</p></td>
<td><p>IRQ ???</p></td>
<td><p>IRQ ???</p></td>
<td></td>
<td><p>IRQ $1D</p></td>
<td><p>IRQ $1E</p></td>
<td><p>IRQ $1F</p></td>
</tr>
<tr class="even">
<td><p>$30</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Control (Lo)</a></p></td>
<td><p>TMR1_CTRL_L</p></td>
<td><p>16-bit Mode</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$31</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Control (Hi)</a></p></td>
<td><p>TMR1_CTRL_H</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$32</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Preset (Lo)</a></p></td>
<td><p>TMR1_PRE_L</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$33</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Preset (Hi)</a></p></td>
<td><p>TMR1_PRE_H</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$34</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Pivot (Lo)</a></p></td>
<td><p>TMR1_PVT_L</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$35</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Pivot (Hi)</a></p></td>
<td><p>TMR1_PVT_H</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$36</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Count (Lo)</a></p></td>
<td><p>TMR1_CNT_L</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$37</p></td>
<td><p><a href="Timers" title="wikilink">Timer 1 Count (Hi)</a></p></td>
<td><p>TMR1_CNT_H</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$38</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Control (Lo)</a></p></td>
<td><p>TMR2_CTRL_L</p></td>
<td><p>16-bit Mode</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$39</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Control (Hi)</a></p></td>
<td><p>TMR2_CTRL_H</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$3A</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Preset (Lo)</a></p></td>
<td><p>TMR2_PRE_L</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$3B</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Preset (Hi)</a></p></td>
<td><p>TMR2_PRE_H</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$3C</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Pivot (Lo)</a></p></td>
<td><p>TMR2_PVT_L</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$3D</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Pivot (Hi)</a></p></td>
<td><p>TMR2_PVT_H</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$3E</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Count (Lo)</a></p></td>
<td><p>TMR2_CNT_L</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$3F</p></td>
<td><p><a href="Timers" title="wikilink">Timer 2 Count (Hi)</a></p></td>
<td><p>TMR2_CNT_H</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$40</p></td>
<td><p><a href="256Hz_Timer" title="wikilink">256Hz Timer Control</a></p></td>
<td><p>TMR256_CTRL</p></td>
<td></td>
<td><p>Reset</p></td>
<td><p>Enable</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$41</p></td>
<td><p><a href="256Hz_Timer" title="wikilink">256Hz Timer Counter</a></p></td>
<td><p>TMR256_CNT</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$44</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$45</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$46</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$47</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$48</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Control (Lo)</a></p></td>
<td><p>TMR3_CTRL_L</p></td>
<td><p>16-bit Mode</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$49</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Control (Hi)</a></p></td>
<td><p>TMR3_CTRL_H</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Enable</p></td>
<td><p>Reset</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$4A</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Preset (Lo)</a></p></td>
<td><p>TMR3_PRE_L</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$4B</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Preset (Hi)</a></p></td>
<td><p>TMR3_PRE_H</p></td>
<td><p>Preset</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$4C</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Pivot (Lo)</a></p></td>
<td><p>TMR3_PVT_L</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$4D</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Pivot (Hi)</a></p></td>
<td><p>TMR3_PVT_H</p></td>
<td><p>Pivot</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$4E</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Count (Lo)</a></p></td>
<td><p>TMR3_CNT_L</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$4F</p></td>
<td><p><a href="Timers" title="wikilink">Timer 3 Count (Hi)</a></p></td>
<td><p>TMR3_CNT_H</p></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$50</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$51</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$52</p></td>
<td><p>Key-Pad Status (Active 0)</p></td>
<td><p>KEY_PAD</p></td>
<td><p>Power</p></td>
<td><p>Right</p></td>
<td><p>Left</p></td>
<td><p>Down</p></td>
<td><p>Up</p></td>
<td><p>C</p></td>
<td><p>B</p></td>
<td><p>A</p></td>
</tr>
<tr class="odd">
<td><p>$53</p></td>
<td><p>Cart Bus</p></td>
<td><p>CART_BUS</p></td>
<td></td>
<td><p>CARD_N</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$54</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$55</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$60</p></td>
<td><p><a href="PM_I_O_Port" title="wikilink">I/O Direction Select</a></p></td>
<td><p>IO_DIR</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>IR Disable</p></td>
<td><p>Rumble</p></td>
<td><p>EEPROM Clock</p></td>
<td><p>EEPROM Data</p></td>
<td><p>IR Rx</p></td>
<td><p>IR Tx</p></td>
</tr>
<tr class="odd">
<td><p>$61</p></td>
<td><p><a href="PM_I_O_Port" title="wikilink">I/O Data Register</a></p></td>
<td><p>IO_DATA</p></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td><p>IR Disable</p></td>
<td><p>Rumble</p></td>
<td><p>EEPROM Clock</p></td>
<td><p>EEPROM Data</p></td>
<td><p>IR Rx</p></td>
<td><p>IR Tx</p></td>
</tr>
<tr class="even">
<td><p>$62</p></td>
<td><p>Unknown</p></td>
<td></td>
<td><p>???</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$70</p></td>
<td><p><a href="PM_Audio" title="wikilink">Audio Control</a></p></td>
<td><p>AUD_CTRL</p></td>
<td></td>
<td><p>???</p></td>
<td><p>Mutes audio if not 0!?</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$71</p></td>
<td><p><a href="PM_Audio" title="wikilink">Audio Volume</a></p></td>
<td><p>AUD_VOL</p></td>
<td></td>
<td><p>Cart Power (1=Off;0=On)</p></td>
<td><p>Volume</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$80</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Stage Control</a></p></td>
<td><p>PRC_MODE</p></td>
<td></td>
<td><p>Map Size</p></td>
<td><p>Ena Copy</p></td>
<td><p>Ena Sprites</p></td>
<td><p>Ena Map</p></td>
<td><p>Invert Map</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$81</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Rate Control</a></p></td>
<td><p>PRC_RATE</p></td>
<td><p>Frame counter</p></td>
<td><p>Rate divider</p></td>
<td><p>???</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$82</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Map Tile Base Low</a></p></td>
<td><p>PRC_MAP_LO</p></td>
<td><p>Map Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$83</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Map Tile Base Middle</a></p></td>
<td><p>PRC_MAP_MID</p></td>
<td><p>Map Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$84</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Map Tile Base High</a></p></td>
<td><p>PRC_MAP_HI</p></td>
<td></td>
<td><p>Map Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$85</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Map Vertical Scroll</a></p></td>
<td><p>PRC_SCROLL_Y</p></td>
<td></td>
<td><p>Map Scroll Y</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$86</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Map Horizontal Scroll</a></p></td>
<td><p>PRC_SCROLL_X</p></td>
<td></td>
<td><p>Map Scroll X</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$87</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Sprite Tile Base Low</a></p></td>
<td><p>PRC_SPR_LO</p></td>
<td><p>Sprite Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$88</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Sprite Tile Base Middle</a></p></td>
<td><p>PRC_SPR_MID</p></td>
<td><p>Sprite Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$89</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Sprite Tile Base Hi</a></p></td>
<td><p>PRC_SPR_HI</p></td>
<td></td>
<td><p>Sprite Tile Base</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$8A</p></td>
<td><p><a href="PM_PRC" title="wikilink">PRC Counter</a></p></td>
<td><p>PRC_CNT</p></td>
<td></td>
<td><p>Count</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$8B</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$8C</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$8D</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$8E</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$8F</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$F0</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$F1</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$F2</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$F3</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$F4</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$F5</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$F6</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$F7</p></td>
<td><p>Unknown (returns 0)</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>$FE</p></td>
<td><p><a href="LCD_Controller" title="wikilink">LCD Raw Control Byte</a></p></td>
<td><p>LCD_CTRL</p></td>
<td><p>LCD Control I/O</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>$FF</p></td>
<td><p><a href="LCD_Controller" title="wikilink">LCD Raw Data Byte</a></p></td>
<td><p>LCD_DATA</p></td>
<td><p>LCD Data I/O</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>