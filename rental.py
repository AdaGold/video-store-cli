import requests
import datetime

class Rental: 
    def __init__(self, url="https://retro-video-store-api.herokuapp.com",selected_customer=None, selected_video=None):
        self.url = url 
        self.selected_customer = selected_customer
        self.selected_video = selected_customer

    # check out a video 
    def check_out_video(self, customer_id=None, video_id=None): 
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        return response.json()

    # check in a video 
    def check_in_video(self, customer_id=None, video_id=None): 
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        return response.json()
    
    # get rental 