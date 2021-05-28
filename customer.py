import requests
from constants import *
from pprint import pprint

class Customer:
    def __init__(self, url=BACKUP_URL):
        self.url = url
    
    def create_customer(self,name,postal_code, phone):
        query_params = {"name": name,
                        "postal_code": postal_code,
                        "phone": phone}
        response = requests.post(self.url+"/customers",json=query_params)
        return response

    def list_all_customers(self):
        response = requests.get(self.url+"/customers")
        print(response.status_code)
        return response.json()

    def get_customer(self, id): 
        response = requests.get(self.url+f"/customers/{id}")
        if response.status_code == 200:
            return response.json()
        return None

    def update_customer(self, customer, name, postal_code, phone ):  
        if not name: # name = name or customer["name"]
            name = customer["name"]
        if not postal_code:  
            postal_code = customer["postal_code"]
        if not phone: 
            phone = customer["phone"]
        query_params = {"name": name,
                        "postal_code": postal_code,
                        "phone": phone}
        response = requests.put(self.url+f"/customers/{customer['id']}", \
            json=query_params)
        pprint(response)
        return response

    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()
    
        
