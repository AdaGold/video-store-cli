import requests
from datetime import datetime

class Customer:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", selected_customer = None):
        self.url = url
        self.selected_customer = selected_customer

    def add_customer(self, name = "Default Name", phone = None, postal_code = None, registered_at = None):
        query_params = {
            "name" : name,
            "phone" : phone,
            "postal_code" : postal_code,
            "registered_at" : datetime.now()
        }
        response = requests.post(self.url+"/customers", json = query_params)
        return response.json()
    
    def update_customer(self, name, phone, postal_code):
        if not name:
            title = self.selected_video["title"]
        if not phone:
            release_date = self.selected_video["release_date"]
        if not postal_code:
            total_inventory = self.selected_video["total_inventory"]
        query_params = {
            "name" : name,
            "phone" : phone,
            "postal_code" : postal_code
        }
        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}", json=query_params)
        self.selected_customer = response.json()["customer"]
        return response.json()
    
    def list_customers(self):
        response = self.get(self.url+"/customers")
        return response.json()
    
    def get_customer(self, name=None, id=None, phone=None, postal_code=None):
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    self.selected_customer = customer
            elif phone:
                if customer["phone"]==phone:
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "I'm sorry, I couldn't find that customer."
        
        response = self.get(self.url+"/customers/{id}")
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
        
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected.")