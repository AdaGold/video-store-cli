import requests
import datetime
from requests.models import CaseInsensitiveDict

def print_stars():
    print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n")

#### VideoStore class ####
class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com/", selected_video=None, selected_customer=None): # "http://localhost:5000"
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

                #######################################
                ########### VIDEO OPTIONS #############
                #######################################

###### "1": "add a video" CREATE VIDEO #####
    def create_video(self,title="Default Video",release_date="Default Release_Date",total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
            }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

###### SELECT VIDEO TO MODIFY or SEE "2" and "3" and "5" helper: UPDATE OR DELETE OR READ ######
    def select_video(self):
        print("\n📼 📼 📼 📼 📼  Select a Video 📼 📼 📼 📼 📼 \n")

        select_by = input("Would you like to select video by the video title or video id? Input either title or id: ")
        if select_by=="title":
            title = input("Which video title would you like to select? Enter Video title: ")
            # the_video_selection = self.get_video(title=title)
            self.selected_video = self.get_video(title=title)

        elif select_by=="id":
            id = input("Which video id would you like to select? Enter Video ID:")
            if id.isnumeric():
                id = int(id)
                self.selected_video = self.get_video(id=id)
            else:
                print("🤷 Could not select. Please enter a valid video id or video title.")
        
        if self.selected_video:
            print_stars()        
            print("Selected video:", self.selected_video)

        return self.selected_video

###### "2": "edit a video" UPDATE VIDEO #####
    def update_video(self,title=None,release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        return response.json()

###### "3": "delete a video" DELETE VIDEO #####
    def delete_video(self):
        print("\n❌ 📼 ❌ THE VIDEO YOU SELECT WILL BE DELETED ❌ 📼 ❌\n")
        self.select_video()
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")

        return response.json()

###### "4": "get information about all videos" READ VIDEO #####
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

###### "5": "get information about one video READ VIDEO" #####
    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if video:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
                elif id == video["id"]:
                    self.selected_video = video

        if self.selected_video == None:
            return "🤷 Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

                #######################################
                ########## CUSTOMER OPTIONS ###########
                #######################################

###### "6": "add a customer" CREATE CUSTOMER #####
    def create_customer(self,name="Default Name",phone="Default Phone",postal_code="Default Postal_code",registered_at=None,videos_checked_out_count=None):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
            "registered_at": registered_at,
            "videos_checked_out_count": videos_checked_out_count
            }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

###### SELECT CUSTOMER TO MODIFY od SEE "7" and "8" and "9" helper: UPDATE OR DELETE ######
    def select_customer(self):
        print("\n 🧑🏿‍🤝‍🧑🏾🧑🏼‍🤝‍🧑🏻 Select a Customer 🧑🏿‍🤝‍🧑🏾🧑🏼‍🤝‍🧑🏻 \n")

        select_by = input("Would you like to select customer by the customer's name or customer's id? Input either name or id: ")
        if select_by=="name":
            name = input("Which customer would you like to select? Enter Customer name: ")
            self.get_customer(name=name)

        elif select_by=="id":
            id = input("Which customer id would you like to select? Enter Customer ID:")
            if id.isnumeric():
                id = int(id)
                self.get_customer(id=id)

            else:
                print("🤷 Could not select. Please enter a valid customer id or customer name.")
            
        if self.selected_customer:
            print_stars()
            print("Selected customer: ", self.selected_customer)
        
        return self.selected_customer

###### "7": "edit a customer" UPDATE CUSTOMER #####
    def update_customer(self,name="Default Name",phone="Default Phone",postal_code="Default Postal_code",registered_at="Default Registered_at",videos_checked_out_count="Default Videos_Checked_Out_Count"):
    #def update_customer(self,name=None,phone=None,postal_code=None,registered_at="Default Registered_at",videos_checked_out_count="Default Videos_Checked_Out_Count"):
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not registered_at:
            registered_at = self.selected_customer["registered_at"]
        if not videos_checked_out_count:
            videos_checked_out_count = self.selected_customer["videos_checked_out_count"]

        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
            "registered_at": registered_at,
            "videos_checked_out_count": videos_checked_out_count
            }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

###### "8": "delete a customer" DELETE CUSTOMER #####
    def delete_customer(self):
        print("\n❌ 📼 ❌ THE CUSTOMER YOU SELECT WILL BE DELETED ❌ 📼 ❌\n")
        self.select_customer()
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

###### "9": "get information about one customer" READ CUSTOMER #####
    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if customer:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
                elif id == customer["id"]:
                    self.selected_customer = customer

        if self.selected_customer == None:
            return "🤷 Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

###### "10": "get information about all customers" READ CUSTOMER #####
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

#######################################
########### RENTAL OPTIONS ############
#######################################

###### "11": "check out a video to a customer" CHECK OUT #####
    def check_out(self, customer_id="Default Customer_ID",video_id="Default Video_ID"):
        self.select_customer()
        self.select_video()

        customer_id = self.selected_customer["id"]
        video_id = self.selected_video["id"]

        video_title = self.selected_video["title"]
        customer_name = self.selected_customer["name"]

        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
            }
        response = requests.post(self.url+f"/rentals/check-out", json=query_params)
        rental_due_date = response.json()['due_date']
        # print (f"THIS IS THE response.json(): {response.json()}")
        print (f"\n 🍿 🍿 ENJOY THE MOVIE 🍿 🍿")
        print (" -----  Check-Out Summary  -----  \n ")
        print (f"Customer Name: {customer_name}")
        print (f"Customer ID: {customer_id}")
        print (f"Video Title: {video_title}")
        print (f"Video ID: {video_id}")
        print (f"Rental Due Date: {rental_due_date}") # How do I grab the rental due_date?
        print (f" \n   📼  Be Kind  🙂  Please Rewind 📼   \n")

        return response.json()

###### "12": "check in a video from a customer" CHECK IN #####
    def check_in(self, customer_id="Default Customer_ID",video_id="Default Video_ID"):
        self.select_customer()
        self.select_video()

        customer_id = self.selected_customer["id"]
        video_id = self.selected_video["id"]

        video_title = self.selected_video["title"]
        customer_name = self.selected_customer["name"]

        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
            }
        response = requests.post(self.url+f"/rentals/check-in", json=query_params)
        print (f"THIS IS THE response.json(): {response.json()}")

        print (f"\n ⭐ 📼 ⭐  RETURN COMPLETE  ⭐ 📼 ⭐ ")
        print (" -------  Check-In Summary  -------  \n ")
        print (f"Customer Name: {customer_name}")
        print (f"Customer ID: {customer_id}")
        print (f"Video Title: {video_title}")
        print (f"Video ID: {video_id}")
        print (f" \n 📼  📼  📼  Thank You 📼  📼  📼  \n")
        
        return response.json()