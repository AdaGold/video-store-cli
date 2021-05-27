from video import Video
from constants import BACKUP_URL
import requests
from pprint import pprint

class Rental:
    def __init__(self, url=BACKUP_URL):
        self.url = url

    # VIDEO METHODS
    #---------------------------------------------------------------
    # POST / CREATE VIDEO  # - 
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
    