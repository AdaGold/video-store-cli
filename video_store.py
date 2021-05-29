import requests
import datetime

# - Customer create, edit, delete  --- check
# - Video create, edit, delete  --- check 
# - List customers --- check
# - List videos --- check
# - Check out video to customer --- *missing
# - Check in video  --- *missing

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None, selected_rental=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
        self.selected_rental = selected_rental # operate through this attribute or video?

    def create_customer(self, name="Default Customer Name", postal_code="Default Postal Code", phone="Default Phone Number",\
                        register_at=str(datetime.datetime.now()), videos_checked_out_count=0): 
        relevant_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "register_at": register_at,
            "videos_checked_out_count": videos_checked_out_count
        }
        response = requests.post(self.url + "/customers", json=relevant_params)
        return response.json() # example return value: {'id': 116}

    def create_video(self, title="Default Movie Title", release_date="Default Date", total_inventory="Default Total Inventory",\
                    available_inventory="Default Available Inventory"):
        relevant_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.post(self.url + "/videos", json=relevant_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url + "/customers")
        return response.json()

    def list_videos(self):
        response = requests.get(self.url + "/videos")
        return response.json() 

    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if customer: 
                if customer["name"] == name:
                    # customer = {'id': 136, 'name': 'Ada Lovelace', 'phone': '333-333-3333', 'postal_code': '88890',
                                # 'registered_at': 'Fri, 28 May 2021 20:13:32 GMT', 'videos_checked_out_count': 1}
                    id = customer["id"]
                    self.selected_customer = customer
                elif customer["id"] == id:
                    name = customer["name"]
                    self.selected_customer = customer
        if self.selected_customer == None:
            return "Could not find a customer by that name or ID."

        response = requests.get(self.url + f"/customers/{id}")
        return response.json()

    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if video:
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video
                elif video["id"] == id:
                    title = video["title"]
                    self.selected_video = video
        if self.selected_video == None:
            return "Could not find a video by that title or ID."
        response = requests.get(self.url + f"/videos/{id}")
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None): 
        if not name: 
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone_number"]
        
        relevant_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }

        response = requests.put(
            self.url + f"/customers/{self.selected_customer['id']}",
            json=relevant_params)
        self.selected_customer = response.json()
        print("Here's what we have now: ", self.selected_customer) # self.selected_customer = {'id': 198, 'name': 'Maxine Waters', 'phone': '222-333-4444', 
                                                                    # 'postal_code': '90211', 'registered_at': 'Sat, 29 May 2021 01:56:21 GMT',
                                                                    # 'videos_checked_out_count': 0}
        return response.json()

    def update_rental(self, due_date=None): # Work on rental instance, not video(?)
        if not due_date:
            due_date = (self.selected_rental["check_out_date"] + (datetime.timedelta(days=7)))
        relevant_param = {"due_date": due_date}
        response = requests.put(self.url + f"/customers/{self.selected_customer['id']}/rentals", # issue is here: TypeError: 'NoneType' object is not subscriptable
                                json=relevant_param)
        # can't see any of this bc path above is wrong
        print("Here's what we have now: ", response)
        self.selected_rental = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url + f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url + f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def show_selected_customer(self):
        if self.selected_customer:
            print(f"Customer with ID {self.selected_customer['id']} is currently selected\n")

    def show_selected_video(self): 
        if self.selected_video:
            print(f"Video with ID {self.selected_video['id']} is currently selected\n")
    
    # incomplete/incorrect logic 5/27/21, 9:03pm
    def check_out(self, customer_id=None, video_id=None, check_out_date=None):
        relevant_params = {
            "customer_id": customer_id,
            "video_id": video_id,
            "check_out_date": check_out_date
        }
        if self.selected_customer == None:
            return "Could not find a customer by that name or ID."
        if self.selected_video == None:
            return "Could not find a video by that title or ID."
        response = requests.post(self.url + "/rentals/check-out", json=relevant_params)
        return response.json()

    def check_in(self):
        pass