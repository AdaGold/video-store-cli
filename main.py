from video import Video
from customer import Customer
from rental import Rental
from constants import *
from program import *
from pprint import pprint

def run_cli(play=True):
    start_program() # main()

    #initialize Customer API
    customerApi = Customer()
    videoApi = Video()
    rentalApi = Rental()

    print(INSTRUCTIONS)
    options = show_options()
    
    while play==True:
        print_little_stars()
        choice = make_choice(options)
        print_little_stars()
        print(f"Your choice was {choice}: {options[choice]}")
        print_little_stars() 

        if choice == 0: # GET ALL VIDEOS  
            all_videos = videoApi.list_videos()
            pprint(all_videos)
            print_little_stars()

        elif choice == 1: # POST - CREATE VIDEO 
            print_stars_centered()
            title = input("Enter video title: ")
            release_date = input("Enter release in YYYY-MM-DD format : ")
            total_inventory = input("Enter video's total inventory: ")
            print_stars_centered()
            try:
                response = videoApi.create_video(title, release_date, \
                    total_inventory)
                if response.status_code != 201:
                    raise Exception("\n\nSomething is wrong with the information you entered")
                else:
                    print_stars_centered()
                    print(f"\nVideo {response.json()} was created succesfully")
                    print_stars_centered()
            except Exception as e:
                print_stars_centered()
                print(f"There was an issue creating that video: {e}")
                print_stars_centered()

        elif choice == 2: # GET VIDEO BY ID 
            try:
                id = (input("Enter video id or press enter to see all: "))
                video = videoApi.get_video(id)
                if not video:
                    print_stars_centered()
                    print(f"Could not find video by that id: {id}")
                    raise Exception("\nSomething went wrong")
                else:
                    print()
                    pprint(video)
            except Exception as e:
                print(f"\nThere was an issue getting that video: {e}")
                print_stars_centered()

        elif choice == 3: # UPDATE - PUT VIDEO BY ID   
            try:
                id = input("Enter id of the video you want to update: ")
                video = videoApi.get_video(id)
                if not id or not video:
                    print_stars_centered() 
                    print(f"\nVideo not found with id {id} provided")
                    print_stars_centered()
                else:
                    print_stars_centered() 
                    pprint(video)
                    print_stars_centered()
                    title = input("Enter a title if you want to update it: ")
                    release_date = input("Enter a release_date in YYYY-MM-DD format if you want to update it: ")
                    total_inventory = input("Enter a total_inventory code if you want to update it: ")
                    response = videoApi.update_video(video,title,\
                        release_date,total_inventory)
                    print_stars_centered()
                    if response.status_code != 200:
                        raise Exception("\nSomething is wrong with the information you entered")
                    else:
                        print_stars_centered() 
                        print(f"\nVideo was updated succesfully:\n")
                        pprint(videoApi.get_video(id))  
            except Exception as e:
                print(f"\nThere was an issue updating that video: {e}")
                print_stars_centered()

        elif choice== 4: # DELETE VIDEO BY ID   
            try:
                id = input("Enter the id of the video you want to delete: ")
                print_stars_centered() 
                print()
                video = videoApi.get_video(id)
                if not id or not video:
                    print(f"Video not found with id {id}")
                    raise Exception("\nSomething went wrong")
                else:
                    print(DELETING_VIDEO)
                    pprint(video)
                    videoApi.delete_video(id)
            except Exception as e:
                print(f"\nThere was an issue deleting that customer: {e}")
                print_stars_centered()

        elif choice == 5:  # POST CHECK OUT VIDEO - RENTAL
            print_stars_centered()
            video_id = input("Enter the video id: ")
            customer_id = (input("Enter the customer id: "))
            print_stars_centered()
            try:
                response = rentalApi.check_out(video_id, customer_id)
                if response.status_code != 200:
                    raise Exception("\nSomething went wrong")
                else:
                    video = videoApi.get_video(video_id)
                    customer = customerApi.get_customer(customer_id)
                    print(f"Video {video_id}: \"{video['title']}\", was cheked_out to \nCustomer id {customer_id}: {customer['name']}, succesfully")
                    print_stars_centered()
            except Exception as e:
                print(f"There was an issue checking out that customer: {e}")
                print_stars_centered()

        elif choice == 6: # POST CHECK IN VIDEO - RENTAL
            print_stars_centered()
            video_id = input("Enter the video id: ")
            customer_id = (input("Enter the customer id: "))
            print_stars_centered()
            try:
                response = rentalApi.check_in(video_id, customer_id)
                if response.status_code != 200:
                    raise Exception("\nSomething went wrong")
                else:
                    video = videoApi.get_video(video_id)
                    customer = customerApi.get_customer(customer_id)
                    print(f"Video {video_id}: \"{video['title']}\", was cheked in by\n Customer id {customer_id}: {customer['name']}, succesfully")
                    print_stars_centered()
            except Exception as e:
                print(f"There was an issue checking_out that customer: {e}")
                print_stars_centered()

        elif choice == 7: # GET ALL CUSTOMERS   
            all_videos = customerApi.list_all_customers()
            pprint(all_videos)
            print_little_stars()

        elif choice == 8: # POST - CREATE - CUSTOMER
            print_stars_centered()
            name = input("Enter a name: ")
            phone_number = input("Enter a phone number: ")
            postal_code = input("Enter a postal code: ")
            print_stars_centered()
            if not name or not phone_number or not postal_code:
                print_stars_centered()
                print("There was something wrong with the info you entered")
                print_stars_centered()
            else:
                try:
                    response = customerApi.create_customer(name,postal_code,phone_number)
                    if response.status_code != 201:
                        raise Exception("Something went wrong")
                    else:
                        print_stars_centered()
                        print(f"User {response.json()} was created succesfully")
                        print_stars_centered()
                except Exception as e:
                    print_stars_centered()
                    print(f"There was an issue creating that customer: {e}")
                    print_stars_centered()

        elif choice == 9: # GET CUSTOMER BY ID 
            try:
                print_stars_centered()
                id = (input("Enter customer to display their information: "))
                print_stars_centered
                customer = customerApi.get_customer(id)
                if not id or not customer:
                    print_stars_centered()
                    print(f"Customer not found with id {id}")
                    raise Exception("\nSomething went wrong")
                else:
                    print_stars_centered()
                    pprint(customer)
                    print_stars_centered()
            except Exception as e:
                print(f"\nThere was an issue getting that customer: {e}")
                print_stars_centered()

        elif choice == 10: # PUT - UPDATE CUSTOMER BY ID
            try:
                print_stars_centered()
                id = input("Enter id of the customer you want to update: ")
                print_stars_centered()  
                customer = customerApi.get_customer(id)
                if not customer:
                    print(f"Customer not found with id {id}")
                    print_stars_centered()
                else:
                    print_stars_centered()
                    pprint(customer)
                    print_stars_centered()
                    name = input("Enter a name if you want to update it: ")
                    phone_number = input("Enter a phone number if you want to update it: ")
                    postal_code = input("Enter a postal code if you want to update it: ")
                    response = customerApi.update_customer(customer,name,\
                        postal_code,phone_number)
                    print_stars_centered()
                    if response.status_code != 200:
                        raise Exception("\nSomething went wrong")
                    else:
                        print_stars_centered() 
                        print(f"\nUser was updated succesfully:\n")
                        pprint(customerApi.get_customer(id)) 
                        print_stars_centered()
            except Exception as e:
                print_stars_centered()
                print(f"There was an issue updating that customer: {e}")
                print_stars_centered()

        elif choice== 11: # DELETE CUSTOMER BY ID  
            try:
                id = input("Enter the id of the customer you want to delete: ")
                print_stars_centered() 
                print()
                customer = customerApi.get_customer(id)
                if not id or not customer:
                    print(f"Customer not found with id {id}")
                    raise Exception("\nSomething went wrong")
                else:
                    print(DELETING_CUSTOMER)
                    pprint(customer)
                    customerApi.delete_customer(id)
            except Exception as e:
                print(f"There was an issue deleting that customer: {e}")
                print_stars_centered()
                
        elif choice == 12: # choice == len(options) - 1
            show_options()

        elif choice == 13: # choice == len(options) - 1
            print(EXIT)
            play = False
            print(STORE_NAME_LITTLE)
            print(BYE)

if __name__ == "__main__":
    run_cli()

