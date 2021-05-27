# from main import select_customer
import requests


class Employee:
    def __init__(
            self,
            url="http://localhost:5000",
            selected_video=None,
            selected_customer=None):

        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    def add_video(
            self,
            title="Default Title",
            release_date="",
            total_inventory=0):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url + "/videos", json=query_params)
        return response.json()

    def list_all_videos(self):
        response = requests.get(self.url + "/videos")
        return response.json()

    def get_one_video(self, id=None):
        for video in self.list_all_videos():
            if video["id"] == id:
                self.selected_video = video

        # if self.selected_video is None:
        #     return "Could not find this video."

        # response = requests.get(self.url + f"/videos/{id}")
        # return response.json()

    def update_video(
            self,
            title=None,
            release_date=None,
            total_inventory=None):

        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": int(total_inventory)
        }
        # print(query_params)

        response = requests.put(
            self.url +
            f"/videos/{self.selected_video['id']}",
            json=query_params)
        # print("response:", response)

        return response.json()

    def delete_video(self):
        response = requests.delete(
            self.url + f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def add_customer(
            self,
            name="Default Name",
            postal_code=10000,
            phone="(000) 000-0000"):

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }

        response = requests.post(self.url + "/customers", json=query_params)
        return response.json()

    def list_all_customers(self):
        response = requests.get(self.url + "/customers")
        return response.json()

    def get_one_customer(self, id=None):
        for customer in self.list_all_customers():
            if customer["id"] == id:
                self.selected_customer = customer

    def delete_customer(self):
        response = requests.delete(
            self.url + f"/customers/{self.selected_customer['id']}")
        self.selected_video = None
        return response.json()

    def update_customer(
            self,
            name=None,
            postal_code=None,
            phone=None):

        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]

        query_params = {
            "name": name,
            "postal_code": int(postal_code),
            "phone": phone
        }
        # print(query_params)

        response = requests.put(
            self.url +
            f"/customers/{self.selected_customer['id']}",
            json=query_params)
        # print("response:", response)

        return response.json()

    def check_out(self, customer_id=None, video_id=None):

        if not customer_id:
            customer_id = self.selected_customer["id"]
        if not video_id:
            video_id = self.selected_video["id"]

        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(
            self.url + "/rentals/check-out",
            json=query_params)
        return response.json()

    def check_in(self, customer_id=None, video_id=None):

        if not customer_id:
            customer_id = self.selected_customer["id"]
        if not video_id:
            video_id = self.selected_video["id"]

        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(
            self.url + "/rentals/check-in",
            json=query_params)
        return response.json()
