# PokMini

Designed by insideGadgets, the [PokMini](https://shop.insidegadgets.com/product/pokemon-mini-2mb-flash-cart/) is a low cost 2 MiB flash cart.

Since this board can fit in an official PM cartridge, it can use [those models](../cartridge.md#shells), but it doesn't have the screw notches causing it to be slightly loose or even fall out of one without a bottom shell designed for it, [like so](https://www.thingiverse.com/thing:6660072).

A label designed by CaptainZ available [here](/assets/other/PokMini_label_by_CaptainZ.psd)
![PokMini label by CaptainZ](/assets/img/flash/pokmini_label.png)

## Features

* Capacity: 2 MiB
* Fits in an official case with no modification
* The dedicated PokMini flasher works for both the PokMini and the [DITTO mini](./ditto.md)

## Issues / limitations

* No multicart support
* Software cannot write to the cart from within the PM (TODO: confirm for v1.1)
* Must be used in a case, board will not make contact loose

## PokMini v1.1

![PokMini v1.1](/assets/img/flash/ig_v1.1.jpg)

### Technical specifications

* Capacity: 2 MiB
* Flashing speeds: ?
* Flash memory: [MX29LV160DTXEI-70G](https://www.macronix.com/Lists/Datasheet/Attachments/8520/MX29LV160D%20T-B,%203V,%2016Mb,%20v1.2.pdf)
* Bridge chip: ?

## PokMini v1.0

### Technical specifications

* Capacity: 2 MiB
* Flashing speeds: ?
* Flash memory: [MX29LV160DTXEI-70G](https://www.macronix.com/Lists/Datasheet/Attachments/8520/MX29LV160D%20T-B,%203V,%2016Mb,%20v1.2.pdf)
* 3x demuxers: [SLG46620](https://www.mouser.com/datasheet/3/1166/1/REN_SLG46620_DS_r122_DST_20250406.pdf)

## Flashing

There are two options for flashing, the official [GBxCart RW](#gbxcart) or the dedicated [PokMini Flasher](#pokmini-flasher).

### GBxCart

You will need a [GBxCart RW](https://www.gbxcart.com/) v1.4 or higher and a GBx edge adapter.

There are two tools usable for this, [FlashGBX](https://github.com/lesserkuma/FlashGBX) for a GUI or [GBx PM Flasher](https://shop.insidegadgets.com/wp-content/uploads/2022/12/GBxCart_RW_PokMini_2MB_Flasher_v1.0a.zip)

1. Remove your cart from the console (or at least remove the battery)
2. Insert the top edge of the cart into the GBx edge adapter with the chips/bottom pins visible
3. Rotate the tab over the board to hold it securely
4. Plug the GBx edge adapter into your GBxCart RW
5. Connect your GBxCart RW with a USB-C cable

With FlashGBX:

6. Open FlashGBX, if it didn't automatically connect click Connect
7. ??? does this work for v1.0??

With GBx PM Flasher:

6. Drag and drop your ROM onto gbxcart_rw_pokmini_2mb_flasher.exe to flash it

![proper connection](/assets/img/flash/ig_flashing.jpg "proper connection")

### PokMini Flasher

You will need the [PokMini 2MB Flasher](https://shop.insidegadgets.com/wp-content/uploads/2023/03/PokMini_2MB_Flasher_v1.0.zip).

This can only flash ROMs to the cart, it cannot read or erase the cart.

1. Remove your cart from the console (or at least remove the battery)
2. Insert the top edge of the cart into the PokMini Flasher with the chips/bottom pins visible
3. Rotate the tab over the board to hold it securely
4. Connect your PokMini Flasher with a USB-C cable
5. Drag and drop your ROM onto pokmini_2mb_flasher.exe to flash it

![PokMini Flasher with cable](/assets/img/flash/ig_dedicated.jpg)
