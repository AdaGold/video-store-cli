from requests import post, put, get, delete

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
        # conversation starters:
        # is there a way to use 'option num' only?
        # self.selected_option = selected_option 
    
    def add_video(self, title=None,release_date=None,total_inventory=None):
        # what is the difference between None and "Default"?
        """Option 1: add a video"""
        query_params = {"title":title, "release_date":release_date, "total_inventory":total_inventory}
        url = self.url+"/videos"
        response = post(url, json=query_params)
        return response.json()

    def update_video(self,title=None,total_inventory=None,release_date=None):
        """Option 2: edit a video"""
        # what if we have not 3, but 10 parameters?
        # how to validate them all?
        if not title: 
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        query_params = {"title": title,"release_date": release_date,"total_inventory": total_inventory}
        url = self.url+f"/videos/{self.selected_video['id']}"
        response = put(url, json=query_params) 
        self.selected_video = response.json()["id"] # Is this line necessary? 
        return response.json()

    def delete_video(self):
        """Option 3: delete a video"""
        response = delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None # Is this line necessary? 
        return response.json()

    def list_videos(self):
        """Option 4: get information about all videos"""
        response = get(self.url+"/videos") 
        return response.json()

    def get_video(self, title=None, id=None):
        """Option 5: get information about one video"""
        found = False
        for video in self.list_videos():
            if id:
                if id == video["id"]:
                    self.selected_video = video
                    found = True
            if title:
                if title == video["title"].lower():
                    self.selected_video = video
                    id = self.selected_video['id']
                    found = True
        if found == False:
            return False
        response = get(self.url+f"/videos/{id}")
        return response.json()

    def add_customer(self, name="Default name",postal_code=None,phone=None): 
        """Option 6: add a customer"""
        query_params = {"name": name,"postal_code": postal_code,"phone": phone}
        url = self.url+"/customers"
        response = post(url, json=query_params)
        return response.json()

    def update_customer(self,name=None,postal_code=None,phone=None):
        """Option 7: edit a customer"""
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        query_params = {"name": name,"postal_code": postal_code,"phone": phone}
        url = self.url+f"/customers/{self.selected_customer['id']}"
        response = put(url, json=query_params)
        self.selected_customer = response.json()["id"]
        return response.json()

    def delete_customer(self):
        """Option 8: delete a customer"""
        response = delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None 
        return response.json()

    def get_customer(self, name=None, id=None):
        """Option 9: get information about one customer"""
        found = False
        for customer in self.list_customers():
            if id:
                if id == customer["id"]:
                    self.selected_customer = customer
                    found = True
            if name:
                if name == customer["name"].lower():
                    self.selected_customer = customer
                    id = self.selected_customer['id']
                    found = True
        if found == False:
            return False
        response = get(self.url+f"/customers/{id}")
        return response.json()

    def list_customers(self):
        """Option 10: get information about all customers"""
        response = get(self.url+"/customers")
        return response.json()

    def check_out_video(self, customer_id=None, video_id=None):
        """Option 11: check out a video to a customer"""
        query_params = {"customer_id": customer_id, "video_id": video_id}
        response = post(self.url+"/rentals/check-out", json=query_params)
        return response.json()

    def check_in_video(self, customer_id=None, video_id=None):
        """Option 12: check in a video from a customer"""
        query_params = {"customer_id": customer_id,"video_id": video_id}
        response = post(self.url+"/rentals/check-in", json=query_params)
        return response.json()
