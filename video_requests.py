import requests
import datetime

#talks to api/holds info about talking to api about videos

class VideoRequests: 
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None): #so you can select customer with video?
        self.url = url
        self.selected_video = selected_video

    def create_video(self, title="Default Title", release_date="Default date", total_inventory="Default Description"):
        query_params = {
            "title" : title,
            "release_date" : release_date,
            "total_inventory": total_inventory
        }

        response = requests.post(self.url+"/videos",json=query_params)
        self.selected_video = response.json()
        return response.json()

    def list_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_specific_video(self, title=None, id=None):
        #you can do a get request with id number of video/can use it to get one specific task with a get request
        
        for video in self.list_all_videos():
    
            if title:
            #if api can query by title then this for loop is not necessary
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video

            elif id == video["id"]:
                self.selected_video = video
        
        #if we didnt have a route that connects to the API that does all of this work already,
        #then we would do the above, otherwise all that is needed is these lines below
        response = requests.get(self.url+f"/videos/{id}") #could also return video from line 29 becuase that is a get rewuest for the same thing
        self.selected_video = response.json()
        return response.json()
    

    def update_video(self, title=None, release_date=None, total_inventory=None):
        #should total_inventory default be 0?
        #if I provide an id here can I just send the query_params to the endpoint with the id and then
        #have the API do the work?

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
        self.selected_video = response.json()
        #["video"] /Do I want this format?
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def print_video(self):

        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")
