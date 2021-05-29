import requests

class VideoStore:
    def __init__(self, url="http://localhost:5000"):
        self.url = url


    def check_out(self, customer_id, video_id):
        request_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }
        response = requests.post(self.url+"/rentals/check-out", json=request_params)
        
        if not response:
            return f"=== Error: Invalid ID ==="
        
        return response.json()

    def check_in(self, customer_id, video_id):
        request_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }
        response = requests.post(self.url+"/rentals/check-in", json=request_params)
        
        if not response:
            return f"=== Error: Invalid ID ==="
        
        return response.json()
    
    """
    Start video-related methods
    """
    def add_video(self, title, release_date, total_inventory):
        try:
            request_params = {
                "title": title,
                "release_date": release_date,
                "total_inventory": total_inventory,
                "available_inventory": total_inventory
            }
            response = requests.post(self.url+"/videos", json=request_params)
            return response.json()
        except ValueError:
            return f"Unable to add video. Please complete all fields."

    def videos_index(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_one_video(self, id=None, title=None):
        try:
            if id:
                response = requests.get(self.url+f"/videos/{id}")
                return response.json()
            elif title:
                inventory = requests.get(self.url+f"/videos")
                for video in inventory.json():
                
                    if video.get("title") == title:
                        return video
        except ValueError:  
            return f"=== Error: Video Not Found ==="
                    
    def update_video(self, id=None, title=None, release_date=None, total_inventory=None):
        try:
            video = requests.get(self.url+f"/videos/{id}")
            video_response = video.json()
        except ValueError:
            return f"=== Error: Video Not Found ==="

        request_params = {
                "title": title,
                "release_date": release_date,
                "total_inventory": total_inventory, 
            }
        if not title:
            request_params["title"] = video_response.get("title")
        if not release_date:
            request_params["release_date"] = video_response.get("release_date")
        if not total_inventory:
            request_params["total_inventory"] = video_response.get("total_inventory")

        updated_video = requests.put(self.url+f"/videos/{id}", json=request_params)
        return updated_video.json()

    def delete_video(self, id):
        try:
            response = requests.delete(self.url+f"/videos/{id}")
            return response.json()
        except ValueError:
            return f"=== Error: Video Not Found ==="
    
    """
    Start customer-related methods
    """
    def add_customer(self, name, postal_code, phone):
        try:
            request_params = {
                "name": name,
                "postal_code": postal_code,
                "phone": phone,
            }
            response = requests.post(self.url+"/customers", json=request_params)
            return response.json()
        except ValueError:
            return f"Unable to add customer. Please complete all fields."

    def update_customer(self, id=None, name=None, postal_code=None, phone=None):
        try:
            customer = requests.get(self.url+f"/customers/{id}")
            customer_response = customer.json()
        except ValueError:
            return f"=== Error: Customer Not Found ==="

        request_params = {
                "name": name,
                "postal_code": postal_code,
                "phone": phone, 
            }
        if not name:
            request_params["name"] = customer_response.get("name")
        if not postal_code:
            request_params["postal_code"] = customer_response.get("postal_code")
        if not phone:
            request_params["phone"] = customer_response.get("phone")

        updated_customer = requests.put(self.url+f"/customers/{id}", json=request_params)
        return updated_customer.json()

    def delete_customer(self, id):
        try:
            response = requests.delete(self.url+f"/customers/{id}")
            return response.json()
        except ValueError:
            return f"=== Error: Customer Not Found ==="

    def customers_index(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_one_customer(self, id=None, name=None, phone=None):
        customers_index = requests.get(self.url+f"/customers")
        try:
            if id:
                response = requests.get(self.url+f"/customers/{id}")
                return response.json()
            elif name:
                for customer in customers_index.json():
                    if customer.get("name") == name:
                        return customer
            elif phone:
                for customer in customers_index.json():
                    if customer.get("phone") == phone:
                        return customer
        except ValueError: 
            return f"=== Error: Customer Not Found ==="

