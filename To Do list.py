tasks = []
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    show_tasks()
    if tasks:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed")
        else:
            print("Invalid task number.")
    else:
        print("No tassks to remove.")

def main():
    while True:
        print("\nTo-Do List Menu:")  
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")   

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Existing...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()                    

