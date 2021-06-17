def welcome_banner():

    print("""\n
    ____    ____   ____   ____   ____   ____   ____   ____ 
    ||W || ||E || ||L || ||C || ||O || ||M || ||E || ||! ||
    ||__|| ||__|| ||__|| ||__|| ||__|| ||__|| ||__|| ||__||
    |/__\| |/__\| |/__\| |/__\| |/__\| |/__\| |/__\| |/__\|
    
    """)


def print_linebreaks():
    print("\n#############################\n")


def main_menu_options(): 
    print("1: Video Information")
    print("2: Customer Information")
    print("3: Rental Information")
    print("4: Exit Program")


def video_menu_options():
    print("1:  List All Videos")
    print("2:  Add a New Video To Stock")
    print("3:  Select A Video To View")
    print("4:  Select A Video To Edit")
    print("5:  Select A Video To Delete")


def customer_menu_options():
    print("1:  List All Customers")
    print("2:  Add A New Customer To System")
    print("3:  Select A Customer To View")
    print("4:  Select A Customer To Edit")
    print("5:  Select A Customer To Delete") 


def rental_menu_options():
    print("1:  Check Out A Video")
    print("2:  Check In A Video")
    print("3:  Look Up Rentals by Video")
    print("4:  Look Up Rentals By Customer")
    print("5:  View All Overdue Movies")


def print_video_info(video):
    print("\n")
    print(f"Title: {video['title']}")
    print(f"ID: {video['id']}")
    print(f"Release Date: {video['release_date']}")
    print(f"Total Inventory: {video['total_inventory']}")
    print(f"Available Inventory: {video['available_inventory']}")


def print_customer_info(customer):
    print("\n")
    print(f"Name:  {customer['name']}")
    print(f"ID:  {customer['id']}")
    print(f"Phone Number:  {customer['phone']}")
    print(f"Zip Code:  {customer['postal_code']}")
    print(f"Registration Date:  {customer['registered_at']}")
    print(f"Videos Checked Out:  {customer['videos_checked_out_count']}")
    

def name_or_id():
    user_input = input("Would you like to search by Customer name? Y/N:  ")
    if user_input.upper() == "Y":
        user_input = input("Please enter the name of the customer you would like to select:  ")
        return user_input.title()
    return False

def title_or_id():
    user_input = input("Would you like to search by title? Y/N   ")
    if user_input.upper() == "Y":
        user_input = input("Please enter the title of the movie you are looking for:   ")
        return user_input.title()
    return False


def print_overdue_info(overdue_video):
    print("\n")
    print(f"Video ID: {overdue_video['video_id']}")
    print(f"Customer ID: {overdue_video['customer_id']}")
    print(f"Due Date:  {overdue_video['due_date']}")

