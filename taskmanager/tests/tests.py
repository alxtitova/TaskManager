#!/usr/bin/env python

import random
import yaml
import time
import os

from taskmanager.manager.utils.graph import Graph
from taskmanager.manager import Manager
from taskmanager.manager import Task
from taskmanager.manager import Build

import networkx as nx

def debug_build_class():
    build = None

    try:
        build = Build('sample_build')
    except Exception as e:
        print('Failed to build build. An exception occurred: {exception}'.format(exception=e))
        exit(6)

    build.add_task('sample_task_1')
    build.add_task('sample_task_2')
    build.add_task('sample_task_3')

    return build.name == 'sample_build' and len(build.tasks) == 3

def debug_task_class():
    task = None

    try:
        task = Task('sample_task')
    except Exception as e:
        print('Failed to build task. An exception occurred: {exception}'.format(exception=e))
        exit(6)

    task.add_dependency('sample_dependency_1')
    task.add_dependency('sample_dependency_2')
    task.add_dependency('sample_dependency_3')

    return task.name == 'sample_task' and len(task.dependencies) == 3


class Random:
    def __init__(self, seed):
        random.seed(seed)
        self.action = ['bring', 'design', 'enable', 'read', 'train', 'create', 'build', 'upgrade', 'update']
        self.feature = ['lime', 'black', 'blue', 'red', 'white', 'orange', 'grey', 'purple']
        self.actor = ['fairies', 'leprechauns', 'cyclops', 'centaurs', 'witches']
        self.build = ['important', 'urgent', 'pack', 'do', 'cool']
        self.target = ['test', 'game', 'release','build','things', 'stuff']

    def make_random_task(self):
        return str(self.action[random.randrange(len(self.action))] + \
                   '_' + self.feature[random.randrange(len(self.feature))]  + \
                   '_' + self.actor[random.randrange(len(self.actor))])

    def make_random_build(self):
        return str(self.build[random.randrange(len(self.build))] + '_' + self.target[random.randrange(len(self.target))])

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

        directory = os.getcwd()

        print(directory)

        with open('builds.yaml', 'w+') as outfile:
            yaml.dump(builds, outfile, default_flow_style=False)

        with open('tasks.yaml', 'w+') as outfile:
            yaml.dump(tasks, outfile, default_flow_style=False, sort_keys=False)


class Test:
    def __init__(self, seed):
        self.r = Random(seed)
        self.r.make_random_builds()
        self.manager = Manager('builds.yaml', 'tasks.yaml')

    def test_utils(self):
        return debug_build_class() and debug_task_class()

    def test_graph(self):
        g = None

        try:
            g = Graph(5)
        except Exception as e:
            print('Failed to build graph. An exception occurred: {exception}'.format(exception=e))
            exit(6)

        g.add_edge(1, 2)
        g.add_edge(0, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 3)
        g.add_edge(3, 4)

        validation = {1: [2], 0: [3], 2: [4, 3], 3: [4]}

        return g.graph == validation and g.nodes == 5


    def test_manager(self, debug=False):
        try:
            self.manager.manage_builds(debug)
        except Exception as e:
            print('Manager has failed. An exception occurred: {exception}'.format(exception=e))
            exit(6)

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
            print('Graph contains a cycle, test is not completed. Please change seed.')
            exit(6)

class Debug:
    def __init__(self):
        print('Debug mode \n')
        self.output_path = 'test_output.txt'

    def run(self):
        print('Running tests')

        seed = input('Enter seed (unsigned int): ')
        test = Test(seed)

        if test.test_utils():
            print('Build class: test passed')
        else:
            print('Build class: test failed')

        time.sleep(1)

        if test.test_graph():
            print('Graph class: test passed')
        else:
            print('Graph class: test failed')

        time.sleep(1)

        if test.test_toposort():
            print('Topological sort: test passed')
        else:
            print('Topological sort: test failed')

        time.sleep(1)

        print('Generating random input data...')

        time.sleep(1)

        test.test_manager(debug=True)
        print('Output written in {output}'.format(output=self.output_path))