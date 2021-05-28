import requests
# from datetime import datetime

class Customer:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    # adds a customer to the connected API with the specified query parameters
    def add_customer(self,name="Default Name",postal_code=None,phone=None, registered_at=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            # "registered_at": datetime.now()
        }
        response = requests.post(self.url+"/customers", json = query_params)
        return response.json()
    # generates a list of all customers
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
    
    # retrieves customer specific data - with options to
    # search by name, phone or id
    def get_customer(self, name=None, phone=None, id=None):

        for customer in self.list_customers():
            if name:
                if customer["name"]== name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif phone:
                if customer["phone"] == phone:
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer
            
        if self.selected_customer == None:
            return "Could not find customer by that name or id"
        
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    # updates customer in the connected API with specified query parameters
    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code =  self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}",
                                json=query_params)
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()
    
    # deletes a customer by id
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    # prints out the selected customer's data
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer {self.selected_customer['name']} with id {self.selected_customer['id']} is currently selected\n")
        else:
            print("Apologies, that customer could not be found")
