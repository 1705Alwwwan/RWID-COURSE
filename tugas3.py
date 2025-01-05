class Task:
    def __init__(self, description, completed=False) ->None:
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        status ="Done" if self.completed else "Not Done"
        return f"{self.description} {status}" 
    
class ToDoList:
    def __init__(self) ->None:
        self.tasks = []

    def add_task(self, description): 
        task = Task(description)
        self.tasks.append(task)
    
    def remove_task(self, index): 
        if 0 <= index < len(self.tasks):
            del self.tasks[index] 

    def mask_task_as_completed(self, index):
        if 0<= index < len(self.tasks):
            self.tasks[index].completed = True 

    def display_tasks(self):
        for index, Task in enumerate(self.tasks):
            print(f'{index}. {Task}') 

def main():
    todo_list = ToDoList()
    while True: 
        print ("\n============Print-To-Do-List=================")
        
        todo_list.display_tasks()

        print("\nOptions")
        print ("1. Add Tasks")
        print ("2. Remove Tasks")
        print ("3. Mark A Tasks As Completed")
        print ("4. Quit")

        choice = input("Enter your options : ")

        if choice == "1":
            desc = input("Enter the descriptions : ")
            todo_list.add_task(desc)

        elif choice == "2":
            index = int(input("Enter the index that you want to erase : "))
            todo_list.remove_task(index)

        elif choice == '3':
            index = int(input("Enter the index that you want to remove: "))
            todo_list.mask_task_as_completed(index) 

            
        
        elif choice == "4":
            print ("Thanks for use this app")
            print ("closing this app")
            break
            
        else:
            print ("your choice invalid. Please, choose the valid choice !")

if __name__ == "__main__":
    main()


