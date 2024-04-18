# Description: A command-line todo list application where users can add tasks, mark them as complete, and view their tasks list.
# Skills Required: Lists, loops, user input handling, basic file I/O


# Check if task file exists
import os.path
path = './tasklist.txt'
if os.path.isfile(path):
    print("Tasklist file already exists. Opening Tasklist.\n")
else:
    print("Tasklist file does not exist. Will create a new one.\n")
    file = open('tasklist.txt','w')
    file.close()

# Add task function
def add_task():
    print("What task would you like to add to the list?")
    task = input()
    task_str = task + "\n"
    file = open('tasklist.txt', 'a')
    file.write(task_str)
    print("Task added.")
    file.close()

# Mark tasks complete function
def mark_complete():
    print("What task would you like to mark complete?")
    task = input()
    file = open('tasklist.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('tasklist.txt', 'w')
    for line in lines:
        if line.strip("\n") != task:
            file.write(line)
    file.close()
    print("Task completed.")

# View list function
def view_list():
    file = open('tasklist.txt','r+')
    print(file.read())
    file.close()

def tasklist():
    want = input()
    if want.lower() == "add tasks":
        add_task()
    elif want.lower() == "mark tasks complete":
        mark_complete()
    elif want.lower() == "view task list":
        view_list()

# Ask user what they wish to do
print("What would you like to do? Add tasks, mark tasks complete, or view task list?")
tasklist()

print("Would you like to do more with the tasklist? y/n")
again = input()
while again == "y":
    print("Enter what you would like to do: add tasks, mark tasks complete, view task list")
    tasklist()
    print("Again?")
    again = input()
print("Thank you!")