import requests
import datetime

class Rental:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental
    #start
    def check_out(self,customer_id=None,video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response.json()



    def check_in(self,customer_id=None,video_id=None):
        query_params = {
            "customer_id":customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        return response.json()
    # def check_in(self):
    #     response = requests.get(self.url+"/rentals/check-in")
    #     return response.json()

    # def check_out(self):
    #     response = requests.get(self.url+"/rentals/check-out")
    #     return response.json()
    
    # def list_rentals(self):
    #     response=requests.get(self.url+"/rentals")
    #     return response.json()
    
    # def get_rental(self,customer_id=None,video_id=None):
    #     for rental in self.list_rentals():
    #         if rental:
    #             if rental["customer_id"]==customer_id and rental["video_id"]==video_id:
    #                 id=rental["id"]
    #                 self.selected_rental=rental
    #         elif id==rental["id"]:
    #             self.selected_rental=rental
            
    #     if self.selected_rental == None:
    #         return "Could not find rental by that rental id, customer id and video id"

    #     response = requests.get(self.url+f"/rentals/check-in") #route ???
    #     return response.json()

    # def get_customer(self, name=None, id=None):
        
    #     for customer in self.list_customers():
    #         if customer:
    #             if customer["name"]==name:
    #                 id = customer["id"]
    #                 self.selected_customer = customer
    #         elif id == customer["id"]:
    #             self.selected_customer = customer

    #     if self.selected_customer == None:
    #         return "Could not find customer by that name or id"

    #     response = requests.get(self.url+f"/customers/{id}")
    #     return response.json()

    # def update_customer(self,name=None,postal_code=None,phone=None):
    #     if not name:
    #         name = self.selected_customer["name"]
    #     if not postal_code:
    #         postal_code = self.selected_customer["postal_code"]
    #     if not phone:
    #         phone=self.phone["phone"]

    #     query_params = {
    #     "name": name,
    #     "postal_code": postal_code,
    #     "phone":phone
    #     #"completed_at": self.selected_task["is_complete"]
    #     }
    #     response = requests.put(
    #         self.url+f"/customers/{self.selected_customer['id']}",
    #         json=query_params
    #         )
    #     print("response:", response)
    #     self.selected_customer = response.json()["customer"]
    #     return response.json()

    # def delete_customer(self):
    #     response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
    #     self.selected_customer = None
    #     return response.json()
    
    # # def mark_complete(self):
    # #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
    # #     self.selected_task = response.json()["task"]
    # #     return response.json()

    # # def mark_incomplete(self):
    # #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
    # #     self.selected_task = response.json()["task"]
    # #     return response.json()

    # def print_selected(self):
    #     if self.selected_video:
    #         print(f"Customer with id {self.selected_customer['id']} is currently selected\n")