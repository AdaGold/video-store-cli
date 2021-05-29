import requests
import datetime
import pprint

class VideoStore:
    def __init__(self, url, selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
    
    def create_video(self,title="Default Video",total_inventory="Default total inventory",release_date=None):
        query_params = {
            "title": title,
            "total_inventory": total_inventory,
            "release_date": release_date
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if video:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
                elif id == video["id"]:
                    self.selected_video = video

        if self.selected_video is None:
            print("Could not find video by that name or id" )

        '''response = requests.get(self.url+f"/videos/{id}")
        return response.json()'''
    
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer_rentals(self, id):
        response = requests.get(self.url+f"/customers/{id}/rentals")
        print(response)
        pprint.pprint(response.json())

    def get_customer(self, id):
        for customer in self.list_customers():
            if customer["id"]==id:
                self.selected_customer = customer
                return self.selected_customer      
        if self.selected_customer==None:
            print ("Could not find customer by that id")


    def update_video(self,title=None,release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.release_date["description"]
        if not total_inventory:
            total_inventory = self.total_inventory["total_inventory"]
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
        return response.json()

    def delete_video(self, id=None):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def check_out_video(self,customer_id,video_id,due_date):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id,
            "due_date": due_date,
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response.json()

    def check_in_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        
        print("Some string")
        print(response)
        print(response.json())

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")

    def create_customer(self, name="Default Name", postal_code="Default Postal-Code", phone="phone"):
        query_params = {
                "name": name,
                "postal_code": postal_code,
                "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.postal_code["postal code"]
        if not phone:
            phone = self.phone["phone number"]
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }

        response = requests.put(
            self.url + f"/customers/{self.selected_customer['id']}",
            json=query_params
        )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self, id=None):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

'''    
    def mark_complete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
        self.selected_task = response.json()["task"]
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
        self.selected_task = response.json()["task"]
        return response.json()
'''

    # def print_selected(self):
    #     if self.selected_video:
    #         print(f"Video with id {self.selected_video['id']} is currently selected\n")
