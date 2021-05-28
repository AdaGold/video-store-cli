# RENTALS
# * check out a video to a customer
# * check in a video from a customer
# * look up all overdue videos (optional)

import requests
import datetime

class Rentals:
    def __init__(self, url="https://whits-video-store.herokuapp.com/rentals"):
        self.url = url

    def get_all_rentals(self):
        response = requests.get(self.url)
        return response.json()

    def get_all_overdue(self):
        response = requests.get(self.url+"/overdue")
        return response.json()

    def check_out(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/check-out", json=query_params)
        return response.json()

    def check_in(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/check-in", json=query_params)
        return response.json()