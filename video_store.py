import requests

#URL = "http://127.0.0.1:5000"
URL = "http://localhost:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# class VideoStore:
#     def __init__(self, url="http://localhost:5000"):
#         self.url = url

def create_video( title, release_date, total_inventory):
    query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
    }
    response = requests.post(URL+ "/videos", json=query_params)
    return response.json()

#   "2": "Edit a video"
def edit_video(title, release_date, total_inventory, video_id):
    query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
    }
    response = requests.put(URL+ "/videos/" + video_id, json=query_params)
    return response.json()

#         "3": "Delete a video from inventory", 

#         "4": "List all videos in the catelog", 
#         "5": "Get information on one video",
#         "6": "Add a new customer",
#         "7": "Edit a customer",
#         "8": "Delete a customer",
#         "9": "Find a customers information",
#         "10": "List all customers",
#         "11": "Check-out a video",
#         "12": "Check-in a video",
#         "13": "Quit"