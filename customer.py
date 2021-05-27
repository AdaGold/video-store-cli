import requests
import datetime

class Customer:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    # DISPLAY LIST OF ALL CUSTOMERS -----------------------------------------------------------------
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    # CREATE A CUSTOMER -----------------------------------------------------------------------------
    def create_customer(self,name="Default Name",postal_code="Default Postal_code",phone="Phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    # GET A SPECIFIC CUSTOMER BY NAME OR ID ----------------------------------------------------------
    def get_customer(self, name=None, id=None):
        
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer
        if self.selected_customer == None:
            return "Could not find customer by that name or id"
        response = requests.get(self.url+f"/customer/{id}")
        return response.json()

    # UPDATE A SPECIFIC CUSTOMER BY NAME OR ID--------------------------------------------------------
    def update_customer(self,name=None,id=None):
        if not name:
            name = self.selected_customer["name"]
        if not id:
            id = self.selected_customer["id"]

        query_params = {
        "name": name,
        "id": id
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()

    # DELETE A SPECIFIC CUSTOMER -------------------------------------------------------------------------
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    
    # ONE CUSTOMER IS CURRENLTY SELECTED --------------------------------------------------------------------
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")

    # DISPLAY MENU FOR CUSTOMER OPTIONS
    def menu(self):
        print("Choose from the list of options")
        print("1. Display all customer")
        print("2. Create a new customer")
        print("3. Display a customer")
        print("4. Update a customer")
        print("5. Delete a customer")
        print("6. Go back to main menu")