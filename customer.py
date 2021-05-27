import requests
import datetime
from constants import *
from pprint import pprint

class Customer:
    def __init__(self, url=BACKUP_URL):
        self.url = url
    
    # POST / CREATE CUSTOMER  #8 - WORKS
    def create_customer(self,name,postal_code, phone):
        query_params = {"name": name,
                        "postal_code": postal_code,
                        "phone": phone}
        response = requests.post(self.url+"/customers",json=query_params)
        return response
    # GET ALL CUSTOMERS #7  - WORKS
    def list_all_customers(self):
        response = requests.get(self.url+"/customers")
        print(response.status_code)
        return response.json()

    # GET CUSTOMER by ID #9 - WORKS
    def get_customer(self, id): 
        response = requests.get(self.url+f"/customers/{id}")
        if response.status_code == 200:
            return response.json()
        return None
        # return response.json()

    # PUT/UPDATE by ID  #10 - WORKS
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
        # print("response:", response) # test
        pprint(response)
        return response

    # DELETE by /ID  #11 - WORKS
    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()
    
        
