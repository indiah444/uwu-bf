"""This file transpiles brainfuck to UwU."""

brainfuck_to_uwu = {
    ">": "OwO",
    "<": "°w°",
    "+": "UwU",
    "-": "QwQ",
    ".": "@w@",
    ",": ">w<",
    "[": "~w~",
    "]": "¯w¯"
}


def transpile_brainfuck_to_uwu(brainfuck_string: str) -> str:
    """Transpiles brainfuck to UwU."""

    uwu_code = ""

    for instruction in brainfuck_string:
        if instruction in brainfuck_to_uwu:
            uwu_code += brainfuck_to_uwu[instruction] + " "

    return uwu_code.strip()


if __name__ == "__main__":

    print(transpile_brainfuck_to_uwu(
        "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++++++++++++++++++.----------.++++++.<<+++++++++.>>---.-------------.<<-------.>>++++++++++++++++++.------------------.+++++++.---------.++++++++++++.--.--------.<<+."))
