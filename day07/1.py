from argparse import ArgumentParser
from graph import Graph, generate_graph

import re


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    graph = generate_graph(data)

    task_order = ''
    while graph.num_free() > 0:
        task = graph.next_free()
        graph.remove_deps(task)
        task_order += task

    print(task_order)


if __name__ == '__main__':
    main()
