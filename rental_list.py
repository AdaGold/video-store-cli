import requests


class RentalList:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental
    
    def create_rental(self, customer_id, video_id,):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=response_body)
        return response

    def return_rental(self, customer_id, video_id):
        response_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=response_body)
        return response
