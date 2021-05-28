import requests
import datetime

class CustomerRequests:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        #I dont understand what this attributes is/what is being giveh here for "selected_customer?"
        self.selected_customer = selected_customer

    def create_customer(self, name=None, postal_code=None, phone=None):
        
        query_params = {
            "name" : name,
            "postal_code" : postal_code,
            "phone": phone
        }

        response = requests.post(self.url+f"/customers",json=query_params)
        return response.json()

    def list_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_specific_customer(self, name=None, id=None):
        
        for customer in self.list_all_customers():

            if name:
                if name == customer["name"]:
                    id = customer["id"]
                    self.selected_customer = customer
                elif name != customer["name"]:
                    print("That name could not be found")
                    #not sure how to handle the error that occurs when a name
                    #is inputted that ahs no match in the database

            elif id == customer["id"]:
                self.selected_customer = customer
            
            #return self.selected_customer
            
        response = requests.get(self.url+f"/customers/{id}")
        #self.selected_customer = response.json()
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):

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

        #print("Customer successfully updated:", response)
        self.selected_customer = response.json() 
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    def print_customer(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")