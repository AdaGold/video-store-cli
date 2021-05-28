
import requests
from VideoStore import VideoStore
from print_functions import *


def main(play=True):
    video_store = VideoStore()

    welcome_banner()
    print_linebreaks()
    while play == True:
        print_linebreaks()
        print("PLEASE CHOOSE FROM THE FOLLOWING MENU:  ")
        main_menu_options()
        user_input = input("::  ")
        if user_input == "1":
        ###### VIDEO OPTIONS ######## 
            print("PLEASE CHOOSE FROM THE FOLLOWING MENU:  ")
            video_menu_options()
            video_user_input = input("::  ")
            if video_user_input == "1":
                all_videos = video_store.get_all_videos()
                for video in all_videos:
                    print_video_info(video)

            elif video_user_input == "2":
                video_store.add_video_to_db()


            elif video_user_input == "3":
                user_input = input("Please enter the ID of the video you would like to select:   ")
                selected_video = video_store.get_single_video(id=int(user_input))
                if selected_video:
                    print_video_info(selected_video)
            
            elif video_user_input == "4":
                user_input = input("Please enter the ID of the video you would like to select:   ")
                selected_video = video_store.get_single_video(id=int(user_input))
                if selected_video:
                    print_video_info(selected_video)
                    video_store.edit_single_video(selected_video)

            
            elif video_user_input == "5":
                running_loop = True
                while running_loop:
                    user_input = input("Please enter the ID of the video you would like to delete:   ")
                    selected_video = video_store.get_single_video(id=int(user_input))
                    print_video_info(selected_video)
                    user_check = input("Are you sure you want to delete this video?   Y/N:    ")
                    if user_check.upper() == "Y":
                        video_store.delete_single_video(selected_video)
                        running_loop = False

        elif user_input == "2":
        ####### CUSTOMER OPTIONS ######### 
            print("PLEASE CHOOSE FROM THE FOLLOWING MENU:  ")
            customer_menu_options()
            customer_user_input = input("::  ")
            if customer_user_input == "1":
                all_customers = video_store.get_all_customers()
                for customer in all_customers:
                    print_customer_info(customer)
            
            elif customer_user_input == "2": 
                video_store.add_customer_to_db()

            elif customer_user_input == "3":
                user_input = name_or_id()
                if user_input:
                    selected_customer = video_store.get_single_customer(name=user_input, id=None)
                else:
                    user_input = input("Please enter the ID of the customer you would like to select:   ")
                    selected_customer = video_store.get_single_customer(id=int(user_input), name=None)
        
                if selected_customer:
                    print_customer_info(selected_customer)
            
            elif customer_user_input == "4":
                # user_input = name_or_id()
                user_input = input("Please enter the ID of the customer you would like to select:   ")
                selected_customer = video_store.get_single_customer(id=int(user_input))
                
                if selected_customer:
                    print_customer_info(selected_customer)
                    video_store.edit_single_customer(selected_customer)


            elif customer_user_input == "5":
                running_loop = True
                while running_loop:
                    user_input = input("Please enter the ID of the customer you would like to delete:   ")
                    selected_customer = video_store.get_single_customer(id=int(user_input))
                    print_customer_info(selected_customer)
                    user_check = input("Are you sure you want to delete this cusotmer?   Y/N:   ")
                    if user_check.upper() == "Y":
                        video_store.delete_single_customer(selected_customer)
                        running_loop = False
        
        elif user_input == "3": 
        ########### RENTAL OPTIONS ########## 
            print("PLEASE CHOOSE FROM THE FOLLOWING MENU:  ")
            rental_menu_options()
            rental_user_input = input("::  ")
            if rental_user_input == "1":
                video_store.check_out_movie()

            elif rental_user_input == "2":
                video_store.check_in_movie()

            elif user_input == "3":
                video_id = input("Please enter the ID of the video:   ")
                video_store.get_rental_list_by_video(int(video_id))

            elif user_input == "4":
                customer_id = input("Please enter the ID of the customer:   ")
                video_store.get_rental_list_by_customer(int(customer_id))


        elif user_input == "4":
        ########### EXIT PROGRAM  ########## 
            play = False












if __name__ == "__main__":
    main()