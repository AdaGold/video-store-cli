import requests
from datetime import datetime


class RentalOps():
    def __init__(self, url= "https://retro-video-store-api.herokuapp.com"):
        self.url = url
        self.selected_rental = None

    def check_out(self, customer_id, video_id):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=response_body)
        return response

    def check_in(self, customer_id, video_id):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=response_body)
        return response
