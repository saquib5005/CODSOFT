# -*- coding: utf-8 -*-
"""To-Do List

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10bOMohDu0g3DrJVOiZFhvDqZstRRF7_N
"""

# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to update a task
def update_task():
    view_tasks()
    task_number = int(input("Enter the task number to update: "))

    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))

    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")