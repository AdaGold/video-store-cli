import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "I am an Employee", 
        "2": "I am a Customer",
        "3": "I don't want to be in this program anymore"
        }
    for num in options:
        print(f"Option {num}. {options[num]}")
    # print_stars()
    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        # print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice

def list_employee_options():
    print("Thank you for being a valued member of our team!")
    print("What would you like to do?")
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        "6": "add a customer", 
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "exit this program"
        }
    for num in options:
        print(f"Option {num}. {options[num]}")
    # print_stars()
    return options


def employee_options(play=True):
    employee_option = list_employee_options()
    while play == True:
        employee_choice = make_choice(employee_options, video_store)
        video_store.print_selected()

        if employee_choice == "2":
            for task in task_list.list_tasks():
                print("add later")


        if employee_choice == "13":
            play=False
            print("\nThanks for using the Video Store CLI!")



def customer_options():
    pass




def main(play=True):
    #I wrote URL instead of TaskList. is that right?
    video_store = URL(url="BACKUP_URL")
    print("WELCOME TO RETRO VIDEO STORE")
    print("Please tell us a bit about yourself")
    user_options = list_options()

    while play == True:
        choice = make_choice(user_options, video_store)
        video_store.print_selected()

        if choice == "1":
            employee_options()

        if choice == "2":
            customer_options()

        if choice == "3":
            play=False
            print("\nThanks for using the Video Store CLI!")






    # def run_cli(play=True):

#     #initialize task_list
#     task_list = TaskList(url="https://beccas-task-list-c15.herokuapp.com/")
    
#     # print choices
#     options = list_options()

#     while play==True:

#         # get input and validate
#         choice = make_choice(options, task_list)

#         task_list.print_selected()

#         if choice=='1':
#             print_stars()
#             for task in task_list.list_tasks():
#                 print(task)
#         elif choice=='2':
#             print("Great! Let's create a new task.")
#             title=input("What is the title of your task? ")
#             description=input("What is the description of your task? ")
#             response = task_list.create_task(title=title, description=description)

#             print_stars()
#             print("New task:", response["task"])

#         elif choice=='3':
#             select_by = input("Would you like to select by? Enter title or id: ")
#             if select_by=="title":
#                 title = input("Which task title would you like to select? ")
#                 task_list.get_task(title=title)
#             elif select_by=="id":
#                 id = input("Which task id would you like to select? ")
#                 if id.isnumeric():
#                     id = int(id)
#                     task_list.get_task(id=id)
#             else:
#                 print("Could not select. Please enter id or title.")
            
#             if task_list.selected_task:
#                 print_stars()
#                 print("Selected task: ", task_list.selected_task)

#         elif choice=='4':
#             print(f"Great! Let's update the task: {task_list.selected_task}")
#             title=input("What is the new title of your task? ")
#             description=input("What is the new description of your task? ")
#             response = task_list.update_task(title=title, description=description)

#             print_stars()
#             print("Updated task:", response["task"])
#         elif choice=='5':
#             task_list.delete_task()

#             print_stars()
#             print("Task has been deleted.")

#             print_stars()
#             print(task_list.list_tasks())

#         elif choice=='6':
#             response = task_list.mark_complete()

#             print_stars()
#             print("Completed task: ", response["task"])

#         elif choice=='7':
#             response = task_list.mark_incomplete()

#             print_stars()
#             print("Incomplete task: ", response["task"])

#         elif choice=='8':
#             for task in task_list.list_tasks():
#                 task_list.get_task(id=task['id'])
#                 task_list.delete_task()

#             print_stars()
#             print("Deleted all tasks.")
#         elif choice=='9':
#             list_options()
#         elif choice=='10':
#             play=False
#             print("\nThanks for using the Task List CLI!")

#         print_stars()

# run_cli()

    # for choice_num in options:
    #     print(f"Option {choice_num}. {options[choice_num]}")

    # print_stars()

    # return options


# def make_choice(options, task_list):
#     valid_choices = options.keys()
#     choice = None

#     while choice not in valid_choices:
#         print("What would you like to do? Select 9 to see all options again")
#         choice = input("Make your selection using the option number: ")

#     if choice in ['4','5','6','7'] and task_list.selected_task == None:
#         print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
#         print("Let's select a task!")
#         choice = "3"
    
#     return choice



if __name__ == "__main__":
    main()