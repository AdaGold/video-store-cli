import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

'''
    =============================================
    HELPER PRINTS
    =============================================
'''

def bar_break():
    print("\n==========================\n")

def list_options_ee():
    options = {
        "1" : "Add Video to Store Stock",
        "2" : "Edit Video Info",
        "3" : "Remove Video From Inventory",
        "4" : "View Current Store Stock",
        "5" : "View Video Info",
        "6" : "Add New Customer",
        "7" : "Edit Existing Customer",
        "8" : "Delete Existing Customer",
        "9" : "View Existing Customer Records",
        "10" : "View All Existing Customers",
        "11" : "Check Out",
        "12" : "Check In"
    }

    bar_break()
    print("Here are your available options:\n")
    for choice in options:
        print(f"Option {choice}. {options[choice]}")

    bar_break()

    return options

def list_options_cust():
    options = {

    }

'''
    =============================================
    ALL OPTION FUNCTIONS
    =============================================
'''

def add_video():
    pass

def edit_video():
    pass

def remove_video():
    pass

def view_video_stock():
    pass

def view_single_video():
    pass

def add_customer():
    pass

def edit_customer():
    pass

def delete_customer():
    pass

def view_customer():
    pass

def view_all_customers():
    pass

def checking_out():
    pass

def checking_in():
    pass

'''
    =============================================
    MAIN
    =============================================
'''

def main(in_use=True, is_employee=False):
    print("WELCOME TO RETRO VIDEO STORE")

    ee_id = input("Employee? Please enter your 4 digit id. Hit Enter to continue as a customer.\n")
    if len(ee_id) == 4 and ee_id.isdigit():
        print(f"Welcome to work, Employee {ee_id}")
        is_employee = True
        options = list_options_ee()

    while is_employee and in_use:
        func_call_dict = {
            "1" : add_video,
            "2" : edit_video,
            "3" : remove_video,
            "4" : view_video_stock,
            "5" : view_single_video,
            "6" : add_customer,
            "7" : edit_customer,
            "8" : delete_customer,
            "9" : view_customer,
            "10" : view_all_customers,
            "11" : checking_out,
            "12" : checking_in
        }

        choice = None
        while choice not in func_call_dict:
            choice = input("What would you like to do? Q to quit.\n")

        if choice == "Q" or choice == 'q':
            print("Thank you for visiting the Retro Video Store!")
            bar_break()
            return
        else:
            func_call_dict[choice]()
    
    while in_use:
        pass


if __name__ == "__main__":
    main()