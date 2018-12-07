from argparse import ArgumentParser
from itertools import product

import numpy as np
import points as pts


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def get_counts(points, minX, maxX, minY, maxY):
    grid = np.zeros((maxX - minX + 1, maxY - minY + 1))

    for x, y in product(range(minX, maxX + 1), range(minY, maxY + 1)):
        nearest_point = pts.nearest_point(x, y, points)
        grid[x - minX, y - minY] = nearest_point

    return np.unique(grid, return_counts=True)


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    points = pts.get_points(data)
    minx, miny, maxx, maxy = pts.get_point_bounds(points)

    _, set_counts = get_counts(points, minx, maxx, miny, maxy)
    _, big_counts = get_counts(points, 0, maxx + 50, 0, maxy + 50)

    print(max(np.take(set_counts, np.where(set_counts - big_counts == 0)[0])))


if __name__ == '__main__':
    main()
