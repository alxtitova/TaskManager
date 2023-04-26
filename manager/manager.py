#!/usr/bin/env python

from .utils.graph import Graph
from .utils.loader import Loader

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
        self.builds = []
        self.tasks = []

        builds = Loader(builds_file).load_yaml()['builds']
        for build in builds:
            current_build = Build(build['name'])
            self.builds.append(current_build)
            for i in range(len(build['tasks'])):
                current_build.add_task(build['tasks'][i])

        tasks = Loader(tasks_file).load_yaml()['tasks']
        for task in tasks:
            current_task = Task(task['name'])
            self.tasks.append(current_task)
            for i in range(len(task['dependencies'])):
                current_task.add_dependency(task['dependencies'][i])

        self.dependency_map = {}
        self.task_map = {}

        for i, task in enumerate(self.tasks):
            self.dependency_map[task.name] = task.dependencies

        for i, build in enumerate(self.builds):
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
        print('Task info: ')
        print('* name: ', name)
        print('* dependencies: ', ', '.join(self.dependency_map[name]))

    def get_build(self, name):
        print('Build info: ')
        print('* name: ', name)
        print('* tasks: ', ', '.join(self.task_map[name]))

    def manage_build(self, build):
        g = Graph(len(build.tasks))

        for i in range(len(build.tasks)):
            for j in range(len(build.tasks)):
                if build.tasks[j] in self.dependency_map[build.tasks[i]]:
                    g.add_edge(j, i)

        order = g.topological_sort()
        valid = not g.check_for_cycles()

        return order, valid

    def manage_builds(self):
        current_builds = self.builds

        for build in current_builds:
            order, valid = self.manage_build(build)

            if valid:
                order = [build.tasks[x] for x in order]
                print('To do in', str(build.name), ': ', ', '.join(str(x) for x in order))
            else:
                print("Invalid build {build}: this build contains cycles".format(build = str(build.name)))


