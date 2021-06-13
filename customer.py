import requests
import datetime

class Customer:
    def __init__(self, url="http://localhost:5000"):
        self.url = url

    
    def create_customer(self, customer_name, postal_code, phone_number):
        
        query_params = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url+"/customers", json=query_params)

        return response.json()

    def update_customer(self, customer_id=None, name=None, postal_code=None, phone_number=None):
        
        if not name:
            name = name["name"]
        if not postal_code:
            postal_code = postal_code["postal_code"]
        if not phone_number:
            phone_number = postal_code["phone"]

        query_params = {
            "name": name,
            "postal code": postal_code,
            "phone": phone_number
        }

        response = requests.put(self.url+f"/customers/{customer_id}", json=query_params)

        return response.json()


    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()


    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()


    def get_specific_customer(self, customer_id):
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

