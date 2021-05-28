import requests

# CVR stand for Customer, Video and Rental
class CVR:
    def __init__(self, url="http://localhost:5000", selected_customer=None, selected_video=None, selected_rental=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video
        self.selected_rental = selected_rental
    
    # CUSTOMER
    def create_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = "Default Name"
        if not postal_code:
            postal_code = None
        if not phone:
            phone = None

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, name=None, id=None):
        
        for customer in self.list_customers():
            if name:
                if customer["name"].lower()==name.lower():
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self,name=None,postal_code=None,phone=None):
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

        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    # VIDEO
    def create_video(self, title=None, release_date=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if title:
                if video["title"].lower()==title.lower():
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self,title=None,release_date=None,total_inventory=None):
        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )

        self.selected_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def print_selected_video(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")    

    # Rental
    def check_out(self, video_id, customer_id):
        query_params = {
        "video_id": video_id,
        "customer_id": customer_id,
        }
        response = requests.post(self.url+f"/rentals/check-out", json=query_params)
        self.selected_rental = response.json()
        return response.json()

    def check_in(self, video_id, customer_id):
        query_params = {
        "video_id": video_id,
        "customer_id": customer_id,
        }
        response = requests.post(self.url+f"/rentals/check-in", json=query_params)
        self.selected_rental = response.json()
        return response.json()

    def print_list_reference(self):
        print("\nGreat! Check below customer list and video list as your reference: ")
        print(f"\nCustomers list: ")
        for customer in self.list_customers():
            print(customer)
        
        print(f"\nVideos list: ")
        for video in self.list_videos():
            print(video)