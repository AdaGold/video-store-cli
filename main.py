import requests


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_options():
    options = {
        "1" : "Add a Video", 
        "2" : "Edit a Video",
        "3" : "Delete a Video",
        "4" : "Browse all Videos",
        "5" : "Select one Video",
        "6" : "Add a new customer",
        "7" : "Update customer profile",
        "8" : "Remove customer",
        "9" : "View customer profile",
        "10" : "View all customers",
        "11" : "Check out a Video",
        "12" : "Return a Video"
    }
    for choice in options:
        print(f"Option {choice}: {options[choice]}")
def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print("Please select from the following options")
    list_options()


if __name__ == "__main__":
    main()