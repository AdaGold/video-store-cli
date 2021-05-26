import requests
import json

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
    return response


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
    return response


def delete_video(video_id):

    url = API_ADDRESS+"/videos/"+video_id
    response = requests.request("DELETE", url)
    return response


def list_videos():
    url = API_ADDRESS+"/videos"
    response = requests.request("GET", url)
    return response


def get_video(video_id):
    url = API_ADDRESS+"/videos/"+video_id
    response = requests.request("GET", url)
    return response


def add_customer(name, postal, phone):
    url = API_ADDRESS+"/customers"
    payload = json.dumps({
        "name": name,
        "postal": postal,
        "phone": phone
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def edit_customer(customer_id, name, postal, phone):
    url = API_ADDRESS+"/customers/"+customer_id
    payload = json.dumps({
        "name": name,
        "postal": postal,
        "phone": phone
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


def delete_customer(customer_id):

    url = API_ADDRESS+"/customers/"+customer_id
    response = requests.request("DELETE", url)
    return response


def list_customers():
    url = API_ADDRESS+"/customers"
    response = requests.request("GET", url)
    return response


def get_customer(customer_id):
    url = API_ADDRESS+"/customers/"+customer_id
    response = requests.request("GET", url)
    return response


def checkout(customer_id, video_id):
    url = API_ADDRESS+"/rentals/check-out"
    payload = json.dumps({
        "customer_id": 23,
        "video_id": 26
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def checkin(customer_id, video_id):
    url = API_ADDRESS+"/rentals/check-in"

    payload = json.dumps({
        "customer_id": 23,
        "video_id": 26
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response
