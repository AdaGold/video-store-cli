import requests
import datetime

class VideoStore:
    def __init__(self, url="http://localhost:5000", current_customer=None, current_video=None):
        self.url = url
        self.current_customer = current_customer
        self.current_video = current_video

    def create_customer(self, name="Default Name", postal_code="00000", phone="000-000-0000"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id=None, name=None, phone=None):
        for customer in self.list_customers():
            if id and customer["id"] == id:
                self.current_customer = customer
            elif name and customer["name"] == name:
                id = customer["id"]
                self.current_customer = customer
            elif phone and customer["phone"] == phone:
                id = customer["id"]
                self.current_customer = customer
        if self.current_customer == None:
            return "I'm sorry, we could not find a customer by that id, name, or phone"
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.current_customer["name"]
        if not postal_code:
            postal_code = self.current_customer["postal_code"]
        if not phone:
            phone = self.current_customer["phone"]
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
            }
        response = requests.put(self.url+f"/customers/{self.current_customer['id']}",
        json=query_params)
        # print("response:", response)
        self.current_customer = response.json()["customer"]
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.current_customer['id']}")
        self.current_customer = None
        return response.json()

    
    # def create_video(self,):

    # def get_video(self, name=None, id=None):
    
    # def update_video(self):

    # def delete_video(self):

    # def list_videos(self):


    #def checkout_video(self):

    #def checkin_video(self):


    # Optional:

    # def list_customers_checked_out_videos(self):

    # def list_videos_current_customers(self):