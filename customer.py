import requests
import datetime


class Customer: 
    def __init__(self, url="https://retro-video-store-api.herokuapp.com",selected_customer=None):
        self.url = url 
        self.selected_customer = selected_customer
    
    # add a customer 
    def add_customer(self, name=None, postal_code=None, phone=None):
        query_params = {
            "name": name, 
            "postal_code": postal_code,
            "phone": phone
        }

        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()

    # get info on all customers 
    def list_customers(self): 
        response = requests.get(self.url+"/customers")
        return response.json()
    
    # get a customer by id
    def get_customer_by_id(self, name=None, id=None):
        
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    # assigning attribute to the data customer (an iteration in the list of customers)
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer
        # ^ if there was no customer found by id or title -> self.selected_customer = None 
        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    # update a customer 
    def update_customer(self, name=None, postal_code=None, phone=None):
        # if these attributes aren't given, will assign them the same value as before(keep it the same)
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone: 
            phone = self.selected_customer["phone"]

        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        # not sure what next line is doing 
        self.selected_customer = response.json() # prints <Response [200]>
        return response.json()

    # delete a customer 
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    # print selected customer 
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected")
        else:
            print("There is no selected customer.")
