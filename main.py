import video_store
import pyfiglet

        
def print_stars():
    print("*********************")

def make_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print("What would you like to do? Select 14 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice


def print_main_menu():
    options = {
        "1": "Add a video to inventory", 
        "2": "Edit a video",
        "3": "Delete a video from inventory", 
        "4": "List all videos in the catalog", 
        "5": "Get information on one video",
        "6": "Add a new customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Find a customers information",
        "10": "List all customers",
        "11": "Check-out a video",
        "12": "Check-in a video",
        "13": "Quit",
        "14": "View options again!"
        }

    print_stars()
    print("These are the options you can choose from:")
    print_stars()
    print_stars()


    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print_stars()
    print_stars()

    return options

def main(play=True):
    welcome_sign = pyfiglet.figlet_format("  WELCOME TO:", font = "bubble" )
    print(welcome_sign)
    store_name = pyfiglet.figlet_format("RETRO VIDEO STORE", font = "5lineoblique" )
    print(store_name)
    options = print_main_menu()

    while play == True:
        choice = make_choice(options)
        if choice=='1':
            print_stars()
            response = creating_video()
            print(f"New Video created! {response}")
            print("\n")
        elif choice=='2':
            print_stars()
            response = updating_video()
            print(f"Video updated! {response}")
            print("\n")
        elif choice == '3':
            print_stars()
            response = delete_video()
            print(f"Video delete! {response}")
            print("\n")
        elif choice == '4':
            print_stars()
            response = list_videos()
            print(f"All the videos: ")
            for video in response:
                print(video)
            print("\n")
        elif choice == '5':
            print_stars()
            response = get_one_video()
            print(f"Video requested!: {response}")
            print("\n")
        elif choice == '6':
            print_stars()
            response = add_new_customer()
            print(f"New Customer Added!: {response}")
            print("\n")
        elif choice == '7':
            print_stars()
            response = update_a_customer()
            print(f"Customer updated! {response}")
            print("\n")
        elif choice == '8':
            print_stars()
            response = delete_a_customer()
            print(f"Customer deleted!! {response}")
            print("\n")
        elif choice == '9':
            print_stars()
            response = get_one_customer()
            print(f"Customer!: {response}")
            print("\n")
        elif choice == '10':
            print_stars()
            response = list_all_customer()
            print(f"All the customers!")
            for custoner in response:
                print(custoner)
            print("\n")
        elif choice == '11':
            print_stars()
            response = checkout_video()
            print(f"Checked out!: {response}")
            print("\n")
        elif choice == '12':
            print_stars()
            response = checkin_video()
            print(f"Checked back in!: {response}")
            print("\n")
        elif choice == '13':
            print_stars()
            print_stars()
            play=False
            # print("\nThanks for coming to the Retro Video Store!")
            Goodbye = pyfiglet.figlet_format("Goodbye!!", font = "slant" )
            print(Goodbye)

        elif choice == '14':
            options = print_main_menu()
        print_stars()
                



def creating_video():
    print("\nAwesome Sauce!! Lets add a new video to our inventory")
    title = input("What is the name of the video? ")
    release_date = input("What is the release_date of the video? ")
    total_inventory = input("What is the starting inventory of the video? ")
    response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
    return response

def updating_video():
    print("\nOkay!! Lets update a video in our inventory")
    video_id = input("What is the video id? ")
    title = input("What is the name of the video? ")
    release_date = input("What is the release_date of the video in datetime format? ")
    total_inventory = input("What is the starting inventory of the video? ")
    response = video_store.edit_video(title=title, release_date=release_date, total_inventory=total_inventory, video_id=video_id)
    return response

def delete_video():
    print("\nSure thing! Let get rid of this rejected video!")
    video_id = input("What is the video id? ")
    response = video_store.delete_video(video_id=video_id)
    return response

def list_videos():
    print("\nAlrighty!! Lets see our inventory!!")
    response = video_store.list_all_videos()
    return response

def get_one_video():
    print("\nInterested in just video? OK!!")
    video_id = input("What is the video id? ")
    response = video_store.get_video(video_id=video_id)
    return response

def add_new_customer():
    print("\nCool!! Lets add a new customer")
    name = input("What is the name of this new customer? ")
    postal_code = input("What is the postal code of this new customer? ")
    phone = input("What is this customers' phone number? ")
    response = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
    return response

def update_a_customer():
    print("\nLet's update this puppy!!")
    customer_id = input("What is the customers' id? ")
    name = input("What is the updated name of this customer? ")
    postal_code = input("What is the updated postal code of this customer? ")
    phone = input("What is this customers' updated phone number? ")
    response = video_store.edit_customer(customer_id=customer_id, name=name, postal_code=postal_code, phone=phone)
    return response

def delete_a_customer():
    print("\nLet's remove this customer!!")
    customer_id = input("What is the customers' id? ")
    response = video_store.delete_customer(customer_id=customer_id)
    return response

def get_one_customer():
    print("\nLet's get just one customer? OK!!")
    customer_id = input("What is the customer id? ")
    response = video_store.get_customer(customer_id=customer_id)
    return response

def list_all_customer():
    print("\nLet's see all the customers!")
    response = video_store.list_customers()
    return response

def checkout_video():
    print("\nWhooyee! You're checking a video out!")
    customer_id = input("What is the customers' id that is checking out the video? ")
    video_id = input("What is the video id of the video being checked out? ")
    response = video_store.checkout(customer_id=customer_id, video_id=video_id)
    return response

def checkin_video():
    print("\nAlrightyyy! I hope you liked the video! Let's check it back in!")
    customer_id = input("What is the customers' id? ")
    video_id = input("What is the video id of the video being checked back in? ")
    response = video_store.checkin(customer_id=customer_id, video_id=video_id)
    return response



if __name__ == "__main__":
    main()