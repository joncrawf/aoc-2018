from collections import defaultdict

import re

class Graph(object):

    def __init__(self, links, free_tasks, dependency_counts):
        self.links = links
        self.free_tasks = free_tasks
        self.dependency_counts = dependency_counts


    def next_free(self):
        return self.free_tasks.pop(0)


    def remove_deps(self, event):
        dependencies = self.links[event]
        for dep in dependencies:
            self.dependency_counts[dep] -= 1
            if self.dependency_counts[dep] == 0:
                self.free_tasks += dep

        self.free_tasks = sorted(self.free_tasks)

    def num_free(self):
        return len(self.free_tasks)


def generate_graph(data):
    links = defaultdict(set)
    dependency_counts = defaultdict(int)
    for line in data:
        task, dep = re.search('Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line).groups()
        links[task].add(dep)
        dependency_counts[dep] += 1

    currently_free = sorted(list(set(links.keys()) - set(dependency_counts.keys())))

    return Graph(links, currently_free, dependency_counts)
