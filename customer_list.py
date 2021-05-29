import requests
# import datetime

class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def add_customer(self, name, postal_code, phone_num):
        query_params = { 
            "name": name,
            "postal_code": postal_code,
            "phone": phone_num 
        }

        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def get_customer(self, name=None, id=None):

        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    self.selected_customer = customer
                    id = customer["id"]
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id."

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name, postal_code, phone_num):
        query_params = { 
            "name": name,
            "postal_code": postal_code,
            "phone": phone_num
        }

        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}", json=query_params)
        self.selected_customer = response
        return response.json()

    def delete_customer(self):

        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
