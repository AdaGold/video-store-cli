import requests

class Rental: 
    def __init__(self, url="http://localhost:5000", selected_customer=None):
        self.url = url
        self.selected_customer = selected_customer
    
    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")
    
    def check_out_rental(self, customer_id=None, video_id=None): 
        query_params = {
            "customer_id": int(customer_id),
            "video_id": int(video_id),
        }
        response = requests.post(self.url+f"/rentals/check-out", json=query_params)
        print("response:", response)

        if response.status_code == 404: 
            return response.text
        self.selected_rentals = response.json()
        return response.json()
    
    def check_in_rental(self, customer_id=None, video_id=None): 
        query_params = {
            "customer_id": int(customer_id),
            "video_id": int(video_id),
        }
        
        response = requests.post(self.url+f"/rentals/check-in", json=query_params)
        print("response:", response)

        if response.status_code == 404: 
            return response.text
        self.selected_rentals = response.json()
        return response.json()