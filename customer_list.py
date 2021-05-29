import requests
import datetime

class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def create_customer(self,title="Default customer",description="Default Description",completed_at=None):
        query_params = {
            "title": title,
            "description": description,
            "completed_at": completed_at
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, title=None, id=None):
        
        for customer in self.list_customers():
            if title:
                if customer["title"]==title:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self,title=None,description=None):
        if not title:
            title = self.selected_customer["title"]
        if not description:
            description = self.selected_customer["description"]

        query_params = {
        "title": title,
        "description": description
        #"completed_at": self.selected_customer["is_complete"]
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    def mark_complete(self):
        response = requests.patch(self.url+f"/customers/{self.selected_customer['id']}/mark_complete")
        self.selected_customer = response.json()["customer"]
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(self.url+f"/customers/{self.selected_customer['id']}/mark_incomplete")
        self.selected_customer = response.json()["customer"]
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(f"customer with id {self.selected_customer['id']} is currently selected\n")


        
