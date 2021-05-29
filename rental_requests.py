import requests
import datetime

class RentalRequests:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental
    
    def create_rental(self, customer_id=None, video_id=None):
        
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+f"/rentals/check-out", json=request_body)

        return response.json()

    def check_in_video(self, customer_id=None, video_id=None): 

        if not customer_id:
            customer_id = self.selected_rental["customer_id"]
        
        if not video_id:
            video_id = self.selected_rental["video_id"]
        
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        
        response = requests.post(
            self.url+f"/rentals/check-in", 
            json=request_body
        )

        print(f"This is the response for the check-in {response}")
        




