# from model import Model # this will be rental, customer and video?
from constants import *
# from customer import Customer
# import requests


def start_program():
    print(f'\n\n {WELCOME} ')
    print(STARS)
    print(STORE_NAME)
    print(STARS)
    
def print_little_stars():
    print(LITTLE_STARS)

def print_stars_centered():
    print(STARS_HIGHLIGHT)

def show_options():
    options = [
        # "# Video - all work"
        "GET Info All Videos", 
        "Add A Video",
        "Get Info One Video ", 
        "Edit A Video", 
        "Delete A Video", 
        # Rental - DOES NOT WORK YET
        "CHECK_OUT a VIDEO to a CUSTOMER (11)-(Mark selected task complete - POST)",
        "CHECK_IN a VIDEO from a CUSTOMER (Mark selected task incomplete - POST)",
        # Customer - all work
        "Get Information On All Customers", 
        "Add A Customer",
        "Get Information On One Customer", 
        "Edit A Customer", 
        "Delete A Customer",
        # Flow
        "List All Options",
        "Quit"]
    for i in range(len(options)):
        print(f' OPTION \n \
            {i}: {options[i]}')
    return options

def make_choice(options):
    valid_choices = set(range(len(options)))
    choice = None
    while (not choice and choice != 0) or not (isinstance(choice, int)) \
        or  int(choice) not in valid_choices:
        # print("\nWhat would you like to do?\n\nSelect 12 to see all options again")
        print(LOOP_OPTIONS) # added instead
        try:
            choice = int(input("\nMake your selection using the option number: "))
        except:
            choice = None
            print("\nPlease enter only a number of the given options")
            print(LOOP_OPTIONS)
    return choice



    


