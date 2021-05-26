import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://aida-retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    response = requests.get(BACKUP_URL + "/videos")
    print(response.json())


if __name__ == "__main__":
    main()


roadmap = {
    #Video
    "1": "Create a video",
    "2": "Update a video",
    "3": "Delete a video",
    "4": "List all videos",
    "5": "Get one video", 
    #Customer
    "6": "Create a customer",
    "7": "Update a customer",
    "8": "Delete a customer",
    "9": "Select one customer", 
    "10": "List all customers",
    #Rental
    "11": "Check out a video to a customer",
    "12": "Check in a video from a customer",
    #Optional
    "13": "Look up rental due",
    "14": "Look up checkout videos",
    "15": "Look up overdue videos",
    "16": "Quit"
    }