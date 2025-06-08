option = 0
tasks = []
answer_list = [1, 2, 3, 4]
filename = "tasks.txt"

# Load tasks from file if exists
try:
    with open(filename, "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

def add():
    new_task = input("Enter task name to add: ")
    tasks.append(new_task)
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def delete():
    if not tasks:
        print("No tasks to delete.")
        return
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")
    try:
        n = int(input("Enter the task number to delete: "))
        if 0 < n <= len(tasks):
            tasks.pop(n - 1)
            with open(filename, "w") as file:
                for task in tasks:
                    file.write(task + "\n")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

while option != 4:
    try:
        option = int(input("\nEnter Choice\n1. View\n2. Add\n3. Delete\n4. Exit\n> "))
        if option not in answer_list:
            print("Invalid input. Choose 1 to 4.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    if option == 1:
        view()
    elif option == 2:
        add()
    elif option == 3:
        delete()
    elif option == 4:
        print("Exiting... Goodbye!")
