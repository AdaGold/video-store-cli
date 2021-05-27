import requests
import datetime

class Customer:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        #self.selected_customer = selected_customer #or selected_action?

    def create_customer(self, customer_name="Default Name", postal_code="0", phone_number="0"):
        query_params = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url + "/customers", json=query_params)
        return response.json()

    def update_customer_info(self, customer_name="Default Name", postal_code="0", phone_number="0" ):
        query_params = {
            "name": customer_name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url + "/customers/{customer_id}", json=query_params)
        return response.json()

    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, customer_id=None):
        for customer in self.all_customers():
            if customer_id:
                if customer["customer_id"]==customer_id:
                # id = customer["id"]
                    self.selected_customer = customer
            if self.selected_customer == None:
                return "No customer found"
            else:
                return "ID necessary"
        
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

    def delete_customer(self, customer_id=None):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()
