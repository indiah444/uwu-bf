# UwU-brainfuck, brainfuck-UwU transpiler 

## Overview 

This is a [UwU](https://esolangs.org/wiki/UwU) to [brainfuck](https://esolangs.org/wiki/Brainfuck), and brainfuck to UwU transpiler. 

## brainfuck

brainfuck is a esoteric programming language (or esolang). It operates on an array of memory cells, with each initially set to 0. A pointer initially points to the first memory cell, and moves and increments the cells according to the commands given. 

| Command | Description |
| ------- | ----------- |
|    >    | Move the pointer to the right |
|    <    | Move the pointer to the left |
|    +    | Increment the memory cell at the pointer |
|    -    | Decrement the memory cell at the pointer |
|    .    | Output the character signified by the cell at the pointer |
|    ,    | Input a character and store it in the cell at the pointer |
|    [    | Jump past the matching ] if the cell at the pointer is 0 |
|    ]    | Jump back to the matching [ if the cell at the pointer is nonzero |

## UwU 

UwU is a joke esoteric programming language. It is based on brainfuck but uses UwU faces instead.

|    brainfuck   |   UwU   | Description |
| -------------- | ------- | ----------- |
|         >      |   OwO   | Move the pointer to the right |
|         <      |   °w°   | Move the pointer to the left |
|         +      |   UwU   | Increment the memory cell at the pointer |
|         -      |   QwQ   | Decrement the memory cell at the pointer |
|         .      |   @w@   | Output the character signified by the cell at the pointer |
|         ,      |   >w<   | Input a character and store it in the cell at the pointer |
|         [      |   ~w~   | Jump past the matching ] if the cell at the pointer is 0 |
|         ]      |   ¯w¯   | Jump back to the matching [ if the cell at the pointer is nonzero |


## Files explained

- `bf_to_uwu.py`: Transpiles brainfuck to UwU
- `uwu_to_bf.py`: Transpiles UwU to brainfuck
- `choose_transpiler.py`: CLI script to allow users to select the input file (with the language they want transpiled), the input language and the output language.