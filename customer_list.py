import requests
import datetime
from requests.api import post

from requests.models import Response

class CustomerList:
    def __init__(self, url='https://retro-video-store-api.herokuapp.com', selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def get_customer(self, name=None, id=None):
        for customer in self.list_all_customers():
            if customer["id"] == id:
                self.selected_customer = customer

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def create_customer(self, name="default", postal_code="default", phone="default"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=query_params )
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response.json())
        # self.selected_task = response.json()["customer"]
        return response.json()

    def list_all_customers(self):
        response = requests.get(self.url +"/customers")
        return response.json()
        
    def delete_customer(self, id=None):
        response = requests.delete(self.url +f"/customers/{self.selected_customer['id']}")
        return response.json()

    def get_rentals(self):
        # get customer
        response = requests.get(self.url +f"/customers/{self.selected_customer['id']}/rentals")
        return response.json()

