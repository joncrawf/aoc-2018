from argparse import ArgumentParser
from collections import defaultdict

import numpy as np
import re


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    return parser


def guard_sleeps(data):
    sleeps = defaultdict(lambda: np.zeros(60, dtype=np.int32))
    guard_id = -1
    falls = 0
    for line in sorted(data):
        date, event = re.search('^\[(.+)\] (.+)$', line).groups()

        if event.startswith('Guard'):
            guard_id = int(re.search('\d+', event).group())
        elif event.startswith('falls'):
            falls = int(date[-2:])
        elif event.startswith('wakes'):
            wakes = int(date[-2:])
            sleeps[guard_id][falls:wakes] += 1
    return sleeps


def main():
    args = build_parser().parse_args()
    with open(args.data_path) as file:
        data = file.read().splitlines()

    sleeps = guard_sleeps(data)

    guard_id, sleep_minutes = max(sleeps.items(), key=lambda s: s[1].sum())
    max_minute = sleep_minutes.argmax()

    print(guard_id * max_minute)


if __name__ == '__main__':
    main()
