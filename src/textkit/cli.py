import argparse

from textkit.core import normalize_text


def main() -> None:
    parser = argparse.ArgumentParser(prog="textkit", description="Textkit CLI")
    parser.add_argument("text", help="Input text")
    parser.add_argument("--lower", action="store_true", help="Lowercase output")
    parser.add_argument("--normalize", action="store_true", help="Trim + collapse whitespace")
    args = parser.parse_args()

    out = args.text
    if args.normalize:
        out = normalize_text(out, lower=args.lower)
    elif args.lower:
        out = out.lower()

    print(out)