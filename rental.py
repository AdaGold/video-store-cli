import requests

class Rental:
    def __init__(self, url = "https://localhost:5000", selected_customer = None, selected_video=None):
        self.url = url

    def check_in(self):
        response = requests.patch(self.url+"/rentals/check-in")
        return response.json()
    
    def check_out(self, customer_id, video_id):
        response = requests.get(self.url+"/rentals/check-out")
        return response.json()