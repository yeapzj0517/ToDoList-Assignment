tasks = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter task name: ")
        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append([task, "Pending"])
            print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task[0]} - {task[1]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            try:
                num = int(input("Enter task number to complete: "))
                if num < 1 or num > len(tasks):
                    print("Invalid task number.")
                else:
                    tasks[num - 1][1] = "Completed"
                    print("Task marked as completed.")
            except:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if num < 1 or num > len(tasks):
                    print("Invalid task number.")
                else:
                    tasks.pop(num - 1)
                    print("Task deleted successfully.")
            except:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye! Program ended.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
