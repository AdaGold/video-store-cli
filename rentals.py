
import requests
from requests.api import post
from requests.models import Response

class Rentals:
    def __init__(self, url='https://retro-video-store-api.herokuapp.com', selected_customer=None, selected_video=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video

    def check_out(self,customer_id=None, video_id=None):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id,
        }
        response = requests.post(self.url+"/rentals/check-out", json=query_params )
        return response.json()
    
    def check_in(self,customer_id=None, video_id=None):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id,
        }
        response = requests.post(self.url+"/rentals/check-in", json=query_params )
        return response.json()
