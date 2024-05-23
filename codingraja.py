import json
from datetime import datetime

class Task:
    def __init__(self, description, priority='low', due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
    
    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f"[{self.priority}] {self.description} - Due: {self.due_date} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def save_tasks_to_file(self, filename='tasks.json'):
        with open(filename, 'w') as file:
            task_data = [{'description': task.description, 'priority': task.priority, 'due_date': task.due_date, 'completed': task.completed} for task in self.tasks]
            json.dump(task_data, file, indent=4)

    def load_tasks_from_file(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task(**task) for task in task_data]
        except FileNotFoundError:
            pass

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. List tasks")
    print("5. Save and exit")

def get_task_details():
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ").lower()
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    return Task(description, priority, due_date)

def main():
    todo_list = ToDoList()
    todo_list.load_tasks_from_file()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = get_task_details()
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            todo_list.save_tasks_to_file()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
