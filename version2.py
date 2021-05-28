import requests
from customer import Customer
from video import Video
import datetime

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_options(): 
    options = {
        "1": "Customer Services", 
        "2": "Video Stock Services",
        "3": "Rental Services", 
        "4": "Quit"
        }
    
    #print_stars()
    print("Welcome to the VideoStore CLI")
    print("These are the actions you can perform")
    #print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options

def make_choice(options):  #what is task_list referring to
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        choice = input("Make your selection using the option number: ")

    if choice == "1":
        return choice
    if choice == "2":
        return choice
    if choice == "3":
        return choice

def customer_info_generator():
    customer_name = input("Please enter customer name:  ")
    postal_code = input("Please enter customer postal code:  ")
    phone_number = input("Please enter customer phone number:  ")
    return customer_name, postal_code, phone_number


def run_cli(play=True):

    customer = Customer(url="https://retro-video-store-api.herokuapp.com")
    video = Video(url="https://retro-video-store-api.herokuapp.com")

    options = list_options()


    while play==True:
        choice = make_choice(options)

    if choice == "1":
        task_prompt1 = input(" 1 for Customer Creation, 2 for Customer Update")
        if task_prompt1 == "1":
            customer_name = input("Please enter customer name:  ")
            postal_code = input("Please enter customer postal code:  ")
            phone_number = input("Please enter customer phone number:  ") 
            respone = customer.create_customer(customer_name=customer_name, postal_code=postal_code, phone_number=phone_number)
            print(f"Customer profile '{customer_name}' has been created.")
        if task_prompt1 == "2":
            customer_id = input("Please enter valid customer ID:  ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                info = customer.get_customer(customer_id=customer_id)
                print(info)
        task_prompt2 = input("type DELETE to delete customer, UPDATE to update customer, Q to return to Main Menu:   ")
        if task_prompt2 == "DELETE":
            pass
            #ask customer for ID or delete customer with self.selected?
        if task_prompt2== "UPDATE":
            pass
            #user ID to update
        if task_prompt2 == "Q":
            pass
            run_cli()

            
        
        selected_customer_task = input("")