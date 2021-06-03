def print_select_one():
    print()
    print("------------------------------------------")
    print("Please select one of the following options:")
    print()


def display_dict(video):
    print()
    for key in video.keys():
        print(key, ": ", video[key])


def display_main_menu():
    """
    returns the number of options in the menu
    """
    print_select_one()
    print("1 - Rental menu")
    print("2 - Customer menu")
    print("3 - Video menu")
    print("q - QUIT")
    print()
    return 3


def display_customer_menu():
    """
    returns the number of options in the menu
    """
    print_select_one()
    print("1 - Get customer details by id")
    print("2 - List all customers")
    print("3 - Create new customer")
    print("4 - Update existing customer")
    print("5 - Delete customer")
    print("6 - BACK to main menu")
    print("q - QUIT")
    print()
    return 6


def display_video_menu():
    """
    returns the number of options in the menu
    """
    print_select_one()
    print("1 - Get video details by id")
    print("2 - List all videos")
    print("3 - Create new video")
    print("4 - Update existing video")
    print("5 - Delete video")
    print("6 - BACK to main menu")
    print("q - QUIT")
    print()
    return 6


def display_rental_menu():
    """
    returns the number of options in the menu
    """
    print_select_one()
    print("1 - Video check-out")
    print("2 - Video check-in")
    print("3 - BACK to main menu")
    print("q - QUIT")
    print()
    return 3


def display_welcome():
    welcome = (
    """
                __________________________________________ ________              
                \______   \_   _____/\__    ___/\______   \\_____  \             
                 |       _/|    __)_   |    |    |       _/ /   |   \            
                 |    |   \|        \  |    |    |    |   \/    |    \           
                 |____|_  /_______  /  |____|    |____|_  /\_______  /           
                        \/        \/                    \/         \/            
             .__    .___                               __                        
       ___  _|__| __| _/____  ____             _______/  |_  ___________   ____  
       \  \/ /  |/ __ |/ __ \/  _ \   ______  /  ___/\   __\/  _ \_  __ \_/ __ \ 
        \   /|  / /_/ \  ___(  <_> ) /_____/  \___ \  |  | (  <_> )  | \/\  ___/ 
         \_/ |__\____ |\___  >____/          /____  > |__|  \____/|__|    \___  >
                     \/    \/                     \/                          \/
    *********************************************************************************
    *                            .------------------------.                         *
    *                            |\\\////////       90 min |                         *
    *                            | \/  __  ______  __     |                         *
    *                            |    /  \|\.....|/  \    |                         *
    *                            |    \__/|/_____|\__/    |                         *
    *                            | A                      |                         *
    *                            |    ________________    |                         *
    *                            |___/_._o________o_._\___|                         *
    *                                                                               *
    *********************************************************************************
    """)
    print(welcome)
