from constants import *
import requests


class Rental:
    def __init__(self, url=BACKUP_URL):
        self.url = url

    def check_out(self, video_id, customer_id):
        query_params = {"video_id": video_id,
                        "customer_id": customer_id}
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response

    def check_in(self, video_id, customer_id):
        query_params = {"video_id": video_id,
                        "customer_id": customer_id}
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        return response
    