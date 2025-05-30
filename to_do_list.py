#Scenario: You are building a to-do list application. Users can add tasks, remove tasks, and
#view all tasks in the list. Additionally, the tasks should be sorted alphabetically when displayed.
#Implement the following functionalities:
#Add a task to the list.
#Remove a task by its name.
#Display the sorted list of tasks.
#Handle edge cases like trying to remove a task that doesn’t exist.


def adding_task(task_add : str, my_tasks: list) -> list:
    """
    Adds task to my_tasks

    Args: task_add (str): the task to be added.
          task_list (list): the list of all tasks.

    Returns: updated the list with new tasks.              
    """
    my_tasks.append(task_add)
    return my_tasks
    
def remv_task(str_remv: str, my_tasks: list) -> list:
    """
    Remove the task from my_tasks.

    Args: str_remv (str): the task to be removed.
          my_tasks (list): the list of all tasks.

    Returns: update the list after removing the specified task 
             from it.         
    """
    if str_remv not in my_tasks:
        print("this task doesnt exist")
        return my_tasks
    else:
        my_tasks.remove(str_remv)
        return my_tasks


def display_tasks(my_tasks: list) ->list:
    """
    Displaying all tasks from my_tasks.

    Args: my_tasks (list): the list of all tasks.

    Returns: None.
    """
    print("The tasks are:")
    for i,task in enumerate(sorted(my_tasks), start = 1):
        print(f"{i}. {task}")


def input_manager(my_tasks: list) ->bool:
    """
    Managing all of the input from the user and performing 
    action on specified input.

    Args: my_tasks (list): the list of all tasks.

    Returns: a bool value to break the while loop outside.
    """
    try:
        choice = int(input("enter the action number: "))
    except ValueError:
        print("Enter valid Input Pls")
        return True
    #the choice section
    if choice == 1:
        input_str = input("enter the task: ")
        adding_task(input_str,my_tasks)
    elif choice == 2:
        remv_str = input("enter the task you want to remove: ")
        remv_task(remv_str,my_tasks)
    elif choice == 3:
        display_tasks(my_tasks)
    elif choice == 4:
        return False
    else:
        print("pls enter valid input command")
    return True       

my_tasks = []
print("To-do App:")
while True:
    print("pls select the following options:")
    print("1. To ADD Task")
    print("2. To Remove Task")
    print("3. Display Task")
    print("4. Exit")

    if not input_manager(my_tasks): 
        break

