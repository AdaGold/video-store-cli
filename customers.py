import requests
import datetime

# CUSTOMERS
# * add a customer
# * edit customer information
# * delete a customer
# * get info about a customer
# * get info about all customers
# * look up what videos a customer has checked out (optional) <<<

class Customers:
    def __init__(self, url="https://whits-video-store.herokuapp.com/customers", selected_customer=None):
        self.url = url

    def add_customer(self, name=None, postal_code=None, phone=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url, json=query_params).json()
        customer_info = requests.get(self.url+f"/{response['id']}")
        return customer_info.json()

    def list_customers(self):
        response = requests.get(self.url)
        return response.json()

    def get_customer(self, name=None, id=None, phone=None):

        selected_customer = None

        for customer in self.list_customers():
            if name:
                if customer["name"] == name:
                    id = customer["id"]
                    selected_customer = customer
            elif phone:
                if customer["phone"] == phone:
                    id = customer["id"]
                    selected_customer == customer
            elif id == customer["id"]:
                selected_customer = customer

        if selected_customer == None:
            return "Could not find customer"

        response = requests.get(self.url+f"/{id}")
        return response.json()

    def get_customer_rentals(self, id=None):
        response = requests.get(self.url+f"/{id}/rentals")
        return response.json()
    

    def update_customer(self, id=None, name=None, phone=None, postal_code=None):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.put(self.url+f"/{id}", json=query_params)
        return response.json()

    def delete_customer(self, id=None):
        response = requests.delete(self.url+f"/{id}")
        return response.json()