import requests


class Retro_Video:
    def __init__(self, url, selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def create_video(self,title,release_date,total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)

        return response.json()

    def update_video(self,id,title,release_date, total_inventory):
        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        
        }
        response = requests.put(self.url+f"/videos/{id}", json=query_params)
       
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        print(response.text)
        return response.json()

    

    def delete_video(self,id):
        response = requests.delete(self.url+f"/videos/{id}")
        print("The response is:", response.text)
        return response.json()
    

    def get_video(self,id):
    
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()


    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    
    def create_customer(self,name,postal_code,phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
        }
        response = requests.post(self.url+"/customers",json=query_params)

        return response.json()

    def update_customer(self,id,name,postal_code, phone):
        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        
        }
        response = requests.put(self.url+f"/customers/{id}", json=query_params)
       
        return response.json()

    
    def delete_customer(self,id):
        response = requests.delete(self.url+f"/customers/{id}")
        print("The response is:", response.text)
        return response.json()



    def get_customer(self,id):
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
        
   
    def checkout_video(self,video_id,customer_id): 
       query_params = {
            "video_id": video_id,
            "customer_id": customer_id,

       }
       response = requests.post(self.url+"/rentals/check-out",json=query_params)

       return response.json()

    
    def checkin_video(self,video_id,customer_id): 
       query_params = {
            "video_id": video_id,
            "customer_id": customer_id,

       }
       response = requests.post(self.url+"/rentals/check-in",json=query_params)

       return response.json()

      
    def videos_checkedout_by_customer(self,customer_id): 
        query_params = {
            "customer_id": customer_id,
         }
        response = requests.get(self.url+f"/customers/{customer_id}/rentals",json=query_params)

        return response.json()

    def customers_checkedout_by_video(self,video_id): 
        query_params = {
            "video_id": video_id,

        }
        response = requests.get(self.url+f"/videos/{video_id}/rentals",json=query_params)
        return response.json()

    def list_videos_by_titles(self,title):
        query_params = {
            "title": title,
        }
        response = requests.get(self.url+f"/videos",json=query_params)
        return response.json()

    

    def print_selected(self):
        if self.selected_task:
            print(f"Task with id {self.selected_task['id']} is currently selected\n")