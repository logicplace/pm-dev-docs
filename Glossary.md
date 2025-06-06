# Glossary of terms

Major terms are sorted alphabetically, but register names and stuff like that are organized under a section dedicated to them. Just use your browser's in-page search to find what you need!

## Endianness

Systems can be either Big Endian or Little Endian. The Pokémon mini is a little endian system. This refers to the byte order for multi-byte numbers. Since Pokémon mini is a 16-bit system, it stores numbers in at most 16-bits (at a time). When doing so, little endian stores the bytes as [least significant](#significant-bytes) first.

## Identifier

An identifier refers to any referenceable name in code. It could be the name of a variable, a function, a structure, etc.

## Open-bus

Open-bus is a state in which no hardware on a data path is actively responding to a request for data. In many cases this results in bus-capacitance driving ghost data to the CPU. This means that when reading from a non-existent hardware location, the CPU will see the last data on the path (read or write). This often means that reading from these locations will result in the data result of things being based around the last instruction byte used, such as an opcode or an immediate value.

## Operator

There are two potential meanings for this term: mathematical operators and assembly operators.

### Mathematical operator

Mathematical operators refer to the typical symbols of mathematics that you will see in C code. This includes unary operators, which refer to an operator which only takes one argument (in C, that argument is generally to the right of it); binary operators, which take two arguments (in C, one to the left and one to the right); and the ternary operator.

#### Unary operator

Includes arithmetic, logical, bitwise, and the de/reference operators.

* `+x` - "positive x" which is essentially no operation (it does not force a number to be positive).
* `-x` - "negative x" which inverts the sign of x.
* `++x` - "pre-increment x" increments x by 1 and returns the _resulting_ value.
* `--x` - "pre-decrement x" decrements x by 1 and returns the _resulting_ value.
* `x++` - "post-increment x" increments x by 1 and returns the _initial_ value.
* `x--` - "post-decrement x" decrements x by 1 and returns the _initial_ value.
* `!x` - "logical negation of x" is the "boolean not" operator. If x is zero then it becomes 1, if x is non-zero then it becomes 0.
* `~x` - "complement of x" also called the "1s complement" or "bitwise not" operator, it inverts the bits of x so that all 0s become 1s and all 1s become 0s.
* `&x` - "reference" returns the address of where the variable x is stored in RAM.
* `*x` - "dereference" treats x as an address pointing to some location anywhere in memory and returns the value from that point.

#### Binary operator

Includes arithmetic, comparison/relational, logical, and bitwise operators, as well as the assignment operator.

* `x + y` - addition of x and y.
* `x - y` - subtraction of y from x.
* `x * y` - multiplication of x and y.
* `x / y` - divide x by y.
* `x % y` - "modulo" or "modulus operator" divides x by y, but returns the remainder.
* `x == y` - "equal to" compares equivalency of x and y, true if equal.
* `x != y` - "not equal to" compares equivalency of x and y, false if equal.
* `x > y` - "greater than" compares difference of x and y, true if x is larger.
* `x < y` - "less than" compares difference of x and y, true if y is larger.
* `x >= y` - "greater than or equal to" compares equivalency and differency of x and y.
* `x <= y` - "less than or equal to" compares equivalency and differency of x and y.
* `x && y` - "logical and" returns true only if both x and y are true.
* `x || y` - "logical or" returns true if either x, y, or both x and y are true.
* `x & y` - "bitwise and" see C tutorial for details
* `x | y` - "bitwise or" see C tutorial for details
* `x ^ y` - "bitwise exclusive or" or "xor" see C tutorial for details
* `x << y` - "shift left" shifts the bits of x left by the number y
* `x >> y` - "shift right" shifts the bits of x right by the number y
* `x = y` - assign the value of y to the variable named x.
* `x op= y` - where `op` is any binary arithmetic or bitwise operator, equivalent to `x = x op y` such as `x += y` being equivalent to `x = x + y`.

#### Ternary operator

There is only one ternary operator in C of the form `x ? y : z` which is functionally equivalent to the following code, but may be used within other operations (since it has a return value) whereas the below must be separated.

```c
if (x) {
    y;
}
else {
    z;
}
```

### Assembly operator

Assembly operators refer to what is typically represented by a mnemonic, such as "addition with carry" operation for `ADC`. Operator and mnemonic (when refering to operators, anyway) will often be used interchangeably.

* `ADD` - Addition
* `ADC` - Addition with carry
* `SUB` - Subtraction
* `SBC` - Subtraction with carry
* `AND` - Logical product
* `OR` - Logical sum
* `XOR` - Exclusive OR
* `CP` - Comparison
* `BIT` - Bit test
* `INC` - Increment by 1
* `DEC` - Decrement by 1
* `MLT` - Multiplication
* `DIV` - Division
* `CPL` - Complement of 1
* `NEG` - Complement of 2 (negation)
* `LD` - Load
* `EX` - Byte or word exchange
* `SWAP` - Nibble exchange
* `RL` - Rotate to left with carry
* `RLC` - Rotate to left
* `RR` - Rotate to right with carry
* `RRC` - Rotate to right
* `SLA` - Arithmetic shift to left
* `SLL` - Logical shift to left
* `SRA` - Arithmetic shift to right
* `SRL` - Logical shift to right
* `PACK` - Pack
* `UPCK` - Unpack
* `SEP` - Code extension
* `PUSH` - Push to stack
* `POP` - Pop to stack
* `JRS` - Relative short jump
* `JRL` - Relative long jump
* `JP` - Indirect jump
* `DJR` - Loop
* `CARS` - Relative short call
* `CARL` - Relative long call
* `CALL` - Indirect call
* `RET` - Return
* `RETE` - Exception processing return
* `RETS` - Return and skip
* `INT` - Software interrupt
* `NOP` - No operation
* `HALT` - Shifts to HALT status
* `SLP` - Shifts to SLEEP status

## Scope

In programming, scope refers to what identifiers are visible from certain perspectives. These scopes tend to be hierarchical starting with the most visible, the _global scope_. If something is defined in the global scope, then it can be seen from everywhere in the program, in theory. However, in C, the identifier must still be made known within a file to be available for use. Thus, often, declarations inside a C file outside of any function are said to be in the global scope, whether or not they're made available in a header file.

A simple way to consider scope in C is that each code block, denoted by curly braces (`{}`), introduces a new scope which is a child of the scope that it's declared in.

Following that logic, it's clear functions also have a scope. This scope is not visible to other functions. That is, variables declared within the function scope are only usable within that function. If you use, for example, a for loop within that function in which you declare a new variable, that varible will be in the scope of the for loop, a child of the function scope, and not be available to the rest of the function.

```c
int example() {
    int hello = 10;
    for (int world=0; world < hello; ++world) {
        // Both `hello` and `world` are available to me!
    }
    // only `hello` is available to me!
}
```

When `world` become unavailable after the closing for the for loop, it's said to "go out of scope".

## Significant bits

There are 8 bits in a single byte, when laid out as a binary number (0-padded to 8 bits), the most significant bit is the the most significant digit, that is, the left-most one. Similarly, the least-significant digit is the right-most one.

The reason for this naming is due to the idea of precision. Given 20054 apples, for instace, misplacing 1 or 2 is relatively meaningless. This means the 2 in the ten-thousands place (fifth digit), is much more signifcant than the 4 in the ones place (first digit).

```
Example: M000 000L
Indices: 7654 3210
M = Most significant bit
L = Least significant bit
```

## Significant bytes

Given a sequence of bytes, arranged in the appropriate order (see [Endianness](#endianness) for more information on when to re-order bytes), the most significant byte is the left-most byte while the least significant byte is the right-most byte.

The reason for this naming is due to the idea of precision. Given 20054 apples, for instace, misplacing 1 or 2 is relatively meaningless. This means the 2 in the ten-thousands place (fifth digit), is much more signifcant than the 4 in the ones place (first digit).

```
Example: MM 00 LL
Indices:  2  1  0
MM = Most significant byte
LL = Least significant byte
```
