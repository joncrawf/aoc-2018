from argparse import ArgumentParser
from collections import Counter


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def num_duplicates(data, num):
    return sum(
        1 if num in Counter(string).values() else 0
        for string in data
    )


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    checksum = (
        num_duplicates(data, 2) *
        num_duplicates(data, 3)
    )
    print(checksum)


if __name__ == '__main__':
    main()
