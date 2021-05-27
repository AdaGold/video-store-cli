import requests

class CustomerInfo:
    # Where the CLI is accessing the DB, chose to access my local machine 
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_customer = None
        
    # Video store employee adding a new customer 
    def add_customer(self, name="default customer name", phone="default phone number", postal_code=0):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()
    
    # Video store employee viewing ALL current customers  
    def get_all_customer_information(self):
        response = requests.get(self.url+"/customers")
        return response.json()
    
    # Video store employee veiwing one customer by ID
    def get_one_customer_information(self, customer_id):
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()
        
    # Video store employee deleting a customer by ID 
    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()
    
    # Video store employee editing an existing customer by ID 
    def edit_customer(self,customer_id, name=None, phone=None, postal_code=None): 
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self. selected_customer["postal_code"]
        
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone}
        
        response = requests.put(
            self.url+f"/customers/{customer_id}", 
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    # Video store employee viewing a specific customer 
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['customer_id']} is currently selected\n")

    
    
