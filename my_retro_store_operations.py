import requests

class CustomerOperations:
    def __init__(self, url="https://aida-retro-video-store-api.herokuapp.com", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def create_customer(self,name="Default customer name",postal_code="Default postal code",phone="Default phone number"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            #"register_at": register_at
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def get_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
    
    def get_one_customer(self, name=None, customer_id=None):
        for customer in self.get_all_customers():
            if name:
                if name["name"]==name:
                    customer_id = customer["id"]
                    self.selected_customer = customer
            elif customer_id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

    def update_customer(self,customer_id, name=None,phone=None, postal_code=None):
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self. selected_customer["postal_code"]

        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
        }
        response = requests.put(
            self.url+f"/customers/{customer_id}",json=query_params)
        return response.json()
    
    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")

class VideoOperations:
    def __init__(self, url="https://aida-retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def create_video(self,title="Default video title",release_date="Default release date",total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_one_video(self, title=None, video_id=None):
        for video in self.get_all_videos():
            if title:
                if title["title"]==title:
                    video_id = video["id"]
                    self.selected_video = video
            elif video_id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    def update_video(self,video_id, title=None,release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self. selected_video["total_inventory"]

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.put(
            self.url+f"/videos/{video_id}",json=query_params)
        return response.json()

    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")

class RentalOperations:
    def __init__(self, url="https://aida-retro-video-store-api.herokuapp.com", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    def check_out(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response.json()

    def check_in(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        return response.json()