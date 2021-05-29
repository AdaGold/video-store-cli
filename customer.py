import requests
import datetime

class Customer:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    # "6": "New Customer Sign Up"
    def create_new_customer(self,name="Default Name",postal_code="Default Description",phone="Defult Phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    ## "10": "View all Customers"
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    #    # "9": "View Rental Info on 1 Customer"
    def get_customer(self, name=None, id=None):
        
        for customer in self.list_customers():
            if name:
                if name == customer["name"]:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            print( "Could not find customer by that name or id")

        return self.selected_customer     
        ## other wise if the customer is there 
        #response = requests.get(self.url+f"/customers/{id}")
        #return response.json()

    # "7": "Update a Customer's Information" 
    def update_customer(self,name=None,postal_code=None, phone=None):
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
        return response.json()
    # "8": "Delete 1 Customer "
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
        
    
    # this will show up after a customer has been selected and you want to move on to another customer related option 
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")      