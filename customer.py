import requests
import datetime

class Customer:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer 

    def create_customer(self, customer_name="Default Name", postal_code="0", phone_number="0"):
        query_params = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url + "/customers", json=query_params)
        return response.json()

    def update_customer_info(self, customer_id=None, customer_name="Default Name", postal_code="0", phone_number="0",):
        
        query_params = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.put(self.url + f"/customers/{customer_id}", json=query_params)
        return response.json()

    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, customer_id=None):

        
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

    def delete_customer(self, customer_id=None):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()

