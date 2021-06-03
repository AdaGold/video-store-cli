import requests

URL = "https://retro-video-store-api.herokuapp.com"


# VideoStore class talks to the server
class VideoStore:
    def __init__(self, url=URL, selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    
    # ADD VIDEO
    def create_video(self, title=None, release_date=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        print(response.text)
        return response.json()


    # EDIT VIDEO
    def update_video(self, title=None, release_date=None, total_inventory=None):
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
        print("response:", response)
        print(response.text)
        self.selected_video = response.json()
        return self.selected_video


    # DELETE VIDEO
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()


    # LIST ONE VIDEO
    def list_one_video(self, title=None, id=None):

        self.selected_video = None 
            
        for video in self.list_all_videos():
            if title:
                if title == video["title"]:
                    id = video["id"]
                    self.selected_video = video
            elif id == int(video["id"]):
                self.selected_video = video
        
        if self.selected_video == None:
            return "Could not find any video by that title or id"

        return self.selected_video


    # LIST ALL VIDEOS
    def list_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
  
    
    # ADD CUSTOMER
    def create_customer(self, name=None, postal_code=None, phone=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()


    # EDIT CUSTOMER
    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        self.selected_customer = response.json()["customer"]
        return response.json()


    # DELETE CUSTOMER
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()


    # LIST ONE CUSTOMER
    def list_one_customer(self, name=None, id=None):  

        self.selected_customer = None 

        for customer in self.list_all_customers():
            if name:
                if name == customer["name"]:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == int(customer["id"]):
                self.selected_customer = customer
            
        if self.selected_customer == None:
            return "Could not find any customer by that name or id"

        return self.selected_customer


    # LIST ALL CUSTOMERS
    def list_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
  

    # CHECK-OUT VIDEO
    def check_out_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url + "/rentals/check-out", json=query_params)
        print(response.text)
        return response.json()


    # CHECK-IN VIDEO
    def check_in_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url + "/rentals/check-in", json=query_params)
        return response.json()


    # CHECKED-OUT VIDEOS PER CUSTOMER
    def checked_out_videos_by_customer(self, customer_id):
        response = requests.get(self.url + f"/customers/{customer_id}/rentals")
        print(response.text)
        return response.json()


    # CUSTOMERS WHO CHECKED-OUT SPECIFIC VIDEO
    def customers_checked_out_this_video(self, video_id):
        response = requests.get(self.url + f"/videos/{video_id}/rentals")
        print(response.text)
        return response.json()

    


