import datetime
import requests


class Customers:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer= None):
        self.url = url 
        self.selected_customer = selected_customer
        

    # def customer_not_found():
    # return "No customer with that id or name has been found."
    
    def add_customer(self, name=None, postal_code=None, phone=None):
        
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        
        url = self.url+"/videos"
        response = requests.post(url, json=query_params)
        return response.json()
    
    
    def update_customer(self,customer_id, name=None, phone=None, postal_code=None): 
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self. selected_customer["postal_code"]
        
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone 
        }
        
        response = requests.put(self.url+f"/customers/{customer_id}", 
            json=query_params)
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()
    
    
    def delete_customer(self, customer_id=None):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        if None:
            return "Customer not found"
        print(response)
        return response.json()
    
    
    
    def get_one_customer(self, customer_id=None):
        response = requests.get(self.url+f"/customers/{customer_id}")
        if None:
            return "Customer not found"
        return response.json()


    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
        
    
   
    