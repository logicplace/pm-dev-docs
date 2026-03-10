## Register Overview

The Pokémon mini maps $2000 \~ $20FF as hardware control registers. This area is reserved for hardware related functions such as video, audio, general purpose timers, hardware I/O, and system control.

Much of this address space is mapped as [Open-Bus](/glossary.md#open-bus), leading us to believe that this area is not used for any purpose. Other areas respond to requests but their purpose is yet undetermined.

Registers tend to be controlled on a bit level, so for the sanity purposes, they will be broken down to this level. At any point they are shown spanning multiple columns, that indicates that it is a multi-bit value and should be treated as if they were a number.

The bits themselves come in four flavors: Read-only, Write-Only, Read-Write, and S-R Strobe. Write-Only registers typically return a zero value, and are generally only used for things such as resetting timers. S-R Strobes are used for clearing interrupt events, writting a logical '1' to any bit that is set will result in a bit being cleared, where as '0' leaves them unchanged. Unused bits always return '0'.

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
</tr><tr>
<td>$00</td><td rowspan="3">
    <a href="00.md">SYS_CTRL</a><br/>System Control</td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="6"><a href="contrast.md">contrast</a><br/>Startup Contrast</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CE1.md">CE1</a><br/>Cartridge I/O Enable</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CE0.md">CE0</a><br/>LCD I/O Enable</td>
</tr><tr>
<td>$01</td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01.7.md">01.7</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01.6.md">01.6</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="awake.md">awake</a><br/>System is awake</td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="01.4.md">01.4</a></td>
<td style="border: 2px solid; background-color:#00ffc0;" colspan="4"><a href="mcgm.md">mcgm</a><br/>Multicart game mode</td>
</tr><tr>
<td>$02</td>
<td style="border: 2px solid; background-color:#c0ff00;"><a href="EBR.md">EBR</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="02.6.md">02.6</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="02.5.md">02.5</a></td>
<td style="border: 2px solid; background-color:#00ffc0;"><a href="02.4.md">02.4</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CLKCHG.md">CLKCHG</a><br/>OSC clocking CPU</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="OSCC.md">OSCC</a><br/>OSC3 on</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="VDC.md">VDC</a><br/>System voltage</td>
</tr><tr>
<td>$08</td><td rowspan="1">
    <a href="08.md">SEC_CTRL</a><br/>Second Counter Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="STRST.md">STRST</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="STRUN.md">STRUN</a><br/>Enable</td>
</tr><tr>
<td>$09</td><td rowspan="3">
    <a href="09.md">SEC_CNT</a><br/>Second Counter</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="STD.md">STD</a><br/>Counter (low)</td>
</tr><tr>
<td>$0A</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="STD.md">STD</a><br/>Counter (mid)</td>
</tr><tr>
<td>$0B</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="STD.md">STD</a><br/>Counter (high)</td>
</tr><tr>
<td>$10</td><td rowspan="1">
    <a href="10.md">SYS_BATT</a><br/>Battery Sensor</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="SVDDT.md">SVDDT</a><br/>Low Battery</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="SVDON.md">SVDON</a><br/>Battery ADC control</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="4"><a href="SVDS.md">SVDS</a><br/>Battery ADC threshold value</td>
</tr><tr>
<td>$18</td><td rowspan="1">
    <a href="18.md">TMR1_SCALE</a><br/>PTM_A Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT1.md">PRPRT1</a><br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST1.md">PST1</a><br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT0.md">PRPRT0</a><br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST0.md">PST0</a><br/>Lo Scalar</td>
</tr><tr>
<td>$19</td><td rowspan="1">
    <a href="18.md">TMR1_OSC</a><br/>PTM_A Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable OSC3?</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable OSC1?</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF1.md">PRTF1</a><br/>2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF0.md">PRTF0</a><br/>2nd Osc. (Lo)</td>
</tr><tr>
<td>$1A</td><td rowspan="1">
    <a href="1A.md">TMR2_SCALE</a><br/>PTM_B Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT3.md">PRPRT3</a><br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST3.md">PST3</a><br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT2.md">PRPRT2</a><br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST2.md">PST2</a><br/>Lo Scalar</td>
</tr><tr>
<td>$1B</td><td rowspan="1">
    <a href="1A.md">TMR2_OSC</a><br/>PTM_B Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF3.md">PRTF3</a><br/>2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF2.md">PRTF2</a><br/>2nd Osc. (Lo)</td>
</tr><tr>
<td>$1C</td><td rowspan="1">
    <a href="1C.md">TMR3_SCALE</a><br/>PTM_C Prescalars</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT5.md">PRPRT5</a><br/>Enable Hi</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST5.md">PST5</a><br/>Hi Scalar</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRPRT4.md">PRPRT4</a><br/>Enable Lo</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="PST4.md">PST4</a><br/>Lo Scalar</td>
</tr><tr>
<td>$1D</td><td rowspan="1">
    <a href="1C.md">TMR3_OSC</a><br/>PTM_C Osc. Select</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF5.md">PRTF5</a><br/>2nd Osc. (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PRTF4.md">PRTF4</a><br/>2nd Osc. (Lo)</td>
</tr><tr>
<td>$20</td><td rowspan="3">
    <a href="20.md">IRQ_PRI</a><br/>IRQ Priority</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PLCD.md">PLCD</a><br/>IRQ 06h ~ 08h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PPTB.md">PPTB</a><br/>IRQ 0Ah ~ 0Ch</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PPTA.md">PPTA</a><br/>IRQ 0Eh ~ 10h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PPTC.md">PPTC</a><br/>IRQ 12h ~ 14h</td>
</tr><tr>
<td>$21</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PTM.md">PTM</a><br/>IRQ 16h ~ 1Ch</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PK1.md">PK1</a><br/>IRQ 26h ~ 28h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PK0.md">PK0</a><br/>IRQ 2Ah ~ 38h</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">IRQ ??? (3Ah ~ 3Eh)</td>
</tr><tr>
<td>$22</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2"><a href="PP0.md">PP0</a><br/>IRQ 1Eh~20h</td>
</tr><tr>
<td>$23</td><td rowspan="4">
    <a href="23.md">IRQ_ENA</a><br/>IRQ Enable</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ELCD.md">ELCD</a><br/>IRQ 06h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ELCFR.md">ELCFR</a><br/>IRQ 08h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETU3.md">ETU3</a><br/>IRQ 0Ah</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETU2.md">ETU2</a><br/>IRQ 0Ch</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETU1.md">ETU1</a><br/>IRQ 0Eh</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETU0.md">ETU0</a><br/>IRQ 10h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETU5.md">ETU5</a><br/>IRQ 12h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETC5.md">ETC5</a><br/>IRQ 14h</td>
</tr><tr>
<td>$24</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETM32.md">ETM32</a><br/>IRQ 16h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETM8.md">ETM8</a><br/>IRQ 18h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETM2.md">ETM2</a><br/>IRQ 1Ah</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="ETM1.md">ETM1</a><br/>IRQ 1Ch</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK11.md">EK11</a><br/>IRQ 26h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK10.md">EK10</a><br/>IRQ 28h</td>
</tr><tr>
<td>$25</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK07.md">EK07</a><br/>IRQ 2Ah</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK06.md">EK06</a><br/>IRQ 2Ch</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK05.md">EK05</a><br/>IRQ 2Eh</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK04.md">EK04</a><br/>IRQ 30h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK03.md">EK03</a><br/>IRQ 32h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK02.md">EK02</a><br/>IRQ 34h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK01.md">EK01</a><br/>IRQ 36h</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EK00.md">EK00</a><br/>IRQ 38h</td>
</tr><tr>
<td>$26</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EP0.md">EP0</a><br/>IRQ 1Eh</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="EP6.md">EP6</a><br/>IRQ 20h</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Ah</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Ch</td>
<td style="border: 2px solid; background-color:#80ff80;">IRQ 3Eh</td>
</tr><tr>
<td>$27</td><td rowspan="4">
    <a href="27.md">IRQ_ACT</a><br/>IRQ Factor</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FLCD.md">FLCD</a><br/>IRQ 06h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="EFCFR.md">EFCFR</a><br/>IRQ 08h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTU3.md">FTU3</a><br/>IRQ 0Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTU2.md">FTU2</a><br/>IRQ 0Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTU1.md">FTU1</a><br/>IRQ 0Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTU0.md">FTU0</a><br/>IRQ 10h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTU5.md">FTU5</a><br/>IRQ 12h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTC5.md">FTC5</a><br/>IRQ 14h</td>
</tr><tr>
<td>$28</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTM32.md">FTM32</a><br/>IRQ 16h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTM8.md">FTM8</a><br/>IRQ 18h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTM2.md">FTM2</a><br/>IRQ 1Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FTM1.md">FTM1</a><br/>IRQ 1Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK11.md">FK11</a><br/>IRQ 26h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK10.md">FK10</a><br/>IRQ 28h</td>
</tr><tr>
<td>$29</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK07.md">FK07</a><br/>IRQ 2Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK06.md">FK06</a><br/>IRQ 2Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK05.md">FK05</a><br/>IRQ 2Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK04.md">FK04</a><br/>IRQ 30h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK03.md">FK03</a><br/>IRQ 32h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK02.md">FK02</a><br/>IRQ 34h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK01.md">FK01</a><br/>IRQ 36h</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="FK00.md">FK00</a><br/>IRQ 38h</td>
</tr><tr>
<td>$2A</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="EP0.md">EP0</a><br/>IRQ 1Eh</td>
<td style="border: 2px solid; background-color:#ffcc00;"><a href="EP6.md">EP6</a><br/>IRQ 20h</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ ???</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Ah</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Ch</td>
<td style="border: 2px solid; background-color:#ffcc00;">IRQ 3Eh</td>
</tr><tr>
<td>$30</td><td rowspan="1">
    <a href="30.md">TMR1_CTRL_L</a><br/>PTM_A Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="MODE16_A.md">MODE16_A</a><br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT0.md">PTOUT0</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN0.md">PTRUN0</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET0.md">PSET0</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL0.md">CKSEL0</a></td>
</tr><tr>
<td>$31</td><td rowspan="1">
    <a href="30.md">TMR1_CTRL_H</a><br/>PTM_A Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT1.md">PTOUT1</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN1.md">PTRUN1</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET1.md">PSET1</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL1.md">CKSEL1</a></td>
</tr><tr>
<td>$32</td><td rowspan="1">
    <a href="32.md">TMR1_PRE_L</a><br/>PTM_A Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR0.md">RDR0</a><br/>Preset</td>
</tr><tr>
<td>$33</td><td rowspan="1">
    <a href="32.md">TMR1_PRE_H</a><br/>PTM_A Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR1.md">RDR1</a><br/>Preset</td>
</tr><tr>
<td>$34</td><td rowspan="1">
    <a href="34.md">TMR1_PVT_L</a><br/>PTM_A Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR0.md">CDR0</a><br/>Compare data</td>
</tr><tr>
<td>$35</td><td rowspan="1">
    <a href="34.md">TMR1_PVT_H</a><br/>PTM_A Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR1.md">CDR1</a><br/>Compare data</td>
</tr><tr>
<td>$36</td><td rowspan="1">
    <a href="36.md">TMR1_CNT_L</a><br/>PTM_A Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM0.md">PTM0</a><br/>Count</td>
</tr><tr>
<td>$37</td><td rowspan="1">
    <a href="36.md">TMR1_CNT_H</a><br/>PTM_A Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM1.md">PTM1</a><br/>Count</td>
</tr><tr>
<td>$38</td><td rowspan="1">
    <a href="38.md">TMR2_CTRL_L</a><br/>PTM_B Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="MODE16_B.md">MODE16_B</a><br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT2.md">PTOUT2</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN2.md">PTRUN2</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET2.md">PSET2</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL2.md">CKSEL2</a></td>
</tr><tr>
<td>$39</td><td rowspan="1">
    <a href="39.md">TMR2_CTRL_H</a><br/>PTM_B Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT3.md">PTOUT3</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN3.md">PTRUN3</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET3.md">PSET3</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL3.md">CKSEL3</a></td>
</tr><tr>
<td>$3A</td><td rowspan="1">
    <a href="3A.md">TMR2_PRE_L</a><br/>PTM_B Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR2.md">RDR2</a><br/>Preset</td>
</tr><tr>
<td>$3B</td><td rowspan="1">
    <a href="3A.md">TMR2_PRE_H</a><br/>PTM_B Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR3.md">RDR3</a><br/>Preset</td>
</tr><tr>
<td>$3C</td><td rowspan="1">
    <a href="3C.md">TMR2_PVT_L</a><br/>PTM_B Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR2.md">CDR2</a><br/>Compare data</td>
</tr><tr>
<td>$3D</td><td rowspan="1">
    <a href="3C.md">TMR2_PVT_H</a><br/>PTM_B Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR3.md">CDR3</a><br/>Compare data</td>
</tr><tr>
<td>$3E</td><td rowspan="1">
    <a href="3E.md">TMR2_CNT_L</a><br/>PTM_B Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM2.md">PTM2</a><br/>Count</td>
</tr><tr>
<td>$3F</td><td rowspan="1">
    <a href="3E.md">TMR2_CNT_H</a><br/>PTM_B Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM3.md">PTM3</a><br/>Count</td>
</tr><tr>
<td>$40</td><td rowspan="1">
    <a href="40.md">TMR256_CTRL</a><br/>Clock Timer Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="TMRST.md">TMRST</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="TMRUN.md">TMRUN</a><br/>Enable</td>
</tr><tr>
<td>$41</td><td rowspan="1">
    <a href="41.md">TMR256_CNT</a><br/>Clock Timer Counter</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="TMD.md">TMD</a><br/>Count</td>
</tr><tr>
<td>$44</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3">???</td>
</tr><tr>
<td>$45</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
<td style="border: 2px solid; background-color:#c0ffc0;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
</tr><tr>
<td>$46</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="8">???</td>
</tr><tr>
<td>$47</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
</tr><tr>
<td>$48</td><td rowspan="1">
    <a href="48.md">TMR3_CTRL_L</a><br/>PTM_C Control (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="MODE16_C.md">MODE16_C</a><br/>16-bit Mode</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT4.md">PTOUT4</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN4.md">PTRUN4</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET4.md">PSET4</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL4.md">CKSEL4</a></td>
</tr><tr>
<td>$49</td><td rowspan="1">
    <a href="49.md">TMR3_CTRL_H</a><br/>PTM_C Control (Hi)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="4">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTOUT5.md">PTOUT5</a></td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="PTRUN5.md">PTRUN5</a><br/>Enable</td>
<td style="border: 2px solid; background-color:#ffff00;"><a href="PSET5.md">PSET5</a><br/>Reset</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="CKSEL5.md">CKSEL5</a></td>
</tr><tr>
<td>$4A</td><td rowspan="1">
    <a href="4A.md">TMR3_PRE_L</a><br/>PTM_C Preset (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR4.md">RDR4</a><br/>Preset</td>
</tr><tr>
<td>$4B</td><td rowspan="1">
    <a href="4A.md">TMR3_PRE_H</a><br/>PTM_C Preset (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="RDR5.md">RDR5</a><br/>Preset</td>
</tr><tr>
<td>$4C</td><td rowspan="1">
    <a href="4C.md">TMR3_PVT_L</a><br/>PTM_C Compare (Lo)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR4.md">CDR4</a><br/>Compare data</td>
</tr><tr>
<td>$4D</td><td rowspan="1">
    <a href="4C.md">TMR3_PVT_H</a><br/>PTM_C Compare (Hi)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8"><a href="CDR5.md">CDR5</a><br/>Compare data</td>
</tr><tr>
<td>$4E</td><td rowspan="1">
    <a href="4E.md">TMR3_CNT_L</a><br/>PTM_C Count (Lo)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM4.md">PTM4</a><br/>Count</td>
</tr><tr>
<td>$4F</td><td rowspan="1">
    <a href="4E.md">TMR3_CNT_H</a><br/>PTM_C Count (Hi)</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="8"><a href="PTM5.md">PTM5</a><br/>Count</td>
</tr><tr>
<td>$50</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP07.md">KCP07</a><br/>Power</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP06.md">KCP06</a><br/>Right</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP05.md">KCP05</a><br/>Left</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP04.md">KCP04</a><br/>Down</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP03.md">KCP03</a><br/>Up</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP02.md">KCP02</a><br/>C</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP01.md">KCP01</a><br/>B</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP00.md">KCP00</a><br/>A</td>
</tr><tr>
<td>$51</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP11.md">KCP11</a><br/>Eject</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="KCP10.md">KCP10</a><br/>Cartridge?</td>
</tr><tr>
<td>$52</td><td rowspan="1">
    <a href="52.md">KEY_PAD</a><br/>Keypad Status (Active 0)</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K07D.md">K07D</a><br/>Power</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K06D.md">K06D</a><br/>Right</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K05D.md">K05D</a><br/>Left</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K04D.md">K04D</a><br/>Down</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K03D.md">K03D</a><br/>Up</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K02D.md">K02D</a><br/>C</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K01D.md">K01D</a><br/>B</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K00D.md">K00D</a><br/>A</td>
</tr><tr>
<td>$53</td><td rowspan="1">
    <a href="53.md">Cart Bus</a><br/>CART_BUS</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K11D.md">K11D</a><br/>CARD_N</td>
<td style="border: 2px solid; background-color:#00ffff;"><a href="K10D.md">K10D</a></td>
</tr><tr>
<td>$54</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3"><a href="CTK0H.md">CTK0H</a><br/>Unused?</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3"><a href="CTK0L.md">CTK0L</a><br/>Keypad debounce rate?</td>
</tr><tr>
<td>$55</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="3"><a href="CTK0L.md">CTK0L</a><br/>Cartridge debounce rate?</td>
</tr><tr>
<td>$60</td><td rowspan="1">
    <a href="60.md">IO_DIR</a><br/>I/O Direction Select</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC07.md">IOC07</a><br/>???</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC06.md">IOC06</a><br/>Shock</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC05.md">IOC05</a><br/>IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC04.md">IOC04</a><br/>Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC03.md">IOC03</a><br/>EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC02.md">IOC02</a><br/>EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC01.md">IOC01</a><br/>IR Rx</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="IOC00.md">IOC00</a><br/>IR Tx</td>
</tr><tr>
<td>$61</td><td rowspan="PM_I_O_Port.md">
    <a href="61.md">I/O Data Register</a><br/>IO_DATA</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P07.md">P07</a><br/>???</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P06.md">P06</a><br/>Shock</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P05.md">P05</a><br/>IR Disable</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P04.md">P04</a><br/>Rumble</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P03.md">P03</a><br/>EEPROM Clock</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P02.md">P02</a><br/>EEPROM Data</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P01.md">P01</a><br/>IR Rx</td>
<td style="border: 2px solid; background-color:#80ff80;"><a href="P00.md">P00</a><br/>IR Tx</td>
</tr><tr>
<td>$62</td>
<td>Unknown</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="4">???</td>
<td style="border: 2px solid; background-color:#c0c0c0;" colspan="4">???</td>
</tr><tr>
<td>$70</td><td rowspan="1">
    <a href="70.md">AUD_CTRL</a><br/>Audio Control</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#c0ff00;">???</td>
<td style="border: 2px solid; background-color:#c0ff00;" colspan="2">Mutes audio if not 0!?</td>
</tr><tr>
<td>$71</td><td rowspan="1">
    <a href="71.md">AUD_VOL</a><br/>Audio Volume</td>
<td style="border: 2px solid; background-color:#808080;" colspan="5">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;">Cart Power (1=Off; 0=On)</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Volume</td>
</tr><tr>
<td>$80</td><td rowspan="1">
    <a href="80.md">PRC_MODE</a><br/>LCD Controller Settings</td>
<td style="border: 2px solid; background-color:#808080;" colspan="2">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Map Size</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Render</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Sprites</td>
<td style="border: 2px solid; background-color:#80ff80;">Enable Map</td>
<td style="border: 2px solid; background-color:#80ff80;">Invert Map</td>
</tr><tr>
<td>$81</td><td rowspan="1">
    <a href="81.md">PRC_RATE</a><br/>LCD Rate Control</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="4">Frame counter</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="3"><a href="CKCN.md">CKCN</a><br/>Rate divider</td>
<td style="border: 2px solid; background-color:#80ff80;">Initable</td>
</tr><tr>
<td>$82</td><td rowspan="1">
    <a href="82.md">PRC_MAP</a><br/>PRC Map Tile Base</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base (low)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
</tr><tr>
<td>$83</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Map Tile Base (mid)</td>
</tr><tr>
<td>$84</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Map Tile Base (high)</td>
</tr><tr>
<td>$85</td><td rowspan="1">
    <a href="85.md">PRC_SCROLL_Y</a><br/>PRC Map Vertical Scroll</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll Y</td>
</tr><tr>
<td>$86</td><td rowspan="1">
    <a href="86.md">PRC_SCROLL_X</a><br/>PRC Map Horizontal Scroll</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="7">Map Scroll X</td>
</tr><tr>
<td>$87</td><td rowspan="1">
    <a href="87.md">PRC_SPR</a><br/>PRC Sprite Tile Base</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="2">Sprite Tile Base (low)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="6">&nbsp;</td>
</tr><tr>
<td>$88</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">Sprite Tile Base (mid)</td>
</tr><tr>
<td>$89</td>
<td style="border: 2px solid; background-color:#808080;" colspan="3">&nbsp;</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="5">Sprite Tile Base (high)</td>
</tr><tr>
<td>$8A</td><td rowspan="1">
    <a href="8A.md">PRC_CNT</a><br/>LCD Line Counter</td>
<td style="border: 2px solid; background-color:#808080;">&nbsp;</td>
<td style="border: 2px solid; background-color:#00ffff;" colspan="7">Count</td>
</tr><tr>
<td>$8B</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8C</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8D</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8E</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$8F</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F0</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F1</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F2</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F3</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F4</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F5</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F6</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$F7</td>
<td>Unknown (returns 0)</td>
<td style="border: 2px solid; background-color:#808080;" colspan="8">&nbsp;</td>
</tr><tr>
<td>$FE</td><td rowspan="1">
    <a href="FE.md">LCD_CTRL</a><br/>LCD Raw Control Byte</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Control I/O</td>
</tr><tr>
<td>$FF</td><td rowspan="1">
    <a href="FE.md">LCD_DATA</a><br/>LCD Raw Data Byte</td>
<td style="border: 2px solid; background-color:#80ff80;" colspan="8">LCD Data I/O</td>
</tr>
</table>