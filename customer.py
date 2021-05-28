from datetime import datetime
import requests

class CustomerOps:
    def __init__(self, url, selected_customer):
        self.url = url 
        self.selected_customer = selected_customer

    def add_customer(self, name, phone, postal_code):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def update_customer(self, name, phone, postal_code):
        query_params = {            
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.put(self.url+"/customers/"+self.selected_customer["id"], json=query_params)
        return response.json()

    def delete_customer(self):
        response = requests.delete (self.url+f"/customers/{id}")
        return response.json()

    def list_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id):
        response = requests.get(self.url+"/customers/"+str(id))
        response = response.json()
        self.selected_customer=response
        return response
    
    def print_selected(self):
        print(self.selected_customer)
        return