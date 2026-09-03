import argparse

from .analyzer import analyze_message


def main():
    parser = argparse.ArgumentParser(
        description="Check a message for common scam indicators."
    )

    parser.add_argument(
        "message",
        help="Message to analyze",
    )

    args = parser.parse_args()

    result = analyze_message(args.message)

    print(result["report"])


if __name__ == "__main__":
    main()
