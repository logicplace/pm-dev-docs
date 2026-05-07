# Cartridge power

$2071 bit 1 is a R/W register.

Determines if the cartridge is powered or not.

* 1 = pins B1, A1, A7, & A8 *do not* receive power
* 0 = pins B1, A1, A7, & A8 *do* receive power

## $2002 bit 6

$2002 bit 6 is a [reserved R/W register](../../../glossary.md#reserved-rw-register).

It's used to store whether or not the cartridge slot should be powered when the console is on.

Besides initialization, the only thing which resets this to 0 in the BIOS is [powering off the cart slot](../bios.md#power-off-cart-slot) manually. There are several places where it's set to 1.

The BIOS checks this bit during every wake up procedure. If it's set, it turns on the cart power via $2071 bit 1.

In previous documentation, this register was known as "Cart power required" which is still acceptible.
