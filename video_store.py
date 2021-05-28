import requests 
import datetime 

class Videostore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer 

#all for videos 
    #1 - add a video so that I can check it out to the customers
    def create_video(self,title="Default Video", release_date="Default"):
        query_params = {
            "title": title,
            "release_date": release_date
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    #2 - edit a video so that information about the video is accurate 
    def update_video(self,title="title"):
        if not title:
            title = self.selected_video["title"]

        query_params = {
        "title": title,
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_task['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()

    #3 - delete a video so that the store records stay up to date
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_task['id']}")
        self.selected_task = None
        return response.json()

    #4 - get information about all videos so that I can see the store stock
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    #5 - get information about one video so that I can see how many copies are available 
    def get_video(self, title=None, id=None):
        
        for video in self.get_video():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_task = video

        if self.selected_video == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()
    
    #6 - add a customer so that I can check out videos to the customer
    def create_customer(self,title="title",postal_code="postal_code",phone="phone"):
        query_params = {
            "title": title,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    #7 - edit a customer so that the information about the customer is accurate 
    def update_customer(self,title="title",postal_code="postal_code",phone="phone"):
        if not title:
            title = self.selected_customer["title"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone =self.selected_customer["phone"]

        query_params = {
        "title": title,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()

    #8 - delete a customer so that the customer is no longer in the store records 
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    #9 - get informaton about one customer so that I can see how many videos a customer had rented currently 
    def get_customer(self, name=None, postal_code=None, phone=None):
        
        for customer in self.list():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            
            elif postal_code == customer["postal"]:
                self.selected_customer = customer
            elif phone == customer["phone"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that title or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
    
    #10 - get information about all customers so that I can how many customers the store has
    def list_customer(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    #11 - check out a video to a customer so that the store has a record of who has the video 
    def check_out(self):
        response = requests.post(self.url+f"/videos/{self.selected_video['id']}/check_out")
        self.selected_video = response.json()["video"]
        return response.json()
        
    #12 - check in a video from a customer so that the video will be available to other customers
    def check_in(self):
        response = requests.post(self.url+f"/videos/{self.selected_video['id']}/check_in")
        self.selected_video = response.json()["video"]
        return response.json()

    #13 print selected video
    def print_selected_video(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is selected")
        else:
            print("There is no selected task.")

    #14 print selected customer 
    def print_selected_customer(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is selected")
        else:
            print("There is no selected customer.")



