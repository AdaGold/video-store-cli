from client import Client
from constants import *

#MAITES_URL = "https://maite-retro-video-store-api.heroku.com"


def main():
    print("******* ******* ******* ******* ******* ******* *******")


def pzzas():
    print("\n************************************************\n")

pzzas()
pzzas()

print(WELCOME)

def option_list():

    options = {
        "1": "Add a video", 
        "2": "Get information about all videos",
        "3": "Select one video", 
        "4": "Edit a video", 
        "5": "Delete a video",

        "6": "Add a customer",
        "7": "Get information on all customers",
        "8": "Select one customer", 
        "9": "Edit a customer", 
        "10": "Delete a customer", 
        
        "11": "Check out a video to a customer", 
        "12": "Check in a video from a customer", 
        "14": "To see all options",
        "15": "To Quit"
        }

    pzzas()
    print(OPTIONS)
    pzzas()

    for option in options:
        print(f"What would you like to do? Option {option} will {options[option]}.")
        print()

    pzzas()
    pzzas()

    return options
    

def choose_option(options):# 
    valid_options = options.keys()
    option = None 

    while option not in valid_options:
        print("Would you like to see all the options again? If so please input 14.\nOtherwise, 15 to Quit")
        print()
        option = input("Please input your choice using numbers:   ")
    
    return option


def run_cli(play=True):
    #initializes the store
    client = Client(url="http://127.0.0.1:5000")
    
    options = option_list()

    selected_video = None
    selected_customer = None
    
    while play == True: 
        option = choose_option(options)
        

        if option=='1': # Add video
            print("Great!") 
            title=input("What is the title of the movie?  ")
            release_date=input("In yyyy-mm-dd format. When was this movie released?  ")
            total_inventory=input("How many copies of this movie are there?  ")
            video = client.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            pzzas()
            print("New video:", video.title)
            


        elif option=='2':  # Info on all videos
            pzzas()
            for video in client.info_about_all_videos():
                print(video) 
            

        elif option=='3': # select the video 
            choose_by = input("Would you like to select by title or id?:  ")
            if choose_by=="title":
                title = input("Which movie title would you like to select?  ")
                selected_video = client.info_about_one_video(title=title)
            elif choose_by=="id":
                id = input("Which movie id would you like to select?  ")
                if id.isnumeric():
                    id = int(id)
                    selected_video = client.info_about_one_video(id=id)

            if selected_video:
                pzzas()
                print("Selected video: ", selected_video.title)
                print("Total inventory:", selected_video.total_inventory)
                print("Release date:", selected_video.release_date) 
            else:
                print("Sorry, we couldn't find a matching video.")
            pzzas()
        


        elif option=='4':  # edit a video
            if not selected_video:
                print("Please select a video")
                continue
            
            print(f"Great! Let's update video: {selected_video}") 
            pzzas()
            title=input(f"What is updated the title of the movie?[{selected_video.title}]  ")
            if len(title) > 0:
                selected_video.title = title
            release_date=input(f"In yyyy-mm-dd format. What is the updated movie released?[{selected_video.release_date}]  ")
            if len(release_date) > 0:
                selected_video.release_date = release_date
            total_inventory=input(f"How many copies of this movie are there now?[{selected_video.total_inventory}]  ")
            if len(total_inventory) > 0:
                selected_video.total_inventory = total_inventory
            selected_video.save()
            pzzas()
            print("Updated video:", selected_video)
            pzzas()


        elif option=='5': # delete video
            if not selected_video:
                print("Please select a video")
                continue

            check = input(f"Are you sure you want to delete {selected_video} yes/no?  ")
            if check == 'yes':
                selected_video.delete()
                pzzas()
                print("Video has been deleted.")
                pzzas()
                selected_video = None
            else:
                continue

            
        elif option=='6':  # creates customer
            print("Awesome!") 
            name=input("What is the customer's name?  ")
            postal_code=input("What is the customer's zip code?  ")
            phone=input("Including area code. What's the customer's phone number?  ")
            customer = client.add_customer(name=name, postal_code=postal_code, phone=phone)
            pzzas()
            print("New customer:", customer.name)
            


        elif option=='7':  # Info on all customers
            pzzas()
            for customer in client.info_about_all_customers():
                print(customer) 


        elif option=='8':   # Selects customer
            choose_by = input("Would you like to select a customer by name or id?  ")
            if choose_by == "name":
                name = input("Which customer name would you like to select?  ")
                selected_customer = client.info_about_one_customer(name=name)
            elif choose_by == "id":
                id = input("Which customer id would you like to select?  ")
                if id.isnumeric():
                    id = int(id)
                    selected_customer = client.info_about_one_customer(id=id)
            
            if selected_customer:
                pzzas()
                print("Selected customer: ", selected_customer.name)
                print("Videos checked out:", selected_customer.videos_checked_out_count)
                
            else:
                print("Sorry, we couldn't find a matching customer.")
            pzzas()
            

        elif option=='9': # edit customer
            if not selected_customer:
                print("Plese select a customer")
                continue
            print(f"Awesome! Let's update customer: {selected_customer}")
            pzzas()
            name = input(f"[{selected_customer.name}] Currently. Enter to keep.\nOtherwise, what is the customer's new name?  ")
            if len(name) > 0:
                selected_customer.name = name
            postal_code = input(f"[{selected_customer.postal_code}] Currently. Enter to keep.\nOtherwise, what is the customer's new postal code?  ")
            if len(postal_code) > 0:
                selected_customer.postal_code = postal_code
            phone = input(f"[{selected_customer.phone}] Currently. Enter to keep.\nOtherwise, what is the customer's new phone?  ")
            if len(phone) > 0:
                selected_customer.phone = phone
            selected_customer.save()
            pzzas()
            print("Updated customer:", selected_customer)
            

        elif option=='10': # delete customer
            check = input(f"Are you sure you want to delete {selected_customer} yes/no?  ")
            if check == 'yes':
                selected_customer.delete()
                pzzas()
                print("Customer has been deleted.")
                pzzas()
                selected_customer = None
            else:
                continue


        elif option=='11': # check out video to a customer
            if not selected_customer:
                print("Please select a customer.")
                continue
            if not selected_video:
                print("Please select a video.")
                continue

            try:
                client.check_out_video_to_customer(selected_video, selected_customer)
                pzzas()
                print("Yay! You have successfully checked out a video!")
                pzzas()
            except:
                pzzas()
                print("Sorry, we ran out of this title.")
                pzzas()

            continue


        elif option=='12':  # check in video from a customer
            if not selected_customer:
                print("Please select a customer")
                continue
            if not selected_video:
                print("Please select a video")
                continue

            try:
                client.check_in_video_from_customer(selected_video, selected_customer)
                pzzas()
                print("Thank you! Come again soon!")
                pzzas()
            except:
                pzzas()
                print("Sorry, we can not find a record for this rental")
                pzzas()
            
            continue


        elif option=='14':
            option_list()
        

        elif option=='15':
            play = False
            pzzas()
        
run_cli()

if __name__ == "__main__":
    print("******* ******* ******* ******* ******* ******* *******")
    print(THANKS)
    print(AGAIN)
    main() 