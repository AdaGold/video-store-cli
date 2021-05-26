import requests
import datetime

class VideoStore:
    def __init__(self, url="http://localhost:5000"):
        self.url = url
    
    def create_customer(self, name, postal_code, phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()


    def create_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        print(response)
        return response.json()


    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()


    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()


    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()


    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()


    def update_customer(self, id_customer=None, name=None, postal_code=None, phone=None):
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{id_customer}",
            json=query_params
            )
        return response.json()


    def update_video(self, id_video=None, title=None, release_date=None, total_inventory=None):
        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{id_video}",
            json=query_params
            )
        return response.json()


    def delete_customer(self, id_customer=None):
        response = requests.delete(self.url+f"/customers/{id_customer}")
        return response.json()


    def delete_video(self, id_video=None):
        response = requests.delete(self.url+f"/videos/{id_video}")
        return response.json()


    def checkout_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        print(response)
        return response.json()


    # def mark_complete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def mark_incomplete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def print_selected(self):
    #     if self.selected_task:
    #         print(f"Task with id {self.selected_task['id']} is currently selected\n")



