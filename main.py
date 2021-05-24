import requests
from video_operations import VideoOperations
from customer_operations import CustomerOperations
from rental_operations import RentalOperations


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():
    
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video", 
        "4": "get information about all videos", 
        "5": "get information about one video", 
        "6": "add a customer",
        "7": "edit a customer",
        "8": "Delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer"
        }
    
def main():
    print("WELCOME TO RETRO VIDEO STORE")
    
    #initialize video_operations
    video_operations = VideoOperations(BACKUP_URL)
    customer_operations = CustomerOperations(BACKUP_URL)
    rental_operations = RentalOperations(BACKUP_URL)
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_operations, customer_operations, rental_operations)

        video_operations.print_selected()
        customer_operations.print_selected()
        rental_operations.print_selected()

        if choice=='1':
            
            print_stars()
            print("Hi, let's add a video to the library")
            title=input("What is the title of your video? ")
            release_date=input("please provide the release date of your video")
            total_inventory=input("how many of these videos would you like to add to the total inventory?")
            response = video_operations.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video:", response["video"])
            
        elif choice=='2':
            print(f"Great! Let's update the task: {video_operations.selected_video}")
            
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your task? ")
            total_inventory=input("What is the new total inventory of this video?")
            
            response = video_operations.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response["video"])

        elif choice=='3':
            video_operations.delete_video()
            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video_operations.get_all_video_information())
        
        elif choice=='4':
            print_stars()
            for video in video_operations.get_all_video_information():
                print(video)
            
        elif choice=='5':
            select_by = input("Would you like to select by? Enter title or video id: ")
            if select_by=="title":
                title = input("Which video title would you like to select? ")
                video_operations.get_one_video_info(title=title)
                
            elif select_by=="video_id":
                video_id = input("Which video id would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_operations.get_one_video_info(video_id=video_id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_operations.selected_video:
                print_stars()
                print("Selected video: ", video_operations.selected_video)

        
            
    

        # elif choice=='6':
        #     response = task_list.mark_complete()

        #     print_stars()
        #     print("Completed task: ", response["task"])

        # elif choice=='7':
        #     response = task_list.mark_incomplete()

        #     print_stars()
        #     print("Incomplete task: ", response["task"])

        # elif choice=='8':
        #     for task in task_list.list_tasks():
        #         task_list.get_task(id=task['id'])
        #         task_list.delete_task()

        #     #print_stars()
        #     print("Deleted all tasks.")
        elif choice=='13':
            list_options()
        elif choice=='14':
            play=False
            print("\nThanks for using the video store CLI!")

        #print_stars()
def make_choice(options, task_list):
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



    print_stars()
    print("Welcome to the Task List CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options



if __name__ == "__main__":
    main()