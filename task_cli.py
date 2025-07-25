#!/usr/bin/env python3

import sys
from commands import AddCommand, UpdateCommand, DeleteCommand, MarkCommand, ListCommand
from task_manager import TaskManager


def main():
    manager = TaskManager()
    commands = {
        "add": AddCommand(manager),
        "update": UpdateCommand(manager),
        "delete": DeleteCommand(manager),
        "mark-done": MarkCommand(manager, 'done'),
        "mark-in-progress": MarkCommand(manager, 'in-progress'),
        "list": ListCommand(manager),
    }

    if len(sys.argv) < 2:
        print("Please provide a command. Use one of: add, update, delete, mark-done, mark-in-progress, list")
        return

    command_name = sys.argv[1]
    args = sys.argv[2:]

    command = commands.get(command_name)
    if not command:
        print(f"Unknown command: {command_name}")
        return

    try:
        command.execute(args)
    except ValueError:
        print("Invalid input. Task ID must be a number.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    main()
