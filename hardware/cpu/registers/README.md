## Register Overview

The Pokémon mini maps $2000 \~ $20FF as hardware control registers. This area is reserved for hardware related functions such as video, audio, general purpose timers, hardware I/O, and system control.

Much of this address space is mapped as [Open-Bus](/glossary.md#open-bus), leading us to believe that this area is not used for any purpose. Other areas respond to requests but their purpose is yet undetermined.

Registers tend to be controlled on a bit level, so for the sanity purposes, they will be broken down to this level. At any point they are shown spanning multiple columns, that indicates that it is a multi-bit value and should be treated as if they were a number.

The bits themselves come in four flavors: Read-only, Write-Only, Read-Write, and <abbr title="Set-Reset">S-R</abbr> Strobe. Write-Only registers typically return a zero value, and are generally only used for things such as resetting timers. S-R Strobes are used for clearing interrupt events, writting a logical '1' to any bit that is set will result in a bit being cleared, where as '0' leaves them unchanged. Unused bits always return '0'.

Any register not included on this list reads as [Open-Bus](/glossary.md#open-bus) and will be excluded unless a function has otherwise been determined.

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
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;7&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;6&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;5&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;4&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;3&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;2&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;1&nbsp;&gt;</th>
<th style="border: 2px solid; width:60px;">&lt;&nbsp;Bit&nbsp;0&nbsp;&gt;</th>
</tr><tr id="user-content-$00">
<td>$00</td><td rowspan="3">SYS_CTRL<br/>System Control</td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="6"><a href="lcd.md#startup-contrast">Startup Contrast</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="chip-enable.md">CE1</a><br/>Cartridge I/O Enable</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="chip-enable.md">CE0</a><br/>LCD I/O Enable</td>
</tr><tr id="user-content-$01">
<td>$01</td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01-7.md">01.7</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01-6.md">01.6</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="awake.md">System is awake</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01-4.md">01.4</a></td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="4"><a href="multicart.md">Multicart game mode</a></td>
</tr><tr id="user-content-$02">
<td>$02</td>
<td style="border: 2px solid; background-color:#c0ff00;"><a href="ebr.md">EBR</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="power.md#2002-bit-6">02.6</a><br/>Cart needs power</td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="suspended.md">02.5</a><br/>Suspended</td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="02-4.md">02.4</a><br/>Copy of OSCC</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="osc.md#clkchg">CLKCHG</a><br/>CPU osc</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="osc.md#oscc">OSCC</a><br/>OSC3 on</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="vdc.md">VDC</a><br/>System voltage</td>
</tr><tr id="user-content-$08">
<td>$08</td><td rowspan="1"><a href="timers.md#seconds-timer">SEC_CTRL</a><br/>Second Counter Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;">STRST<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">STRUN<br/>Enable</td>
</tr><tr id="user-content-$09">
<td>$09</td><td rowspan="3"><a href="timers.md#seconds-timer">SEC_CNT</a><br/>Second Counter</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">STD<br/>Counter (low)</td>
</tr><tr id="user-content-$0A">
<td>$0A</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">STD<br/>Counter (mid)</td>
</tr><tr id="user-content-$0B">
<td>$0B</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">STD<br/>Counter (high)</td>
</tr><tr id="user-content-$10">
<td>$10</td><td rowspan="1"><a href="svd.md">SYS_BATT</a><br/>Battery Sensor</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;">SVDDT<br/>Low Battery</td>
<td style="border: 2px solid; background-color:#80ff80;">SVDON<br/>Battery ADC control</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="4">SVDS<br/>Battery ADC threshold value</td>
</tr><tr id="user-content-$18">
<td>$18</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_SCALE</a><br/>PTM_A Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT1<br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST1<br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT0<br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST0<br/>Lo Scalar</td>
</tr><tr id="user-content-$19">
<td>$19</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_OSC</a><br/>PTM_A Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable OSC3?</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable OSC1?</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF1<br/>Use OSC1 (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF0<br/>Use OSC1 (Lo)</td>
</tr><tr id="user-content-$1A">
<td>$1A</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_SCALE</a><br/>PTM_B Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT3<br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST3<br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT2<br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST2<br/>Lo Scalar</td>
</tr><tr id="user-content-$1B">
<td>$1B</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_OSC</a><br/>PTM_B Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF3<br/>Use OSC1 (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF2<br/>Use OSC1 (Lo)</td>
</tr><tr id="user-content-$1C">
<td>$1C</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_SCALE</a><br/>PTM_C Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT5<br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST5<br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;">PRPRT4<br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">PST4<br/>Lo Scalar</td>
</tr><tr id="user-content-$1D">
<td>$1D</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_OSC</a><br/>PTM_C Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF5<br/>Use OSC1 (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;">PRTF4<br/>Use OSC1 (Lo)</td>
</tr><tr id="user-content-$20">
<td>$20</td><td rowspan="3"><a href="irq.md">IRQ_PRI</a><br/>IRQ Priority</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PLCD<br/>IRQ 06h ~ 08h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PPTB<br/>IRQ 0Ah ~ 0Ch</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PPTA<br/>IRQ 0Eh ~ 10h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PPTC<br/>IRQ 12h ~ 14h</td>
</tr><tr id="user-content-$21">
<td>$21</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PTM<br/>IRQ 16h ~ 1Ch</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PK1<br/>IRQ 26h ~ 28h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PK0<br/>IRQ 2Ah ~ 38h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ ??? (3Ah ~ 3Eh)</td>
</tr><tr id="user-content-$22">
<td>$22</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">PP0<br/>IRQ 1Eh~20h</td>
</tr><tr id="user-content-$23">
<td>$23</td><td rowspan="4"><a href="irq.md">IRQ_ENA</a><br/>IRQ Enable</td>
<td style="border: 2px solid; background-color:#80ff80;">ELCD<br/>IRQ 06h</td>
<td style="border: 2px solid; background-color:#80ff80;">ELCFR<br/>IRQ 08h</td>
<td style="border: 2px solid; background-color:#80ff80;">ETU3<br/>IRQ 0Ah</td>
<td style="border: 2px solid; background-color:#80ff80;">ETU2<br/>IRQ 0Ch</td>
<td style="border: 2px solid; background-color:#80ff80;">ETU1<br/>IRQ 0Eh</td>
<td style="border: 2px solid; background-color:#80ff80;">ETU0<br/>IRQ 10h</td>
<td style="border: 2px solid; background-color:#80ff80;">ETU5<br/>IRQ 12h</td>
<td style="border: 2px solid; background-color:#80ff80;">ETC5<br/>IRQ 14h</td>
</tr><tr id="user-content-$24">
<td>$24</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">ETM32<br/>IRQ 16h</td>
<td style="border: 2px solid; background-color:#80ff80;">ETM8<br/>IRQ 18h</td>
<td style="border: 2px solid; background-color:#80ff80;">ETM2<br/>IRQ 1Ah</td>
<td style="border: 2px solid; background-color:#80ff80;">ETM1<br/>IRQ 1Ch</td>
<td style="border: 2px solid; background-color:#80ff80;">EK11<br/>IRQ 26h</td>
<td style="border: 2px solid; background-color:#80ff80;">EK10<br/>IRQ 28h</td>
</tr><tr id="user-content-$25">
<td>$25</td>
<td style="border: 2px solid; background-color:#80ff80;">EK07<br/>IRQ 2Ah</td>
<td style="border: 2px solid; background-color:#80ff80;">EK06<br/>IRQ 2Ch</td>
<td style="border: 2px solid; background-color:#80ff80;">EK05<br/>IRQ 2Eh</td>
<td style="border: 2px solid; background-color:#80ff80;">EK04<br/>IRQ 30h</td>
<td style="border: 2px solid; background-color:#80ff80;">EK03<br/>IRQ 32h</td>
<td style="border: 2px solid; background-color:#80ff80;">EK02<br/>IRQ 34h</td>
<td style="border: 2px solid; background-color:#80ff80;">EK01<br/>IRQ 36h</td>
<td style="border: 2px solid; background-color:#80ff80;">EK00<br/>IRQ 38h</td>
</tr><tr id="user-content-$26">
<td>$26</td>
<td style="border: 2px solid; background-color:#80ff80;">EP0<br/>IRQ 1Eh</td>
<td style="border: 2px solid; background-color:#80ff80;">EP6<br/>IRQ 20h</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Ah</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Ch</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Eh</td>
</tr><tr id="user-content-$27">
<td>$27</td><td rowspan="4"><a href="irq.md">IRQ_ACT</a><br/>IRQ Factor</td>
<td style="border: 2px solid; background-color:#ffcc00;">FLCD<br/>IRQ 06h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FLCFR<br/>IRQ 08h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTU3<br/>IRQ 0Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTU2<br/>IRQ 0Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTU1<br/>IRQ 0Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTU0<br/>IRQ 10h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTU5<br/>IRQ 12h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTC5<br/>IRQ 14h</td>
</tr><tr id="user-content-$28">
<td>$28</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTM32<br/>IRQ 16h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTM8<br/>IRQ 18h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTM2<br/>IRQ 1Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;">FTM1<br/>IRQ 1Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK11<br/>IRQ 26h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK10<br/>IRQ 28h</td>
</tr><tr id="user-content-$29">
<td>$29</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK07<br/>IRQ 2Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK06<br/>IRQ 2Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK05<br/>IRQ 2Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK04<br/>IRQ 30h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK03<br/>IRQ 32h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK02<br/>IRQ 34h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK01<br/>IRQ 36h</td>
<td style="border: 2px solid; background-color:#ffcc00;">FK00<br/>IRQ 38h</td>
</tr><tr id="user-content-$2A">
<td>$2A</td>
<td style="border: 2px solid; background-color:#ffcc00;">FP0<br/>IRQ 1Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;">FP6<br/>IRQ 20h</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Eh</td>
</tr><tr id="user-content-$30">
<td>$30</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_CTRL_L</a><br/>PTM_A Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80; padding-left:0; padding-right:0">MODE16_A<br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT0</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN0<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET0<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL0</td>
</tr><tr id="user-content-$31">
<td>$31</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_CTRL_H</a><br/>PTM_A Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT1</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN1<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET1<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL1</td>
</tr><tr id="user-content-$32">
<td>$32</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_PRE_L</a><br/>PTM_A Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR0<br/>Preset</td>
</tr><tr id="user-content-$33">
<td>$33</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_PRE_H</a><br/>PTM_A Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR1<br/>Preset</td>
</tr><tr id="user-content-$34">
<td>$34</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_PVT_L</a><br/>PTM_A Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR0<br/>Compare data</td>
</tr><tr id="user-content-$35">
<td>$35</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_PVT_H</a><br/>PTM_A Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR1<br/>Compare data</td>
</tr><tr id="user-content-$36">
<td>$36</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_CNT_L</a><br/>PTM_A Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM0<br/>Count</td>
</tr><tr id="user-content-$37">
<td>$37</td><td rowspan="1"><a href="timers.md#ptm_a">TMR1_CNT_H</a><br/>PTM_A Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM1<br/>Count</td>
</tr><tr id="user-content-$38">
<td>$38</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_CTRL_L</a><br/>PTM_B Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80; padding-left:0; padding-right:0">MODE16_B<br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT2</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN2<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET2<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL2</td>
</tr><tr id="user-content-$39">
<td>$39</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_CTRL_H</a><br/>PTM_B Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT3</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN3<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET3<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL3</td>
</tr><tr id="user-content-$3A">
<td>$3A</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_PRE_L</a><br/>PTM_B Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR2<br/>Preset</td>
</tr><tr id="user-content-$3B">
<td>$3B</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_PRE_H</a><br/>PTM_B Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR3<br/>Preset</td>
</tr><tr id="user-content-$3C">
<td>$3C</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_PVT_L</a><br/>PTM_B Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR2<br/>Compare data</td>
</tr><tr id="user-content-$3D">
<td>$3D</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_PVT_H</a><br/>PTM_B Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR3<br/>Compare data</td>
</tr><tr id="user-content-$3E">
<td>$3E</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_CNT_L</a><br/>PTM_B Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM2<br/>Count</td>
</tr><tr id="user-content-$3F">
<td>$3F</td><td rowspan="1"><a href="timers.md#ptm_b">TMR2_CNT_H</a><br/>PTM_B Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM3<br/>Count</td>
</tr><tr id="user-content-$40">
<td>$40</td><td rowspan="1"><a href="timers.md#clock-timer">TMR256_CTRL</a><br/>Clock Timer Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;">TMRST<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">TMRUN<br/>Enable</td>
</tr><tr id="user-content-$41">
<td>$41</td><td rowspan="1"><a href="timers.md#clock-timer">TMR256_CNT</a><br/>Clock Timer Counter</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">TMD<br/>Count</td>
</tr><tr>
<td>$44</td>
<td rowspan="1">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
</tr><tr>
<td>$45</td>
<td rowspan="1">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
</tr><tr>
<td>$46</td>
<td rowspan="1">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="8">???</td>
</tr><tr>
<td>$47</td>
<td rowspan="1">Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
</tr><tr id="user-content-$48">
<td>$48</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_CTRL_L</a><br/>PTM_C Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80; padding-left:0; padding-right:0">MODE16_C<br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT4</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN4<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET4<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL4</td>
</tr><tr id="user-content-$49">
<td>$49</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_CTRL_H</a><br/>PTM_C Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">PTOUT5</td>
<td style="border: 2px solid; background-color:#80ff80;">PTRUN5<br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;">PSET5<br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;">CKSEL5</td>
</tr><tr id="user-content-$4A">
<td>$4A</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_PRE_L</a><br/>PTM_C Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR4<br/>Preset</td>
</tr><tr id="user-content-$4B">
<td>$4B</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_PRE_H</a><br/>PTM_C Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">RDR5<br/>Preset</td>
</tr><tr id="user-content-$4C">
<td>$4C</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_PVT_L</a><br/>PTM_C Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR4<br/>Compare data</td>
</tr><tr id="user-content-$4D">
<td>$4D</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_PVT_H</a><br/>PTM_C Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">CDR5<br/>Compare data</td>
</tr><tr id="user-content-$4E">
<td>$4E</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_CNT_L</a><br/>PTM_C Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM4<br/>Count</td>
</tr><tr id="user-content-$4F">
<td>$4F</td><td rowspan="1"><a href="timers.md#ptm_c">TMR3_CNT_H</a><br/>PTM_C Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8">PTM5<br/>Count</td>
</tr><tr id="user-content-$50">
<td>$50</td><td rowspan="1"><a href="irq.md#kcp1--kcp0">Keypad IRQ edge</a></td>
<td style="border: 2px solid; background-color:#80ff80;">KCP07<br/>Power</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP06<br/>Right</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP05<br/>Left</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP04<br/>Down</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP03<br/>Up</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP02<br/>C</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP01<br/>B</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP00<br/>A</td>
</tr><tr id="user-content-$51">
<td>$51</td><td rowspan="1"><a href="irq.md#kcp1--kcp0">Cartridge IRQ edge</a></td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP11<br/>Eject</td>
<td style="border: 2px solid; background-color:#80ff80;">KCP10<br/>Cartridge</td>
</tr><tr id="user-content-$52">
<td>$52</td><td rowspan="1"><a href="input.md">KEY_PAD</a><br/>Keypad Status (Active 0)</td>
<td style="border: 2px solid; background-color:#00ffff;">K07D<br/>Power</td>
<td style="border: 2px solid; background-color:#00ffff;">K06D<br/>Right</td>
<td style="border: 2px solid; background-color:#00ffff;">K05D<br/>Left</td>
<td style="border: 2px solid; background-color:#00ffff;">K04D<br/>Down</td>
<td style="border: 2px solid; background-color:#00ffff;">K03D<br/>Up</td>
<td style="border: 2px solid; background-color:#00ffff;">K02D<br/>C</td>
<td style="border: 2px solid; background-color:#00ffff;">K01D<br/>B</td>
<td style="border: 2px solid; background-color:#00ffff;">K00D<br/>A</td>
</tr><tr id="user-content-$53">
<td>$53</td><td rowspan="1"><a href="input.md">CART_BUS</a><br/>Cart Bus</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;">K11D<br/>CARD_N</td>
<td style="border: 2px solid; background-color:#00ffff;">K10D</td>
</tr><tr id="user-content-$54">
<td>$54</td><td rowspan="1"><a href="irq.md#ctk">unconfirmed</a></td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">CTK0H<br/>Unused?</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">CTK0L<br/>Keypad debounce rate?</td>
</tr><tr id="user-content-$55">
<td>$55</td><td rowspan="1"><a href="irq.md#ctk">unconfirmed</a></td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">CTK1L<br/>Cartridge debounce rate?</td>
</tr><tr id="user-content-$60">
<td>$60</td><td rowspan="1"><a href="io.md">IO_DIR</a><br/>I/O Direction Select</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC07<br/>???</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC06<br/>Shock</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC05<br/>IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC04<br/>Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC03<br/>EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC02<br/>EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC01<br/>IR Tx</td>
<td style="border: 2px solid; background-color:#80ff80;">IOC00<br/>IR Rx</td>
</tr><tr id="user-content-$61">
<td>$61</td><td rowspan="1"><a href="io.md">IO_DATA</a><br/>I/O Data Register</td>
<td style="border: 2px solid; background-color:#80ff80;">P07D<br/>???</td>
<td style="border: 2px solid; background-color:#80ff80;">P06D<br/>Shock</td>
<td style="border: 2px solid; background-color:#80ff80;">P05D<br/>IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;">P04D<br/>Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;">P03D<br/>EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;">P02D<br/>EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;">P01D<br/>IR Tx</td>
<td style="border: 2px solid; background-color:#80ff80;">P00D<br/>IR Rx</td>
</tr><tr>
<td>$62</td>
<td rowspan="1">Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
</tr><tr id="user-content-$70">
<td>$70</td><td rowspan="1">AUD_CTRL<br/>Audio Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="2"><a href="audio.md#2070-bits-10">Mutes audio if not 0!?</a></td>
</tr><tr id="user-content-$71">
<td>$71</td><td rowspan="1">AUD_VOL<br/>Audio Volume</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="power.md">Cart Power (1=Off; 0=On)</a></td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="audio.md#volume">Volume</a></td>
</tr><tr id="user-content-$80">
<td>$80</td><td rowspan="1"><a href="lcd.md#lcd-controller">PRC_MODE</a><br/>LCD Controller Settings</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Map Size</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Render</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Sprites</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Map</td>
<td style="border: 2px solid; background-color:#80ff80;">Invert Map</td>
</tr><tr id="user-content-$81">
<td>$81</td><td rowspan="1"><a href="lcd.md#frame-rate">PRC_RATE</a><br/>LCD Rate Control</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="4">Frame counter</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3">Rate divider</td>
<td style="border: 2px solid; background-color:#80ff80;">LCDEN<br/>Enabled</td>
</tr><tr id="user-content-$82">
<td>$82</td><td rowspan="3"><a href="lcd.md#tilemap">PRC_MAP</a><br/>PRC Map Tile Base</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base (low)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
</tr><tr id="user-content-$83">
<td>$83</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Map Tile Base (mid)</td>
</tr><tr id="user-content-$84">
<td>$84</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base (high)</td>
</tr><tr id="user-content-$85">
<td>$85</td><td rowspan="1"><a href="lcd.md#scrolling">PRC_SCROLL_Y</a><br/>PRC Map Vertical Scroll</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll Y</td>
</tr><tr id="user-content-$86">
<td>$86</td><td rowspan="1"><a href="lcd.md#scrolling">PRC_SCROLL_X</a><br/>PRC Map Horizontal Scroll</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll X</td>
</tr><tr id="user-content-$87">
<td>$87</td><td rowspan="3"><a href="lcd.md#sprites">PRC_SPR</a><br/>PRC Sprite Tile Base</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Sprite Tile Base (low)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
</tr><tr id="user-content-$88">
<td>$88</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Sprite Tile Base (mid)</td>
</tr><tr id="user-content-$89">
<td>$89</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Sprite Tile Base (high)</td>
</tr><tr id="user-content-$8A">
<td>$8A</td><td rowspan="1"><a href="lcd.md#lcd-line-counter">PRC_CNT</a><br/>LCD Line Counter</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="7">Count</td>
</tr><tr>
<td>$8B</td>
<td rowspan="13">Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8C</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8D</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8E</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8F</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F0</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F1</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F2</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F3</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F4</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F5</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F6</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F7</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr id="user-content-$FE">
<td>$FE</td><td rowspan="1"><a href="lcd.md">LCD_CTRL</a><br/>LCD Raw Control Byte</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Control I/O</td>
</tr><tr id="user-content-$FF">
<td>$FF</td><td rowspan="1"><a href="lcd.md">LCD_DATA</a><br/>LCD Raw Data Byte</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Data I/O</td>
</tr>
</table>