
from video_store import VideoStore 
from menus import *
from commands import check_out_rental, check_in_rental


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


#video_store=VideoStore(url=BACKUP_URL)


def main(play=True):
    video_store=VideoStore(url=BACKUP_URL)

    print("WELCOME TO RETRO VIDEO STORE")
    
    while play==True:
        options=main_menu()
        choice = make_main_choice(options)
        if choice =='1':
            options=customer_menu()
            choice=make_customer_choice(options)

        elif choice=='2':
            options=video_menu()
            choice=make_video_choice(options) #put in video_menu?

        elif choice=='3':
            check_out_rental()
            

        elif choice=='4':
            check_in_rental()


        elif choice=='5':
            play==False
            print("\n See you later!")

        print_stars()




if __name__ == "__main__":
    main()