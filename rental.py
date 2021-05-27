import requests

class Rental:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com"):
        self.url = url

    def check_in(self):
        response = self.get(self.url+"/check-in")
        return response.json()
    
    def check_out(self):
        response = self.get(self.url+"/check-out")
        return response.json()