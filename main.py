from cvr import CVR
from customer import get_main_menu_choice, get_customer_choice, print_stars, respond_customer_choice
from video import get_video_choice, respond_video_choice
from rental import get_rental_choice, respond_rental_choice

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main(play=True):
    #initialize cvr
    cvr = CVR(url=BACKUP_URL)
    
    #print and select main menu options
    main_menu_choice = get_main_menu_choice()

    while play==True:
        # print response to selected main menu option
        if main_menu_choice == "a":
            choice = get_customer_choice()
            main_menu_choice = respond_customer_choice(choice, cvr, main_menu_choice)
        elif main_menu_choice == "b":
            choice = get_video_choice()
            main_menu_choice = respond_video_choice(choice, cvr, main_menu_choice)
        elif main_menu_choice == "c":
            choice = get_rental_choice()
            main_menu_choice = respond_rental_choice(choice, cvr, main_menu_choice)
        elif main_menu_choice == "d":
            play=False
            print_stars()
            print("Thanks for using the Video Store CLI!")
            print_stars()
        else:
            print("\nInvalid option.\n")
            main_menu_choice = input("Make your selection using valid option letters(A ~ E): ")


if __name__ == "__main__":
    main()