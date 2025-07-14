# todo list 

tasks=[]

while True:
    print("1.Add the task")
    print("2.View the task")
    print("3.mark task as completed")
    print("4.Delet task")
    print("5.Exit")

    choice = input("enter your choice between (1-5):")

    if choice == '1':
        title = input("enter the task")
        task = {"title":title, "done":False}
        tasks.append(task)
        print("Task added")

    elif choice == '2':
        if not tasks:
            print("No task available")
        else:
            print("your task")
            for i, task in enumerate(tasks,start=1):
                status="done" if task["done"] else "Not done"
                print(f"{i} {task['title']}{status}")

    elif choice == '3':
        if not tasks:
            print ("task not available")
        else:
            task_num=int(input("Enter task number to mark as complete"))
            if 1 <= task_num <= len(tasks):
                tasks[task_num -1]["done"]=True
                print("Task mark as completed")
            else:
                print("invalid task")
    elif choice == '4':
        if not tasks:
            print("task not found")
        else:
            task_num= int(input ("enter the task you want to delete"))
            if 1<= task_num <= len(tasks):
                remove=tasks.pop(task_num-1)
                print(f"Task '{remove['title']}' deleted")
            else:
                print("Invalid number")
    elif choice == '5':
        print("Exiting To-Do list. Goode by")
        break
    else:
        print("Invalid choice. Please enter the number betweent 1 to 5.")


     


