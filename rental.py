import requests

class Rental:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com"):
        self.url = url
    
    # checks in a video(id specified) from a customer(id specified)
    def check_in(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = self.get(self.url+"/rentals/check-in", json=query_params)
        # response not jsonified to retain data structure specific methods
        return response

    # checks out a video(id specified) to a customer(id specified)
    def check_out(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = self.get(self.url+"/rentals/check-out", json=query_params)
        # response not jsonified to retain data structure specific methods
        return response