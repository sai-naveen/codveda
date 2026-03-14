import json

file_name = "tasks.json"

# Load tasks from file
try:
    with open(file_name, "r") as file:
        tasks = json.load(file)
except:
    tasks = []

# Save tasks to file
def save_tasks():
    with open(file_name, "w") as file:
        json.dump(tasks, file)

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add")
    print("2. List")
    print("3. Mark")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        n = input("Enter the task: ")
        tasks.append({"task": n, "done": False})
        save_tasks()
        print("Task added successfully!")

    # List tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                status = "Done" if t["done"] else "Not Done"
                print(i+1, "-", t["task"], "-", status)

    # Mark task as done
    elif choice == "3":
        num = int(input("Enter the task: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid task number")

    # Delete task
    elif choice == "4":
        num = int(input("Enter the task: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task number")

    # Exit
    elif choice == "5":
        print("Program closed")
        break

    else:
        print("Invalid choice")