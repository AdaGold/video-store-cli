import requests
# import datetime

class RentalList:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    def check_out(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }

        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        self.selected_rental = response
        return response.json()

    def check_in(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }

        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        self.selected_rental = response
        return response.json()


