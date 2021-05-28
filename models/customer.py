import requests
from datetime import datetime

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

    def update_customer(self, customer_id=None, name=None, postal_code=None,
        phone=0):

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(self.url+f"/customers/{customer_id}",
            json=query_params)
        if response.status_code != 200:
            return "Could not find customer by that id"
        print("response:", response)
        return response.json()

    def delete_customer(self, customer_id=None):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        if response.status_code != 200:
            return "Could not find customer by that id"
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, customer_id=None):
        response = requests.get(self.url+f"/customers/{customer_id}")
        if response.status_code != 200:
            return "Could not find customer by that id"
        return response.json()
