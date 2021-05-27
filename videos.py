# import requests
# import datetime

# class VideoList:
#     def __init__(self, url="http://localhost:5000", selected_video=None):
#         self.url = url
#         self.selected_video = selected_video
    
#     # CREATE A VIDEO -----------------------------------------------------------------------------
#     def create_video(self,title="Default Title",release_date="Default Release_Date",total_inventory="Total_Inventory"):
#         query_params = {
#             "title": title,
#             "release_date": release_date,
#             "total_inventory": total_inventory
#         }
#         response = requests.post(self.url+"/videos",json=query_params)
#         return response.json()

#     # DISPLAY LIST OF ALL VIDEOS -----------------------------------------------------------------
#     def list_videos(self):
#         response = requests.get(self.url+"/videos")
#         return response.json()

#     # GET A SPECIFIC VIDEOS BY TITLE OR ID ----------------------------------------------------------
#     def get_video(self, title=None, id=None):
        
#         for video in self.list_videos():
#             if title:
#                 if  video["title"]==title:
#                     self.selected_video = video
#             elif id == video["id"]:
#                 self.selected_video = video
#         if self.selected_video == None:
#             return "Could not find video by that title or id"
#         response = requests.get(self.url+f"/video/{id}")
#         return response.json()

#     # UPDATE A SPECIFIC VIDEO BY TITLE OR ID--------------------------------------------------------
#     def update_videos(self,title=None,id=None):
#         if not title:
#             title = self.selected_video["title"]
#         if not id:
#             id = self.selected_video["id"]

#         query_params = {
#         "title": title,
#         "id": id
#         }
#         response = requests.put(
#             self.url+f"/videos/{self.selected_video['id']}",
#             json=query_params
#             )
#         print("response:", response)
#         self.selected_video = response.json()["video"]
#         return response.json()

#     # DELETE A SPECIFIC VIDEO -------------------------------------------------------------------------
#     def delete_video(self):
#         response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
#         self.selected_video = None
#         return response.json()

    
#     # ONE VIDEO  IS CURRENLTY SELECTED --------------------------------------------------------------------
#     def print_selected(self):
#         if self.selected_video:
#             print(f"Video with id {self.selected_video['id']} is currently selected\n")