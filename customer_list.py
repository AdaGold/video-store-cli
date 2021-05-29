import requests
import datetime
from requests.models import Response

class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    def get_customers(self):
        r = requests.get(self.url+"/customers")
        return r.json()

    def add_customer(self, name, phone, postal_code):
        new_customer ={"name":name,
                    "phone":phone,
                    "postal_code":postal_code
        }
        response = requests.post(self.url+"/customers",json=new_customer)
        return response.json()

    def get_one_customer(self, name=None, id=None):
        
        for customer in self.get_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
    
    def edit_one_customer(self, name, phone, postal_code):
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        
        edit_customer={
            "name":name,
            "phone":phone,
            "postal_code":postal_code
        }

        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}",
            json = edit_customer )

        print("response:",response)
        self.selected_customer=response.json()
        return response.json()
    
    def delete_a_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")

    