import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="textkit", description="Textkit CLI")
    parser.add_argument("text", help="Input text")
    parser.add_argument("--lower", action="store_true", help="Lowercase output")
    args = parser.parse_args()

    out = args.text.lower() if args.lower else args.text
    print(out)