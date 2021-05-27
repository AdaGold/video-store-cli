from menu_options import *

def get_video_choice(rental):
    options = {
        "1": "List all videos", 
        "2": "Create a video",
        "3": "Select a video", 
        "4": "Update selected video", 
        "5": "Delete selected video", 
        "6": "Delete all videos",
        "7": "Back to main menu"
        }
    
    print("\nThese are the actions you can perform: \n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    video_choice = None

    while video_choice not in valid_choices:
        if video_choice != None:
            print("\nInvalid option.")
            video_choice = input("\nMake your selection using valid option number: ")
        else:
            video_choice = input("\nMake your selection using the option number: ")

    if video_choice in ['4','5'] and rental.selected_video == None:
        print("You must select a video before updating it or deleting it.")
        print("Let's select a video!")
        video_choice = "3"
    
    return video_choice

def respond_video_choice(choice, rental, main_menu_choice):
    rental.print_selected_video()
    if choice=='1':
        print_stars()
        print("All videos:")
        for video in rental.list_videos():
            print(video)
    elif choice=='2':
        print("Great! Let's create a new video.")
        title=input("What is the title of your video? ") 
        release_date=input("What is the release date of your video? ")
        total_inventory=input("What is the total inventory of your video? ") 
        response = rental.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("New video:", response)

    elif choice=='3':
        select_by = input("Would you like to select by? Enter title or id: ")
        if select_by=="title":
            title = input("Which video title would you like to select? ")
            rental.get_video(title=title)
        elif select_by=="id":
            id = input("Which video id would you like to select? ")
            if id.isnumeric():
                id = int(id)
                rental.get_video(id=id)
        else:
            print("Could not select. Please enter id or title.")
        
        if rental.selected_video:
            print_stars()
            print("Selected video: ", rental.selected_video)

    elif choice=='4':
        print(f"Great! Let's update the video: {rental.selected_video}")
        title=input("What is the new title of your video? ")
        release_date=input("What is the new release_date of your video? ")
        total_inventory=input("What is the new total_inventory of your video? ")
        response = rental.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("Updated video:", response)
    elif choice=='5':
        rental.delete_video()

        print_stars()
        print("Video has been deleted.")
        print("Current videos:")
        print_stars()
        for video in rental.list_videos():
            print(video)

    elif choice=='6':
        delete_all = input("Are you sure you want to delete all videos? Y/N:  ").lower()
        if delete_all == "y":
            for video in rental.list_videos():
                rental.get_video(id=video['id'])
                rental.delete_video()

            print_stars()
            print("Deleted all videos.")

    else:
        main_menu_choice = get_main_menu_choice()

    print_stars()

    return main_menu_choice