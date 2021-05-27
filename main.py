import video_store


# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
        
def print_stars():
    print("*********************")

def make_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print("What would you like to do? Select 12 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice


def print_main_menu():
    options = {
        "1": "Add a video to inventory", 
        "2": "Edit a video",
        "3": "Delete a video from inventory", 
        "4": "List all videos in the catelog", 
        "5": "Get information on one video",
        "6": "Add a new customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Find a customers information",
        "10": "List all customers",
        "11": "Check-out a video",
        "12": "Check-in a video",
        "13": "Quit"
        }

    print_stars()
    print("WELCOME TO RETRO VIDEO STORE")
    print("These are the options you can choose from")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print_stars()

    return options

def main(play=True):
    options = print_main_menu()
    while play == True:
        choice = make_choice(options)

        if choice=='1':
            print_stars()
            response = creating_video()
            print(f"New Video created! {response}")
        elif choice=='2':
            print_stars()
            response = updating_video()
            print(f"Video updated! {response}")
            
        
                
    return "the end!!"



def creating_video():
    print("Awesome Sauce!! Lets add a new video to our inventory")
    title = input("What is the name of the video? ")
    release_date = input("What is the release_date of the video? ")
    total_inventory = input("What is the starting inventory of the video? ")
    response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
    return response

def updating_video():
    print("Okay!! Lets update a video in our inventory")
    video_id = input("What is the video id? ")
    title = input("What is the name of the video? ")
    release_date = input("What is the release_date of the video in datetime format? ")
    total_inventory = input("What is the starting inventory of the video? ")
    response = video_store.edit_video(title=title, release_date=release_date, total_inventory=total_inventory, video_id=video_id)
    return response

if __name__ == "__main__":
    main()