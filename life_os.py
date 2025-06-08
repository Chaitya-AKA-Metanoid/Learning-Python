option = 0 
tasks =[]
answer_list = [1,2,3,4]

def add():
    new_task = str(input("Enter task name to enter"))
    tasks.append(new_task)

def delete():
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")
    n = int(input("Enter the task number to delete: "))
    if 0 < n <= len(tasks):
        tasks.pop(n - 1)

while option !=4:
    option = int(input("Enter Choice \n 1.View \n 2.Add \n 3.Delete \n 4.Exit"))

    try:
        option = int(input("\nEnter Choice\n1. View\n2. Add\n3. Delete\n4. Exit\n> "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    if option not in answer_list:
        print("Invalid Input")

    if option == 1:
       #View Task 
       print(tasks)
        
    elif option == 2:
        #add task
        add()
             
    elif option == 3:
        pass#delete task
        delete()
            
    elif option == 4:
        pass#exit 

