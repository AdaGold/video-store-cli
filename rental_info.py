import requests
import datetime

class RentalInfo:
    # Where the CLI is accessing the DB, chose to access my local machine
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_rental = None
    
    # Video store employee checking out a video to a customer 
    def checkout_vid_to_customer(self, customer_id, video_id,):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=response_body)
        return response
        
    # Video store employee checking in a video from a customer 
    def checkin_vid_from_customer(self, customer_id, video_id):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=response_body)
        return response

    # def print_selected(self):
    #     if self.selected_rental:
    #         print(f"Rental with id {self.selected_customer['customer_id']} is currently selected\n")