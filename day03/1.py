from argparse import ArgumentParser

import numpy as np
import re


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    boxes = []
    for line in data:
        _, left, top, width, height = re.search('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', line).groups()
        boxes.append([int(left), int(top), int(width), int(height)])

    furthest_right = max(boxes, key=lambda b: b[0])
    furthest_up = max(boxes, key=lambda b: b[1])
    env = np.zeros([furthest_up[1] + furthest_up[3] + 5, furthest_right[0] +
                    furthest_right[2] + 5])

    for left, top, width, height in boxes:
        env[left:left+width, top:top+height] += 1

    print(np.sum(env > 1))


if __name__ == '__main__':
    main()
