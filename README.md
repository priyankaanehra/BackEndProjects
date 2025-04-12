# Task Manager CLI

This is a simple command-line interface (CLI) task manager built in Python. It allows users to manage tasks by performing operations such as adding, updating, marking, listing, and deleting tasks. Task data is stored in a local tasks.json file.

Features
-Add a new task: Create a new task with a description.
-Update a task: Modify the description of an existing task.
-Mark a task: Update the status of a task (e.g., done, not_done, in_progress).
-List tasks: View all tasks, optionally filtered by status.
-Delete a task: Remove a task from the list by its ID.

Requirements
-Python 3.7 or higher
-No additional external libraries are required. The script uses built-in Python modules: json, os, argparse, and datetime.
-To make the script executable, you need to grant it execution permissions: chmod +x taskcli.py

Running the CLI commands
The script uses argparse for parsing command-line arguments. Below are the available commands:
1. Add a new task to the task list: ./taskcli.py add "Buy groceries"
2. Update the description of an existing task by its ID: ./taskcli.py update 1 "Buy groceries and clean the house"
3. Change the status of a task. Available status options: done, not_done, or in_progress: ./taskcli.py mark 1 "done"
4. List all tasks: ./taskcli.py list
5. List all tasks filter by status (done, not_done, in_progress): ./taskcli.py list done
6. Delete a task by its ID: ./taskcli.py delete 1

Data Storage
Task data is stored in a JSON file (tasks.json). Each task is represented by a dictionary with the following fields:
id: A unique identifier for the task.
description: The name or description of the task.
status: The current status of the task (not_done, in_progress, done).
createdAt: The date when the task was created.
updatedAt: The date when the task was last updated.

Example tasks.json file:
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "not_done",
    "createdAt": "2025-04-10",
    "updatedAt": "2025-04-10"
  },
  {
    "id": 2,
    "description": "Clean the house",
    "status": "in_progress",
    "createdAt": "2025-04-11",
    "updatedAt": "2025-04-11"
  }
]
