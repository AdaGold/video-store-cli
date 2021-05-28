import requests
import datetime


class Customer:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_one=None):
        self.url = url
        self.selected_one = selected_one

    def create_customer(self, name="Default Customer", postal_code="Default Postal", phone="Default Phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if name:
                if name["title"] == name:
                    id = customer["id"]
                    self.selected_one = customer
            elif id == customer["id"]:
                self.selected_one = customer

        if self.selected_one == None:
            return "Could not find customer by that name or ID"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def upgrade_customer(self, id=None, name=None, postal_code=None, phone=None):
        if not name:
            title = self.selected_one["name"]
        if not postal_code:
            release_date = self.selected_one["postal_code"]
        if not phone:
            total_inventory = self.selected_one["phone"]

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_one['id']}",
            json=query_params
        )
        print("response:", response)
        # self.selected_video = response.json()["video"]
        return response.json()

    def delete_customer(self):
        response = requests.delete(
            self.url+f"/customers/{self.selected_one['id']}")
        self.selected_one = None
        return response.json()
