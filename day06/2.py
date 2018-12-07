from argparse import ArgumentParser
from itertools import product

import numpy as np
import points as pts


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path',    type=str, required=True)
    parser.add_argument('--max-distance', type=int, default=10000)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    points = pts.get_points(data)
    minx, miny, maxx, maxy = pts.get_point_bounds(points)
    max_distance = args.max_distance
    area = 0

    for x, y in product(range(minx, maxx + 1), range(miny, maxy + 1)):
        distance = sum(
            pts.manhattan_distance([x, y], point)
            for point in points
        )
        if distance < max_distance:
            area += 1

    print(area)


if __name__ == '__main__':
    main()
