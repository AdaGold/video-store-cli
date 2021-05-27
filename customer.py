import requests
from datetime import datetime

# do I need to make separate classes for customers, videos, and rental
# like I did in my API?

# do you have to "select" something before updating/deleting it? why?

class Customer:
    def __init__(self, url="http://localhost:5000"):
        self.url = url

    def add_customer(self, name=None, postal_code=None, phone=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def update_customer(self, customer_id=None, name=None,postal_code=None,
        phone=0):
        # if not customer_id:
        #     name = self.selected_customer["name"]
        # if not postal_code:
        #     postal_code = self.selected_customer["postal_code"]
        # if not phone:
        #     phone = self.selected_customer["phone"]

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{customer_id}",
            json=query_params
            )
        print("response:", response)
        return response.json()

    def delete_customer(self, customer_id=None):
        if customer_id == None:
            return "Could not find customer by that id"
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, customer_id=None):

        response = requests.get(self.url+f"/customers/{customer_id}")
        if customer_id == None:
            return "Could not find customer by that id"
        return response.json()

    # def print_selected_customer(self):
    #     if self.selected_customer:
    #         print(f"Customer with id {self.get_customer['customer_id']} is currently selected\n")
    #         # how are we able to pull a key-value pair directly from a method here?
