import requests
import datetime

class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    # DISPLAY LIST OF ALL CUSTOMERS -----------------------------------------------------------------
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    # CREATE A CUSTOMER -----------------------------------------------------------------------------
    def create_customer(self,name,postal_code, phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    # GET A SPECIFIC CUSTOMER BY NAME OR ID ----------------------------------------------------------
    def get_customer(self, id):
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    # UPDATE A SPECIFIC CUSTOMER BY NAME OR ID--------------------------------------------------------
    def update_customer(self, id, name, postal_code, phone):

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{id}",
            json=query_params
            )
        return response.json()

    # DELETE A SPECIFIC CUSTOMER -------------------------------------------------------------------------
    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        self.selected_customer = None
        return response.json()

    
    # ONE CUSTOMER IS CURRENLTY SELECTED --------------------------------------------------------------------
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")

#