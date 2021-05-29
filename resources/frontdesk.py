OPTIONS = {
    0: "Quit",
    1: "Add a new video",
    2: "Edit a video",
    3: "Delete a video",
    4: "View inventory",
    5: "Get video information",
    6: "Add a new customer",
    7: "Edit a customer",
    8: "Remove a customer",
    9: "Get customer information",
    10: "View all registered customers",
    11: "Check-out a video to a customer",
    12: "Check-in a video from a customer",
        }

def show_options():
    for choice, option in OPTIONS.items():
        print(f"Option #{choice}: {option}")



def print_inventory(inventory):

    for entry, value in inventory.items():

        print("-"*40)
        print()
        print(f"\tID: {entry}")
        print(f"Title: {value['title']}")
        print(f"Release: {value['release_date']}")
        print(f"Available to rent: {value['available_inventory']}")
        print(f"Total Inventory: {value['total_inventory']}\n")


def print_accounts(accounts):

    for entry, value in accounts.items():

        print("-"*30)
        print()
        print(f"Customer ID: {entry}")
        print(f"Name: {value['name']}")
        print(f"Phone: {value['phone']}")
        print(f"Postal Code: {value['postal_code']}")
        print(f"Videos checked-out: {value['videos_checked_out_count']}\n")