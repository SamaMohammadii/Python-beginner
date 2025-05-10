your_todo_list = {}
def add_new_task():
    while True:
        add_task = input("Enter your new task (or 'exit' to finish): ").lower()
        if add_task == "exit":
            break
        your_todo_list.update({add_task: "not done"})

def status():
    for status_of_task in your_todo_list: 
        status_of_task = input("Please enter name of every task is done (or exit to finish): ").lower()
        if status_of_task == "exit": 
            break 
        your_todo_list[status_of_task] = "done" 
        
def show_todo_list():
    for index, (task, status) in enumerate(your_todo_list.items(), start = 1): 
        print(f"{index}. {task} : {status}")

def remove_task():
    while True:
        remove_input = input("Please enter name of task you want to remove (or exit to finish): ").lower()
        if remove_input == "exit": 
            break 
        your_todo_list.pop(remove_input)

while True:
    print("1 = 'Add new task'\n2 = 'Check list'\n3 = 'Show todo list'\n4 = 'Remove task'\nexit = 5")
    user_input = int(input("Enter the number of function: "))
    if user_input == 1: add_new_task()
    elif user_input == 2: status()
    elif user_input == 3: show_todo_list()
    elif user_input == 4: remove_task()
    elif user_input == 5: break
    else: print("Enter a valid input")