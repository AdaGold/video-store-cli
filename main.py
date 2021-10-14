from flask import json
import requests
from requests.api import request

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


'''
    =============================================
    HELPER PRINTS
    =============================================
'''

def bar_break():
    print("\n==========================\n")

def list_options_ee():
    options = {
        "1" : "Add Video to Store Stock",
        "2" : "Edit Video Info",
        "3" : "Remove Video From Inventory",
        "4" : "View Current Store Stock",
        "5" : "View Video Info",
        "6" : "Add New Customer",
        "7" : "Edit Existing Customer",
        "8" : "Delete Existing Customer",
        "9" : "View Existing Customer Records",
        "10" : "View All Existing Customers",
        "11" : "Check Out",
        "12" : "Check In"
    }

    bar_break()
    print("Here are your available options:\n")
    for choice in options:
        print(f"Option {choice}. {options[choice]}")

    bar_break()

    return options

def list_options_cust():
    options = {

    }
    pass

'''
    =============================================
    EMPLOYEE OPTION FUNCTIONS
    =============================================
'''

def add_video():
    print("Enter video info below:")
    request_body = {}
    request_body["title"] = input("Title: ")
    request_body["release_date"] = input("Release date: ")
    request_body["total_inventory"] = input("Total inventory: ")

    response = requests.post(URL +"/videos", json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

def edit_video():
    print("Enter updated video info below:")
    request_body = {}
    video_id = input("Video ID: ")
    request_body["title"] = input("Title: ")
    request_body["release_date"] = input("Release date: ")
    request_body["total_inventory"] = input("Total inventory: ")

    response = requests.put(URL +"/videos/" +video_id, json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

def remove_video():
    print("DELETE VIDEO - THIS ACTION CANNOT BE UNDONE")
    if input("Are you sure? Y/N ") != "Y":
        print("ACTION CANCELLED")
        return
    
    video_id = input("Video ID: ")
    response = requests.delete(URL +"/videos/" +video_id)
    print(json.dumps(response.json(), indent=1))
    return

def view_video_stock():
    print("All Videos in Store Stock:")
    response = requests.get(URL +"/videos")
    print(json.dumps(response.json(), indent=2))
    return

def view_single_video():
    print("Video Info Request:")
    video_id = input("Video ID: ")
    response = requests.get(URL +"/videos/" +video_id)
    print(json.dumps(response.json(), indent=1))
    return

def add_customer():
    print("Enter customer info below:")
    request_body = {}
    request_body["name"] = input("Name: ")
    request_body["phone"] = input("Phone number: ")
    request_body["postal_code"] = input("Postal code: ")

    response = requests.post(URL +"/customers", json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

def edit_customer():
    print("Enter updated customer info below:")
    request_body = {}
    customer_id = input("Customer ID: ")
    request_body["name"] = input("Name: ")
    request_body["phone"] = input("Phone number: ")
    request_body["postal_code"] = input("Postal code: ")
    
    response = requests.put(URL +"/customers/" +customer_id, json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

def delete_customer():
    print("DELETE CUSTOMER - THIS ACTION CANNOT BE UNDONE")
    if input("Are you sure? Y/N ") != "Y":
        print("ACTION CANCELLED")
        return
    
    customer_id = input("Customer ID: ")
    response = requests.delete(URL +"/customers/" +customer_id)
    print(json.dumps(response.json(), indent=1))
    return

def view_customer():
    print("Customer Info Request:")
    customer_id = input("Customer ID: ")
    response = requests.get(URL +"/customers/" +customer_id)
    print(json.dumps(response.json(), indent=1))
    return

def view_all_customers():
    print("All Active Customer Accounts:")
    response = requests.get(URL +"/customers")
    print(json.dumps(response.json(), indent=2))
    return

def checking_out():
    print("Check Out a Video:")
    request_body = {}
    request_body["customer_id"] = int(input("Customer ID: "))
    request_body["video_id"] = int(input("Video ID: "))

    response = requests.post(URL +"/rentals/check-out", json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

def checking_in():
    print("Check In a Video:")
    request_body = {}
    request_body["customer_id"] = int(input("Customer ID: "))
    request_body["video_id"] = int(input("Video ID: "))

    response = requests.post(URL +"/rentals/check-in", json=request_body)
    print(json.dumps(response.json(), indent=1))
    return

'''
    =============================================
    CUSTOMER OPTION FUNCTIONS
    =============================================
'''

def find_videos_by():
    print("I'm sorry, that feature is not yet available in your area")
    return

def check_current_rentals():
    print("I'm sorry, that feature is not yet available in your area")
    return

'''
    =============================================
    MAIN
    =============================================
'''

def main(in_use=True, is_employee=False):
    print("WELCOME TO RETRO VIDEO STORE")

    ee_id = input("Employee? Please enter your 4 digit id. Hit Enter to continue as a customer.\n")
    if len(ee_id) == 4 and ee_id.isdigit():
        print(f"Welcome to work, Employee {ee_id}")
        is_employee = True
        list_options_ee()

    while is_employee and in_use:
        func_call_dict = {
            "1" : add_video,
            "2" : edit_video,
            "3" : remove_video,
            "4" : view_video_stock,
            "5" : view_single_video,
            "6" : add_customer,
            "7" : edit_customer,
            "8" : delete_customer,
            "9" : view_customer,
            "10" : view_all_customers,
            "11" : checking_out,
            "12" : checking_in
        }

        choice = None
        while choice not in func_call_dict:
            choice = input("What would you like to do? Q to quit.\n")

            if choice == "Q" or choice == 'q':
                print(f"Goodbye Retro Video Store Employee {ee_id}!")
                bar_break()
                return
        
        func_call_dict[choice]()
        bar_break()
    
    while in_use:
        func_call_dict = {
            "1" : find_videos_by,
            "2" : check_current_rentals
        }

        choice = None
        while choice not in func_call_dict:
            choice = input("What would you like to do? Q to quit.\n")

            if choice == "Q" or choice == 'q':
                print(f"Goodbye Retro Video Store Employee {ee_id}!")
                bar_break()
                return


if __name__ == "__main__":
    main()
