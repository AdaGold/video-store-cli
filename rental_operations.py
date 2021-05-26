import requests
import datetime

class RentalOperations:
    
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_rental = None
    
    def checkout_vid_to_customer(self, customer_id, video_id,):
        req_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=req_body)
        return response
        
    
    def checkin_vid_from_customer(self, customer_id, video_id):
        req_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=req_body)
        return response