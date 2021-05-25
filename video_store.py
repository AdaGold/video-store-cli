import requests

class VideoStore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    # "1": "Add a Video" 
    def create_video(self, title="default", release_date="default", total_inventory=0):
        #consider validating release date format because if it's entered incorrectly, CRASH!
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    # "2": "Edit a Video"


    # "3": "Delete a Video"
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    # "4": "Get all Videos"
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    # "5": "Get One Video"
    def get_video(self, title=None, id=None):
    
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return None

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    # "6": "Add a Customer"
    # "7": "Edit a Customer"
    # "8": "Delete a Customer"
    # "9": "Get Customer Info for One Customer"
    # "10": "Get Customer Info for All Customers"
    # "11": "Check OUT a Video"
    # "12": "Check IN a Video"
    # "13": "QUIT"



