from rental import Rental
from customer_options import *
from video_options import *
from menu_options import *

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api-kl.herokuapp.com/"

def main(play=True):
    #initialize rental
    rental = Rental(url=BACKUP_URL)
    
    #print record type
    main_menu_choice = get_main_menu_choice()

    while play==True:
        # get input and validate
        if main_menu_choice == "a":
            choice = get_customer_choice(rental)
            main_menu_choice = respond_customer_choice(choice, rental, main_menu_choice)
        elif main_menu_choice == "b":
            choice = get_video_choice(rental)
            main_menu_choice = respond_video_choice(choice, rental, main_menu_choice)
        elif main_menu_choice == "c":
            pass
        elif main_menu_choice == "d":
            pass
        elif main_menu_choice == "e":
            play=False
            print("\nThanks for using the Video Store CLI!")
        else:
            print("\nInvalid option.")
            main_menu_choice = input("Make your selection using valid option letters(A ~ E): ")


if __name__ == "__main__":
    main()