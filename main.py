from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text, HTML

import requests
# from retro_video_store import ?
import click


column = "|||"
center = column.center(20, " ")
padding = (" " * 20)



BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def get_option_from_employee(num):
        valid_input = False
        user_input = None
        while not valid_input:
            if user_input != "1":
                print(f"Invalid option.")

def print_options():
    options = {
        "1": "add a video",
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        "6": "add a customer",
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer"
    }
    

    for choice in options:
        print_formatted_text(HTML(f"Enter option <b>{choice}</b> to <u>{options[choice]}</u>"))
        print()

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print()

    print_options()
    print()
    choice = input("What would you like to do? ")

    if choice == "1": 
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos")
        print()
        print(f"{padding} add a video")
        print()
        title = input("enter video title: ")
        release_date = input("enter video release date yyyy/mm/dd: ")
        total_inventory = input("enter inventory total: ")
        new_video = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        print_formatted_text(HTML(f"<b>{new_video['title']} successfully added.</b>"))


    if choice == "2":
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos/<video_id>")
        print(f"{padding} edit existing video")
        input("re-enter video title: ")
        input("re-enter release date: ")
        input("re-enter inventory total:  ")

        updated_video = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        print_formatted_text(HTML(f"<b>{updated_video['title']} successfully updated.</b>"))

    if choice == "3":
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos/<video_id>")

        print(f"{padding} delete a video")
        ya_sure = input("are you sure you want to delete video? yes or no: ")
        if ya_sure == "yes":
            print_formatted_text(HTML(f"<b>{response} successfully deleted.</b>"))
        print_formatted_text(HTML("f{response} not deleted."))

    if choice == "4":
        print(f"{padding} all videos")
        print()
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos")
        video_list = response.json()

        for video in video_list:
            print_formatted_text(HTML(f"<b>{video['id']:03d}{center}{video['title']}</b>"))

    if choice == "5":
        print(f"{padding} get information about one video")
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos")
        video_list = response.json()

        for video in video_list:
            for a_vid in video:
                print_formatted_text(HTML(f"<b>{video[a_vid]}</b>"))
            print()         

    if choice == "6":
        print(f"{padding} add a customer")
        print()
        name = input("enter customer name: ")
        phone = input("enter phone number: ")
        postal_code = input("enter postal code:  ")
        new_customer = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }
        
        print_formatted_text(HTML(f"<b>{new_customer['name']} successfully added </b>"))
    
    if choice == "7":
        print("update a customer")
        print()
        name = input("re-enter customer name: ")
        phone = input("re-enter phone number: ")
        postal_code = input("re-enter postal code: ")

        updated_customer = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code
        }

        print_formatted_text(HTML(f"<b>{updated_customer['name']} successfully updated</b>"))


    if choice == "8":
        response = requests.get("https://retro-video-store-api.herokuapp.com/videos/")

        print(f"{padding} delete a customer")
        print()
        
        ya_sure = input("are you sure you want to delete customer? yes or no: ")
        if ya_sure == "yes":
            print_formatted_text(HTML(f"<b>{response} successfully deleted.</b>"))
        print_formatted_text(HTML("f{response} not deleted."))

    # if choice == "9":
    #     response = requests.get("https://retro-video-store-api.herokuapp.com/videos")
    #     customer_list = response.json()

    #     for customer in customer_list:
    #         print(customer)



    # if choice == "10":
    #     response = requests.get("https://retro-video-store-api.herokuapp.com/videos")
    #     customer_list = response.json()
        
    #     for customer in customer_list:
    #         for id in customer:
    #             print(id["customer_id"])

    # if choice == "11":
    #     print("checkout customer")
    #     print()

    # if choice == "12":
    #     print("check-in video")
    #     print()







    

        




if __name__ == "__main__":
    main()