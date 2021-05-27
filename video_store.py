import requests
import datetime

class VideoStore: # how many params for __init__? selected_video and selected_customer? so you can choose to work via either entity?
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None, selected_rental=None): # url is for local machine... do you even need to deploy to Heroku??
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
        self.selected_rental = selected_rental # is this right? or operate through the video model?

    def create_customer(self, name="Default Customer Name", postal_code="Default Postal Code", phone="Default Phone Number", register_at=datetime.datetime.now(), videos_checked_out_count=0): # what other params? all the ones that make up the customer object? just the ones the blockbuster emp can work on?
        relevant_params = { # new customer must have an account; blockbuster employee adds them to the system
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "register_at": register_at,
            "videos_checked_out_count": videos_checked_out_count
        }
        response = requests.post(self.url + "/customers", json=relevant_params)
        return response.json()

    def create_video(self, title="Default Movie Title", release_date="Default Date", total_inventory="Default Total Inventory", available_inventory="Default Available Inventory"): # add video to database
        relevant_params = { # blockbuster employee has to add new movie to bb system for potental rent-out
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.post(self.url + "/videos", json=relevant_params)
        return response.json()

    def list_customers(self): # show all customers in blockbuster db
        response = requests.get(self.url + "/customers")
        return response.json()

    def list_videos(self): # show all movies blockbuster has to offer
        response = requests.get(self.url + "/videos")
        return response.json() 

    def get_customer(self, name=None, id=None): # pull up specific customer acct, by name, phone number or customer id(would a customer even have that info? phone num's prob best)
        for customer in self.list_customers():
            if customer:
                if customer["name"] == name:
                    id = customer["customer_id"]
                    self.selected_customer = customer
            elif id == customer["customer_id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find a customer by that name or ID."
        
        response = requests.get(self.url + f"/customers/{id}")
        return response.json()

    def get_video(self, title=None, id=None): # pull up a video by its title or ID in the system (likely to see if it's been checked out or to refresh customer on when it's due)
        for video in self.list_videos():
            if video:
                if video["title"] == title:
                    id = video["video_id"]
                    self.selected_video = video
            elif id == video["video_id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find a video by that title or ID."
        
        response = requests.get(self.url + f"/videos/{id}")
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None): # 'phone' or 'phone_number'??? --- > params should be what can be updated by user
    # maybe customer renews it to keep it for longer and the due date field needs to change as a result
        if not name: # customer's phone number or postal code or name changed; update system per their request
            name = self.selected_customer["name"] # if employee doenst change name, maintain original
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone_number"] # phone_number or phone?
        
        relevant_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone # phone or phone_number?
        }

        response = requests.put(
            self.url + f"/customers/{self.selected_customer['customer_id']}",
            json=relevant_params)
        print("Here's what we have now: ", response)
        self.selected_customer = response.json()["customer"] # right param?
        return response.json()

    def update_rental(self, due_date=None): # "" ******** WORK ON RENTAL MODEL, NOT VIDEO (??)
        if not due_date: # customer's phone number or postal code or name changed; update system per their request
            due_date = (self.selected_rental["check_out_date"] + (datetime.timedelta(days=7)))# if employee doenst change due date, maintain original
        
        relevant_param = {"due_date": due_date}
# THE CORRECT LOGIC HERE DEPENDS ON IF WORKING THROUGH RENTAL OR VIDEO
        response = requests.put(
            self.url + f"/customers/{self.selected_customer['customer_id']}/rentals", # look up rentals asso'd w X customer, change their due date: right path ????
            json=relevant_param)
        print("Here's what we have now: ", response)
        self.selected_rental = response.json()["rental"] # right param?
        return response.json()
        

    def delete_customer(self):
        response = requests.delete(self.url + f"customers/{self.selected_customer['id']}")
        self.selected_customer = None # reassign to falsey value = deletion
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url + f"videos/{self.selected_video['id']}")
        self.selected_video = None # reassign to falsey value = deletion
        return response.json()
    
    def delete_rental(self): # don't need this right? bc why would you delete a rental from a customer's account? (XXX? video in wrong box at checkout? sounds like getting into the weeds)
        pass

    def show_selected_customer(self): # ""
        # print "Let's confirm that you want to work with Customer X" to the blockbuster employee user
        if self.selected_customer:
            print(f"Customer with ID {self.selected_customer['id']} is currently selected\n")

    def show_selected_video(self): # ""
        # print "Let's confirm that you want to work with Video X" to the blockbuster employee user
        if self.selected_video:
            print(f"Video with ID {self.selected_video['id']} is currently selected\n")

    def show_selected_rental(self): # dont need to work w this bc no menu option
        pass