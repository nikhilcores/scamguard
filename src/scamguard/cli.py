import argparse

from .analyzer import analyze_message
from .input import read_message
from .reporter import format_json_report


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

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the analysis as JSON",
    )

    args = parser.parse_args()

    try:
        if args.file:
            message = read_message(args.file)
        else:
            message = args.message

        result = analyze_message(message)

    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))

    if args.json:
        print(format_json_report(result))
    else:
        print(result["report"])


if __name__ == "__main__":
    main()
