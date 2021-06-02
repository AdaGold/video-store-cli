import requests
import datetime

class Customer:
    def __init__(self, URL="https://retro-video-store-api.herokuapp.com", customer=None):
        self.url = URL
        self.customer = customer

    def create_customer(self,id="Default ID",name="Default Name",phone="Default Phone Number",postal_code="Default Postal Code",registered_at=0,videos_checked_out_count=
        query_params = {
                "id": customer_id,
                "name": name,
                "phone": phone,
                "postal_code": postal_code,
                "registered_at": registered_at,
                "videos_checked_out_count": videos_checked_out_count
        }
        response = requests.post(self.url+"/tasks",json=query_params)
        return response.json()