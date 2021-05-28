from constants import *

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
        # "# Video 
        "GET Info All Videos", 
        "Add A Video",
        "Get Info One Video ", 
        "Edit A Video", 
        "Delete A Video", 
        # Rental 
        "Check Out A Video To A Customer",
        "Check In A Video From A Customer",
        # Customer 
        "Get Information On All Customers", 
        "Add A Customer",
        "Get Information On One Customer", 
        "Edit A Customer", 
        "Delete A Customer",
        # Other
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
        print(LOOP_OPTIONS)  
        try:
            choice = int(input("\nMake your selection using the option number: "))
        except:
            choice = None
            print("\nPlease enter only a number of the given options")
            print(LOOP_OPTIONS)
    return choice



    


