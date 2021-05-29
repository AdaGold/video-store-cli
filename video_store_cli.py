#!/usr/bin/env python3
from app.send_requests import *
from app.display import *


def get_option(n):
    option = input().lower()
    while True:
        if option == 'q':
            quit()
        elif is_integer(option) and int(option) in range(1, n + 1):
            return option
        option = input("Sorry, that's not a valid option. Please try again.").lower()


def get_id(resource):
    resource_id = input(f"Please provide the {resource}'s id: ")
    if not is_integer(resource_id):
        print("Please provide an integer.")
        get_option(resource)
    return resource_id


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def main_menu():
    n = display_main_menu()
    option = get_option(n)
    if option == '1':
        rental_menu()
    elif option == '2':
        customer_menu()
    elif option == '3':
        video_menu()


def rental_menu():
    n = display_rental_menu()
    option = get_option(n)
    if option == '1':
        print("CHECKOUT")
        customer_id = get_id("customer")
        video_id = get_id("video")
        checkout(customer_id, video_id)
        rental_menu()

    elif option == '2':
        print("CHECKIN")
        customer_id = get_id("customer")
        video_id = get_id("video")
        checkin(customer_id, video_id)
        rental_menu()

    elif option == '3':
        main_menu()


def video_menu():
    n = display_video_menu()
    option = get_option(n)
    if option == '1':
        print("GET VIDEO BY ID")
        video_id = get_id("video")
        get_video(video_id)
        video_menu()

    elif option == '2':
        print("LIST ALL VIDEOS")
        list_videos()
        video_menu()

    elif option == '3':
        print("CREATE NEW VIDEO")
        print("Please enter the following:")
        title = input("Title: ")
        release_date = input("Release date (YYYY/MM/DD): ")
        total_inventory = input("Total inventory: ")
        add_video(title, release_date, total_inventory)
        video_menu()

    elif option == '4':
        print("EDIT VIDEO")
        print("Please enter the following:")
        video_id = get_id("video")
        title = input("Title: ")
        release_date = input("Release date (YYYY/MM/DD): ")
        total_inventory = input("Total inventory: ")
        edit_video(video_id, title, release_date, total_inventory)
        video_menu()

    elif option == '5':
        print("DELETE VIDEO")
        video_id = get_id("video")
        delete_video(video_id)
        video_menu()

    elif option == '6':
        main_menu()


def customer_menu():
    n = display_customer_menu()
    option = get_option(n)
    if option == '1':
        print("GET customer BY ID")
        customer_id = get_id("customer")
        get_customer(customer_id)
        customer_menu()

    elif option == '2':
        print("LIST ALL CUSTOMERS")
        list_customers()
        customer_menu()

    elif option == '3':
        print("CREATE NEW CUSTOMER")
        print("Please enter the following:")
        name = input("Name: ")
        postal = input("Postal code: ")
        phone = input("Phone number: ")
        add_customer(name, postal, phone)
        customer_menu()

    elif option == '4':
        print("EDIT CUSTOMER")
        print("Please enter the following:")
        customer_id = get_id("customer")
        name = input("Name: ")
        postal = input("Postal code: ")
        phone = input("Phone number: ")
        edit_customer(customer_id, name, postal, phone)
        customer_menu()

    elif option == '5':
        print("DELETE CUSTOMER")
        customer_id = get_id("customer")
        delete_customer(customer_id)
        customer_menu()

    elif option == '6':
        main_menu()


if __name__ == '__main__':
    display_welcome()
    main_menu()
