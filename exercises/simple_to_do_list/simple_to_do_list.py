file_path = r"C:\Users\bkozi\Desktop\Nauka\PYTHON BARTEK\exercises\simple_to_do_list\tasks.txt"

def add_task():
    task_to_add = input("Enter task you want to add: ")
    with open(file_path, 'a') as file:
        file.write(task_to_add + "\n")

def display_tasks():
    with open(file_path, 'r') as file:
        lines = file.readlines()

        if not lines:
            print("Your to-do list is empty")
            return
        
        for index, line in enumerate(lines, 1):
            print(f"{index}. {line}")

def delete_task():
    display_tasks()

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            if not lines:
                return
            
            user_choice = input("\n Enter the task number to be deleted (q to quit): ")

            if user_choice.lower() == "q":
                return
            
            if user_choice.isdigit():
                index = int(user_choice)

                if 1 <= index <= len(lines):
                    deleted_task = lines.pop(index-1)

                    with open(file_path, 'w') as file:
                        file.writelines(lines)

                        print(f"✅ Task {delete_task} deleted successfully")
                else:
                    print("❌ Invalid task number.")
            else:
                print("❌ Please enter a valid number")
    except FileNotFoundError:
        print("Your to-do list is empty")


def main():
    
    while True:

        print(" --- TO-DO LIST --- ")
        print("""
        (1) Add new task
        (2) Display tasks
        (3) Delete task
        (q) To quit
    """)
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "1":
            add_task()
        elif user_choice == "2":
            display_tasks()
        elif user_choice == "3":
            delete_task()
        elif user_choice == "q":
            print("Godbyee!")
            break
        else:
            print("Invalid input")
    

main()