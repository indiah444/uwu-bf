"""CLI script that allows users specify an input file, input language, and output language."""

from argparse import ArgumentParser

from uwu_to_bf import transpile_uwu_to_brainfuck
from bf_to_uwu import transpile_brainfuck_to_uwu


def get_console_arguments() -> str:
    """Get the user's choices from the CLI"""

    parser = ArgumentParser(
        description="A tool to transpile between brainfuck and UwU esolangs.")
    parser.add_argument("--input-file", required=True,
                        help="Path to the input file.")
    parser.add_argument("--input-lang", choices=["brainfuck", "uwu"],
                        required=True, help="Input language (brainfuck or UwU).")
    parser.add_argument("--output-lang", choices=[
                        "brainfuck", "uwu"], required=True, help="Output language (brainfuck or UwU).")
    args = parser.parse_args()

    return args


def transpile(input_text: str, input_lang: str, output_lang: str) -> str:
    """Transpule the input text from the input language to the output language."""

    if input_lang == "uwu" and output_lang == "brainfuck":
        return transpile_uwu_to_brainfuck(input_text)
    elif input_lang == "brainfuck" and output_lang == "uwu":
        return transpile_brainfuck_to_uwu
    else:
        raise ValueError(f"Unsupported language conversion: {
                         input_lang} to {output_lang}")


if __name__ == "__main__":

    args = get_console_arguments()

    try:
        with open(args.input_file, "r") as f:
            input_text = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file} not found.")

    try:
        output_text = transpile(input_text, args.input_lang, args.output_lang)
    except ValueError as e:
        print(f"Error: {e}")

    print(output_text)
