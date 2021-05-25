import requests
from datetime import datetime

class Customer:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    def create_customer(self, name="Default Name", postal_code="Default Postal Code", phone="Phone", \
                    registered_at=datetime.now().strftime("%a, %d %b %Y, %H:%M:%S"), videos_checked_out_count=0):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "registered_at": registered_at,
            "videos_checked_out_count": videos_checked_out_count
        }
        response = requests.post(self.url+"/customers", json=query_params)
        # print("*****", response)
        # print("*****", response.json())
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, name=None, id=None):

        for customer in self.list_customers():
            if name:
                if customer["name"] == name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        print("***", self.selected_customer["name"])
        print("***", self.selected_customer["postal_code"])
        print("***", self.selected_customer["phone"])

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }

        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
        )
        print("reponse:", response)
        print("response.json", response.json())
        # print("customer", response.json()["customer"])
        self.selected_customer = response.json()#["customer"]
        return response.json()

    def delete_customer(self, id=None, name=None):
        for customer in self.list_customers():
            if name:
                if customer["name"] == name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    def get_customer_rentals(self):
        response = requests.get(self.url+f"/customers/{self.selected_customer['id']}/rentals")
        self.selected_customer = response.json()["rental"]
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(f"Task with id {self.selected_customer['id']} is currently selected\n")

