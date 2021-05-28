
import requests

class CustomerOperations:

    def __init__(self, url="http://localhost:5000"):
        self.url = url

         
    def add_customer(self, name="default customer name", phone="default phone number", postal_code=0):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()
    
    def edit_customer(self,customer_id, name=None, phone=None, postal_code=None): 
             
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone}
        
        response = requests.put(
            self.url+f"/customers/{customer_id}", 
            json=query_params
            )
        print("response:", response)
        return response.json()


    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()
    
    
    def get_all_customer_information(self):
        response = requests.get(self.url+"/customers")
        return response.json()
    
    
    def get_one_customer_information(self, cust_id):
        response = requests.get(self.url+f"/customers/{cust_id}")
        return response.json()
        