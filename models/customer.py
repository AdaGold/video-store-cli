import requests
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

class Customer:
    def __init__(self, url=BACKUP_URL, selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def create_customer(self, name="Default Customer", postal_code=0, phone="Default Postal Code"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()
    
    def list_customers(self):
        response = requests.get(self.url + "/customers")
        return response.json()


    def get_one_customer(self, customer_id= None):
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

    def update_customer(self, customer_id, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{customer_id}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected")
        else:
            print("There is no selected customer.")