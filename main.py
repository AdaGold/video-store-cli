import requests
from requests.api import options
from video_store import Employee


def print_stars():
    print("\n**************************\n")


def list_actions_on():

    actions_on = {
        "1": "Videos",
        "2": "Customers",
        "3": "Rentals",
        "6": "Quit"
    }

    print_stars()
    print("Welcome to the Retro Video Store CLI")
    print("Make your choice. You can manage:")
    print_stars()

    for choice_num in actions_on:
        print(f"Action {choice_num}. {actions_on[choice_num]}")

    return actions_on


def list_actions_video():

    actions_video = {
        "1": "Add a video",
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Get information about all videos",
        "5": "Get information about one video",
        "6": "Quit"
    }

    print_stars()
    print("What would you like to do? Make your choice.")
    print("These are the actions you can perform on Videos:")
    print_stars()

    for choice_num in actions_video:
        print(f"Action {choice_num}. {actions_video[choice_num]}")

    print_stars()

    return actions_video


def list_actions_customer():

    actions_customer = {
        "1": "Add a customer",
        "2": "Edit a customer",
        "3": "Delete a customer",
        "4": "Get information about all customers",
        "5": "Get information about one customer",
        "6": "Quit"
    }

    print_stars()
    print("What would you like to do? Make your choice.")
    print("These are the actions you can perform on Customers:")
    print_stars()

    for choice_num in actions_customer:
        print(f"Action {choice_num}. {actions_customer[choice_num]}")

    print_stars()

    return actions_customer


def list_actions_rentals():

    actions_rentals = {
        "1": "Check-out a video to a customer",
        "2": "Check-in a video to a customer",
        "6": "Quit"
    }

    print_stars()
    print("What would you like to do? Make your choice.")
    print("These are the actions you can perform on Rentals:")
    print_stars()

    for choice_num in actions_rentals:
        print(f"Action {choice_num}. {actions_rentals[choice_num]}")

    print_stars()

    return actions_rentals


def make_choice():
    # print_stars()
    choice = input("\nMake your selection using the option number >> ")
    return choice


def select_video(employee):
    video_id = input("Enter video ID >> ")
    if video_id.isnumeric():
        video_id = int(video_id)
        response = employee.get_one_video(id=video_id)
        return response
    else:
        print("Could not select a video. Please, enter valid ID.")


def select_customer(employee):
    customer_id = input("Enter customer ID >> ")
    if customer_id.isnumeric():
        customer_id = int(customer_id)
        employee.get_one_customer(id=customer_id)
    else:
        print("Could not select a customer. Please, enter valid ID.")


def print_video(video):
    print(f"""
        ID: {video["id"]}
        Title: {video["title"]}
        Release date: {video["release_date"]}
        Total inventory: {video["total_inventory"]}
        Available inventory: {video["available_inventory"]}
        """)


def print_customer(customer):
    print(f"""
        ID: {customer["id"]}
        Name: {customer["name"]}
        Phone: {customer["phone"]}
        Postal code: {customer["postal_code"]}
        Date Registered: {customer["registered_at"]},
        Videos checked-out: {customer["videos_checked_out_count"]}
        """)


def run_video_store_cli(active=True):

    employee = Employee()

    list_actions_on()

    while active:
        choice = make_choice()
        if choice == "1":
            options = list_actions_video()
            choice = make_choice()

            if choice == '1':
                print("Add a video")
                title = input("Enter the video title >> ")
                release_date = input("Enter the video release date >> ")
                total_inventory = input("Enter the video total inventory >> ")
                response = employee.add_video(title=title,
                                              release_date=release_date,
                                              total_inventory=total_inventory)

                print(
                    "New video has been added: ",
                    response["title"],
                    "has ID",
                    response["id"])

            elif choice == '2':
                print("Edit a video")
                print("Select video to edit.")
                select_video(employee)
                video = employee.selected_video
                print_video(video)
                new_title = input("Enter new title >> ")
                new_release_date = input("Enter new release date >> ")
                new_total_inventory = input("Enter new total inventory >> ")
                response = employee.update_video(
                    title=new_title,
                    release_date=new_release_date,
                    total_inventory=new_total_inventory)
                print("Video has been updated. Here is the updated video.")
                print_video(response)

            elif choice == '3':
                print("Delete a video")
                print("Select video to delete.")
                select_video(employee)
                response = employee.delete_video()
                print(f"Video with ID {response['id']} has been deleted.")

            elif choice == '4':
                print("Get information about all videos")
                for video in employee.list_all_videos():
                    print_video(video)

            elif choice == '5':
                print("Get information about one video")
                print("Select video.")
                response = select_video(employee)
                video = employee.selected_video
                if video is not None:
                    print_video(video)
                else:
                    print(response)

            elif choice == '6':
                # Quit
                active = False
                print("\nYou just stopped using the Retro Video Store CLI!")

        elif choice == "2":
            list_actions_customer()
            choice = make_choice()

            if choice == '1':
                print("Add a customer")
                name = input("Enter the customer name >> ")
                postal_code = input("Enter the customer postal code >> ")
                phone = input("Enter the customer phone >> ")
                response = employee.add_customer(name=name,
                                                 postal_code=postal_code,
                                                 phone=phone)

                print("New customer: ", response["name"])

            elif choice == '2':
                print("Edit a customer")
                print("Select customer to edit.")
                select_customer(employee)
                customer = employee.selected_customer
                print_customer(customer)

                name = input("Enter new customer name >> ")
                postal_code = input("Enter new customer postal code >> ")
                phone = input("Enter new customer phone >> ")
                updated_customer = employee.update_customer(
                    name=name,
                    postal_code=postal_code,
                    phone=phone)
                print("Customer has been updated. Here is the updated customer.")
                print_customer(updated_customer)

            elif choice == '3':
                print("Delete a customer")
                print("Select customer.")
                select_customer(employee)
                deleted_customer = employee.delete_customer()
                print(
                    f"Video with ID {deleted_customer['id']} has been deleted.")
            elif choice == '4':
                print("Get information about all customers")
                for customer in employee.list_all_customers():
                    print_customer(customer)
            elif choice == '5':
                print("Get information about one customer")
                print("Select customer.")
                select_customer(employee)
                customer = employee.selected_customer
                print_customer(customer)
            else:
                # Quit
                active = False
                print("\nYou just stopped using the Retro Video Store CLI!")

        elif choice == "3":
            list_actions_rentals()
            choice = make_choice()
            if choice == '1':
                print("Check-out a video to a customer")
                print("Select customer.")
                select_customer(employee)
                customer = employee.selected_customer
                print("Select video.")
                select_video(employee)
                video = employee.selected_video
                employee.check_out()
                print(
                    f"Video with ID {video['id']}, title '{video['title'].capitalize()}' checked-out to a customer {customer['name'].capitalize()} with ID {customer['id']}")

            elif choice == '2':
                print("Check-in a video to a customer")
                print("Select customer.")
                select_customer(employee)
                customer = employee.selected_customer
                print("Select video.")
                select_video(employee)
                video = employee.selected_video
                employee.check_in()
                print(
                    f"Video with ID {video['id']}, title '{video['title'].capitalize()}' checked-in from a customer {customer['name'].capitalize()} with ID {customer['id']}")

            else:
                # Quit
                active = False
                print("\nYou just stopped using the Retro Video Store CLI!")
        else:
            # Quit
            active = False
            print("\nYou just stopped using the Retro Video Store CLI!")


if __name__ == "__main__":
    run_video_store_cli()
