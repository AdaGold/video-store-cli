import requests
from customer import Customer
from video import Video

# look at the user stories here for each path 
class Rental:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com"):
        self.url = url
        self.selected_rental = None



    # "11" : "Check out 1 Video" 
    def check_out(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=request_body)
        return response

    #  "12": "Check in 1 Video Return" 
    def check_in(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=request_body)
        return response 