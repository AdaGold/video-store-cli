import requests
import datetime

class RentalList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def check_out_video(self,customer_id,video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        print(response)
        print(response.json())
        return response

    def check_in_video(self,customer_id,video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        print(response)
        print(response.json())