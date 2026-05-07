# Audio

*For more information, see its [main page](../sound.md)*

The PM produces audio via the TOUT (TODO: confirm) port using signal from [PTM_C](timers.md#ptm_c). This page is about the other registers which contribute to sound.

## $2070 bits 1~0

$2070 bits 1~0 is a R/W register.

A value of 0 allows the PM to produce sound, any other value mutes all sound.

It is unknown what purpose these registers serve and exactly what they do. The BIOS's [init_io](../../../software/bios/disasm.md#user-content-init_io) as well as MINLIB's audio initialization section sets them to 0.

## Volume

$2071 bits 1~0 is a R/W register.

| VOL1~0 | Amplitude |
|:------:| --------- |
|  0 0   | 0%        |
|  0 1   | 50%       |
|  1 0   | 50%       |
|  1 1   | 100%      |
