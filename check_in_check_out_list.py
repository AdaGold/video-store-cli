import requests
import datetime
from requests.models import Response

class CheckInOut:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    def checkin_video_from_customer(self, customer_id, video_id):
        checkin_video ={
            "customer_id":customer_id,
            "video_id":video_id
        }
        r=requests.post(self.url+f"/rentals/check-in", json=checkin_video)
        return r

    def checkout_video_to_customer(self, customer_id, video_id):
        checkout_video ={
            "customer_id":customer_id,
            "video_id":video_id
        }
        r=requests.post(self.url+f"/rentals/check-out", json=checkout_video)
        return r