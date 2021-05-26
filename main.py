import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    

if __name__ == "__main__":
    main()

def list_options():

    options = {
        "1": "Add a Video",
        "2": "Edit a Video",
        "3": "Delete a Video",
        "4": "Get all of the Videos Information",
        "5": "Get one of the Videos Information",
        "6": "Add a Customer",
        "7": "Edit a Customer",
        "8": "Delete a Customer",
        "9": "Get all of the Customers Information",
        "10": "Get one of the Customers Information",
        "11": "Check out a Video to a Customer",
        "12": "Check in a Video from a Customer"
    }