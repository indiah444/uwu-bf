"""This file transpiles UwU to brainfuck, then interprets brainfuck into English."""


def interpret_brainfuck(brainfuck_code: str) -> str:
    """Interprets brainfuck code and converts it to English. Note: tape is initially set to 1000 cells (all set to 0), instead of the specified 30,000. This is to save
    time and space, as most brainfuck code rarely requires the full memory space."""

    tape = [0] * 1000
    pointer = 0
    output = ""
    code_pointer = 0
    loop_stack = []

    while code_pointer < len(brainfuck_code):
        command = brainfuck_code[code_pointer]
