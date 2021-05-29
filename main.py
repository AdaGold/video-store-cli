import requests
import json
from resources.frontdesk import show_options, print_inventory, print_accounts


def get_path(path):
    endpoints = {
        1:'videos/', 
        2: 'customers/', 
        3: 'rentals/check-out/', 
        4: 'rentals/check-in/'
        }

    return f'https://loucadoura.herokuapp.com/{endpoints[path]}'


#=========================HELPERS=========================


def valid_video(title, release, inventory):

    if not(title and release and inventory):
        return False

    return {"title": title, "release_date": release, "total_inventory": inventory}


def valid_customer(name, postal_code, phone):

    if not(name and postal_code and phone):
        return False

    return {"name": name, "postal_code": postal_code, "phone": phone}


#=========================EMPLOYEE/STOREROOM=========================

all_videos = {}
# would be lazy-loading inside its class but no time


def get_all_videos():

    if len(all_videos) == 0:
        path = get_path(1)
        videos_list = requests.get(path).json()

        for vhs in videos_list:
            all_videos[vhs["id"]] = vhs

    return all_videos

def get_video(video_id):

    path = get_path(1)
    video = requests.get(path+f"{video_id}/").json()

    return video


def post_video(new_title, new_release, inventory):
    body = valid_video(new_title, new_release, inventory)

    if not body:
        print("\n Invalid Data. Please try again\n")
        return get_options()

    path = get_path(1)
    response = requests.post(path, json=body)
    return response

def edit_video(video_id, new_title, release_date, inventory):

    body = valid_video(new_title, release_date, inventory)
    if not body:
        print("\n Invalid Data. Please try again\n")
        return get_options()

    path = get_path(1)
    response = requests.put(path+f"{video_id}/", json=body) #.json()
    return response


def delete_video(video_id):

    to_delete = get_video(video_id)
    path = get_path(1)
    response = requests.delete(path+f"{video_id}/").json()

    return response


#=======================CASHIER=============================


all_customers = {}


def get_all_customers():
    if len(all_customers) == 0:
        path = get_path(2)
        customer_list = requests.get(path).json()
        for account in customer_list:
            all_customers[account["id"]] = account
        
    return all_customers


def get_customer_info(customer_id):
    path = get_path(2)
    customer = requests.get(path+f"{customer_id}/").json()
    return customer


def add_customer(new_customer, postal_code, phone):
    body = valid_customer(new_customer, postal_code, phone)

    if not body:
        print("\n Invalid Data. Please try again\n")
        return get_options()

    path = get_path(2)
    response = requests.post(path,json=body)

    return response


def edit_customer(customer_id, new_profile, new_postal_code, new_phone):
    to_update = get_customer_info(customer_id)
    body = valid_customer(new_profile, new_postal_code, new_phone)

    if not body:
        print("\n Invalid Data. Please try again\n")
        return get_options()

    path = get_path(2)
    response = requests.put(path+f"{customer_id}/", json=body)

    return response


def delete_customer(customer_id):
    to_delete = get_customer_info(customer_id)

    path = get_path(2)
    response = requests.delete(path+f"{customer_id}/").json()

    return response


def check_out_video(customer_id, video_id):
    path = get_path(3)
    body = {"customer_id": customer_id, "video_id": video_id}
    response = requests.post(path, json=body)
    return response


def check_in_video(customer_id,  video_id):
    path = get_path(4)
    body = {"customer_id": customer_id, "video_id": video_id}
    response = requests.post(path, json=body)
    return response


# ======================MAIN===============================


def get_options():
    inventory = get_all_videos()
    accounts = get_all_customers()

    show_options()
    choice = int(input())

    if choice == 0:
        print("Quitting.")

    elif choice == 1:
        new_title = input("Title to add: ")
        new_release = input("Release date: ")
        inventory = input("Total Inventory: ")

        print(post_video(new_title, new_release, inventory))

    elif choice == 2:
        video_id = input("To edid a video, insert its ID: ")
        new_title = input("New Title: ")
        release_date = input("Release date: ")
        inventory = input("Total Inventory: ")

        to_edit = get_video(video_id)

        print(f"Video to edit: {to_edit}")  # TODO: update available_inventory
        print(edit_video(video_id, new_title, release_date, inventory))

    elif choice == 3:
        video_id = input("Insert the video ID to be deleted: ")
        print(delete_video(video_id))

    elif choice == 4:
        print_inventory(inventory)

    elif choice == 5:
        video_id = input("Insert the video ID to get its information: ")
        print(get_video(video_id))

    elif choice == 6:
        new_customer = input("Name: ")
        postal_code = input("Postal Code: ")
        phone = input("Phone: ")

        print(add_customer(new_customer, postal_code, phone))

    elif choice == 7:
        customer_id = input("Customer ID to edit pls: ")
        new_profile = input("New Profile Name: ")
        new_postal_code = input("New Postal Code: ")
        new_phone = input("New Phone: ")

        print(edit_customer(customer_id, new_profile, new_postal_code, new_phone))

    elif choice == 8:
        customer_id = input("Insert the customer's ID to be removed: ")
        print(delete_customer(customer_id))

    elif choice == 9:
        customer_id = input("Customer ID to check pls: ")
        print(get_customer_info(customer_id))

    elif choice == 10:
        print_accounts(accounts)

    elif choice == 11:
        video_id = input("Insert video ID to check-out: ")
        customer_id = input("Insert customer ID to check-out: ")

        print(check_out_video(customer_id, video_id))

    elif choice == 12:
        video_id = input("Insert video ID to check-in: ")
        customer_id = input("Insert customer ID to check-in: ")

        print(check_in_video(customer_id, video_id))


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print("Choose an option:")
    get_options()


if __name__ == "__main__":
    main()
