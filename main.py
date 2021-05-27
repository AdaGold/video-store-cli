import requests

from video_store_API_stuff import Customer, Video, Rental


URL = "http://127.0.0.1:5000"
# URL = "http://localhost:5000" 

BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass

if __name__ == "__main__":
    main()

def print_frogges():

    print("\n🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 \n")


def list_options():
    """
    input: none
    output: presents a list of options the end-user can choose from 
    """

    options = {
        "1": "List all videos",
        "2": "Add a video", 
        "3": "Select a video",
        "4": "Edit selected video",
        "5": "Delete selected video", 
        "6": "List all customers",
        "7": "Add a customer",
        "8": "Select a customer",
        "9": "Update a customer",
        "10": "Delete a customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video to a customer",
        "13": "List all options",
        "14": "Quit"
        }

    print_frogges()
    print("These are the actions you can perform:")
    print_frogges()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_frogges()

    return options



def make_choice(options, customer, video):
    """
    input: the list of options from list_options()
    output: 
    """
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again, OR\n")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5'] and video.selected_video == None:
        print("You must select a video before updating it or deleting it.")
        print("Let's select a video!")
        choice = "3"

    if choice in ['9', '10'] and customer.selected_customer == None:
        print("You must select a customer record before updating it or deleting it.")
        print("Let's select a customer!")
        choice = "8"
    
    return choice
    


def run_cli(play=True):
    """
    input
    output
    """

    # initialize lists using the models made in the other .py file

    # task_list = TaskList(url="https://beccas-task-list-c15.herokuapp.com/")

    customer_list = Customer()

    video_list = Video()
    
    # ? = Rental()

    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, customer_list, video_list)

        customer_list.print_selected_customer()
        video_list.print_selected_video()

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
            pass

        elif choice=='14':
            play=False
            print("\nThanks for using the FROGGE VIDEO STORE CLI")

        print_frogges()

run_cli()
