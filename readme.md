# Task Tracker CLI

A simple, lightweight command-line task tracker application written in Python.  
Manage your tasks efficiently using the terminal — add, update, delete, mark status, and list tasks with ease. Tasks are stored locally in a JSON file.

---

## Features

- Add new tasks with descriptions  
- Update existing tasks  
- Delete tasks by ID  
- Mark tasks as `in-progress` or `done`  
- List all tasks or filter by status (`todo`, `in-progress`, `done`)  
- Human-readable timestamps with "time ago" format  
- Zero external dependencies — pure Python  
- Cross-platform (Linux, macOS, Windows with Python 3)

---

## Installation

### From source

Clone this repository and make the main script executable:

```bash
git clone git@github.com:hasinur1997/task-tracker-cli.git
cd task-tracker-cli
chmod +x task_cli.py

sudo ln -s $(pwd)/task_cli.py /usr/local/bin/task
```

Now you can run the command from anywhere:

```bash
task add "Buy groceries"
task list
```


### Usage Commands

| Command                 | Description                                                   | Example                       |
| ----------------------- | ------------------------------------------------------------- | ----------------------------- |
| `task add`              | Add a new task                                                | `task add "Buy groceries"`    |
| `task update`           | Update an existing task by ID                                 | `task update 1 "Cook dinner"` |
| `task delete`           | Delete a task by ID                                           | `task delete 1`               |
| `task mark-done`        | Mark a task as done by ID                                     | `task mark-done 1`            |
| `task mark-in-progress` | Mark a task as in-progress by ID                              | `task mark-in-progress 2`     |
| `task list`             | List all tasks                                                | `task list`                   |
| `task list <status>`    | List tasks filtered by status (`todo`, `in-progress`, `done`) | `task list done`              |


### Task Properties

 **Each task includes:**

```id: Unique task identifier

description: Task description

status: Task status (todo, in-progress, done)

createdAt: Timestamp when the task was created

updatedAt: Timestamp when the task was last updated
```

### Development

**Prerequisites**
* Python 3.6+

```bash
python3 task_cli.py <command> [args]
```


### Project Structure

```task-tracker-cli/
├── task_cli.py          # Main CLI entry point
├── task_manager.py      # Task management logic
├── commands.py          # CLI command implementations
├── utils.py             # Utility functions (date formatting, etc.)
├── tasks.json           # JSON file storing tasks
└── README.md            # This file
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

