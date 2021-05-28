import requests
import datetime
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

class Rental:
    def __init__(self, url=BACKUP_URL, selected_customer=None, selected_video=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video

    def check_out(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response.json()

    def check_in(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        return response.json()