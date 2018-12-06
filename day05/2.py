from argparse import ArgumentParser
from react import react
from string import ascii_lowercase

import re


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().strip()

    string = react(data)
    min_length = 1e9

    for c in ascii_lowercase:
        remaining_string = re.sub(f'{c}|{c.upper()}', '', string)
        min_length = min(min_length, len(react(remaining_string)))

    print(min_length)


if __name__ == "__main__":
    main()
