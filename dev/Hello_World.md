# Hello World example walkthrough

If you have not, take a look at the Hello World example included with c88-pokemini [here](https://github.com/pokemon-mini/c88-pokemini/tree/master/examples/helloworld). This tutorial will walk you through what each part of it does and how it works.

This tutorial assumes you have no C knowledge.

## main.c

### Includes

Firstly let's start with the entry-point's file, `main.c`. Let's take a look at the includes.

```c
#include <pm.h>
#include <stdint.h>

#include "hello_tiles.h"
```

This section is including header files (denoted by the `.h` extension, which is part of the filename) from elsewhere into this file's [scope](/Glossary.md#scope). This is done through the `#include` _preprocessor directive_. That is, an instruction given to the C preprocessor, a system which executes prior to compilation. You can think of this directive as copying and pasting the entire contents of the header file into this file, right where the include line is written.

If you haven't guessed, preprocessor directives are always prefixed by `#` and there are more of them! But this is the only one used in this tutorial.

There is indeed a difference between the usage of double-quotes vs angled brackets here: it has to do with how it searches for the files. For C88 tools the search order is like this:

1. The directory of the file containing the include line. (In this case, `examples/helloworld/src`)
2. The directories specified via the `-I` command line argument, left to right. (In `pm.mk`'s case, `include`)
3. The directories specified in the environment variable `C88INC` (we do not use this)
4. Lastly, the `c88tools/include` directory.

When using double quotes, it searches all these locations, but when using angled brackets, it does not search #1, and only searches 2 through 4. Thus, people tend to use this as indicating that we're searching local headers with double quotes and standard headers with angled brackets.

Explaining the contents of the headers is beyond the scope of this document, but in terms of what they do, `pm.h` defines all the hardware registers and other helpful things you will need to interact with, such as `PRC_MODE` in the `main` function. `stdint.h` defines some number types with names and sizes that are standard across all compilers, such as `uint8_t` below. We will go over `hello_tiles.h` later as it's part of this project.

### Globals

This part after the includes is just declaring a variable inside the global scope. This means it's available to any function defined in this file, and they can all share data through it.

```c
uint8_t free_time;
```

There are two parts to this declaration: the _type_ and the _name_. These are `uint8_t` and `free_time`, respectively.

First let's discuss the type, this is the most important part. This is a type from our `stdint.h` include, it has a standardized naming scheme which will help you understand your memory usage and how you interface with it, so it's good to understand.
It stands for "Unsigned INTeger, 8 bits (Type)".
You may also know an integer as a whole number - essentially a number with nothing after the decimal, such as `1` but not `1.01`.
Unsigned refers to the sign that comes before a number, `+` or `-`. It's called unsigned because it doesn't respect any sign in front of it. Implicitly what this means is that it can only contain positive integers. More than that, it can contain more positive integers than its _signed_ counterpart. More on that in a moment.
`stdint` notates all of its sizes in terms of bit sizes, but they are all multiples of 8, at least for this system. A single byte is 8 bits, so this type contains a 1-byte integer value. A single byte can represent 256 distinct values. Knowing this, we can determine what specifically an _unsigned integer_ occupying this space can represent. We talk about this in terms of its _minimum value_ and its _maximum value_, which are 0 (hex of 0x00) and 255 (hex of 0xFF) respectively. For the signed counterpart, its minimum is -128 (hex of 0x80) and its positive is 127 (hex of 0x7F).

So we now understand the format of a stdint type: signedness + "int" + size in bits + "_t".
However, signedness is either blank or "u", not "s". That is, a signed integer of 8 bits is `int8_t`.

The name is a identifier for the reader's sake. The name does not make its way into what's compiled, so it can be as long as you, and other readers, need. There are conventions on how names should be styled in C, which help with some implicit information. The primary thing to keep in mind is that variables and functions in C should be what's called _lower snake case_, that is, all lower case, and using and underscore (`_`) to separate words. This distinguished them from `#defines`, which we haven't discussed yet, which are in _upper snake case_. There are other similar naming conventions for other things, but we will discuss them as they're introduced.

Similarly, the `_t` used in `uint8_t` merely identifies it as a type as opposed to, for instance, a struct. Whether or not you want to continue that convention should you define your own types is up to you, but it's fine to consider it a quirk of `stdint.h`.

### main

The first part of declaring a function is called the _function signature_, this defines how to interact with the function. Let's go through the parts in turn.

```c
int main(void) {
	// ...
}
```

1. `int` is the _return type_. This means any value you `return` must be of type `int`. On this system, `int` is 16-bits (this is not always the case in C), but it is implicitly signed across all systems.
2. `main` is the name of the function. You use this name to call the function, normally. However, you won't call `main` yourself, `startup.asm` will call it.
3. `void` is a way to state that this function accepts no arguments. You may think then that `int main()` would work, but that means something slightly different. The feature isn't used by anyone so what it does isn't too important, just remember to use `void` like this for functions which take no arguments.
4. The code inside `{}` is the _function body_. When `main` is called, this is the code that's executed.

```c
uint8_t i, keys;
```

At the start of the body are local variable declarations. It's generally good practice to declare all your local variables for a function at the start of it, but it's not required.

```c
PRC_MODE = COPY_ENABLE|SPRITE_ENABLE|MAP_ENABLE|MAP_16X12;
PRC_RATE = RATE_36FPS;

PRC_MAP = hello_tiles;
```

Here we set up the PRC, which stands for _Program Rendering Chip_. This subsystem is what handles graphical rendering on the PM. It's fairly configurable so you have to tell it how you want it to work.
These three variables are called _hardware registers_. Rather than thinking of these statements as like assigning to a variable, think of them as communicating to the hardware. This is because reading from a hardware register may not return what you wrote to it.

* `PRC_MODE` - This allows you to enable or disable certain parts of the PRC and select the tilemap dimensions. A different tutorial will discuss the importance of the tilemap dimensions. We use the `|` operator here to combine these options, since the options are stored in separate _bit flags_. This is a convention you'll use often when writing to hardware registers.
  * `COPY_ENABLE` - This enables the _frame copy_ step of the PRC, which is what blits the frame buffer to the LCD. If this is disabled, the PRC doesn't run at all, and nothing is rendered.
  * `MAP_ENABLE` - This enables tilemap rendering, which one might think of as the background.
  * `SPRITE_ENABLE` - This enables sprites to be drawn over the tilemap, though each sprite that's in use must be enabled individually, and this example doesn't use any.
  * `MAP_16X12` - This sets the tilemap to 16 tiles wide and 12 tiles tall. The visible screen area is 12x8, but there's no PRC option for that (for good reasons which will be discussed elsewhere).
* `PRC_RATE` - This controls how often a frame is rendered, essentially the framerate.
* `PRC_MAP` - This is where you put the reference to your tile graphics, the PRC reads the tile graphical data from here based on `TILEMAP`. `hello_tiles` is defined in `hello_tiles.h` so you can peek at the definition there, but it will be discussed more in-depth later.

```c
for (i=0; i<16*12; i++) {
	TILEMAP[i] = i;
}
```

This is a for loop. It's initializing the tilemap to display the "Hi World" image 1:1, essentially not really using it as tiles but just displaying an image. Let's go through exactly how it's doing that.

A for loop contains an initialization, condition, and iteration expression, in addition to the _loop body_. `i=0` is the initialization, it sets the `i` variable we declared earlier to `0`. `i<16*12` is the condition, which is read as "`i` is less than `16 * 12` (16 multiplied by 12)". It's checked before running the loop body each time. `i++` is the iteration expression, which increments `i` by 1. It's run at the end of the loop body each time.

Any for loop can be rewritten as a `while` loop. This one can be written like so, for example:

```c
i = 0;
while (i < 16*12) {
	TILEMAP[i] = i;
	i++;
}
```

Next we enter what's called the _main loop_ or _main game loop_. Essentially, this loop will run until the power is turned off, which makes some intuitive sense if you've ever played a game, right?

```c
for(;;) {
	// ...
}
```

If you recall from before, there should be three expressions inside the parentheses of the `for` loop. Technically there still are, they're just empty! Looking at the equivalent `while` loop from before, it makes sense that the initialization and iteration expressions can be blank, since they can just be removed, but the condition is a special case. If it's removed, it's equivalent to always being true, essentially `while(1)`, so it runs forever.

The first part of the main loop isn't really used for anything, so I've left some comments in-line explaining it for those interested. Timers will be explained in another tutorial.

```c
// Sets up a general purpose timer
TMR1_OSC = 0x11; // Use Oscillator 2 (31768Hz)
TMR1_SCALE = 0x08 | 0x02; // Scale 2 (8192 Hz)
TMR1_CTRL = 0x06; // Enable timer 2 at 0

// Waits for the PRC to finish copying the frame to the LCD
wait_vsync();

// Stops the timer
TMR1_CTRL = 0; // Pause timer
free_time = 255-TMR1_CNT_L;
```

The next bit of code checks for button presses, specifically of the directional pad (d-pad). KEY_PAD is a hardware register where each bit represents a different button. If the respective bit is 1, the button is current unpressed, if it's 0 then it's currently pressed. This is why the first line inverts all the bits, making it so that 1 means pressed.

```c
keys = ~KEY_PAD;
if ((keys & KEY_UP) && (PRC_SCROLL_Y > 0)) {
	PRC_SCROLL_Y--;
} else if ((keys & KEY_DOWN) && (PRC_SCROLL_Y < 31)) {
	PRC_SCROLL_Y++;
}
if ((keys & KEY_LEFT) && (PRC_SCROLL_X > 0)) {
	PRC_SCROLL_X--;
} else if ((keys & KEY_RIGHT) && (PRC_SCROLL_X < 31)) {
	PRC_SCROLL_X++;
}
```

Code such as `keys & KEY_UP` is a way of using a _bit mask_ to check the value of a certain flag. To explain, `KEY_UP` has a value of `0b00001000`, if the player is currently pressing the up and C buttons, then `~KEY_PAD`  would have a value of `0b00001100`. Since we only want to check the value of up, we need a way to ignore C being pressed (as well as any other button!) so we use the bit mask to extract it.

Stepping back for a moment, `&` is in a class of operations called _bitwise operations_. Bitwise operations can be thought of as applying the operation per pair of bits between the two numbers. In the following, we have two 8-bit numbers where each binary digit is represented by a single letter variable. This is how the operation is applied:

```txt
  hgfedcba
& HFGEDCBA
----------
  zyxwvuts

s = a & A
t = b & B
u = c & C
...
```

The result of a bitwise opeeration is determined by what's called its _truth table_, which comes from the assumption that `0` is `false` and `1` is `true`, and corresponding to the respective _boolean operation_. You may know `true and true` results in `true` either from logic or from English language use. But if either operand is `false` then the result is `false`. This is the same in the bitwise operation, but using `0` and `1`. We represent this in an actual table:

|  &|  0|  1|
|---|---|---|
|  0|  0|  0|
|  1|  0|  1|

Now taking our two numbers from before, we apply this truth table over each pair of bits:

```txt
  00001100
& 00001000
----------
  00001000
```

So what happened? The mask only contains a single `1`, in the position that we need it. We know every other bit will be 0, because 0 & anything is always 0. Thus we've "extracted" the real state of the up button from `~KEY_PAD`, because we know that if it was `1`, the result would have `1` in that bit and if it was `0` the result would have `0`.

Using this value in a _boolean_ expression renders the whole value as `true`, because it's non-zero. Thus this whole expression `(keys & KEY_UP)` is `true` (non-zero) if the up key is pressed and `false` (zero) if it's not.

The next part of the boolean expression, `(PRC_SCROLL_Y > 0)`, is checking to make sure we haven't reached 0 in this variable before decreasing it one further `PRC_SCROLL_Y--`. In C, zero minus one ends up _underflowing_, so it's not something we want to do unintentionally, especially since `PRC_SCROLL_Y` is an _unsigned integer_.
What this means in total is that, while the up button is pressed, the viewport will scroll upwards until reaching the top (0).

This logic is then repeated for each direction. Since the player can't press up and down at the same time, we use `else if` instead of just `if`. But since the player can press, for instance, up+left, we do a new `if` for checking `KEY_LEFT`.

The maximum values we allow for `PRC_SCROLL_X` and `PRC_SCROLL_Y` (such as in the expression `(PRC_SCROLL_Y < 31)`) are simply based on the size of the background image used. Scrolling right 31 pixels shows the right-most pixel at the right edge of the screen.

## hello_tiles.h

This is a C header file which contains graphics data converted to an array of hexadecimal values. It's very bad practice to define contents of variables in a header file because it won't be able to be imported (and thus the identifier referenced) by multiple C files. This file was generated by a conversion utility which is not included.

```c
const uint8_t hello_tile_count = 192;
const uint8_t _rom hello_tiles[] _at(0x10000) = {
	// ...
};
```

Firstly we have `const`, which isn't a type like `uint8_t` is, but rather a _qualifier_. Its meaning can change across different languages, but its purpose in C is to act as a way to inform the optimizer that the author won't modify its value. This is slightly different from read-only, because the value could be modified in other ways (by the hardware, for instance).

Next is the `_rom` _addressing qualifier_, this is an EPSON extension which tells the compiler to leave the data in ROM and reference it directly in ROM. If one were to use `_far` instead, the compiler would leave the data in ROM but create a pointer to it in RAM (thus putting two bytes in RAM). Not having any addressing qualifier defaults to `_near` and causes an error due to the `_at` address being out of range.

`_at` is also an EPSON extension, this specifies an absolute address to place the data in the resulting code. This address needs to be far enough from the end of a _bank_ (a multiple of 0x10000) that the data doesn't attempt to write past the end. Additionally, the data cannot overlap with any other absolutely possitioned data.

Finally, for the normal C part of this, essentially `const uint8_t hello_tiles[] = {0x00,0x00,...};`
This portion is declaring an _array_. The `[]` part is what indicates it's an array type. Normally a number would need to be inside, such as `[10]`, in order to specify the fixed length of the array, but since the data is directly specified inside the `{}`, it's able to infer the size from how many entries are provided.

## Makefile

This project uses the included makefile system, `pm.mk`, so all it has to do is define some information it uses then include the common makefile. The full amount of configuration available will be covered in a separate tutorial, but let's discussed what's used here.

Firstly `TARGET` is the filename of the final ROM you want to make, that is, with this specified as `helloworld`, the final binary is `helloworld.min`

More importantly, you need to specify which files to compile, as the system can't automatically discover them. You do this in `C_SOURCES` and `ASM_SOURCES`.
These are _space-separated_ lists of files. This means two things: you must list each file with the path relative to the your `Makefile` separated by a single space and the filenames and directories in your projects cannot contain spaces themselves.
As the names imply, you specify your C files in `C_SOURCES` and any assembly files, if you make any more, in `ASM_SOURCES`. You may use `\` as the path separator on Windows, but `/` also works and is more cross-compatible.

Finally, it `include`s the main Makefile which does all the heavy lifting. `..` refers to "the directory above this one" So, `..` refers to `examples` and `../..` refers to your repository root folder, probably `c88-pokemini`. If you place any new projects you make in a `projects` folder next to but not inside of `examples`, then your `include` statement will look the exact same.

## Binary files you will see after building

* `main.obj`, `isr.obj`, `startup.obj` - These are "object" files, they're compiled binaries of the individual C/asm files which will be used by the _linker_ in order to eventually product the final binary.
* `helloworld.map` - This is the application map file produced by the _locator_. It's a text file which records the locations various _sections_ were placed in the game binary.
* `helloworld.sre` - This is the binary before _padding_. You don't need to know it, but it's a Motorola S-record
* `helloworld.min` - This is the final, playable ROM file.
* `main.src`, `isr.src` - These aren't made during the normal build process, but you can request one to be made using `mk88 main.src` These are the respective C files after they've been compiled to assembly, but before being assembled into a binary. If you want to see what your C code turns into, you can check this way!
