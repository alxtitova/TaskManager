#!/usr/bin/env python

from taskmanager.manager.utils.graph import Graph
from taskmanager.manager.utils.loader import Loader

import sys

class Build:
    def __init__(self, name):
        self._name = name
        self._tasks = {}

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return self._name

    @property
    def tasks(self):
        return self._tasks

    def add_task(self, name):
        self._tasks[name] = name

class Task:
    def __init__(self, name):
        self._name = name
        self._dependencies = {}

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return self._name

    @property
    def dependencies(self):
        return self._dependencies

    def add_dependency(self, name):
        self._dependencies[name] = name

class Manager:
    def __init__(self, builds_file, tasks_file):
        self._builds = []
        self._tasks = []

        self.dependency_map = {}
        self.task_map = {}

        try:
            self.set_builds(builds_file)
        except Exception as e:
            print('Builds file is empty or incorrect. An exception occurred: {exception} '.format(exception=type(e)))
            exit(2)

        try:
            self.set_tasks(tasks_file)
        except Exception as e:
            print('Tasks file is empty or incorrect. An exception occurred: {exception}'.format(exception=type(e)))
            exit(2)

        self.map_dependencies()
        self.map_tasks()


    @property
    def builds(self):
        return self._builds

    @property
    def tasks(self):
        return self._tasks

    def set_builds(self, builds_file):
        builds = Loader(builds_file).load_yaml()['builds']
        for build in builds:
            b = Build(build['name'])

            if b.__hash__() in [x.__hash__() for x in self._builds]:
                print('Warning: duplicate build {build}'.format(build=b.name))

            self._builds.append(b)

            for i in range(len(build['tasks'])):
                self._builds[-1].add_task(build['tasks'][i])

    def set_tasks(self, tasks_file):
        tasks = Loader(tasks_file).load_yaml()['tasks']
        for task in tasks:
            t = Task(task['name'])

            if t.__hash__() in [x.__hash__() for x in self._tasks]:
                print('Warning: duplicate task {task}'.format(task=t.name))

            self._tasks.append(t)

            for i in range(len(task['dependencies'])):
                self._tasks[-1].add_dependency(task['dependencies'][i])

    def map_dependencies(self):
        for i, task in enumerate(self._tasks):
            self.dependency_map[task.name] = task.dependencies

    def map_tasks(self):
        for i, build in enumerate(self._builds):
            self.task_map[build.name] = build.tasks

    def list_tasks(self):
        print('List of available tasks: ')
        for task in self.tasks:
            print('* ', task.name)

    def list_builds(self):
        print('List of available builds: ')
        for build in self.builds:
            print('* ', build.name)

    def get_task(self, name):
        if name in self.dependency_map:
            print('Task info: ')
            print('* name: ', name)
            print('* dependencies: ')

            for dependency in self.dependency_map[name]:
                print(dependency)
        else:
            print('There is no task named {name}'.format(name=name))
            exit(3)

    def get_build(self, name):
        if name in self.task_map:
            print('Build info: ')
            print('* name: ', name)
            print('* tasks: ')

            for task in self.task_map[name]:
                print(task)
        else:
            print('There is no build named {name}'.format(name=name))
            exit(3)

    def manage_build(self, build):
        """
        Returns a proper order of tasks in the build and a validation flag
        valid = True if there is no cycles in build, else valid = False
        """
        g = None

        try:
            g = Graph(len(build.tasks))
        except Exception as e:
            print('Failed to create graph. An exception occurred: {exception}'.format(exception=type(e)))
            exit(4)

        for i in range(len(build.tasks)):
            for j in range(len(build.tasks)):
                tl = list(build.tasks)
                if tl[j] in self.dependency_map[tl[i]]:
                    g.add_edge(j, i)

        order = g.topological_sort()
        valid = not g.check_for_cycles()

        return order, valid

    def manage_builds(self, debug=False):
        """
        Manages all the builds in builds.yaml and outputs the result in .txt file
        """

        current_builds = self.builds
        orig_stdout = sys.stdout
        f = None

        s = 'test_output.txt' if debug else 'output.txt'

        try:
            f = open(s, 'w+')
        except Exception as e:
            print('Failed to create output.txt. An exception occurred: {exception}'.format(exception=type(e)))
            exit(5)

        if f:
            sys.stdout = f

        for build in current_builds:
            order, valid = self.manage_build(build)

            if valid:
                tl = list(build.tasks)
                task_list = [tl[x] for x in order]
                print('To do in', str(build.name), ': ')
                for task in task_list:
                    print('  ' + task)
                print('\n')
            else:
                print("Invalid build {build}: this build contains cycles \n".format(build = str(build.name)))

        if f:
            sys.stdout = orig_stdout
            f.close()
