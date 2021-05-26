from client import Client

#from my_store import Customer #need to make this
#from my_store import Rental #need to make this




#URL = "http://127.0.0.1:5000"
#BACKUP_URL = "https://retro-video-store-api.herokuapp.com"
#MAITES_URL = "https://maite-retro-video-store-api.heroku.com/"



def main():
    print("*******  WELCOME TO RETRO VIDEO STORE  *******")


def pzzas():
    print("\n************************************************\n")


def option_list():

    options = {
        "1": "Add a video", 
        "2": "Get information about all videos",
        "3": "Select one video", #needs id
        "4": "Edit a video", # needs id
        "5": "Delete a video", # needs id 

        "6": "Add a customer",
        "7": "Get information on all customers",
        "8": "Select one customer", # needs id
        "9": "Edit a customer", # needs id
        "10": "Delete a customer", # need id
        
        "11": "Check out a video to a customer", # nedds id
        "12": "Check in a video from a customer", # needs id
        }

    pzzas()
    print("The following are your options")
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
        

        if option=='1':
            print("Great!") 
            title=input("What is the title of the movie?  ")
            release_date=input("In yyyy-mm-dd format. When was this movie released?  ")
            total_inventory=input("How many copies of this movie are there?  ")
            video = client.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            pzzas()
            print("New video:", video.title)
            selected_video = video


        elif option=='2':
            pzzas()
            for video in client.info_about_all_videos():
                print(video) 
            

        elif option=='3': #this selects the video 
            choose_by = input("Would you like to select by title or id?:  ")
            if choose_by=="title":
                title = input("Which movie title would you like to select?  ")
                selected_video = client.info_about_one_video(title=title)
            elif choose_by=="id":
                id = input("Which movie id would you like to select?  ")
                if id.isnumeric():
                    id = int(id)
                    selected_video = client.info_about_one_video(id=id)
            else:
                print("Oops! Please try again. Enter id or title.")

            if selected_video:
                pzzas()
                print("Selected video: ", selected_video.title) # add info like id and stuff 
            else:
                print("Sorry, we couldn't find a matching video.")
            pzzas()
        #show info on selected video    

        elif option=='4':
            if not selected_video:
                print("Please select a video")
                continue

            print(f"Great! Let's update video: {selected_video}") 
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
            

        elif option=='5':
            #maybe an 'are you sure message?
            selected_video.delete()
            pzzas()
            print("Video has been deleted.")
            pzzas()
            selected_video = None

            
        elif option=='6':
            print("Awesome!") 
            name=input("What is the customer's name?  ")
            postal_code=input("What is the customer's zip code?  ")
            phone=input("Including area code. What's the customer's phone number?  ")
            customer = client.add_customer(name=name, postal_code=postal_code, phone=phone)
            pzzas()
            print("New customer:", customer.name)
            selected_video = customer

        elif option=='7':
            pzzas()
            for customer in client.info_about_all_customers():
                print(customer) 

        elif option=='8':
            choose_by = input("Would you like to select a customer by name or id?  ")
            if choose_by == "name":
                name = input("Which customer name would you like to select?  ")
                selected_customer = client.info_about_one_customer(name=name)
            elif choose_by == "id":
                id = input("Which customer id would you like to select?  ")
                if id.isnumeric():
                    id = int(id)
                    selected_customer = client.info_about_one_customer(id=id)
            else:
                print("Oops! Please try again.")

            if selected_customer:
                pzzas()
                print("Selected customer: ", selected_customer.name) # more info?
            else:
                print("Sorry, we couldn't find a matching customer.")
            pzzas()
            #show info on selected customer  

        elif option=='9':
            if not selected_customer:
                print("Plese select a customer")
                continue
            print(f"Awesome! Let's update customer: {selected_customer}")
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
            

        elif option=='10':
            #maybe an 'are you sure message?
            selected_customer.delete()
            pzzas()
            print("Customer has been deleted.")
            pzzas()
            selected_customer = None


        # elif option=='11':
        #     pass
        # elif option=='12':
        #     pass


        elif option=='14':
            option_list()
        

        elif option=='15':
            play = False
            pzzas()
            print("Thank you for using the Retro Video Store!")
            pzzas()
        
run_cli()

if __name__ == "__main__":
    main()