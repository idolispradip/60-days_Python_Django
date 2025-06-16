# List : A list is a collection of items , stored in a single varibale.
# List are:
# 1. Ordered: (items have a defined order)
# 2. changeable: (you can add, remove, or modify items)
# 3.can hold different data types 

# How to create a list
# steps:
# 1. Use square brackets []
# 2. Separate items with commas
# example:
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# To-do- list app simple console program 
# features:
# 1. Add a task
# 2.Remove a task
# 3.view all tasks
# 4. Exit the program 

# Initialize an empty list to store tasks
tasks = []
# Function to add a task
def add_task():
    task= input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your to-do list.")
# function to remove a task 
def remove_task():
    view_tasks()
    tasks_to_remove = input("Enter the task you want to remove: ")
    if tasks_to_remove in tasks:
        tasks.remove(tasks_to_remove)
        print(f"Task '{tasks_to_remove}' has been removed from your to-do list.")
    else:
        print(f"Task not found in the list.")
# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for task in tasks:
            print(f"-{task}")
        print()
# Main program loop
while True:
        print("=======To-Do List App=======")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        