# VIDEOS
# * Add a video
# * Edit a video
# * Delete a video
# * get info about a video
# * get info about all videos
# * look up videos by genre (optional)
# * look up videos by title (optional) <<<
# * look up who has checked out a particular video (optional) <<<

import requests
import datetime

class Videos:
    def __init__(self, url="https://whits-video-store.herokuapp.com/videos"):
        self.url = url

    def add_video(self, title="Default Video", release_date=None, genre=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "genre": genre,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url, json=query_params)
        response_body = response.json()
        video_info = requests.get(self.url+f"/{response_body['id']}")
        return video_info.json()

    def list_videos(self):
        response = requests.get(self.url)
        return response.json()

    def get_video(self, title=None, id=None):
        
        selected_video = None

        for video in self.list_videos():
            if title:
                if video['title']==title:
                    id = video["id"]
                    selected_video = video
            elif id == video["id"]:
                selected_video = video
        
        if selected_video == None:
            return "Could not find video"

        response = requests.get(self.url+f"/{id}")
        return response.json()


    def get_videos_by_genre(self, genre=None):

        selected_videos = [video for video in self.list_videos() if video['genre'] == genre]

        if len(selected_videos) == 0:
            return "No matching videos found"

        return selected_videos


    def update_video(self, id=None, title=None, release_date=None, genre=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "genre": genre,
            "total_inventory": total_inventory
        }

        response = requests.put(self.url+f"/{id}", json=query_params)

        return response.json()

    def delete_video(self, id=None):
        response = requests.delete(self.url+f"/{id}")
        return response.json()


    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")