import requests
import datetime

class RentalRequests:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental
    
    def create_rental(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/check-out")

    def check_out_video(self, customer_id=None, video_id=None):
        #do I send the same query params here? 
        # query_params = {
        #     "customer_id": customer_id,
        #     "video_id": video_id
        # }
        pass

    def check_in_video(self, customer_id=None, video_id=None):
        #do I send the same query params here? 
        # query_params = {
        #     "customer_id": customer_id,
        #     "video_id": video_id
        # }
        pass



