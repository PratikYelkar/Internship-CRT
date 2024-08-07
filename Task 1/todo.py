import json
from datetime import datetime

class Task:
    def __init__(self, title, priority="low", due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            title=task_dict["title"],
            priority=task_dict["priority"],
            due_date=task_dict["due_date"],
            completed=task_dict["completed"],
        )

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, priority="low", due_date=None):
        self.tasks.append(Task(title, priority, due_date))
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            due_date = task.due_date if task.due_date else "No due date"
            print(f"{idx+1}. [{status}] {task.title} (Priority: {task.priority}, Due: {due_date})")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ").lower()
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            try:
                if due_date:
                    datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
                else:
                    due_date = None
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                continue
            todo_list.add_task(title, priority, due_date)
        elif choice == "2":
            todo_list.list_tasks()
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
            except IndexError:
                print("Task number out of range. Please enter a valid task number.")
        elif choice == "3":
            todo_list.list_tasks()
            try:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
            except IndexError:
                print("Task number out of range. Please enter a valid task number.")
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
