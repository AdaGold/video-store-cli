import requests



#https://maite-retro-video-store-api.heroku.com/

class Client:
    def __init__(self, url="http://127.0.0.1:5000"):
        self.url = url
        #self.selected = selected
        

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
            video_log.append(Video(self, video_json['id'], video_json['title'], video_json['release_date'], video_json['total_inventory']))
        return video_log


    def info_about_one_video(self,title=None,id=None):
        for video in self.info_about_all_videos():
            if title:
                if video.title==title:
                    return video        
            elif id == video.id:
                return video
        
        return None

    def delete_video(self, video):
        response = requests.delete(self.url+f"/videos/{video.id}")
        



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
        # if not title:
        #     title = self.selected["title"]
        # if not release_date:
        #     release_date = self.selected["release_date"]
        # if not total_invetory:
        #     total_invetory = self.selected["total_inventory"]
    def __str__(self):
        return f"{self.title} ({self.release_date} {self.id})"


class Customer:
    def __init__(self, client, id, name, postal_code, phone):
        self.id = id
        self.client = client
        self.name = name
        self.postal_code = postal_code
        self.phone = phone


    def add_customer(self, name, postal_code, phone):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customer",json=request_body)
        return response.json() #response.json() #object instead?


    def edit_customer(self,name=None,postal_code=None,phone=None):
        if not name:
            name = self.selected["customer"]
        if not postal_code:
            postal_code = self.selected["postal_code"]
        if not phone:
            phone = self.selected["phone"]
        
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
            }
        response = requests.put(
            self.url+f"/customers/{self.selected['id']}",
            json=request_body
            )
        print("response:", response)
        self.selected = response.json()["video"]
        return response.json()


    def delete_customer(self):
        response = requests.delete(self.url+f"/customer/{self.selected['id']}")
        self.selected = None
        return response.json()

    
    def info_about_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
        

    def info_about_one_customer(self,name=None,id=None):
        for customer in self.info_about_all_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected = customer
                elif id == customer["id"]:
                    self.selected = customer

            if self.selected == None:
                return "Sorry, we could not find a matching customer"

            response = requests.get(self.url+f"/customers/{id}")
            return response.json()
        

# def info_about_one_video(self,title=None,id=None):
#         for video in self.info_about_all_videos():
#             if title:
#                 if video["title"]==title:
#                     id = video["id"]
#                     self.selected_video = video 
#             elif id == video["id"]:
#                 self.selected_video = video 
        
#         if self.selected_video == None:
#             return "Sorry, we could not find a video with that id or title."


    def check_out_video_to_customer():
        pass


    def check_in_video_from_customer():
        pass