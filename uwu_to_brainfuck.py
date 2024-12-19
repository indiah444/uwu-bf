"""This file transpiles UwU to brainfuck."""

uwu_to_brainfuck = {
    "OwO": ">",
    "°w°": "<",
    "UwU": "+",
    "QwQ": "-",
    "@w@": ".",
    ">w<": ",",
    "~w~": "[",
    "¯w¯": "]"
}


def transpile_uwu_to_brainfuck(uwu_string: str) -> str:
    """Transpiles UwU to brainfuck."""

    instructions = uwu_string.split()
    brainfuck_code = ""

    for instr in instructions:
        if instr in uwu_to_brainfuck:
            brainfuck_code += uwu_to_brainfuck[instr]

    return brainfuck_code


print(transpile_uwu_to_brainfuck("UwU UwU UwU UwU ~w~ OwO UwU UwU UwU UwU ~w~ OwO UwU UwU UwU UwU UwU OwO UwU UwU UwU UwU OwO UwU UwU UwU UwU OwO UwU UwU °w° °w° °w° °w° QwQ ¯w¯ °w° QwQ ¯w¯ OwO UwU UwU UwU UwU OwO UwU UwU UwU UwU @w@ OwO °w° °w° ~w~ OwO OwO UwU UwU °w° °w° QwQ ¯w¯ OwO OwO @w@ OwO UwU @w@ °w° °w° °w° UwU UwU UwU ~w~ OwO QwQ QwQ °w° QwQ ¯w¯ OwO @w@ OwO UwU UwU UwU @w@ OwO OwO @w@ °w° °w° °w° °w° UwU UwU UwU UwU UwU ~w~ OwO UwU UwU °w° QwQ ¯w¯ OwO UwU @w@ OwO UwU UwU UwU UwU @w@ °w° QwQ QwQ QwQ QwQ @w@ OwO OwO OwO UwU @w@"))
