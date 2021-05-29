import requests

def get_one(cust_id):
    try: 
        print(requests.get(f"https://retro-video-store-api.herokuapp.com/customers/{ui}/rentals").text)
    except:
        print("Invalid Customer ID")
        
def get_all():
    print(response=requests.get("https://retro-video-store-api.herokuapp.com/customers").text)


if __name__ == "__main__":
    ui=str()
    
    while ui != "exit":
        ui=input("Enter a customer_id to get rentals, or enter None for all.")
        if ui:
            get_one(ui)
        else:
            get_all()
