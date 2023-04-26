#!/usr/bin/env python

"""
Command-Line Interface for the task manager
"""

import argparse
import os

from taskmanager.manager.manager import Manager
from taskmanager.tests.tests import Debug

def main():
    parser = argparse.ArgumentParser(
        description="A simple task manager with dependency resolution"
    )

    subparsers = parser.add_subparsers(dest='command', help='command to execute')

    parser_list = subparsers.add_parser('list', help='{builds, tasks} print titles of all the items in the specified list')
    parser_list.add_argument('list_type', type=str, nargs='?')

    parser_get = subparsers.add_parser('get', help='{build, task} print an item by name (with dependencies set in order)')
    parser_get.add_argument('get_type', type=str, nargs='?')
    parser_get.add_argument('name', type=str, nargs='?')

    subparsers.add_parser('manage', help='rearrange tasks in every build in the proper order and print the result')

    subparsers.add_parser('test', help='run builtin tests')

    args = parser.parse_args()

    if args.command == 'test':
        debug = Debug()
        debug.run()
    else:
        if os.path.isfile('builds.yaml') and os.path.isfile('tasks.yaml'):
            mymanager = Manager('builds.yaml', 'tasks.yaml')
        else:
            print('No input files')
            exit(0)

        if args.command == 'list':
            if args.list_type == 'builds':
                print('Current builds: ')
                mymanager.list_builds()

            if args.list_type == 'tasks':
                print('Current tasks: ')
                mymanager.list_tasks()

        if args.command == 'get':
            if args.get_type == 'build':
                mymanager.get_build(args.name)

            if args.get_type == 'task':
                mymanager.get_task(args.name)

        if args.command == 'manage':
            print('Successfully managed builds in build.yaml. Open output.txt to see the result.')
            mymanager.manage_builds()

if __name__ == "__main__":
    main()