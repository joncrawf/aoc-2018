import numpy as np


def get_points(data):
    return [ np.array(list(map(int, line.split(',')))) for line in data ]


def nearest_point(x, y, points):
    distances = np.array([ manhattan_distance([x, y], p) for p in points ])
    min_distance = np.where(distances == distances.min())[0]
    return min_distance[0] if len(min_distance) == 1 else -1


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_point_bounds(points):
    x, y = list(zip(*points))
    return min(x), min(y), max(x), max(y)
