import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_all_videos():
    response = requests.get(f"{BACKUP_URL}/videos")
    movies = []
    for movie in response.json():
        movies.append({"id": movie['id'], "title": movie['title']})
    for mov in movies:
        print(f"{mov['id']}: {mov['title']}")

def list_one_video():
    choice = input("Please provide the video id: ")
    response = requests.get(f"{BACKUP_URL}/videos/{choice}")
    if response.status_code == 200:
        response = response.json()
        print(f"{response['id']}: {response['title']} has {response['total_inventory']} copy.")
        return(True)
    else:
        print(f"There is an error with the id you provided.")
        return(False)

def create_a_video():
    title = input("Please provide the video title: ")
    total_inventory = input("How many copies do you have?  ")
    release_date = input("What is the release date?  ")
    choice = {"title": title, "total_inventory": total_inventory, "release_date": release_date}
    response = requests.post(f"{BACKUP_URL}/videos", json = choice)
    response = response.json()
    print(f"{response['title']} was successfully created with id {response['id']}")

def update_a_video():
    id = input("Please enter the id of the video you would like to update:  ")
    title = input("Please provide the video title: ")
    total_inventory = input("How many copies do you have?  ")
    release_date = input("What is the release date?  ")
    choice = {"title": title, "total_inventory": total_inventory, "release_date": release_date}
    response = requests.put(f"{BACKUP_URL}/videos/{id}", json = choice)
    response = response.json()
    print(f"Video ID {response['id']} was successfully updated.")

def delete_a_video():
    id = input("Please enter the id of the video you would like to delete:  ")
    response = requests.delete(f"{BACKUP_URL}/videos/{id}")
    if response.status_code == 200:
        response = response.json()
        print(f"Video ID {response['id']} has been deleted.")
        return(True)
    else:
        print(f"There is an error with the id you provided.")
        return(False)

def list_all_customers():
    response = requests.get(f"{BACKUP_URL}/customers")
    customers = []
    for customer in response.json():
        customers.append({"id": customer['id'], "name": customer['name'], "registered_at": customer['registered_at'], "postal_code": customer['postal_code'], "phone": customer['phone']})
    for cus in customers:
        print(f"{cus['id']}: {cus['name']} \n registered_at: {cus['registered_at']} \n postal_code: {cus['postal_code']} \n phone: {cus['phone']}")

def list_one_customer():
    choice = input("Please provide the customer id: ")
    response = requests.get(f"{BACKUP_URL}/customers/{choice}")
    if response.status_code == 200:
        response = response.json()
        print(f"{response['id']}: {response['name']} registered at {response['registered_at']}.")
        return(True)
    else:
        print(f"There is an error with the id you provided.")
        return(False)

def create_a_customer():
    name = input("Please provide the customer's name: ")
    postal_code = input("What is the customer's postal code?:  ")
    phone = input("What is the customer's phone number?:  ")
    choice = {"name": name, "postal_code": postal_code, "phone": phone}
    response = requests.post(f"{BACKUP_URL}/customers", json = choice)
    response = response.json()
    print(f"Customer {name} was successfully created with id {response['id']}")

def update_a_customer():
    id = input("Please enter the id of the customer you would like to update:  ")
    name = input("Please provide the customer's name: ")
    postal_code = input("What is the customer's postal code?:  ")
    phone = input("What is the customer's phone number?:  ")
    choice = {"name": name, "postal_code": postal_code, "phone": phone}
    response = requests.put(f"{BACKUP_URL}/customers/{id}", json = choice)
    response = response.json()
    print(f"Customer ID {response['id']} was successfully updated.")

def delete_a_customer():
    id = input("Please enter the id of the customer you would like to update:  ")
    response = requests.delete(f"{BACKUP_URL}/customers/{id}")
    if response.status_code == 200:
        response = response.json()
        print(f"Customer ID {response['id']} has been deleted.")
        return(True)
    else:
        print(f"There is an error with the id you provided.")
        return(False)

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print()
    options = {
        "1": "List all videos", 
        "2": "List one video",
        "3": "Create a video",
        "4": "Update a video", 
        "5": "Delete a video",
        "6": "List all customers", 
        "7": "Get one customer",
        "8": "Create a customer",
        "9": "Update a customer", 
        "10": "Delete a customer", 
        "11": "Quit"
        # "12": "Check out a video to a customer",
        # "13": "Check in a video to a customer",
        }

    for opt in options:
        print(f"{opt}: {options[opt]}")
    print()
    choice = input("SELECT AN OPTION FROM THE MENU: ")

    if choice == "1":
        list_all_videos()

    if choice == "2":
        success = False
        while not success:
            success = list_one_video()

    if choice == "3":
        create_a_video()

    if choice == "4":
        update_a_video()

    if choice == "5":
        success = False
        while not success:
            success = delete_a_video()

    if choice == "6":
        list_all_customers()

    if choice == "7":
        success = False
        while not success:
            success = list_one_customer()

    if choice == "8":
        create_a_customer()

    if choice == "9":
        update_a_customer()

    if choice == "10":
        delete_a_customer()
    
    if choice == "11":
        print("You have now exited the interface.")

if __name__ == "__main__":
    main()