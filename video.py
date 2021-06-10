import requests


class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    # add a video
    def add_video(self, title="Default Title", release_date=None, total_inventory=0, available_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }

        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    # get info on all videos
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    # get a video
    def get_video(self, title=None, id=None):

        for video in self.list_videos():
            if title:
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    # edit a video
    def edit_video(self, title=None, release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
        )
        print("response:", response)
        self.selected_video = None
        return response.json()

    # delete a video
    def delete_video(self):
        response = requests.delete(
            self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
