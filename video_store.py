import requests

class VideoStore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    def create_video(self, title="default", release_date="default", total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()