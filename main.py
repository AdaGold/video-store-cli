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

        # pprint(choice) - TESTING
        if choice == 0: # GET ALL CUSTOMERS   
            all_videos = videoApi.list_videos()
            pprint(all_videos)
            print_little_stars()
        elif choice == 1: # POST / CREATE - VIDEO - NEED TO TEST
            title = input("Enter video title: ")
            release_date = input("Enter release in YYYY-MM-DD format : ")
            total_inventory = input("Enter video's total inventory: ")
            
            # year, month, day = map(int, date_entry.split('-'))
            # date1 = datetime.date(year, month, day)
            try:
                response = videoApi.create_video(title, release_date, \
                    total_inventory)
                if response.status_code != 201:
                    raise Exception("Something is wrong with the information you entered")
                else:
                    print(f"Video {response.json()} was created succesfully")
            except Exception as e:
                print(f"There was an issue creating that video: {e}")

        elif choice == 2: # GET VIDEO by ID - NEED TO TEST
            try:
                id = (input("Enter video id: "))
                video = videoApi.get_video(id)
                if not video:
                    print("Could not find video by that id {id}")
                    raise Exception("Something went wrong")
                else:
                    pprint(video)
            except Exception as e:
                print(f"There was an issue getting that video: {e}")

        elif choice == 3: # PUT/UPDATE VIDEO by /ID  - NEED TO TEST
            try:
                id = input("Enter id of the video you want to update: ")
                print_stars_centered()  # added
                video = videoApi.get_video(id)
                if not video:
                    print("Video not found with id {id}")
                else:
                    pprint(video)
                    print_stars_centered()
                    title = input("Enter a title if you want to update it: ")
                    release_date = input("Enter a release_date in YYYY-MM-DD format if you want to update it: ")
                    total_inventory = input("Enter a total_inventory code if you want to update it: ")
                    response = videoApi.update_video(video,title,\
                        release_date,total_inventory)
                    if response.status_code != 200:
                        raise Exception("Something went wrong")
                    else:
                        print_stars_centered() # added 1:58
                        print(f"\nVideo was updated succesfully:\n")
                        pprint(videoApi.get_video(id)) # to display updated video
            except Exception as e:
                print(f"There was an issue updating that video: {e}")
        # I'M HERE
        elif choice== 4: # DELETE VIDEO by ID  - NEED TO TEST - WIP - HERE
            try:
                id = input("Enter the id of the video you want to delete: ")
                print_stars_centered() 
                print()
                video = videoApi.get_video(id)
                if not video:
                    print("Video not found with id {id}")
                    raise Exception("Something went wrong")
                else:
                    print(DELETING_VIDEO)
                    pprint(video)
                    videoApi.delete_video(id)
            except Exception as e:
                print(f"There was an issue deleting that customer: {e}")

        elif choice == 5: #POST CHECK OUT VIDEO - RENTAL
            video_id = input("Enter the video id: ")
            customer_id = (input("Enter the customer id: "))
            try:
                response = rentalApi.check_out(video_id, customer_id)
                if response.status_code != 200:
                    print(response.status_code)
                    pprint(response)
                    raise Exception("Something went wrong")
                else:
                    video = videoApi.get_video(video_id)
                    customer = customerApi.get_customer(customer_id)

                    # print(f"Video {video_id} was cheked_out to Customer id {customer_id} succesfully")
                    print(f"Video {video_id}: {video['title']} was cheked_out to Customer id {customer_id}: {customer['name']} succesfully")

            except Exception as e:
                print(f"There was an issue checking_out that customer: {e}")

        elif choice == 6: #POST CHECK IN VIDEO - RENTAL
            video_id = input("Enter the video id: ")
            customer_id = (input("Enter the customer id: "))

            try:
                response = rentalApi.check_in(video_id, customer_id)
                if response.status_code != 200:
                    raise Exception("Something went wrong")
                else:
                    print(f"Video {video_id} was cheked_in to Customer id {customer_id} succesfully")
            except Exception as e:
                print(f"There was an issue checking_out that customer: {e}")

        elif choice == 7: # GET ALL CUSTOMERS   
            all_videos = customerApi.list_all_customers()
            pprint(all_videos)
            print_little_stars()

        elif choice == 8: # POST / CREATE - CUSTOMER
            name = input("Enter a name: ")
            phone_number = input("Enter a phone number: ")
            postal_code = input("Enter a postal code: ")
            try:
                response = customerApi.create_customer(name,postal_code,phone_number)
                if response.status_code != 201:
                    raise Exception("Something went wrong")
                else:
                    print(f"User {response.json()} was created succesfully")
            except Exception as e:
                print(f"There was an issue creating that customer: {e}")

        elif choice == 9: # GET CUSTOMER by /ID 
            try:
                id = (input("Enter the id of the customer you want to update: "))
                customer = customerApi.get_customer(id)
                if not customer:
                    print("Customer not found with id {id}")
                    raise Exception("Something went wrong")
                else:
                    pprint(customer)
            except Exception as e:
                print(f"There was an issue getting that customer: {e}")

        elif choice == 10: # PUT / UPDATE by /ID  - CUSTOMER
            try:
                id = input("Enter id of the customer you want to update: ")
                print_stars_centered()  # added
                customer = customerApi.get_customer(id)
                if not customer:
                    print("Customer not found with id {id}")
                else:
                    pprint(customer)
                    print_stars_centered()
                    name = input("Enter a name if you want to update it: ")
                    phone_number = input("Enter a phone number if you want to update it: ")
                    postal_code = input("Enter a postal code if you want to update it: ")
                    response = customerApi.update_customer(customer,name,\
                        postal_code,phone_number)
                    if response.status_code != 200:
                        raise Exception("Something went wrong")
                    else:
                        print_stars_centered() 
                        print(f"\nUser was updated succesfully:\n")
                        # to display updated customer
                        pprint(customerApi.get_customer(id)) # should print updated customer
            except Exception as e:
                print(f"There was an issue updating that customer: {e}")
        
        elif choice== 11: # DELETE by ID  
            try:
                id = input("Enter the id of the customer you want to delete: ")
                print_stars_centered() 
                print()
                customer = customerApi.get_customer(id)
                if not customer:
                    print("Customer not found with id {id}")
                    raise Exception("Something went wrong")
                else:
                    print(DELETING)
                    pprint(customer)
                    customerApi.delete_customer(id)
            except Exception as e:
                print(f"There was an issue deleting that customer: {e}")

        elif choice == 12: # choice == len(options) - 1
            show_options()

        elif choice == 13: # choice == len(options) - 1
            print(EXIT)
            play = False
            print(BYE)


if __name__ == "__main__":
    run_cli()

