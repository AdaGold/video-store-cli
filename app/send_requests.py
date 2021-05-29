import requests
import json
from app.display import display_dict

API_ADDRESS = "https://retrovideostoreformai.herokuapp.com"


def add_video(title, release_date, total_inventory):
    url = API_ADDRESS+"/videos"
    payload = json.dumps({
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def edit_video(video_id, title, release_date, total_inventory):
    url = API_ADDRESS+"/videos/"+video_id
    payload = json.dumps({
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def delete_video(video_id):

    url = API_ADDRESS+"/videos/"+video_id
    response = requests.request("DELETE", url)
    if check_response(response):
        display_dict(response.json())


def list_videos():
    url = API_ADDRESS+"/videos"
    response = requests.request("GET", url)
    videos = response.json()
    for video in videos:
        display_dict(video)


def get_video(video_id):
    url = API_ADDRESS+"/videos/"+video_id
    response = requests.request("GET", url)
    if check_response(response):
        display_dict(response.json())


def add_customer(name, postal, phone):
    url = API_ADDRESS+"/customers"
    payload = json.dumps({
        "name": name,
        "postal_code": postal,
        "phone": phone
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def edit_customer(customer_id, name, postal, phone):
    url = API_ADDRESS+"/customers/"+customer_id
    payload = json.dumps({
        "name": name,
        "postal_code": postal,
        "phone": phone
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def delete_customer(customer_id):

    url = API_ADDRESS+"/customers/"+customer_id
    response = requests.request("DELETE", url)
    if check_response(response):
        display_dict(response.json())


def list_customers():
    url = API_ADDRESS+"/customers"
    response = requests.request("GET", url)
    if check_response(response):
        customers = response.json()
        for customer in customers:
            display_dict(customer)


def get_customer(customer_id):
    url = API_ADDRESS+"/customers/"+customer_id
    response = requests.request("GET", url)
    if check_response(response):
        display_dict(response.json())


def checkout(customer_id, video_id):
    url = API_ADDRESS+"/rentals/check-out"
    payload = json.dumps({
        "customer_id": customer_id,
        "video_id": video_id
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def checkin(customer_id, video_id):
    url = API_ADDRESS+"/rentals/check-in"

    payload = json.dumps({
        "customer_id": customer_id,
        "video_id": video_id
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if check_response(response):
        display_dict(response.json())


def check_response(response):
    if response.status_code == 200 or response.status_code == 201:
        print()
        print('--SUCCESS--')
        print()
        return True
    elif response.status_code == 404:
        print()
        print('Resource not found, please try again.')
        print()
    else:
        print()
        print('Something went wrong, please try again.')
        print()
    return False
