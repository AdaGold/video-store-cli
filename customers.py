import requests
import datetime     

class Customer:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    def create_customer(self, name = "Default Name", phone = "default phone", postal_code = 00000):
        query_params = {
            "name" : name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if not customer:
                return "No customer with that name or id"
            if customer["name"]==name:
                id = customer["id"]
                self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name = None, phone = None, postal_code = None):
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]

        query_params = {
        "name": name,
        "phone": phone,
        "postal_code": postal_code
        }

        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params)
        print("response:", response)
        self.selected_customer = response.json()["name"]
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    