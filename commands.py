from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass


class AddCommand(Command):
    def __init__(self, manager):
        self.manager = manager

    def execute(self, args):
        if len(args) < 1:
            print("Usage: add <description>")
            return
        self.manager.add_task(args[0])


class UpdateCommand(Command):
    def __init__(self, manager):
        self.manager = manager

    def execute(self, args):
        if len(args) < 2:
            print("Usage: update <id> <description>")
            return
        self.manager.update_task(int(args[0]), args[1])


class DeleteCommand(Command):
    def __init__(self, manager):
        self.manager = manager

    def execute(self, args):
        if len(args) < 1:
            print("Usage: delete <id>")
            return
        self.manager.delete_task(int(args[0]))


class MarkCommand(Command):
    def __init__(self, manager, status):
        self.manager = manager
        self.status = status

    def execute(self, args):
        if len(args) < 1:
            print(f"Usage: mark-{self.status} <id>")
            return
        self.manager.mark_status(int(args[0]), self.status)


class ListCommand(Command):
    def __init__(self, manager):
        self.manager = manager

    def execute(self, args):
        status = args[0] if args else None
        if status and status not in ['todo', 'in-progress', 'done']:
            print("Invalid status. Use one of: todo, in-progress, done")
            return
        self.manager.list_tasks(status)

