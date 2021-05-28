from retro_video import Retro_Video

def print_stars():
    print("\n**************************\n")

def list_options():

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
        "12": "Check in a video from a customer",
        "13": "List videos checked out to a customer",
        "14": "List customers who have checked out a particular video",
        "15": "Lookup videos by title", 
        "16": "List all options",
        "17": "Quit"
        }

    print_stars()
    print("Welcome to the Retro Video CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, retro_video):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13  to see all options again")
        choice = input("Make your selection using the option number: ")
    
    return choice

def run_cli(play=True):

    #initialize retro_video
    #retro_video = Retro_Video(url="http://localhost:5000")
    retro_video = Retro_Video(url="https://retro-video-store-api.herokuapp.com")
    
    # print choices
    options = list_options()

    while play==True:
        print(r'''
   _____  __  __  ____
  |_   _|| (_) | |  __)
    | |  |  _  | |  __)
    |_|  |_( )_| |____)                     _   _
  ________         ________              ``/_\"/_\''
 /        \       (__    __)             /-(o).(o)-\
|     __   |  _____  |  |                \-\_/-\_/-/____,
|    |  )__) /  _  \ |  |                 \-      =  =  =\
|    |   __ |  (_)  ||  |                 /-             -\,
|    |__)  )|       ||  |                (=   |      /-    -\__
|          ||   _   ||  |                 \, _/-    _\-   __|_-\
 \________/ |__( )__||__|                (__(__/___(____/(_____/''')
       
        # get input and validate
        choice = make_choice(options, retro_video)


        if choice=='1':
            print("Great! Let's create a new video.")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video? ")
            total_inventory=input("What is the total inventory of your video? ")
            response = retro_video.create_video(title=title, release_date=release_date,total_inventory=total_inventory)

            print_stars()
            print("New video:", response["id"])


        elif choice=='2':
            print(f"What video would you like to edit? ")
            id=input("What is the id of the video you would like to update? ")
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your video? ")
            total_inventory=input("What is the new total inventory of your video? ")
            response = retro_video.update_video(id=id,title=title, release_date=release_date,total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response["id"])

        elif choice=='3':
            id=input(f"What is the id of the video you would like to delete? ")
            retro_video.delete_video(id)

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(retro_video.list_videos())

          
        elif choice=='4':
            print_stars()
            for video in retro_video.list_videos():
                print(video)

        
            

        elif choice=='5':           
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video = retro_video.get_video(id=id)
            
                print_stars()
                print(video)

        elif choice=='6':
            print("Great! Let's create a new customer.")
            name=input("What is the name of your customer? ")
            postal_code=input("What is the postal code of your customer? ")
            phone=input("What is the phone number for your customer? ")
            response = retro_video.create_customer(name=name, postal_code=postal_code,phone=phone)

            print_stars()
            print("New customer:", response["id"])

        elif choice=='7':
            print(f"What customer would you like to edit? ")
            id=input("What is the id of the customer you would like to update? ")
            name=input("What is the name of your customer? ")
            postal_code=input("What is the postal code of your customer? ")
            phone=input("What is the phone number for your customer? ")
            response = retro_video.update_customer(id=id,name=name, postal_code=postal_code,phone=phone)

            print_stars()
            print("Updated customer", response)


        elif choice=='8':
            id=input(f"What is the id of the customer you would like to delete? ")
            retro_video.delete_customer(id)

            print_stars()
            print("Customer has been deleted.")

            print_stars()
            print(retro_video.list_customers())


        elif choice=='9':           
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer = retro_video.get_customer(id=id)
            
                print_stars()
                print(customer)

           
        elif choice=='10':
            print_stars()
            for customer in retro_video.list_customers():
                print(customer)

        
        elif choice=='11':
            print("Great! Let's check out a video to a customer.")
            video_id=input("What is the video id for the video you would like to check out? ")
            customer_id=input("What is the customer id? ")
            response = retro_video.checkout_video(video_id=video_id,customer_id=customer_id )

            print_stars()
            print("New video checked out to customer:", response)
        
           
        elif choice=='12':
            print("Great! Let's check in a video from a customer.")
            video_id=input("What is the video id for the video you would like to check in? ")
            customer_id=input("What is the customer id? ")
            response = retro_video.checkin_video(video_id=video_id,customer_id=customer_id )

            print_stars()
            print("Video checked in from customer:", response)

          
        elif choice=='13':
            print("Great! Let's list all videos checked out to a customer.")
            customer_id=input("What is the customer id? ")
            response = retro_video.videos_checkedout_by_customer(customer_id=customer_id )

            print_stars()
            print("Video checked out to customer:", response)

        
        elif choice=='14':
            print("Great! Let's list all customers who checked out a video.")
            video_id=input("What is the video id? ")
            response = retro_video.customers_checkedout_by_video(video_id=video_id )

            print_stars()
            print("Customers checked out specific video:", response)


         
        elif choice=='15':
            print("Great! Let's lookup all videos by title.")
            title=input("What is the video title you wish to view? ")
            response = retro_video.list_videos_by_titles(title=title )

            print_stars()
            print("All videos by title:", response)
   
    
        elif choice=='16':
            list_options()
        elif choice=='17':
            play=False
            print("\nThanks for using the Retro Store CLI!")

        print_stars()

run_cli()