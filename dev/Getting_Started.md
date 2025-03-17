# Getting Started

Before getting started with Pokémon mini development you will first need some basics to get started. This tutorial will largely presume that you don't know what these tools are, what they do, or how to use them. If you do know how, this tutorial will endeavor to be skimmable; look out for bulleted lists and code blocks.

First of all you will need the following (install instructions per OS below):

* A terminal environment
* [git](https://git-scm.com/)
* If you want to test on hardware, a [flash card](/hardware/Flash_Cards.md)

## Windows setup

First, to get a good terminal environment, install [Windows Terminal](https://apps.microsoft.com/detail/9N0DX20HK701) from the Microsoft Store. This isn't strictly required, but you will need PowerShell 7+ at least, which it comes with.

Next you should install git, which you can do via its Windows installer [here](https://git-scm.com/downloads/win). If you don't know what portable means, get the setup version. If you don't know if you have 32 or 64 bit, you probably have 64 bit, but you can confirm by right-clicking the Windows icon on your task bar and selecting `System`; it will be displayed under `System type`. During the setup, make sure `git` is added to your path (TODO: use terminology from the installer). If your terminal was already open, restart it now so that your PATH variable is correctly updated.

To open the terminal, go to your search bar and search for `terminal` and you'll see Windows Terminal come up. Click and wait, the default terminal should be PowerShell 7 but if it's not, you can click the down arrow next to the + in the tab list in order to open one. You're looking for `PowerShell` in that list, not `Windows PowerShell`.

## Linux setup

Your system already comes with a shell environment and you surely know how to use it. Install git with your package manager and you're ready to move to the next step. Currently the tools installer only supports apt and Homebrew, so if your system doesn't use apt and you feel uncomfortable adapting the install scripts to your own system, I'd recommend installing Homebrew.

## Mac setup

Your system comes with one but it may be an old version. I recommend installing [Homebrew](https://brew.sh/#install) and using that to install [iTerm2](https://formulae.brew.sh/cask/iterm2#default). You will need Homebrew for further steps anyway, regardless of whether or not you choose to install iTerm2.

Open the terminal with Cmd+Space and searching for `iterm`, this will bring up both the built-in iTerm and iTerm2, if you installed it. Select the appropriate one to open it.

Once you do, you can install git by typing `brew install git` and pressing the enter key. Wait for it to install and configure and you're ready for the next step.

## Set up the development suite

Now that you have your terminal open and git installed, you can begin setting up the tools. First `cd` to whatever folder you intend to develop in then the following:

```sh
git clone https://github.com/pokemon-mini/c88-pokemini.git
cd c88-pokemini
```

Then follow the setup instructions [here](https://github.com/pokemon-mini/c88-pokemini/blob/master/README.md). You will need to use it to install the tools and PokeMini as it recommends there. It will be easiest if when it asks `Set environment variables for the build tools` you say `Y`. You may also choose to install `dittoflash` if you have a DITTO mini flash card you intend to test your software on (and you don't already have the software installed).

Now from the same document you can follow those instruction to build the example project in order to make sure everything works.

## Setting up your code editor

There are several code editors you can choose from such as [VS Code](#visual-studio-code), [Notepad++](notepad), or Sublime Text. We will only cover how to set up a couple of these. If your favorite isn't here and you figure out how to set it up for PM development nicely, let us know how!

### Visual Studio Code

First install VS Code if you haven't already from the download link on [this page](https://code.visualstudio.com/).

Next, you will need the following extensions. You can install extensions by clicking the four blocks looking icon in the left-hand sidebar and searching for the name.

* [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
* TODO: assembly highlighters
* Optional: [Number System Converter](https://marketplace.visualstudio.com/items?itemName=frogstair.number-system-converter)
* Optional: [PMMusic](https://marketplace.visualstudio.com/items?itemName=logicplace.pmmusic)

When you make a new project, you'll want to set up the C information for it. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> to open the command palette, type `C/C` and look for `C/C++: Edit Configurations (JSON)`. Paste the following into it:

```json
{
    "configurations": [
        {
            "name": "Pokemon mini",
            "includePath": [
                "${workspaceFolder}/**",
                "${workspaceFolder}/../../include",
                "${workspaceFolder}/../../c88tools/include"
            ],
            "forcedInclude": ["${workspaceFolder}/../../c88tools/include/c88.h"],
            "compilerPath": "${workspaceFolder}/../../c88tools/bin/cc88",
            "cStandard": "c99",
            "intelliSenseMode": "${default}"
        }
    ],
    "version": 4
}
```

Your status bar should look something like this with your project folder open and a C file selected:

![image](https://github.com/user-attachments/assets/2968f9a5-2ad1-4102-90a5-8b968595bc41)


### Notepad++

TODO

## Setting up a new project

For your first project it's a good idea to use the included Makefile to not worry about how `make` systems work. I'd also recommend making a C project over an assembly project as there will be more resources for C projects and it will be overall faster to develop.

Firstly, from the c88-pokemini folder, run the following commands:

```sh
mkdir projects
cd projects
mkdir my-first-project
cd my-first-project
git init
mkdir src
cp ../../examples/helloworld/Makefile .
cp ../../examples/helloworld/src/isr.c src
cp ../../examples/helloworld/src/startup.asm src
```

If your code editor supports it, open the `my-first-project` folder as your project. Now open `isr.c` and look at the two declarations on top:

```c
const _rom char game_code[4] _at(0x21AC) = "HW";
const _rom char game_title[12] _at(0x21B0) = "Hi World!";
```

You will want to change these to represent your game's name. Per the array size declarations in each we can see the game_code is limited to 4 characters and the game_title is limited to 12.
While it's not required, the official games follow a format for the game code of `NxxR` where `N` is a literal N, which presumably stands for "Nintendo", `xx` is a two letter unique representation of the game title, and `R` is a single letter region code representing the game's language.
This can be `J` for Japanese, `E` for English, `D` for Deutsch (German), `F` for French, or `P` for multi-language.
If you want to follow this format, you can make the first letter one that represents your group or your own name as appropriate or just `H` for Homebrew, then two letters for the game name, and an appropriate region code (there is no standard for other languages yet, though!).
Your game title should be as close to the full name as you can get. The text encoding is something of a reduced Shift-JIS encoding, but if you can limit it to basic ASCII characters (unaccented latin letters, arabic numerals, and certain punctuation) it will be simpler and more likely to work. This name shows up when managing the save files should your console be full, and how it renders will be based on the font from the game that's running the save manager.

You do not need to worry about the rest of this file at the moment, but it may be useful in the future! This is where you define how to handle interrupts.

Next you need to make a `main.c` file in your `src` directory with the following contents, minimally:

```c
#include "pm.h"

int main(void)
{
    // Set up... set PRC_MODE or etc
    
    for(;;) {
        // Main loop
        // ... stuff ...
        wait_vsync();
        // ... stuff ...
    }
}
```

If you add more C files to your project (hopefully you will!) you will need to add them to the right side of the `C_SOURCES` line in your `Makefile`. Note that when building, changing a header file will not cause a C file that includes it to rebuild, with the included make system. If you want that functionality, you can explore developing your own custom `Makefile`, but save that for after building your first project. No need to be too ambitious for the first go.
