#!/usr/bin/env python3
#########1#########2#########3#########4#########5#########6#########7#########8
#
#########1#########2#########3#########4#########5#########6#########7#########8

import sys


def print_help():
    help_message = """
Usage: echo -en "Hello World\\r\\n" | rstrip

Arguments:
    <filename>  The name of the file to process, or None

Options:
    -h, --help  Show this help message and exit.
"""

    print(help_message)


def trim_trailing_spaces(filename=None):
    """
    trim trailing spaces
    """
    try:
        if filename:
            with open(filename, "r") as file:
                print("".join([line.rstrip() for line in file]), end="")

        else:
            print("".join([line.rstrip() for line in sys.stdin]), end="")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("-h", "--help"):
            print_help()
            return
        else:
            trim_trailing_spaces(arg)
    else:
        trim_trailing_spaces()


if __name__ == "__main__":
    main()
