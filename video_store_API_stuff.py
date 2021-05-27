import requests
import datetime



class Video:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    # User story 1
    def add_video(self, title="The Void", release_date=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()



    # User story 2
    def edit_video(self, title=None, release_date=None, total_inventory=None):
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
        self.selected_video = response.json()["video"]
        return response.json()


    # User story 3
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    
    
    # User story 4
    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def print_selected_video(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['video_id']} is currently selected\n")


class Customer:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer


    # User story 6
    def add_customer(self, name="Frogge Queen", postal_code=00000, phone="000-000-0000", registered_at=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "registered_at": registered_at
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()


    # User story 7
    def edit_customer(self, name=None, postal_code=None, phone=None):

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
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()


    # User story 8
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    


    # User story 9
    def get_single_customer(self, name=None, id=None):
        
        for customer in self.get_all_customers():
            if name:
                if customer["name"]==name:
                    id = customer["cust_id"]
                    self.selected_customer = customer 
            elif id == customer["cust_id"]:
                self.selected_customer = customer 

        if self.selected_customer == None:
            return f"Could not find customer with name:{name} or id: {id}"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()


    # User story 10
    def get_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()


    def print_selected_customer(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['cust_id']} is currently selected\n")

class Rental:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    # User story 11
    def check_out_video(self):
        response = requests.post(self.url+f"/rentals/{self.selected_rental['id']}/check-out")
        # ❗️ what in the shit is going on here: 
        # self.selected_rental = response.json()["task"]
        # return response.json()

        # User story 12
    def check_in_video(self):
        response = requests.post(self.url+f"/rentals/{self.selected_rental['id']}/check-in")
        # self.selected_rental = response.json()["task"]
        # return response.json() 

