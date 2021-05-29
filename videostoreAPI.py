import requests

URL = "http://127.0.0.1:5000"

############################################################################################

class CustomerAPI:  
    @classmethod
    def register_user(cls,name,postal_code,phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(URL+"/customers",json=query_params)
        return response.json()

    @classmethod
    def list_users(cls):
        response = requests.get(URL+"/customers")
        return response.json()

    @classmethod
    def get_user(cls, id=None):
        if not id:
            return "Could not find customer by that id"
        response = requests.get(URL+f"/customers/{id}")
        if not response:
            return "User with this ID does not exist."
        return response.json()

    @classmethod
    def update_user_account(cls, user_id, name, postal_code, phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(URL+f"/customers/{user_id}",json=query_params)
        return response.json()

    @classmethod
    def delete_customer(cls, user_id):
        response = requests.delete(URL+f"/customers/{user_id}")
        return response.json()

############################################################################################

class VideoAPI:
    @classmethod
    def register_video(cls,title,release_date,total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(URL+"/videos",json=query_params)
        return response.json()

    @classmethod
    def list_videos(cls):
        response = requests.get(URL+"/videos")
        return response.json()

    @classmethod
    def get_video(cls, id):
        if not id:
            return "Could not find video by that id"
        response = requests.get(URL+f"/videos/{id}")
        if not response:
            return "Video with this ID does not exist."
        return response.json()

    @classmethod
    def update_video_info(cls, video_id, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.put(URL+f"/videos/{video_id}",json=query_params)
        return response.json()

    @classmethod
    def delete_video(cls, video_id):
        response = requests.delete(URL+f"/videos/{video_id}")
        return response.json()

############################################################################################

class RentalAPI:
    @classmethod
    def checkout(cls, user_id, video_id):
        query_params = {
            "user_id": user_id,
            "video_id": video_id
        }
        response = requests.post(URL+"/rentals/check-out",json=query_params)
        return response.json()
        
    @classmethod
    def checkin(cls, user_id, video_id):
        query_params = {
            "user_id": user_id,
            "video_id": video_id
        }
        response = requests.post(URL+"/rentals/check-in",json=query_params)
        return response.json()