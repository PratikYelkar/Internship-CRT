# Command-Line To-Do List Application

This is a simple command-line to-do list application written in Python. It allows users to manage tasks with features such as adding, removing, and marking tasks as completed. Tasks can also have priorities and due dates, and they are stored persistently in a JSON file.

## Features

1. **Task Management**: Add, remove, and mark tasks as completed.
2. **Task Priority**: Assign priority levels to tasks (high, medium, low).
3. **Due Dates**: Set due dates for tasks.
4. **List View**: Display tasks with their details.
5. **Data Persistence**: Store tasks in a JSON file for persistence across sessions.

## Requirements

- Python 3.x


## Usage

To run the application, execute the following command in your terminal:

```sh
python todo.py


File Structure :

1. todo.py: The main application script.
2. tasks.json: The JSON file where tasks are stored. This file is created automatically if it does not exist.

Example

1. Adding a Task

Enter task title: Buy groceries
Enter task priority (high, medium, low): high
Enter due date (YYYY-MM-DD) or leave blank: 2024-07-04


2. Listing Tasks

1. [Pending] Buy groceries (Priority: high, Due: 2024-07-04)


3. Marking a Task as Completed

Enter the task number to mark as completed: 1

4. Removing a Task

Enter the task number to remove: 1



Menu Options

1. Add Task:

Enter task title.
Enter task priority (high, medium, low).
Enter due date (optional, format: YYYY-MM-DD).

2. Remove Task:

List all tasks.
Enter the task number to remove.

3. Mark Task as Completed:

List all tasks.
Enter the task number to mark as completed.

4. List Tasks:

Display all tasks with their details including status, title, priority, and due date.

5. Exit:

Exit the application.
