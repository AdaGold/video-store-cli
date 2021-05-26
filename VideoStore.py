import requests
import datetime as dt 
import maya




class VideoStore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer


    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_single_video(self, id=None, title=None):
        for video in self.get_all_videos():
            if video["id"] == id:
                self.selected_video = video
            elif video["title"] == title:
                self.selected_video = video
        if self.selected_video == None:
            return "Could not find that video."
        return self.selected_video

    def edit_single_video(self, selected_video):
        new_title = input(f'Update the title for video {selected_video["id"]}:')
        new_release_date = input(f"Update the release date for video {selected_video['id']}:  ")
        date_time_object= maya.parse(new_release_date).datetime()
        new_total_inventory = input(f"Update the total inventory for video {selected_video['id']}:  ")
        query_params = {
            "title": new_title, 
            "release_date": str(date_time_object),
            "total_inventory": new_total_inventory
        }
        response = requests.put(self.url+f'/videos/{selected_video["id"]}', json=query_params)
        if response:
            print("Success!",  response)
        else: 
            print("Oops! Something went wrong. ")
        self.selected_video = response.json()
        return response.json()
    
    def delete_single_video(self, selected_video): 
        response = requests.delete(self.url+f"/videos/{selected_video['id']}")
        print(response)
        if response:
            print(f"The video {selected_video['id']} has been deleted. ")
        else: 
            return "Oops, something went wrong. "
            

