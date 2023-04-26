#!/usr/bin/env python

import random
import yaml

import sys
sys.path.insert(0, '..')

from manager.utils.graph import Graph
from manager import Manager

import networkx as nx

class Random:
    def __init__(self):
        random.seed(11)

    def make_random_task(self):
        do = ['bring', 'design', 'enable', 'read', 'train', 'create', 'build', 'upgrade', 'update']
        which = ['lime', 'black', 'blue', 'red', 'white', 'orange', 'grey', 'purple']
        what = ['fairies', 'leprechauns', 'cyclops', 'centaurs', 'witches']

        return str(do[random.randrange(len(do))] + '_' + which[random.randrange(len(which))]  + '_' + what[random.randrange(len(what))])

    def make_random_build(self):
        do = ['important', 'urgent', 'pack', 'do', 'cool']
        what = ['test', 'game', 'release','build','things', 'stuff']

        return str(do[random.randrange(len(do))] + '_' + what[random.randrange(len(what))])

    def make_random_builds(self):
        builds = {'builds': []}
        tasks = {'tasks': []}

        random_tasks = [self.make_random_task() for x in range(random.randint(1, 100))]

        for i in range(random.randint(1, 10)):
            di = {'name': self.make_random_build(), 'tasks' : []}
            for j in range(random.randint(1, 10)):
                task = random_tasks[random.randint(0, len(random_tasks)-1)]
                di['tasks'].append(task)
                dt = {'name': task, 'dependencies' : []}
                for k in range(random.randint(0, 10)):
                    dt['dependencies'].append(random_tasks[random.randint(0, len(random_tasks)-1)])
                tasks['tasks'].append(dt)
            builds['builds'].append(di)

        with open('test_input/builds.yaml', 'w') as outfile:
            yaml.dump(builds, outfile, default_flow_style=False)

        with open('test_input/tasks.yaml', 'w') as outfile:
            yaml.dump(tasks, outfile, default_flow_style=False, sort_keys=False)


class Test:
    def __init__(self):
        r = Random()
        r.make_random_builds()

    def test_manager(self):
        manager = Manager('test_input/builds.yaml', 'test_input/tasks.yaml')
        manager.manage_builds()

    def test_toposort(self):
        n = random.randint(1, 10)
        p = 1/random.randint(1,100)

        gnx = nx.gnp_random_graph(n, p, directed=True)
        g = Graph(n)

        for e in list(gnx.edges):
            g.add_edge(e[1], e[0])

        topo = g.topological_sort()

        if not g.check_for_cycles():
            topo_list = list(nx.all_topological_sorts(gnx))

            return topo in topo_list
        else:
            print('Graph contains a cycle.')

            return False

def main():
    print('Running tests')

    test = Test()

    if test.test_toposort():
        print('Topological sort: test passed')
    else:
        print('Topological sort: test failed')

    print('Generating random input data')
    test.test_manager()

if __name__ == '__main__':
    main()