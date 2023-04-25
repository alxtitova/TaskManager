"""
The command-line interface for the task manager
"""
import argparse
from manager import Manager

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

    parser_manage = subparsers.add_parser('manage', help='rearrange tasks in every build in the proper order and print the result')

    args = parser.parse_args()

    mymanager = Manager('../input/builds.yaml', '../input/tasks.yaml')

    if args.command == 'list':
        if args.list_type == 'builds':
            mymanager.list_builds()

        if args.list_type == 'tasks':
            mymanager.list_tasks()

    if args.command == 'get':
        if args.get_type == 'build':
            mymanager.get_build(args.name)

        if args.get_type == 'task':
            mymanager.get_task(args.name)

    if args.command == 'manage':
        mymanager.manage_builds()

if __name__ == "__main__":
    main()