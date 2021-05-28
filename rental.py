import requests
import datetime


class Rental:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    def check_out(self, video_id=None, customer_id=None):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id
        }
        response = requests.post(
            self.url+"/rentals/check-out", json=query_params)
        return response.json()

    def check_in(self, video_id=None, customer_id=None):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id
        }
        response = requests.post(
            self.url+"/rentals/check-in", json=query_params)
        return response.json()
