# The List Which Will Store All Tasks
all_tasks  = []
tasks_in_progress = []
tasks_done = []


# Adding An element to the list
def add (element):
    all_tasks.append(element)
    tasks_in_progress.append(element)
    print(f"The Task \"{element}\" Is Added")
    print(f"Your Tasks_List => {all_tasks}")
    print(f"Your Tasks In Progress => {tasks_in_progress}")



# Deleting An Element From The List
def delete (element):
    if element not in tasks_in_progress:
        print("This Element is Invalid")

    else:
        all_tasks.remove(element)
        tasks_in_progress.remove(element)
        print("The Task Is Deleted")
        print(f"Your Tasks_List => {all_tasks}")
        print(f"Your Tasks In Progress => {tasks_in_progress}")



# Updating An Element In The List
def update (removed_element , added_element):
    if removed_element not in tasks_in_progress:
        print("This Element is Invalid")

    
    else:
        all_tasks.remove(removed_element)
        tasks_in_progress.remove(removed_element)

        all_tasks.append(added_element)
        tasks_in_progress.append(added_element)
        print(f"The Element \"{removed_element}\" Is Removed And The Element \"{added_element}\" Is Added")

        print(f"Your Tasks_List => {all_tasks}")
        print(f"Your Tasks In Progress => {tasks_in_progress}")



# Done Tasks
def done (element):
    if element not in tasks_in_progress:
        print("This Element is Invalid")
        
    else:
        tasks_done.append(element)
        tasks_in_progress.remove(element)
        print(f"Your Task \"{element}\" Has done")
        print(f"Your Tasks in Progress is {tasks_in_progress}")







while True:
    print("\nChoose Your Operation")
    print("""
            1 => Add
            2 => Update
            3 => Delete
            4 => Mark Task As A Done_Task
            5 => exit    """)
    choice = input("Enter The Number Of Operation: ").strip()





    if choice == "1":
        task = input("Enter Your Task: ").strip().capitalize()
        add(task)




    elif choice == "2":
        if bool(tasks_in_progress) == False :
            print("There is no tasks to update it")
        else:
            removed_task = input("Enter Removed_Task: ").strip().capitalize()
            added_task = input("Enter Added_Task: ").strip().capitalize()
            update(removed_task,added_task)
    


    elif choice == "3":
        if bool(tasks_in_progress) == False :
            print("There is no tasks to remove it")
        else:
            removed_element = input("Enter The Removed_Task: ").strip().capitalize()
            delete(removed_element)



    elif choice == "4":
        if bool(tasks_in_progress) == False:
            print("There is no tasks to make it done ")
        else:    
            done_task = input("Enter The Task Has Done: ").strip().capitalize()
            done(done_task)


    elif choice == "5":
        break





    else:
        print("Your Choice Is Invalid , Please Try Again")
        continue
    
