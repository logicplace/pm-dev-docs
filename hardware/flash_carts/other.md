# Other flash carts

Carts on this page are essentially ones I don't own and therefore can't write articles about. Many are also personal projects that no one besides the creator has access to, but I wanted to feature the work done in this community.

## DarkFader's flash cart

This was the first ever flash cart created for the PM. It apparently only worked for a short time before failing. Afterwards he started developing v1 and v2 versions of the cart. The v2 promised some interesting features, but was never finished. It's unclear if v1 was ever printed or distributed.

![DarkFader's proto flash cart](/assets/img/flash/darkfader_proto.jpg "proto")
![DarkFader's v1 flash cart PCB](/assets/img/flash/darkfader_v1_design.png "V1 PCB design")
![DarkFader's v2 flash cart PCB](/assets/img/flash/darkfader_v2_design.png "V2 PCB design")

Adapter boards for flashcard prototyping and cartridge emulation:

![DarkFader's adapter boards](/assets/img/flash/darkfader_connectors.jpg "adapter boards")

## JustBurn's flash cart

This was the first commercially available flash cart, designed by JustBurn and p0p.

Unlike flash carts these days, these had to be programmed from the regular cartridge pins, requiring an official Pokémon mini connector ripped from the console.

This cart stuck out slightly from the console and did not require a shell to be used, nor were any ever designed.

It was sold alongside a programmer which used a <abbr title="Line Printer Terminal">LPT</abbr> port to connect to the computer. The programmer came pre-installed with the cartridge adapter. No clue what software supported this programmer.

However, I believe [PokeUSB](./pokecard.md#pokeusb) supported this card once that was released.

![sales flyer](/assets/img/flash/jb_cardsale.jpg "Sales flyer")
![cart and console](/assets/img/flash/jb_cart_in_play.jpg "Flash cart next to a console using it to play the Team PokéMe demo")

### Technical specifications

* Capacity: 512 KiB
* Theoretical flashing speeds: 30~50 μs per byte, so ~16~26s for 512 KiB
* Flash memory: [AT46LV040-90TC](https://www.cs.columbia.edu/~sedwards/classes/2006/4840/DOC0679.pdf)
* Bridge chip: [XC9536XL-10VQ44C](https://docs.amd.com/api/khub/documents/zErlwbqjsWXW2We6pxE8rQ/content)

## Happysoul's flash carts

Happysoul is a member of the community who has produced a few flash carts for his own use. Two of his designs use the [SST39VF040-70-4C-WH](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/SST39LF010-SST39LF020-SST39LF040-SST39VF010-SST39VF020-SST39VF040-Data-Sheet-DS20005023.pdf) for flash ROM which is 4 Mbit, or 512 KiB.

![Happysoul's 3 flash carts](/assets/img/flash/happysoul.png "all three carts")
![Happysoul's linker](/assets/img/flash/happysoul_linker.jpg "linker in use")
![Happysoul's flashing software](/assets/img/flash/happysoul_flashing.png "flashing software")

## Rem's flash cart

This was a design of the [PM2040](./pm2040.md) in the form factor of a typical cartridge size. Rem was able to produce working versions, but never distributed them.

![Rem's flash cart proto](/assets/img/flash/rem_2025-07-11.jpg "first print, not entirely functional")
![Rem's flash cart PCB](/assets/img/flash/rem_2025-07-17.png "board layout")
![Rem's flash cart running his test ROM](/assets/img/flash/rem_2025-07-23.jpg "working print")
