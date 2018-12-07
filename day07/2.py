from argparse import ArgumentParser
from graph import Graph, generate_graph
from worker import WorkingWorker

import re


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path',   type=str, required=True)
    parser.add_argument('--num-workers', type=int, default=5)
    return parser


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    graph = generate_graph(data)
    workers_working = []
    total_time = 0
    task_order = ''

    while graph.num_free() or workers_working:
        while len(workers_working) < args.num_workers and graph.num_free():
            task = graph.next_free()
            workers_working.append(WorkingWorker(task))

        max_time_jump = min(workers_working, key=lambda x: x.time_remaining).time_remaining
        total_time += max_time_jump
        for worker in workers_working:
            worker.time_remaining = worker.time_remaining - max_time_jump
            if worker.time_remaining == 0:
                graph.remove_deps(worker.task)
                task_order += worker.task

        workers_working = [worker for worker in workers_working if worker.time_remaining > 0]

    print(task_order)
    print(total_time)


if __name__ == '__main__':
    main()
