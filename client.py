import requests
from requests.models import Response



#https://maite-retro-video-store-api.heroku.com/

class Client:
    def __init__(self, url="http://127.0.0.1:5000"):
        self.url = url
        


    def add_video(self, title, release_date, total_inventory):  
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory  
        }
        response = requests.post(self.url+"/videos",json=request_body) 
        return Video(self, response.json()['id'], title, release_date, total_inventory)

    def edit_video(self, video):
        request_body = {
            "title": video.title,
            "release_date": video.release_date,
            "total_inventory": video.total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{video.id}",
            json=request_body
            )

    def info_about_all_videos(self):
        video_log = []
        response = requests.get(self.url+"/videos")
        for video_json in response.json():
            video_log.append(Video(self, video_json['id'],
            video_json['title'], video_json['release_date'], 
            video_json['total_inventory']))
        return video_log

    def info_about_one_video(self,title=None,id=None):
        for video in self.info_about_all_videos():
            if title:
                if video.title == title:
                    return video        
            elif id == video.id:
                return video
        return None

    def delete_video(self, video):
        response = requests.delete(self.url+f"/videos/{video.id}")



    def add_customer(self, name, postal_code, phone):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customer",json=request_body)
        return Customer(self, response.json()['id'], name, postal_code, phone)

    def edit_customer(self, customer):
        request_body = {
            "name": customer.name,
            "postal_code": customer.postal_code,
            "phone": customer.phone
        }
        response = requests.put(
            self.url+f"/customers/{customer.id}",
            json=request_body
            )

    def info_about_all_customers(self):
        customer_roster = []
        response = requests.get(self.url+"/customers")
        for customer_json in response.json():
            customer_roster.append(Customer(self, customer_json['id'],
            customer_json['name'], customer_json['postal_code'],
            customer_json['phone']))
        return customer_roster

    def info_about_one_customer(self, name=None,id=None):
        for customer in self.info_about_all_customers():
            if name:
                if customer.name == name:
                    return customer
            elif id == customer.id:
                return customer
        return None
    
    def delete_customer(self, customer):
        response = requests.delete(self.url+f"/customers/{customer.id}")



class Video:
    def __init__(self, client, id, title, release_date, total_inventory):
        self.id = id
        self.client = client
        self.title = title
        self.release_date = release_date
        self.total_inventory = total_inventory
    
    def delete(self):
        return self.client.delete_video(self)

    def save(self):
        return self.client.edit_video(self)
        
    def __str__(self):
        return f"{self.title} ({self.release_date} {self.id})"



class Customer:
    def __init__(self, client, id, name, postal_code, phone):
        self.id = id
        self.client = client
        self.name = name
        self.postal_code = postal_code
        self.phone = phone

    def delete(self):
        return self.client.delete_customer(self)

    def save(self):
        return self.client.edit_customer(self)





    def check_out_video_to_customer():
        pass


    def check_in_video_from_customer():
        pass