
# TO-DO LIST APP USING CLASS


class TodoList:

    def __init__(self):
        self.tasks = []

    # Add Task
    def add_task(self):
        task = input("Enter Task: ")
        self.tasks.append({"task": task, "completed": False})
        print("Task Added Successfully!")

    # View Tasks
    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No Tasks Available")
        else:
            print("\n------ TASK LIST ------")
            for i in range(len(self.tasks)):
                if self.tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(i + 1, ".", self.tasks[i]["task"], "-", status)

    # Complete Task
    def complete_task(self):
        if len(self.tasks) == 0:
            print("No Tasks Available")
        else:
            self.view_tasks()
            num = int(input("Enter Task Number: "))

            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1]["completed"] = True
                print("Task Completed!")
            else:
                print("Invalid Task Number")

    # Remove Task
    def remove_task(self):
        if len(self.tasks) == 0:
            print("No Tasks Available")
        else:
            self.view_tasks()
            num = int(input("Enter Task Number to Remove: "))

            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                print("Removed:", removed["task"])
            else:
                print("Invalid Task Number")



# Main Program


todo = TodoList()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        todo.add_task()

    elif choice == "2":
        todo.view_tasks()

    elif choice == "3":
        todo.complete_task()

    elif choice == "4":
        todo.remove_task()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")