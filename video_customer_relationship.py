import requests 
import datetime 

# relationship between customer and video 
class Video_customer_relationship:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer 

    #11 - check out a video to a customer so that the store has a record of who has the video 
    def check_out(self):
        response = requests.post(self.url+f"/videos/{self.selected_video['id']}/check_out")
        self.selected_video = response.json()["video"]
        return response.json()
        
    #12 - check in a video from a customer so that the video will be available to other customers
    def check_in(self):
        response = requests.post(self.url+f"/videos/{self.selected_video['id']}/check_in")
        self.selected_video = response.json()["video"]
        return response.json()

    #13 print selected video
    def print_selected_video(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is selected")
        else:
            print("There is no selected task.")

    #14 print selected customer 
    def print_selected_customer(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is selected")
        else:
            print("There is no selected customer.")