import requests
from requests.api import post

BACKUP_URL = "https://retro-video-store-api.herokuapp.com"



class Customer():#is this class getting info from the customer.py file in the API about its behaviors,datatypes? what is the purpose of creating this class?
    def __init__(self, url=BACKUP_URL,selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
       
    
    # def create_customer(self,name,postal_code,phone):# instance of Customer is being created here correct? its referring to the API for acceptable datatypes written in the API?
        
    #     query_params = {
    #     "name": name,
    #     "postal_code": postal_code,
    #     "phone": phone
    #     }
    #     response = requests.post(self.url+"/customers",json=query_params)#matches up with what API is expecting
    #     return response.json()
    
    
    # def list_customers(self):
    #     response = requests.get(self.url+"/customers")#sends out a get request to API? what value is response holding?
    #     return response.json()#turning response into readable python dicts
    
    
    # def get_customer(self,id=None):# user input determines value of id
        
    #     response = requests.get(self.url+f"/customers/{id}")#what is the order of transactions that happen here with the url?
    #     return response.json()
    
  
   


    
    