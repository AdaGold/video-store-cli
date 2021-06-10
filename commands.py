
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


video_store= VideoStore(url=URL)

def print_stars():
    print("\n*********************************\n")

def to_int(input):
    if input.isnumeric():
        input=int(input)
    else:
        print("Please enter valid id number: ")

    
    def get_vid():
        print("Great! Let's look-up a video!")
        video_id= input("Please enter the video id: ")
        to_int(video_id)

        video_store.get_video(video_id)


    def add_video():
        print("Let's add a New Video!")
        video_id= input("Please input the video id: ")
        to_int(video_id)

        title=input("Please enter a title: ")
        release_date=input("Please enter a release date: ")
        total_inventory=input("Please enter the total inventory: ")
        
        response= video_store.create_video(
        title=title,
        release_date=release_date, 
        total_inventory=total_inventory)

        print("New Video: ", response["video"])

    def del_vid():
        print("Let's Delete a video!")
        video_id= input("Please input the video id: ")
        to_int(video_id)
        video_store.delete_video()

        print_stars()
        print("Video has been deleted")


    def update_vid():
        print("Let's update a Video!")
        video_id= input("Please input the video id: ")
        to_int(video_id)

        title=input("Please enter the updated or current title: ")
        release_date=input("Please enter the updated or current release date: ")
        total_inventory=input("Please enter the total inventory: ")
        
        response= video_store.update_video(
        title=title,
        release_date=release_date, 
        total_inventory=total_inventory)

        print("New Video: ", response["video"])


    def all_videos():
        print_stars()
        for vid in video_store.list_videos():
            print(vid)


    def get_customer():
        print("Let's pull up a customer account!")
        customer_id= input("Please enter the customer id:")
        to_int(customer_id)

        video_store.get_customer(customer_id)


    def del_customer():
        print("Let's delete a customer!")
        customer_id=input("Please enter customer id: ")
        to_int(customer_id)

        response=video_store.delete_customer(customer_id)
        print(response)


    def update_customer():
        print("Great! Let's update a customer!")
        customer_id="Please input customer id: "
        to_int(customer_id)

        name=input("Please enter the updated or current name: ")
        postal_code=input("Please enter the updated or current postal code: ")
        phone = input("Please enter the updated or current phone number: ")
        response = video_store.update_customer(name = name,postal_code = postal_code,phone = phone)

        print_stars()
        print("Updated customer:", response["customer"])


    def all_customers():
        for cust in video_store.list_customers():
            print(cust)


    def check_in_rental():
        print("Great! Let's check-in a video")

        customer_id=("Please enter customer id: ")
        to_int(customer_id)
        video_id= input("Please enter the video id: ")
        to_int(video_id)

        response = video_store.check_in(customer_id=customer_id, video_id=video_id)

        print_stars()
        print("Video Rental:", response["rental"])


    def check_out_rental():
        print("Great! Let's check-out a video")

        customer_id=("Please enter customer id: ")
        to_int(customer_id)
        video_id= input("Please enter the video id: ")
        to_int(video_id)

        response = video_store.check_out(customer_id=customer_id, video_id=video_id)

        print_stars()
        print("Video Rental:", response["rental"])



