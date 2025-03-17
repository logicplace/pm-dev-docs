## Register Overview

The Pokémon mini maps $2000 \~ $20FF as hardware control registers. This area is reserved for hardware related functions such as video, audio, general purpose timers, hardware I/O and system control.

Much of this address space is mapped as [Open-Bus](/Glossary.md#open-bus "wikilink"), leading us to believe that this area is not used for any purpose. Other areas respond to requests but their purpose is yet undetermined.

Registers tend to be controlled on a bit level, so for the sanity purposes, they will be broken down to this level. At any point they are shown spanning multiple columns, that indicates that it is a multi-bit value and should be treated as if they were a number.

The bits themselves come in four flavors: Read-only, Write-Only, Read-Write, and S-R Strobe. Write-Only registers typically return a zero value, and are generally only used for things such as resetting timers. S-R Strobes are used for clearing interrupt events, writting a logical '1' to any bit that is set will result in a bit being cleared, where as '0' leaves them unchanged. Unused bits always return '0'.

Any register not included on this list reads as [Open-Bus](/Glossary.md#open-bus "wikilink") and will be excluded unless a function has otherwise been determined.

## Register Mapping

<table style="text-align: center;">
<caption><strong>Register Map Legend</strong></caption>
<tr>
<td style="border: 2px solid; background-color:#808080;">Unused</td>
<td style="border: 2px solid; background-color:#80ff80;">Read/Write</td>
<td style="border: 2px solid; background-color:#00ffff;">Read Only</td>
<td style="border: 2px solid; background-color:#ffff00;">Write Only</td>
<td style="border: 2px solid; background-color:#ffcc00;">S-R Strobe</td>
<td style="border: 2px solid; background-color:#00ffc0;">Read/Write (BIOS, Software only)</td>
<td style="border: 2px solid; background-color:#c0ff00;">Unknown (Read/Write)</td>
<td style="border: 2px solid; background-color:#c0ffc0;">Unknown (Weird)</td>
<td style="border: 2px solid; background-color:#c0c0c0;">Unknown (Unused)</td>
</tr>
</table>

<table style="text-align: center;">
<caption><strong>Registers ($2000 to $20FF)</strong></caption>
<tr>
<th style="border: 2px solid;">Address</th>
<th style="border: 2px solid;">Register</th>
<th style="border: 2px solid;">Const Name</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;7&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;6&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;5&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;4&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;3&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;2&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;1&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;0&nbsp;&gt;</th>
</tr><tr>
<td>$00</td>
<td>System Control 1</td>
<td>SYS_CTRL1</td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="6">Startup Contrast</td>
<td style="border: 2px solid; background-color:#80ff80;">Cartridge I/O Enable</td>
<td style="border: 2px solid; background-color:#80ff80;">LCD I/O Enable</td>
</tr><tr>
<td>$01</td>
<td>System Control 2</td>
<td>SYS_CTRL2</td>
<td style="border: 2px solid; background-color:#00ffc0;">Ram vector</td>
<td style="border: 2px solid; background-color:#00ffc0;">Int abort</td>
<td style="border: 2px solid; background-color:#00ffc0;">Enable cart interrupts</td>
<td style="border: 2px solid; background-color:#00ffc0;">Power on reset</td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="4">Cart type</td>
</tr><tr>
<td>$02</td>
<td>System Control 3</td>
<td>SYS_CTRL3</td>
<td style="border: 2px solid; background-color:#00ffc0;">Cart power state</td>
<td style="border: 2px solid; background-color:#00ffc0;">Cart power required</td>
<td style="border: 2px solid; background-color:#00ffc0;">Suspend mode</td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="3">???</td>
<td style="border: 2px solid; background-color:#00ffc0;">RTC Timer valid</td>
<td style="border: 2px solid; background-color:#00ffc0;">???</td>
</tr><tr>
<td>$08</td>
<td><a href="PM_Second_Counter.md" title="wikilink">Second Counter Control</a></td>
<td>SEC_CTRL</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
</tr><tr>
<td>$09</td>
<td><a href="PM_Second_Counter.md" title="wikilink">Second Counter Low</a></td>
<td>SEC_CNT_LO</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Counter</td>
</tr><tr>
<td>$0A</td>
<td><a href="PM_Second_Counter.md" title="wikilink">Second Counter Middle</a></td>
<td>SEC_CNT_MID</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Counter</td>
</tr><tr>
<td>$0B</td>
<td><a href="PM_Second_Counter.md" title="wikilink">Second Counter High</a></td>
<td>SEC_CNT_HI</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Counter</td>
</tr><tr>
<td>$10</td>
<td>Battery Sensor</td>
<td>SYS_BATT</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;">Low Battery</td>
<td style="border: 2px solid; background-color:#80ff80;">Battery ADC control</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="4">Battery ADC threshold value</td>
</tr><tr>
<td>$18</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Prescalars</a></td>
<td>TMR1_SCALE</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$19</td>
<td><a href="Timers.md" title="wikilink">Timers Osc. Enable<br />Timer 1 Osc. Select</a></td>
<td>TMR1_ENA_OSC<br />TMR1_OSC</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Osc. 1</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Osc. 2</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Lo)</td>
</tr><tr>
<td>$1A</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Prescalars</a></td>
<td>TMR2_SCALE</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$1B</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Osc. Select</a></td>
<td>TMR2_OSC</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Lo)</td>
</tr><tr>
<td>$1C</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Prescalars</a></td>
<td>TMR3_SCALE</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$1D</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Osc. Select</a></td>
<td>TMR3_OSC</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">2nd Osc. (Lo)</td>
</tr><tr>
<td>$20</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Priority 1</a></td>
<td>IRQ_PRI1</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $03 ~ $04</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $05 ~ $06</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $07 ~ $08</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $09 ~ $0A</td>
</tr><tr>
<td>$21</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Priority 2</a></td>
<td>IRQ_PRI2</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $0B ~ $0E</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $13 ~ $14</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $15 ~ $1C</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ ??? ($1D ~ $1F?)</td>
</tr><tr>
<td>$22</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Priority 3</a></td>
<td>IRQ_PRI3</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ $0F~$10</td>
</tr><tr>
<td>$23</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Enable 1</a></td>
<td>IRQ_ENA1</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $03</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $04</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $05</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $06</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $07</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $08</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $09</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0A</td>
</tr><tr>
<td>$24</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Enable 2</a></td>
<td>IRQ_ENA2</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0B</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0C</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0D</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0E</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $13</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $14</td>
</tr><tr>
<td>$25</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Enable 3</a></td>
<td>IRQ_ENA3</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $15</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $16</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $17</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $18</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $19</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1A</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1B</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1C</td>
</tr><tr>
<td>$26</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Enable 4</a></td>
<td>IRQ_ENA4</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $0F</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $10</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1D</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1E</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ $1F</td>
</tr><tr>
<td>$27</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Active 1</a></td>
<td>IRQ_ACT1</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $03</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $04</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $05</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $06</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $07</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $08</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $09</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0A</td>
</tr><tr>
<td>$28</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Active 2</a></td>
<td>IRQ_ACT2</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0B</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0C</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0D</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0E</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $13</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $14</td>
</tr><tr>
<td>$29</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Active 3</a></td>
<td>IRQ_ACT3</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $15</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $16</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $17</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $18</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $19</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1A</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1B</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1C</td>
</tr><tr>
<td>$2A</td>
<td><a href="PM_IRQs.md" title="wikilink">IRQ Active 4</a></td>
<td>IRQ_ACT4</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $0F</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $10</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1D</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1E</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ $1F</td>
</tr><tr>
<td>$30</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Control (Lo)</a></td>
<td>TMR1_CTRL_L</td>
<td style="border: 2px solid; background-color:#80ff80;">16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$31</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Control (Hi)</a></td>
<td>TMR1_CTRL_H</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$32</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Preset (Lo)</a></td>
<td>TMR1_PRE_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$33</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Preset (Hi)</a></td>
<td>TMR1_PRE_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$34</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Pivot (Lo)</a></td>
<td>TMR1_PVT_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$35</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Pivot (Hi)</a></td>
<td>TMR1_PVT_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$36</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Count (Lo)</a></td>
<td>TMR1_CNT_L</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$37</td>
<td><a href="Timers.md" title="wikilink">Timer 1 Count (Hi)</a></td>
<td>TMR1_CNT_H</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$38</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Control (Lo)</a></td>
<td>TMR2_CTRL_L</td>
<td style="border: 2px solid; background-color:#80ff80;">16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$39</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Control (Hi)</a></td>
<td>TMR2_CTRL_H</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$3A</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Preset (Lo)</a></td>
<td>TMR2_PRE_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$3B</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Preset (Hi)</a></td>
<td>TMR2_PRE_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$3C</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Pivot (Lo)</a></td>
<td>TMR2_PVT_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$3D</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Pivot (Hi)</a></td>
<td>TMR2_PVT_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$3E</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Count (Lo)</a></td>
<td>TMR2_CNT_L</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$3F</td>
<td><a href="Timers.md" title="wikilink">Timer 2 Count (Hi)</a></td>
<td>TMR2_CNT_H</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$40</td>
<td><a href="256Hz_Timer.md" title="wikilink">256Hz Timer Control</a></td>
<td>TMR256_CTRL</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
</tr><tr>
<td>$41</td>
<td><a href="256Hz_Timer.md" title="wikilink">256Hz Timer Counter</a></td>
<td>TMR256_CNT</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$44</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
</tr><tr>
<td>$45</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
</tr><tr>
<td>$46</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="8">???</td>
</tr><tr>
<td>$47</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
</tr><tr>
<td>$48</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Control (Lo)</a></td>
<td>TMR3_CTRL_L</td>
<td style="border: 2px solid; background-color:#80ff80;">16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$49</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Control (Hi)</a></td>
<td>TMR3_CTRL_H</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$4A</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Preset (Lo)</a></td>
<td>TMR3_PRE_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$4B</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Preset (Hi)</a></td>
<td>TMR3_PRE_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Preset</td>
</tr><tr>
<td>$4C</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Pivot (Lo)</a></td>
<td>TMR3_PVT_L</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$4D</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Pivot (Hi)</a></td>
<td>TMR3_PVT_H</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Pivot</td>
</tr><tr>
<td>$4E</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Count (Lo)</a></td>
<td>TMR3_CNT_L</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$4F</td>
<td><a href="Timers.md" title="wikilink">Timer 3 Count (Hi)</a></td>
<td>TMR3_CNT_H</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">Count</td>
</tr><tr>
<td>$50</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="8">???</td>
</tr><tr>
<td>$51</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="6">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="2">???</td>
</tr><tr>
<td>$52</td>
<td>Key-Pad Status (Active 0)</td>
<td>KEY_PAD</td>
<td style="border: 2px solid; background-color:#00ffff;">Power</td>
<td style="border: 2px solid; background-color:#00ffff;">Right</td>
<td style="border: 2px solid; background-color:#00ffff;">Left</td>
<td style="border: 2px solid; background-color:#00ffff;">Down</td>
<td style="border: 2px solid; background-color:#00ffff;">Up</td>
<td style="border: 2px solid; background-color:#00ffff;">C</td>
<td style="border: 2px solid; background-color:#00ffff;">B</td>
<td style="border: 2px solid; background-color:#00ffff;">A</td>
</tr><tr>
<td>$53</td>
<td>Cart Bus</td>
<td>CART_BUS</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;">CARD_N</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
</tr><tr>
<td>$54</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
</tr><tr>
<td>$55</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="5">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
</tr><tr>
<td>$60</td>
<td><a href="PM_I_O_Port.md" title="wikilink">I/O Direction Select</a></td>
<td>IO_DIR</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;">Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;">EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;">EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Rx</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Tx</td>
</tr><tr>
<td>$61</td>
<td><a href="PM_I_O_Port.md" title="wikilink">I/O Data Register</a></td>
<td>IO_DATA</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;">Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;">EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;">EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Rx</td>
<td style="border: 2px solid; background-color:#80ff80;">IR Tx</td>
</tr><tr>
<td>$62</td>
<td colspan="2">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
</tr><tr>
<td>$70</td>
<td><a href="PM_Audio.md" title="wikilink">Audio Control</a></td>
<td>AUD_CTRL</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Mutes audio if not 0!?</td>
</tr><tr>
<td>$71</td>
<td><a href="PM_Audio.md" title="wikilink">Audio Volume</a></td>
<td>AUD_VOL</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">Cart Power (1=Off; 0=On)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Volume</td>
</tr><tr>
<td>$80</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Stage Control</a></td>
<td>PRC_MODE</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Map Size</td>
<td style="border: 2px solid; background-color:#80ff80;">Ena Copy</td>
<td style="border: 2px solid; background-color:#80ff80;">Ena Sprites</td>
<td style="border: 2px solid; background-color:#80ff80;">Ena Map</td>
<td style="border: 2px solid; background-color:#80ff80;">Invert Map</td>
</tr><tr>
<td>$81</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Rate Control</a></td>
<td>PRC_RATE</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="4">Frame counter</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Rate divider</td>
<td style="border: 2px solid; background-color:#80ff80;">???</td>
</tr><tr>
<td>$82</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Map Tile Base Low</a></td>
<td>PRC_MAP_LO</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
</tr><tr>
<td>$83</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Map Tile Base Middle</a></td>
<td>PRC_MAP_MID</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Map Tile Base</td>
</tr><tr>
<td>$84</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Map Tile Base High</a></td>
<td>PRC_MAP_HI</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base</td>
</tr><tr>
<td>$85</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Map Vertical Scroll</a></td>
<td>PRC_SCROLL_Y</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll Y</td>
</tr><tr>
<td>$86</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Map Horizontal Scroll</a></td>
<td>PRC_SCROLL_X</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll X</td>
</tr><tr>
<td>$87</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Sprite Tile Base Low</a></td>
<td>PRC_SPR_LO</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Sprite Tile Base</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
</tr><tr>
<td>$88</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Sprite Tile Base Middle</a></td>
<td>PRC_SPR_MID</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Sprite Tile Base</td>
</tr><tr>
<td>$89</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Sprite Tile Base Hi</a></td>
<td>PRC_SPR_HI</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Sprite Tile Base</td>
</tr><tr>
<td>$8A</td>
<td><a href="PM_PRC.md" title="wikilink">PRC Counter</a></td>
<td>PRC_CNT</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="7">Count</td>
</tr><tr>
<td>$8B</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8C</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8D</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8E</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8F</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F0</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F1</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F2</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F3</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F4</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F5</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F6</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F7</td>
<td colspan="2">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$FE</td>
<td><a href="LCD_Controller.md" title="wikilink">LCD Raw Control Byte</a></td>
<td>LCD_CTRL</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Control I/O</td>
</tr><tr>
<td>$FF</td>
<td><a href="LCD_Controller.md" title="wikilink">LCD Raw Data Byte</a></td>
<td>LCD_DATA</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Data I/O</td>
</tr>
</table>
