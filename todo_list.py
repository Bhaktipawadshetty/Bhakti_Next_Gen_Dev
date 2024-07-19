class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print(f"Task {task_number} marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(task_number)
        elif choice == '5':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
