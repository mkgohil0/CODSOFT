# A simple To-Do List application in Python

# List to store the tasks. Each task is a dictionary.
tasks = []

def display_menu():
    """Displays the main menu to the user."""
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("-----------------------")

def add_task():
    """Prompts the user to add a new task to the list."""
    task_description = input("Enter the description of the new task: ")
    task = {
        "description": task_description,
        "completed": False
    }
    tasks.append(task)
    print(f"✅ Task '{task_description}' added successfully!")

def view_tasks():
    """Displays all the tasks currently in the list."""
    print("\n--- YOUR TASKS ---")
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "⬜"
            print(f"{i}. {status} {task['description']}")
    print("------------------")

def mark_task_complete():
    """Marks an existing task as completed."""
    view_tasks()
    if not tasks:
        return # No tasks to mark, so return to menu

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            # Check if the task is already completed
            if tasks[task_num - 1]["completed"]:
                print("⚠️ That task is already marked as complete.")
            else:
                tasks[task_num - 1]["completed"] = True
                print(f"🎉 Task {task_num} marked as complete!")
        else:
            print("❌ Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def delete_task():
    """Deletes a task from the list."""
    view_tasks()
    if not tasks:
        return # No tasks to delete, so return to menu

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"🗑️ Task '{removed_task['description']}' was successfully deleted.")
        else:
            print("❌ Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def main():
    """The main function to run the application loop."""
    print("Welcome to your To-Do List!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye! Keep up the great work! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# Run the application
if __name__ == "__main__":
    main()