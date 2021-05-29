import requests
import datetime

class Customer:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def create_customer(self, customer_name, postal_code, phone_number):
        request_body = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url+"/customers",json=request_body)
        return response.json()


    def update_customer(self, customer_name=None, postal_code=None, phone_number=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone_number:
            phone_number = self.selected_customer["phone"]

        query_params = {
        "name": customer_name,
        "postal code": postal_code,
        "phone": phone_number
        }

        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}", 
            json=query_params)
        return response.json()


    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()


    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()


    def get_specific_customer(self, name=None, id=None):

        for customer in self.all_customers():
            if name:
                if customer["name"] == name:
                    id = customer["id"]
                    self.selected_customer = customer
                elif id == customer["id"]: 
                    self.selected_customer = customer

            if self.selected_customer == None:
                return "Could not find task by that name or ID."

        response = request.get(self.url+f"/customers/{id}")

        print("response:", response)
        self.selected_customer = response.json()["customer"]

        return response.json()


    def print_selected(self):
        if self.selected_task:
            print(f"Task with id {self.selected_task['id']} is currently selected\n")