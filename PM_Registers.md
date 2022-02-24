## Register Overview

The Pokémon mini maps $2000 \~ $20FF as hardware control registers. This area is reserved for hardware related functions such as video, audio, general purpose timers, hardware I/O and system control.

Much of this address space is mapped as [Open-Bus](Open-Bus.md "wikilink"), leading us to believe that this area is not used for any purpose. Other areas respond to requests but their purpose is yet undetermined.

Registers tend to be controlled on a bit level, so for the sanity purposes, they will be broken down to this level. At any point they are shown spanning multiple columns, that indicates that it is a multi-bit value and should be treated as if they were a number.

The bits themselves come in four flavors: Read-only, Write-Only, Read-Write, and S-R Strobe. Write-Only registers typically return a zero value, and are generally only used for things such as resetting timers. S-R Strobes are used for clearing interrupt events, writting a logical '1' to any bit that is set will result in a bit being cleared, where as '0' leaves them unchanged. Unused bits always return '0'.

Any register not included on this list reads as [Open-Bus](Open-Bus.md "wikilink") and will be excluded unless a function has otherwise been determined.

## Register Mapping

<style>
th, td { border: 2px solid; text-align: center; }
.reg-x { background-color: #808080; }
.reg-rw { background-color: #80ff80; }
.reg-ro { background-color: #00ffff; }
.reg-wo { background-color: #ffff00; }
.reg-sr { background-color: #ffcc00; }
.reg-rwb { background-color: #00ffc0; }
.reg-unk-rw { background-color: #c0ff00; }
.reg-unk-q { background-color: #c0ffc0; }
.reg-unk-x { background-color: #c0c0c0; }
</style>

<table>
<caption><strong>Register Map Legend</strong></caption>
<tr>
<td class="reg-x">Unused</td>
<td class="reg-rw">Read/Write</td>
<td class="reg-ro">Read Only</td>
<td class="reg-wo">Write Only</td>
<td class="reg-sr">S-R Strobe</td>
<td class="reg-rwb">Read/Write (BIOS, Software only)</td>
<td class="reg-unk-rw">Unknown (Read/Write)</td>
<td class="reg-unk-q">Unknown (Weird)</td>
<td class="reg-unk-x">Unknown (Unused)</td>
</tr></table>

<table>
<caption><strong>Registers ($2000 to $20FF)</strong></caption>
<tr>
<th>Address</th>
<th>Register</th>
<th>Const Name</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;7&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;6&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;5&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;4&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;3&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;2&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;1&nbsp;&gt;</th>
<th style="width:60px;">&lt;&nbsp;Bit&nbsp;0&nbsp;&gt;</th>
</tr><tr>
<td>$00</td>
<td>System Control 1</td>
<td>SYS_CTRL1</td>
<td class="reg-rwb" colspan="6">Startup Contrast</td>
<td class="reg-rw">Cartridge I/O Enable</td>
<td class="reg-rw">LCD I/O Enable</td>
</tr><tr>
<td>$01</td>
<td>System Control 2</td>
<td>SYS_CTRL2</td>
<td class="reg-rwb">Ram vector</td>
<td class="reg-rwb">Int abort</td>
<td class="reg-rwb">Enable cart interrupts</td>
<td class="reg-rwb">Power on reset</td>
<td class="reg-rwb" colspan="4">Cart type</td>
</tr><tr>
<td>$02</td>
<td>System Control 3</td>
<td>SYS_CTRL3</td>
<td class="reg-rwb">Cart power state</td>
<td class="reg-rwb">Cart power required</td>
<td class="reg-rwb">Suspend mode</td>
<td class="reg-rwb" colspan="3">???</td>
<td class="reg-rwb">RTC Timer valid</td>
<td class="reg-rwb">???</td>
</tr><tr>
<td>$08</td>
<td>[Second Counter Control](PM_Second_Counter.md "wikilink")</td>
<td>SEC_CTRL</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">Enable</td>
</tr><tr>
<td>$09</td>
<td>[Second Counter Low](PM_Second_Counter.md "wikilink")</td>
<td>SEC_CNT_LO</td>
<td class="reg-ro" colspan="8">Counter</td>
</tr><tr>
<td>$0A</td>
<td>[Second Counter Middle](PM_Second_Counter.md "wikilink")</td>
<td>SEC_CNT_MID</td>
<td class="reg-ro" colspan="8">Counter</td>
</tr><tr>
<td>$0B</td>
<td>[Second Counter High](PM_Second_Counter.md "wikilink")</td>
<td>SEC_CNT_HI</td>
<td class="reg-ro" colspan="8">Counter</td>
</tr><tr>
<td>$10</td>
<td>Battery Sensor</td>
<td>SYS_BATT</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-ro">Low Battery</td>
<td class="reg-rw">Battery ADC control</td>
<td class="reg-rw" colspan="4">Battery ADC threshold value</td>
</tr><tr>
<td>$18</td>
<td>[Timer 1 Prescalars](Timers.md "wikilink")</td>
<td>TMR1_SCALE</td>
<td class="reg-rw">Enable Hi</td>
<td class="reg-rw" colspan="3">Hi Scalar</td>
<td class="reg-rw">Enable Lo</td>
<td class="reg-rw" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$19</td>
<td>[Timers Osc. Enable<br />Timer 1 Osc. Select](Timers.md "wikilink")</td>
<td>TMR1_ENA_OSC<br />TMR1_OSC</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-rw">Enable Osc. 1</td>
<td class="reg-rw">Enable Osc. 2</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-rw">2nd Osc. (Hi)</td>
<td class="reg-rw">2nd Osc. (Lo)</td>
</tr><tr>
<td>$1A</td>
<td>[Timer 2 Prescalars](Timers.md "wikilink")</td>
<td>TMR2_SCALE</td>
<td class="reg-rw">Enable Hi</td>
<td class="reg-rw" colspan="3">Hi Scalar</td>
<td class="reg-rw">Enable Lo</td>
<td class="reg-rw" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$1B</td>
<td>[Timer 2 Osc. Select](Timers.md "wikilink")</td>
<td>TMR2_OSC</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-rw">2nd Osc. (Hi)</td>
<td class="reg-rw">2nd Osc. (Lo)</td>
</tr><tr>
<td>$1C</td>
<td>[Timer 3 Prescalars](Timers.md "wikilink")</td>
<td>TMR3_SCALE</td>
<td class="reg-rw">Enable Hi</td>
<td class="reg-rw" colspan="3">Hi Scalar</td>
<td class="reg-rw">Enable Lo</td>
<td class="reg-rw" colspan="3">Lo Scalar</td>
</tr><tr>
<td>$1D</td>
<td>[Timer 3 Osc. Select](Timers.md "wikilink")</td>
<td>TMR3_OSC</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-rw">2nd Osc. (Hi)</td>
<td class="reg-rw">2nd Osc. (Lo)</td>
</tr><tr>
<td>$20</td>
<td>[IRQ Priority 1](PM_IRQs.md "wikilink")</td>
<td>IRQ_PRI1</td>
<td class="reg-rw" colspan="2">IRQ $03 ~ $04</td>
<td class="reg-rw" colspan="2">IRQ $05 ~ $06</td>
<td class="reg-rw" colspan="2">IRQ $07 ~ $08</td>
<td class="reg-rw" colspan="2">IRQ $09 ~ $0A</td>
</tr><tr>
<td>$21</td>
<td>[IRQ Priority 2](PM_IRQs.md "wikilink")</td>
<td>IRQ_PRI2</td>
<td class="reg-rw" colspan="2">IRQ $0B ~ $0E</td>
<td class="reg-rw" colspan="2">IRQ $13 ~ $14</td>
<td class="reg-rw" colspan="2">IRQ $15 ~ $1C</td>
<td class="reg-rw" colspan="2">IRQ ??? ($1D ~ $1F?)</td>
</tr><tr>
<td>$22</td>
<td>[IRQ Priority 3](PM_IRQs.md "wikilink")</td>
<td>IRQ_PRI3</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-rw" colspan="2">IRQ $0F~$10</td>
</tr><tr>
<td>$23</td>
<td>[IRQ Enable 1](PM_IRQs.md "wikilink")</td>
<td>IRQ_ENA1</td>
<td class="reg-rw">IRQ $03</td>
<td class="reg-rw">IRQ $04</td>
<td class="reg-rw">IRQ $05</td>
<td class="reg-rw">IRQ $06</td>
<td class="reg-rw">IRQ $07</td>
<td class="reg-rw">IRQ $08</td>
<td class="reg-rw">IRQ $09</td>
<td class="reg-rw">IRQ $0A</td>
</tr><tr>
<td>$24</td>
<td>[IRQ Enable 2](PM_IRQs.md "wikilink")</td>
<td>IRQ_ENA2</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-rw">IRQ $0B</td>
<td class="reg-rw">IRQ $0C</td>
<td class="reg-rw">IRQ $0D</td>
<td class="reg-rw">IRQ $0E</td>
<td class="reg-rw">IRQ $13</td>
<td class="reg-rw">IRQ $14</td>
</tr><tr>
<td>$25</td>
<td>[IRQ Enable 3](PM_IRQs.md "wikilink")</td>
<td>IRQ_ENA3</td>
<td class="reg-rw">IRQ $15</td>
<td class="reg-rw">IRQ $16</td>
<td class="reg-rw">IRQ $17</td>
<td class="reg-rw">IRQ $18</td>
<td class="reg-rw">IRQ $19</td>
<td class="reg-rw">IRQ $1A</td>
<td class="reg-rw">IRQ $1B</td>
<td class="reg-rw">IRQ $1C</td>
</tr><tr>
<td>$26</td>
<td>[IRQ Enable 4](PM_IRQs.md "wikilink")</td>
<td>IRQ_ENA4</td>
<td class="reg-rw">IRQ $0F</td>
<td class="reg-rw">IRQ $10</td>
<td class="reg-rw">IRQ ???</td>
<td class="reg-rw">IRQ ???</td>
<td class="reg-x">&nbsp;</td>
<td class="reg-rw">IRQ $1D</td>
<td class="reg-rw">IRQ $1E</td>
<td class="reg-rw">IRQ $1F</td>
</tr><tr>
<td>$27</td>
<td>[IRQ Active 1](PM_IRQs.md "wikilink")</td>
<td>IRQ_ACT1</td>
<td class="reg-sr">IRQ $03</td>
<td class="reg-sr">IRQ $04</td>
<td class="reg-sr">IRQ $05</td>
<td class="reg-sr">IRQ $06</td>
<td class="reg-sr">IRQ $07</td>
<td class="reg-sr">IRQ $08</td>
<td class="reg-sr">IRQ $09</td>
<td class="reg-sr">IRQ $0A</td>
</tr><tr>
<td>$28</td>
<td>[IRQ Active 2](PM_IRQs.md "wikilink")</td>
<td>IRQ_ACT2</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-sr">IRQ $0B</td>
<td class="reg-sr">IRQ $0C</td>
<td class="reg-sr">IRQ $0D</td>
<td class="reg-sr">IRQ $0E</td>
<td class="reg-sr">IRQ $13</td>
<td class="reg-sr">IRQ $14</td>
</tr><tr>
<td>$29</td>
<td>[IRQ Active 3](PM_IRQs.md "wikilink")</td>
<td>IRQ_ACT3</td>
<td class="reg-sr">IRQ $15</td>
<td class="reg-sr">IRQ $16</td>
<td class="reg-sr">IRQ $17</td>
<td class="reg-sr">IRQ $18</td>
<td class="reg-sr">IRQ $19</td>
<td class="reg-sr">IRQ $1A</td>
<td class="reg-sr">IRQ $1B</td>
<td class="reg-sr">IRQ $1C</td>
</tr><tr>
<td>$2A</td>
<td>[IRQ Active 4](PM_IRQs.md "wikilink")</td>
<td>IRQ_ACT4</td>
<td class="reg-sr">IRQ $0F</td>
<td class="reg-sr">IRQ $10</td>
<td class="reg-sr">IRQ ???</td>
<td class="reg-sr">IRQ ???</td>
<td class="reg-x">&nbsp;</td>
<td class="reg-sr">IRQ $1D</td>
<td class="reg-sr">IRQ $1E</td>
<td class="reg-sr">IRQ $1F</td>
</tr><tr>
<td>$30</td>
<td>[Timer 1 Control (Lo)](Timers.md "wikilink")</td>
<td>TMR1_CTRL_L</td>
<td class="reg-rw">16-bit Mode</td>
<td class="reg-x" colspan="3">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$31</td>
<td>[Timer 1 Control (Hi)](Timers.md "wikilink")</td>
<td>TMR1_CTRL_H</td>
<td class="reg-x" colspan="4">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$32</td>
<td>[Timer 1 Preset (Lo)](Timers.md "wikilink")</td>
<td>TMR1_PRE_L</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$33</td>
<td>[Timer 1 Preset (Hi)](Timers.md "wikilink")</td>
<td>TMR1_PRE_H</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$34</td>
<td>[Timer 1 Pivot (Lo)](Timers.md "wikilink")</td>
<td>TMR1_PVT_L</td>
<td class="reg-rw" colspan="8">Pivot</td>
</tr><tr>
<td>$35</td>
<td>[Timer 1 Pivot (Hi)](Timers.md "wikilink")</td>
<td>TMR1_PVT_H</td>
<td class="reg-rw" colspan="8">Pivot</td>
</tr><tr>
<td>$36</td>
<td>[Timer 1 Count (Lo)](Timers.md "wikilink")</td>
<td>TMR1_CNT_L</td>
<td class="reg-ro" colspan="8">Count</td>
</tr><tr>
<td>$37</td>
<td>[Timer 1 Count (Hi)](Timers.md "wikilink")</td>
<td>TMR1_CNT_H</td>
<td class="reg-ro" colspan="8">Count</td>
</tr><tr>
<td>$38</td>
<td>[Timer 2 Control (Lo)](Timers.md "wikilink")</td>
<td>TMR2_CTRL_L</td>
<td class="reg-rw">16-bit Mode</td>
<td class="reg-x" colspan="3">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$39</td>
<td>[Timer 2 Control (Hi)](Timers.md "wikilink")</td>
<td>TMR2_CTRL_H</td>
<td class="reg-x" colspan="4">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$3A</td>
<td>[Timer 2 Preset (Lo)](Timers.md "wikilink")</td>
<td>TMR2_PRE_L</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$3B</td>
<td>[Timer 2 Preset (Hi)](Timers.md "wikilink")</td>
<td>TMR2_PRE_H</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$3C</td>
<td>[Timer 2 Pivot (Lo)](Timers.md "wikilink")</td>
<td>TMR2_PVT_L</td>
<td class="reg-rw" colspan="8">Pivot</td>
<td>Pivot</td>
</tr><tr>
<td>$3D</td>
<td>[Timer 2 Pivot (Hi)](Timers.md "wikilink")</td>
<td>TMR2_PVT_H</td>
<td class="reg-rw" colspan="8">Pivot</td>
<td>Pivot</td>
</tr><tr>
<td>$3E</td>
<td>[Timer 2 Count (Lo)](Timers.md "wikilink")</td>
<td>TMR2_CNT_L</td>
<td class="reg-ro" colspan="8">Count</td>
<td>Count</td>
</tr><tr>
<td>$3F</td>
<td>[Timer 2 Count (Hi)](Timers.md "wikilink")</td>
<td>TMR2_CNT_H</td>
<td class="reg-ro" colspan="8">Count</td>
<td>Count</td>
</tr><tr>
<td>$40</td>
<td>[256Hz Timer Control](256Hz_Timer.md "wikilink")</td>
<td>TMR256_CTRL</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">Enable</td>
</tr><tr>
<td>$41</td>
<td>[256Hz Timer Counter](256Hz_Timer.md "wikilink")</td>
<td>TMR256_CNT</td>
<td class="reg-ro" colspan="8">Count</td>
</tr><tr>
<td>$44</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-rw" colspan="4">???</td>
<td class="reg-unk-x">???</td>
<td class="reg-unk-rw" colspan="3">???</td>
</tr><tr>
<td>$45</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-x" colspan="4">???</td>
<td class="reg-unk-q">???</td>
<td class="reg-unk-rw">???</td>
<td class="reg-unk-q">???</td>
<td class="reg-unk-rw">???</td>
</tr><tr>
<td>$46</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-rw" colspan="8">???</td>
</tr><tr>
<td>$47</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-x" colspan="4">???</td>
<td class="reg-unk-rw" colspan="4">???</td>
</tr><tr>
<td>$48</td>
<td>[Timer 3 Control (Lo)](Timers.md "wikilink")</td>
<td>TMR3_CTRL_L</td>
<td class="reg-rw">16-bit Mode</td>
<td class="reg-x" colspan="3">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$49</td>
<td>[Timer 3 Control (Hi)](Timers.md "wikilink")</td>
<td>TMR3_CTRL_H</td>
<td class="reg-x" colspan="4">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw">Enable</td>
<td class="reg-wo">Reset</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$4A</td>
<td>[Timer 3 Preset (Lo)](Timers.md "wikilink")</td>
<td>TMR3_PRE_L</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$4B</td>
<td>[Timer 3 Preset (Hi)](Timers.md "wikilink")</td>
<td>TMR3_PRE_H</td>
<td class="reg-rw" colspan="8">Preset</td>
</tr><tr>
<td>$4C</td>
<td>[Timer 3 Pivot (Lo)](Timers.md "wikilink")</td>
<td>TMR3_PVT_L</td>
<td class="reg-rw" colspan="8">Pivot</td>
</tr><tr>
<td>$4D</td>
<td>[Timer 3 Pivot (Hi)](Timers.md "wikilink")</td>
<td>TMR3_PVT_H</td>
<td class="reg-rw" colspan="8">Pivot</td>
</tr><tr>
<td>$4E</td>
<td>[Timer 3 Count (Lo)](Timers.md "wikilink")</td>
<td>TMR3_CNT_L</td>
<td class="reg-ro" colspan="8">Count</td>
</tr><tr>
<td>$4F</td>
<td>[Timer 3 Count (Hi)](Timers.md "wikilink")</td>
<td>TMR3_CNT_H</td>
<td class="reg-ro" colspan="8">Count</td>
</tr><tr>
<td>$50</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-rw" colspan="8">???</td>
</tr><tr>
<td>$51</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-x" colspan="6">???</td>
<td class="reg-unk-rw" colspan="2">???</td>
</tr><tr>
<td>$52</td>
<td>Key-Pad Status (Active 0)</td>
<td>KEY_PAD</td>
<td class="reg-ro">Power</td>
<td class="reg-ro">Right</td>
<td class="reg-ro">Left</td>
<td class="reg-ro">Down</td>
<td class="reg-ro">Up</td>
<td class="reg-ro">C</td>
<td class="reg-ro">B</td>
<td class="reg-ro">A</td>
</tr><tr>
<td>$53</td>
<td>Cart Bus</td>
<td>CART_BUS</td>
<td class="reg-x" colspan="6">&nbsp;</td>
<td class="reg-ro">CARD_N</td>
<td class="reg-x">&nbsp;</td>
</tr><tr>
<td>$54</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-x">???</td>
<td class="reg-unk-rw" colspan="3">???</td>
<td class="reg-unk-x">???</td>
<td class="reg-unk-rw" colspan="3">???</td>
</tr><tr>
<td>$55</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-x" colspan="5">???</td>
<td class="reg-unk-rw" colspan="3">???</td>
</tr><tr>
<td>$60</td>
<td>[I/O Direction Select](PM_I_O_Port.md "wikilink")</td>
<td>IO_DIR</td>
<td class="reg-rw">???</td>
<td class="reg-rw">???</td>
<td class="reg-rw">IR Disable</td>
<td class="reg-rw">Rumble</td>
<td class="reg-rw">EEPROM Clock</td>
<td class="reg-rw">EEPROM Data</td>
<td class="reg-rw">IR Rx</td>
<td class="reg-rw">IR Tx</td>
</tr><tr>
<td>$61</td>
<td>[I/O Data Register](PM_I_O_Port.md "wikilink")</td>
<td>IO_DATA</td>
<td class="reg-rw">???</td>
<td class="reg-rw">???</td>
<td class="reg-rw">IR Disable</td>
<td class="reg-rw">Rumble</td>
<td class="reg-rw">EEPROM Clock</td>
<td class="reg-rw">EEPROM Data</td>
<td class="reg-rw">IR Rx</td>
<td class="reg-rw">IR Tx</td>
</tr><tr>
<td>$62</td>
<td colspan="2">Unknown</td>
<td class="reg-unk-rw" colspan="4">???</td>
<td class="reg-unk-x" colspan="4">???</td>
</tr><tr>
<td>$70</td>
<td>[Audio Control](PM_Audio.md "wikilink")</td>
<td>AUD_CTRL</td>
<td class="reg-x" colspan="5">&nbsp;</td>
<td class="reg-rw">???</td>
<td class="reg-rw" colspan="2">Mutes audio if not 0!?</td>
</tr><tr>
<td>$71</td>
<td>[Audio Volume](PM_Audio.md "wikilink")</td>
<td>AUD_VOL</td>
<td class="reg-x" colspan="5">&nbsp;</td>
<td class="reg-rw">Cart Power (1=Off; 0=On)</td>
<td class="reg-rw" colspan="2">Volume</td>
</tr><tr>
<td>$80</td>
<td>[PRC Stage Control](PM_PRC.md "wikilink")</td>
<td>PRC_MODE</td>
<td class="reg-x" colspan="2">&nbsp;</td>
<td class="reg-rw" colspan="2">Map Size</td>
<td class="reg-rw">Ena Copy</td>
<td class="reg-rw">Ena Sprites</td>
<td class="reg-rw">Ena Map</td>
<td class="reg-rw">Invert Map</td>
</tr><tr>
<td>$81</td>
<td>[PRC Rate Control](PM_PRC.md "wikilink")</td>
<td>PRC_RATE</td>
<td class="reg-ro" colspan="4">Frame counter</td>
<td class="reg-rw" colspan="3">Rate divider</td>
<td class="reg-rw">???</td>
</tr><tr>
<td>$82</td>
<td>[PRC Map Tile Base Low](PM_PRC.md "wikilink")</td>
<td>PRC_MAP_LO</td>
<td class="reg-rw" colspan="5">Map Tile Base</td>
<td class="reg-x" colspan="3">&nbsp;</td>
</tr><tr>
<td>$83</td>
<td>[PRC Map Tile Base Middle](PM_PRC.md "wikilink")</td>
<td>PRC_MAP_MID</td>
<td class="reg-rw" colspan="8">Map Tile Base</td>
</tr><tr>
<td>$84</td>
<td>[PRC Map Tile Base High](PM_PRC.md "wikilink")</td>
<td>PRC_MAP_HI</td>
<td class="reg-x" colspan="3">&nbsp;</td>
<td class="reg-rw" colspan="5">Map Tile Base</td>
</tr><tr>
<td>$85</td>
<td>[PRC Map Vertical Scroll](PM_PRC.md "wikilink")</td>
<td>PRC_SCROLL_Y</td>
<td class="reg-x">&nbsp;</td>
<td class="reg-rw" colspan="7">Map Scroll Y</td>
</tr><tr>
<td>$86</td>
<td>[PRC Map Horizontal Scroll](PM_PRC.md "wikilink")</td>
<td>PRC_SCROLL_X</td>
<td class="reg-x">&nbsp;</td>
<td class="reg-rw" colspan="7">Map Scroll X</td>
</tr><tr>
<td>$87</td>
<td>[PRC Sprite Tile Base Low](PM_PRC.md "wikilink")</td>
<td>PRC_SPR_LO</td>
<td class="reg-rw" colspan="2">Sprite Tile Base</td>
<td class="reg-x" colspan="6">&nbsp;</td>
</tr><tr>
<td>$88</td>
<td>[PRC Sprite Tile Base Middle](PM_PRC.md "wikilink")</td>
<td>PRC_SPR_MID</td>
<td class="reg-rw" colspan="8">Sprite Tile Base</td>
</tr><tr>
<td>$89</td>
<td>[PRC Sprite Tile Base Hi](PM_PRC.md "wikilink")</td>
<td>PRC_SPR_HI</td>
<td class="reg-x" colspan="3">&nbsp;</td>
<td class="reg-rw" colspan="5">Sprite Tile Base</td>
</tr><tr>
<td>$8A</td>
<td>[PRC Counter](PM_PRC.md "wikilink")</td>
<td>PRC_CNT</td>
<td class="reg-x">&nbsp;</td>
<td class="reg-ro" colspan="7">Count</td>
</tr><tr>
<td>$8B</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8C</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8D</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8E</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8F</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F0</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F1</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F2</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F3</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F4</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F5</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F6</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F7</td>
<td colspan="2">Unknown (returns 0)</td>
<td class="reg-x" colspan="8">&nbsp;</td>
</tr><tr>
<td>$FE</td>
<td>[LCD Raw Control Byte](LCD_Controller.md "wikilink")</td>
<td>LCD_CTRL</td>
<td class="reg-rw" colspan="8">LCD Control I/O</td>
</tr><tr>
<td>$FF</td>
<td>[LCD Raw Data Byte](LCD_Controller.md "wikilink")</td>
<td>LCD_DATA</td>
<td class="reg-rw" colspan="8">LCD Data I/O</td>
</tr>
</table>
