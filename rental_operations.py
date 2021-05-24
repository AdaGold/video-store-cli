import requests
import datetime

class RentalOperations:
    
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_rental = None
    
    def checkout_vid_to_customer(self, customer_id=None, video_id=None):
        pass
    
    def checkin_vid_from_customer(self, customer_id=None, video_id=None):
        pass