# "EBR"

It's not particularly likely this register functions as the "bus release enable register" per chips like the [S1C88112](../s1c88/112.md), however it does seem to have some function and this is the candidate by position.

Thus, $2002 bit 7 is likely a R/W register.

A hard reset initializes it to 0 [here](../../../software/bios/disasm.md#user-content-00A8) then the BIOS writes 1 to it after [chip enables](chip-enable.md). Otherwise, the BIOS writes 1 to this in certain situations surrounding what are presumably dev cart related functions. Notably in [power_cart](../../../software/bios/disasm.md#user-content-power_cart) and [_read_structure](../../../software/bios/disasm.md#user-content-_read_structure).

Its usage in the BIOS makes it seem like a write-only register but it does read back the value correctly.
