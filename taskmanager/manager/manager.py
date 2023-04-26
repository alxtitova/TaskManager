#!/usr/bin/env python

from taskmanager.manager.utils.graph import Graph
from taskmanager.manager.utils.loader import Loader

import sys

class Build:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(name)

class Task:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, name):
        self.dependencies.append(name)

class Manager:
    def __init__(self, builds_file, tasks_file):
        self._builds = []
        self._tasks = []

        self.dependency_map = {}
        self.task_map = {}

        try:
            self.set_builds(builds_file)
        except:
            print('Builds file is empty or incorrect')
            exit(2)

        try:
            self.set_tasks(tasks_file)
        except:
            print('Tasks file is empty or incorrect')
            exit(2)

        self.map_dependencies()
        self.map_tasks()


    @property
    def get_builds(self):
        return self._builds

    @property
    def get_tasks(self):
        return self._tasks

    def set_builds(self, builds_file):
        builds = Loader(builds_file).load_yaml()['builds']
        for build in builds:
            b = Build(build['name'])
            self._builds.append(b)
            for i in range(len(build['tasks'])):
                self._builds[-1].add_task(build['tasks'][i])

    def set_tasks(self, tasks_file):
        tasks = Loader(tasks_file).load_yaml()['tasks']
        for task in tasks:
            t = Task(task['name'])
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
        for task in self.get_tasks:
            print('* ', task.name)

    def list_builds(self):
        print('List of available builds: ')
        for build in self.get_builds:
            print('* ', build.name)

    def get_task(self, name):
        if name in self.dependency_map:
            print('Task info: ')
            print('* name: ', name)
            print('* dependencies: ')

            for dependency in self.dependency_map[name]:
                print(dependency, '\n')
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

        g = Graph(len(build.tasks))

        for i in range(len(build.tasks)):
            for j in range(len(build.tasks)):
                if build.tasks[j] in self.dependency_map[build.tasks[i]]:
                    g.add_edge(j, i)

        order = g.topological_sort()
        valid = not g.check_for_cycles()

        return order, valid

    def manage_builds(self, debug=False):
        """
        Manages all the builds in builds.yaml and outputs the result in .txt file
        """

        current_builds = self.get_builds
        orig_stdout = sys.stdout

        s = 'test_output.txt' if debug else 'output.txt'
        f = open(s, 'w+')

        sys.stdout = f

        for build in current_builds:
            order, valid = self.manage_build(build)

            if valid:
                task_list = [build.tasks[x] for x in order]
                print('To do in', str(build.name), ': ')
                for task in task_list:
                    print('  ' + task)
                print('\n')
            else:
                print("Invalid build {build}: this build contains cycles \n".format(build = str(build.name)))

        sys.stdout = orig_stdout
        f.close()
