import requests

class Rental:
    def __init__(self, url = "https://localhost:5000", selected_customer = None, selected_video=None):
        self.url = url

    def check_in(self, customer_id, video_id):
#checks in a video with query_params collected from MAIN
        query_params = {
            "customer_id": customer_id,
            "video_id" : video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json = query_params)
        return response
    
    def check_out(self, customer_id, video_id):
#checks out a video
        query_params = {
            "customer_id": customer_id,
            "video_id" : video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json = query_params)

        return response
    

