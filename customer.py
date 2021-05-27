import requests 
import datetime 

#all for customer 
class Customer: 
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        # self.selected_video = selected_video
        self.selected_customer = selected_customer 

    #6 - add a customer so that I can check out videos to the customer
    def create_customer(self,title="title",postal_code="postal_code",phone="phone"):
        query_params = {
            "title": title,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    #7 - edit a customer so that the information about the customer is accurate 
    def update_customer(self,title="title",postal_code="postal_code",phone="phone"):
        if not title:
            title = self.selected_customer["title"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone =self.selected_customer["phone"]

        query_params = {
        "title": title,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()

    #8 - delete a customer so that the customer is no longer in the store records 
    def delete_task(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

    #9 - get informaton about one customer so that I can see how many videos a customer had rented currently 
    def get_customer(self, title="title", postal_code="postal_code", phone="phone"):
        
        for customer in self.get_customers():
            if title:
                if customer["title"]==title:
                    id = customer["id"]
                    self.get_customers = customer
            elif id == customer["id"]:
                self.get_customers = customer

        if self.get_customers == None:
            return "Could not find customer by that title or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
    
    #10 - get information about all customers so that I can how many customers the store has
    def list_tasks(self):
        response = requests.get(self.url+"/customers")
        return response.json()
