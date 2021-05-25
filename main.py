import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    choice = input("Pick something! ")
    
    if choice == "1":
        response = requests.get(BACKUP_URL +"/videos")
        print(response.json())
    pass

if __name__ == "__main__":
    main()