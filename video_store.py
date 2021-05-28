import requests

class VideoStore:
    def __init__(self, url="http://localhost:5000"):
        self.url = url


    def check_out(self, customer_id, video_id):
        request_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }

        response = requests.post(self.url+"/check-out", json=request_params)
        return response.json()

    def check_in(self, customer_id, video_id):
        pass

    def add_video(self, title, release_date, total_inventory):
        request_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": total_inventory
        }

        response = requests.post(self.url+"/videos", json=request_params)
        return response.json()

    def videos_index(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_one_video(self, id):
        pass

    def update_video(self, id):
        pass

    def delete_video(self, id):
        pass

    def add_customer(self, name, postal_code, phone):
        pass

    def update_customer(self, id):
        pass

    def delete_customer(self, id):
        pass

    def customers_index(self):
        pass

    def get_one_customer(self, id):
        pass
