import requests
from datetime import datetime

class Rental:
    def __init__(self, url="http://localhost:5000"):
        self.url = url

    def check_out(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",
        json=query_params)
        return response.json()

    def check_in(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",
        json=query_params)
        return response.json()
