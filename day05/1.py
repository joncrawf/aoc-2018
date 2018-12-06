from argparse import ArgumentParser
from react import react


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().strip()

    print(len(react(data)))


if __name__ == "__main__":
    main()
