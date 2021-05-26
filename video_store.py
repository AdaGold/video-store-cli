import requests


class Employee:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

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

    def list_all_videos(self):
        response = requests.get(self.url + "/videos")
        return response.json()

    def get_one_video(self, id=None):
        for video in self.list_all_videos():
            if video["id"] == id:
                self.selected_video = video

    def update_video(self):
        pass

    def delete_video(self):
        response = requests.delete(
            self.url + f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()


class Customer:
    pass
