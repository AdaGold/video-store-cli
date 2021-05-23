import requests


class Employee:
    def __init__(self, url="http://localhost:5000", action=None):
        self.url = url
        self.action = action

    def add_video(
            self,
            title="Default Title",
            release_date="",
            total_inventory=0):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url + "/videos", json=query_params)
        return response.json()


class Customer:
    pass
