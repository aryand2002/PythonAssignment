import json
import os

class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["description"], data["completed"])


class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, name, description):
        self.tasks.append(Task(name, description))
        self.save_tasks()
        print("Task added.")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks):
            status = "Done" if task.completed else "Pending"
            print(f"{i}. {task.name} - {task.description} [{status}]")


def main():
    app = ToDoApp()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Show All Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            desc = input("Enter task description: ")
            app.add_task(name, desc)

        elif choice == "2":
            app.display_tasks()
            index = int(input("Enter task index to mark as completed: "))
            app.mark_complete(index)

        elif choice == "3":
            app.display_tasks()

        elif choice == "4":
            print("Exiting. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()