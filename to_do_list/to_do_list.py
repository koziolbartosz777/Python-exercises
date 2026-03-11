import json 
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "to_do_list.json")

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}
    
def save_taks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("Failed to save")
    

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_taks(tasks)
        print("Taks added")
        

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index+1}. {task['description']} | {status}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: ").strip())
        task_list = tasks["tasks"]

        if 1<=task_number<=len(task_list):
            removed_task = task_list.pop(task_number-1)
            save_taks(tasks)    
            print(f"Task {removed_task['description']} deleted")
        else: 
            print("Invalid task number")
    except:
        print("Enter a valid number")


def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1<=task_number<=len(tasks["tasks"]):
            tasks["tasks"][task_number-1]["complete"] = True
            save_taks(tasks)
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")


def main():
    tasks = load_tasks()

    while True:
        print("\n --- To-Do List Manager ---")
        print("1. Display Tasks")
        print("2. Add Taks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye")
            break
        else:
            print("Invalid choice. Please try again.")

main()