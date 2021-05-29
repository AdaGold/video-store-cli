import requests
import datetime


class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    def add_customer(self, name="Default Customer", postal_code="1922-01-01", phone=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()
    # Number 4 GET all customers

    def list_customer(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id):

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def edit_customer(self):

        query_params = {
            "name": self.selected_customer['name'],
            "postal_code": self.selected_customer['postal_code'],
            "phone": self.selected_customer['phone']
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
        )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    #pass in id directly
    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        self.selected_customer = None
        return response.json()

    def mark_complete(self):
        response = requests.patch(
            self.url+f"/customers/{self.selected_customer['id']}/mark_complete")
        self.selected_customer = response.json()["customer"]
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(
            self.url+f"/customers/{self.selected_customer['id']}/mark_incomplete")
        self.selected_customer = response.json()["customer"]
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(
                f"Customer with id {self.selected_customer['id']} is currently selected\n")
