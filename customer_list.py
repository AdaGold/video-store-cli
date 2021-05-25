import requests
import datetime

class CustomerList:
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer

    # list all videos (see store stock)
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()