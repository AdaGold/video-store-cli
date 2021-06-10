import requests


class VideoStore:
    def __init__(self, url="http://localhost:5000"):
        self.url = url
    

    def create_customer(self, name=None, postal_code=None, phone=None):
        form_data = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone}

        response = requests.post(self.url+"/customers",json=form_data)
        return response.json()

    def update_customer(self,name=None,postal_code=None, phone=None):
        form_data = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone}

        response = requests.put(self.url+f"/customers/{id}",json=form_data)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id):
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()


    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()


    def create_video(self,title=None, release_date=None,total_inventory=None):
        form_data = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory}

        response = requests.post(self.url+"/videos",json=form_data)
        return response.json()
    
    
    def update_video(self,title=None,release_date=None, total_inventory=None):
        form_data = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory}
        #Available inventory?
        response = requests.put(self.url+f"/videos/{id}",json= form_data)
        return response.json()


    def get_video(self, id=None):
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()


    def list_videos(self):
        response = requests.get(self.url+"/videos")
        print(response)
        return response.json()


    def delete_video(self, id=None):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()


    def check_in(self, customer_id=None, video_id=None):
        form_data = {
        "customer_id" : customer_id,
        "video_id" : video_id}
        #patch?
        response = requests.patch(self.url+f"/rentals/check-in", json=form_data )
        return response.json()


    def check_out(self, customer_id=None, video_id=None):
        form_data = {
        "customer_id" : customer_id,
        "video_id" : video_id}
        
        response = requests.patch(self.url+f"/rentals/check-out",json=form_data )
        return response.json()



