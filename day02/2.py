from argparse import ArgumentParser
from itertools import combinations


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def hamming_distance(string1, string2):
    similarities = [char1 if char1 == char2 else ''
                   for char1, char2 in zip(string1, string2)]
    similarities = list(filter(lambda c: c != '', similarities))
    return len(string1) - len(similarities), similarities


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    for first, second in combinations(data, r=2):
        dist, sim = hamming_distance(first, second)
        if dist == 1:
            print('similarities {}'.format(''.join(sim)))
            break


if __name__ == '__main__':
    main()
