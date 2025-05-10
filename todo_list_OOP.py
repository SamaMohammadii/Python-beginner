class TodoList:
    def __init__(self):
        self.tasks = []    
            
    def add_task(self, task):
            self.tasks.append({"task": task, "status": "not done"})
    
    def show_todo_list(self):
        if not self.tasks:
            print("No tasks yet.")
        for index, item in enumerate(self.tasks, 1): 
            print(f"{index}. {item['task']} : {item['status']}")

    def check_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "done"
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"removed task: {removed["task"]}")
        else:
            print("Invalid task number.")

    def menu(self):
        while True:
            print("1= Add new task\n2= Check task\n3= Show todo list\n4= Remove task\n5= exit")
            try:
                user_input = int(input("Enter yout choice: "))
                if user_input == 1:
                    add_task = input("Enter your new task: ").lower()
                    self.add_task(add_task)
                elif user_input == 2:
                    self.show_todo_list()
                    index = int(input("Please enter task number to mark as done: ")) - 1
                    self.check_task(index)
                elif user_input == 3:
                    self.show_todo_list()
                elif user_input == 4: 
                    self.show_todo_list()
                    index = int(input("Please enter task number you want to remove: ")) - 1
                    self.remove_task(index)
                elif user_input == 5: 
                    print("Have a good time!") 
                    break
                else: print("Enter a valid input.")
            except ValueError:
                print("Please enter a number.")
todo_list = TodoList()
todo_list.menu()


 

    
