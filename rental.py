from video import is_int
from customer import print_stars, get_main_menu_choice

# Select rental option
def get_rental_choice():
    options = {
        "1": "Check out rental", 
        "2": "Chech in rental",
        "3": "Back to main menu"
        }
    
    print("\nThese are the actions you can perform: \n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    customer_choice = None

    while customer_choice not in valid_choices:
        if customer_choice != None:
            print("\nInvalid option.")
            customer_choice = input("\nMake your selection using valid option number: ")
        else:
            customer_choice = input("\nMake your selection using the option number: ")
    
    return customer_choice

# Response to selected rental option
def respond_rental_choice(choice, cvr, main_menu_choice):
    if choice=='1':
        cvr.print_list_reference()
        print("\nTo rent a video to a customer please enter following infomation: ")
        customer_id=input("Customer id: ") 
        if is_int(customer_id):
            cvr.get_customer(id=is_int(customer_id))

        video_id=input("Video id: ")
        if is_int(video_id):
            cvr.get_video(id=is_int(video_id))

        if not cvr.selected_video or not cvr.selected_customer:
            print("Invalid customer id or video id, could not check out.")
        else:
            cvr.check_out(video_id=video_id, customer_id=customer_id)
            print_stars()
            if "message" in cvr.selected_rental:
                print("View check-out info: ", cvr.selected_rental["message"])
            elif "Message" in cvr.selected_rental:
                print("View check-out info: ", cvr.selected_rental["Message"])
            else:
                print("View check-out info: ", cvr.selected_rental)

    elif choice == "2":
        cvr.print_list_reference()            
        print("\nTo return a video please enter following infomation: ")
        customer_id=input("Customer id: ") 
        if is_int(customer_id):
            cvr.get_customer(id=is_int(customer_id))

        video_id=input("Video id: ")
        if is_int(video_id):
            cvr.get_video(id=is_int(video_id))

        if not cvr.selected_video or not cvr.selected_customer:
            print("Invalid customer id or video id, could not check out.")
        else:
            cvr.check_in(video_id=video_id, customer_id=customer_id)
            print_stars()
            if "message" in cvr.selected_rental:
                print("View check-in info: ", cvr.selected_rental["message"])
            else:
                print("View check-in info: ", cvr.selected_rental)

    else:
        main_menu_choice = get_main_menu_choice()
    
    print_stars()

    return main_menu_choice