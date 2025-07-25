import os
import json
from datetime import datetime, timedelta
from utils import format_datetime, time_ago

TASK_FILE = 'tasks.json'


class Task:
    def __init__(self, task_id, description, status='todo', created_at=None, updated_at=None):
        now = datetime.now().isoformat()
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = created_at or now
        self.updatedAt = updated_at or now

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data['id'],
            data['description'],
            data['status'],
            data['createdAt'],
            data['updatedAt']
        )


# ---------- Task Manager ----------

class TaskManager:
    def __init__(self, file_path=TASK_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            return [Task.from_dict(t) for t in json.load(file)]

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=2)

    def get_new_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def find_task(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def add_task(self, description):
        task_id = self.get_new_id()
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id, new_description):
        task = self.find_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task.description = new_description
        task.updatedAt = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {task_id} updated.")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted.")

    def mark_status(self, task_id, status):
        task = self.find_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        task.status = status
        task.updatedAt = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {task_id} marked as {status}.")

    def list_tasks(self, status=None):
        tasks = self.tasks
        if status:
            tasks = [t for t in tasks if t.status == status]

        if not tasks:
            print("No tasks found.")
            return

        print("\nID  Description".ljust(40) + "Status".ljust(15) + "Created At".ljust(25) + "Updated")
        print("-" * 100)
        for t in sorted(tasks, key=lambda t: t.id):
            print(
                f"{str(t.id).ljust(3)} "
                f"{t.description.ljust(35)} "
                f"{t.status.ljust(12)} "
                f"{format_datetime(t.createdAt).ljust(24)} "
                f"{time_ago(t.updatedAt)}"
            )
