import requests
import datetime

class VideoStore: # how many params for __init__? selected_video and selected_customer? so you can choose to work via either entity?
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None): # url is for local machine... do you even need to deploy to Heroku??
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    def create_customer(self, name="Default Customer Name", postal_code="Default Postal Code", phone="Default Phone Number", register_at=datetime.datetime.now(), videos_checked_out_count=0): # what other params? all the ones that make up the customer object? just the ones the blockbuster emp can work on?
        pass # new customer must have an account; blockbuster employee adds them to the system

    def create_video(self): # ""
        pass # blockbuster employee has to add new movie to bb system for potental rent-out

    def list_customers(self): # ""
        pass # show all customers in blockbuster db

    def list_videos(self): # ""
        pass # show all movies blockbuster has to offer

    def get_customer(self): # ""
        pass # pull up specific customer acct, by name, phone number or customer id(would a customer even have that info? phone num's prob best)

    def get_video(self):
        pass # pull up a video by its title or ID in the system (likely to see if it's been checked out or to refresh customer on when it's due)

    def update_customer(self): # ""
        pass # customer's phone number or postal code or name changed; update system per their request

    def update_rental(self): # "" ******** WORK ON RENTAL MODEL, NOT VIDEO
        pass # maybe customer renews it to keep it for longer and the due date field needs to change as a result

    def delete_customer(self):
        pass

    def delete_video(self):
        pass

    def show_selected_customer(self): # ""
        # print "Let's confirm that you want to work with Customer X" to the blockbuster employee user
        if self.selected_customer:
            print(f"Customer with ID {self.selected_customer['id']} is currently selected\n")


    def show_selected_video(self): # ""
        # print "Let's confirm that you want to work with Video X" to the blockbuster employee user
        if self.selected_video:
            print(f"Video with ID {self.selected_video['id']} is currently selected\n")