import os

# Function to add a task to the to-do list
def add_task(task):
    with open('todo.txt', 'a') as f:
        f.write(task + '\n')

# Function to view all tasks in the to-do list
def view_tasks():
    if os.path.exists('todo.txt'):
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
            if tasks:
                print("To-Do List:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as completed
def complete_task(task_index):
    with open('todo.txt', 'r') as f:
        tasks = f.readlines()
    if len(tasks) >= task_index:
        tasks.pop(task_index - 1)
        with open('todo.txt', 'w') as f:
            for task in tasks:
                f.write(task)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    complete_task(task_index)  # Just reusing complete_task function to remove task

# Main program loop
def main():
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: "))
            delete_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
