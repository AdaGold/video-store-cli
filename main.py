import requests

# from pyfiglet import figlet

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def front_logo():
#     logo = Figlet[font="rounded"]
#     print(colored(logo.renderText("flippant Video"), "blue"))

print_stars = lambda:print("*"*20)

def main():
    print("\n=================================\n")
    print("\nWELCOME TO RETRO VIDEO STORE\n")
    print("\n=================================\n")
    
    ui=str()
    rental_directory()

    while ui != "exit":
        ui=input("\nEnter an option: ")
        print("\n")
        print_stars()

        if ui== "1":
            add_a_video()
        elif ui == "2":
            edit_a_video()
        elif ui == "3":
            delete_a_video()
        elif ui == "4":
            get_info_all_videos()
        elif ui == "5":
            get_info_video()
        elif ui == "6":
            add_a_cutomer()
        elif ui == "7":
            edit_a_customer()
        elif ui == "8":
            delete_a_customer()
        elif ui == "9":
            get_info_one_customer()
        elif ui == "10":
            get_info_all_customers()
        elif ui == "11":
            checkout_video_to_customer()
        elif ui == "12":
            checkin_video_to_customer()
        elif ui=="13":
            break
        else:
            print("Invalid Option")
#1
def add_a_video():
    title=input("\nEnter a title: ")
    release_date=input("Enter a release date: ")
    total_inventory=input("Enter inventory: ")

    request_body = {
            "title":title,
            "release_date":release_date,
            "total_inventory":total_inventory,
            }
    
    r = requests.post(f"{URL}/videos", json=request_body)
    
    if r.status_code != 201:
        print(r.text)
    else:
        print("Add Successful!")
#2
def edit_a_video():
    video=input("\nEnter Video Id: ")
    title=input("Enter a title: ")
    release_date=input("Enter a release date: ")
    total_inventory=input("Enter inventory: ")

    request_body = {
            "title":title,
            "release_date":release_date,
            "total_inventory":total_inventory,
            }
    
    r = requests.put(f"{URL}/videos/{video}", json=request_body)

    if r.status_code != 200:
        print(r.text)   # explain?
    else:
        print("Edit Successful!")

#3
def delete_a_video():
    video=input("\nEnter Video Id: ")
    
    r = requests.delete(f"{URL}/videos/{video}")

    if r.status_code != 200:
        print(r.text)
    else:
        print("Delete Video Successful!")

#4
def get_info_all_videos():
    r = requests.get(f"{URL}/videos")

    if r.status_code != 200:
        print(r.text)   
    else:
        print(r.json()) 

#5
def get_info_video():
    video=input("\nEnter Video Id: ")

    r = requests.get(f"{URL}/videos/{video}")

    if r.status_code != 200:
        print(r.text)   
    else:
        print(r.json()) 

#6
def add_a_cutomer():
    name=input("\nEnter a customer name: ")
    postal_code=input("Enter postal code: ")
    phone=input("Enter phone number: ")

    request_body = {
            "name":name,
            "postal_code":int(postal_code),
            "phone":phone,
            }
    
    r = requests.post(f"{URL}/customers", json=request_body)
    
    if r.status_code != 201:
        print(r.text)
    else:
        print("✅ 👍 Add Successful!")
#7
def edit_a_customer():
    customer_id=input("\n Enter Customer ID: ")
    name=input("Enter a customer: ")
    postal_code=input("Enter postal code: ")
    phone=input("Enter phone number: ")

    request_body = {
            "name":name,
            "postal_code":int(postal_code),
            "phone":phone,
            }
    
    r = requests.put(f"{URL}/customers/{customer_id}", json=request_body) #???

    if r.status_code != 200:
        print(r.text)   # explain?
    else:
        print("Edit Successful!")
# 8
def delete_a_customer():
    customer_id=input("\n Enter Customer ID: ")

    r = requests.delete(f"{URL}/customers/{customer_id}")

    if r.status_code != 200:
        print(r.text)
    else:
        print("Delete Customer Successful!")   
#9
def get_info_one_customer():
    r = requests.get(f"{URL}/customers")
    if r.status_code != 200:
        print(r.text)   
    else:
        print(r.json()) 
        
#10
def get_info_all_customers():
    r = requests.get(f"{URL}/customers")

    if r.status_code != 200:
        print(r.text)   
    else:
        print(r.json()) 

#11
def checkout_video_to_customer():
    customer_id=input("Enter Customer ID: ")
    video_id=input("Enter Video ID: ")

    request_body={
        "customer_id": int(customer_id),
        "video_id": int(video_id),
    }
    
    r = requests.post(f"{URL}/rentals/check-out", json=request_body)

    if r.status_code != 200:
        print(r.text)   
    else:
        print("Rental Check-Out Successful!")


#12
def checkin_video_to_customer():
    customer_id=input("Enter Customer ID: ")
    video_id=input("Enter Video ID: ")

    request_body={
        "customer_id": int(customer_id),
        "video_id": int(video_id),
    }
    
    r = requests.post(f"{URL}/rentals/check-in", json=request_body)

    if r.status_code != 200:
        print(r.text)   
    else:
        print("Rental Check-In Successful!")


print_stars = lambda:print("*"*20)

def rental_directory():
    options = {
        "1": "➕ Add a video 🎥", 
        "2": "🔎 Edit a video 🎥",
        "3": "❌ Delete a video 🎥", 
        "4": "📙 Get info about ALL videos 🎥", 
        "5": "📘 Get info about ONE video 🎥", 
        "6": "➕ Add a customer",
        "7": "🔎 Edit a customer 🤠",
        "8": "❌ Delete a customer 🤠",
        "9": "📙 Get info about ONE customer 🤠",
        "10":"📘 Get info about ALL customers 🤠",
        "11":"📤 Check-OUT a video to a customer",
        "12":"📩 Check-IN a video from a customer",
        "13":"⏏ Quit"
        }

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options




if __name__ == "__main__":
    main()
    