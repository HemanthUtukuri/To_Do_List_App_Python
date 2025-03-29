print("\U0001F4CC\U0001F4CC TO DO LIST APP \U0001F4CC\U0001F4CC")
user_name = input("Let us know about you: ")
print(f"Hello, {user_name}\U0001F60A! Let's start your day by adding tasks")

def show_menu():
    print("-----------------------------------------------------------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark as done")
    print("4. Delete tasks")
    print("5. Exit")
    print("-----------------------------------------------------------")

while True:
    show_menu()
    try:
        choice = int(input("What do you want to do? "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Processing \U0001F680. Okay, see you later!")
        break

    elif choice == 1:
        try:
            n = int(input("Enter the number of tasks you want to add: "))
            with open("task.txt", "a") as file:
                for i in range(n):
                    line = input(f"Enter your task {i+1}: ")
                    file.write(line + "\n")
            print("Tasks added successfully!\U0001F44D")
        except :
            print("Invalid input! Please enter a valid number.")

    elif choice == 2:
        try:
            with open("task.txt", "r") as f:
                lines = f.readlines()
            if not lines:
                print("No tasks found!")
            else:
                print("Your tasks:")
                for line in lines:
                    print(f"- {line.strip()}")
        except FileNotFoundError:
            print("No tasks found!")

    elif choice == 3:
        try:
            with open("task.txt", "r") as f:
                tasks = f.readlines()
            
            if not tasks:
                print("No tasks to mark as done!")
                continue
            
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

            task_no = int(input("Enter the task number to mark as done: "))

            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1] = tasks[task_no - 1].strip() + " \u2705\n"
                with open("task.txt", "w") as f:
                    f.writelines(tasks)
                print("\u2705 Task marked as done!")
            else:
                print("Invalid task number!")
        except (FileNotFoundError, ValueError):
            print("Error occurred! Make sure tasks are available and input is correct.")
    
    elif choice == 4:
        with open("task.txt", "w") as f:
            pass
        print("I refreshed everything for you, boss \U0001F44D")
    
    else:
        print("You entered a wrong number, check again.")

            
        
            

        
    

    
            
        
        
        


