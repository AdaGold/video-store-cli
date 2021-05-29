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

#   "3": "Delete a video from inventory", 
def delete_video(video_id):
    response = requests.delete(URL+ "/videos/" + video_id)
    return response.json()

#         "4": "List all videos in the catelog", 
def list_all_videos():
    response = requests.get(URL+ "/videos/")
    return response.json()

#         "5": "Get information on one video",
def get_video(video_id):
    response = requests.get(URL+ "/videos/" + video_id)
    return response.json()

def add_customer(name, postal_code, phone):
    query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
    }
    response = requests.post(URL+ "/customers", json=query_params)
    return response.json()

def edit_customer(customer_id, name, postal_code, phone):
    query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
    }
    response = requests.put(URL+ "/customers/"+ customer_id, json=query_params)
    return response.json()

def delete_customer(customer_id):
    response = requests.delete(URL+ "/customers/" + customer_id)
    return response.json()

def get_customer(customer_id):
    response = requests.get(URL+ "/customers/" + customer_id)
    return response.json()
#
def list_customers():
    response = requests.get(URL+ "/customers/")
    return response.json()

def checkout(customer_id, video_id):
    query_params = {
        "customer_id": customer_id,
        "video_id": video_id
    }
    response = requests.post(URL+ "/rentals/check-out", json=query_params)
    return response.json()

def checkin(customer_id, video_id):
    query_params = {
        "customer_id": customer_id,
        "video_id": video_id
    }
    response = requests.post(URL+ "/rentals/check-in", json=query_params)
    return response.json()

#         "11": "Check-out a video",
#         "12": "Check-in a video",
#         "13": "Quit"