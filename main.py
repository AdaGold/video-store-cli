import requests

# import models n stuff


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass

if __name__ == "__main__":
    main()

def print_frogges():
    print("\n🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸\n")


def list_options():
    """
    input: none
    output: presents a list of options the end-user can choose from 
    """

    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "Get information about all videos", 
        "5": "Get information about one video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information about one customer",
        "10": "Get information about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video to a customer",
        "13": "Quit"
        }

    print_frogges()
    print("These are the actions you can perform")
    print_frogges()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_frogges()

    return options



def make_choice(options, task_list):
    """
    input
    output
    """
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5','6','7'] and task_list.selected_task == None:
        print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
        print("Let's select a task!")
        choice = "3"
    
    return choice


def run_cli(play=True):
    """
    input
    output
    """

    #initialize task_list
    task_list = TaskList(url="https://beccas-task-list-c15.herokuapp.com/")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, task_list)

        task_list.print_selected()

        if choice=='1':
            pass

        elif choice=='2':
            pass

        elif choice=='3':
            pass

        elif choice=='4':
            pass
            
        elif choice=='5':
            pass

        elif choice=='6':
            pass

        elif choice=='7':
            pass

        elif choice=='8':
            pass

        elif choice=='9':
            pass

        elif choice=='10':
            pass

        elif choice=='11':
            pass

        elif choice=='12':
            pass

        elif choice=='13':
            play=False
            print("\nThanks for using the Task List CLI!")

        print_frogges()

run_cli()
