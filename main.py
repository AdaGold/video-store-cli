#installed request in local machine 
import requests
from video_store import Videostore


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()

options = {
    "1": "Create a video",
    "2": "Update selected video",
    "3": "Delete selected video",
    "4": "list all videos",
    "5": "Select a video", 

    "6": "Create a customer",
    "7": "Update selected customer",
    "8": "Delete selected customer",
    "9": "Select a customer", 
    "10": "Select all customers",

    "11": "Mark selected video complete",
    "12": "Mark selected video incomplete",

    "13": "Quit"
    }

#feel free to use Class 
# ada Resources - Slack CLI 