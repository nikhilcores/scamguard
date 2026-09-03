import argparse

from .analyzer import analyze_message
from .input import read_message


def main():
    parser = argparse.ArgumentParser(
        description="Check a message for common scam indicators."
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "message",
        nargs="?",
        help="Message to analyze",
    )

    group.add_argument(
        "--file",
        help="Read the message from a text file",
    )

    args = parser.parse_args()

    if args.file:
        message = read_message(args.file)
    else:
        message = args.message

    result = analyze_message(message)

    print(result["report"])


if __name__ == "__main__":
    main()
