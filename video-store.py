import requests

class VideoStore:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", video, customer, rental):
        self.url = url
        self.video = video 
        self.customer = customer
        self.rental = rental

    def add_video(self, title = "Default Title", release_date = None, total_inventory = None):
        query_params = {
            "title" : title,
            "release date" : release_date,
            "total_inventory" : total_inventory
        }
        response = requests.post(self.url+"/videos", json = query_params)
        return response.json()