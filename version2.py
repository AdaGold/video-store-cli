# THIS IS A VERSION I PIVOTED TOO FOR AN UPDATE ON PROCESS, I WOULD LIKE TO NOTE THAT I ALSO HAD
#AN UPDATED VIDEO AND CUSTOMER.PY UTILIZING AN ATTRIBUTE SELF.SELECTED TASK, WHICH WAS HELPFUL


# import requests
# from customer import Customer
# from video import Video


# URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def list_options(): 
#     options = {
#         "C": "Customer Services", 
#         "V": "Video Stock Services",
#         "R": "Rental Services", 
#         "Q": "Quit"
#         }
    
#     #print_stars()
#     print("Welcome to the VideoStore CLI")
#     print("These are the actions you can perform")
#     #print_stars()
    
#     for choice_num in options:
#         print(f"Option {choice_num}. {options[choice_num]}")

#     return options

# def make_choice(options):  #what is task_list referring to
#     valid_choices = options.keys()
#     choice = None

#     # while choice not in valid_choices:
#     choice = input("Make your selection using the option number: ")

#     if choice == "1":
#         return choice
#     if choice == "2":
#         return choice
#     if choice == "3":
#         return choice
#     # return choice

# def customer_info_generator():
#     customer_name = input("Please enter customer name:  ")
#     postal_code = input("Please enter customer postal code:  ")
#     phone_number = input("Please enter customer phone number:  ")
#     return customer_name, postal_code, phone_number


# def run_cli(play=True):

#     customer = Customer(url="https://retro-video-store-api.herokuapp.com")
#     video = Video(url="https://retro-video-store-api.herokuapp.com")

#     options = list_options()


#     while play==True:
#         choice = make_choice(options)

#         if choice == "C":
#             c_task_prompt1 = input(" 1 for Customer Creation, 2 for Customer Update")

#         if c_task_prompt1 == "1":
#             customer_name = input("Please enter customer name:  ")
#             postal_code = input("Please enter customer postal code:  ")
#             phone_number = input("Please enter customer phone number:  ") 
#             respone = customer.create_customer(customer_name=customer_name, postal_code=postal_code, phone_number=phone_number)
#             print(f"Customer profile '{customer_name}' has been created.")

#         elif c_task_prompt1 == "2":
#             customer_id = input("Please enter valid customer ID:  ")
#             if customer_id.isnumeric():
#                 customer_id = int(customer_id)
#                 info = customer.get_customer(customer_id=customer_id)
#                 print(info)
#         c_task_prompt2 = input("type DELETE to delete customer, UPDATE to update customer, Q to return to Main Menu:   ")

#         if c_task_prompt2 == "DELETE":
#             delete = input("Are you sure you want to delete, action cannot be undone. Enter Y or N:  ")
#             if delete == "Y":
#                 response = customer.delete_customer()
#                 print(f"Customer id '{customer_id}' has been deleted")
#             else:
#                 pass

#         if c_task_prompt2== "UPDATE":
#             customer_name = input("Please enter customer name:  ")
#             postal_code = input("Please enter customer postal code:  ")
#             phone_number = input("Please enter customer phone number:  ")
#             response = customer.update_customer_info(customer_name=customer_name, postal_code=postal_code, phone_number=phone_number)
#             print(f"Customer profile '{customer_name}' has been updated. ")
            
#         if c_task_prompt2 == "Q":
#             run_cli()

#         if choice == "V":
#             v_task_prompt1 = input(" Enter 1 for Video Creation or 2 for Video Update: ")
#             if v_task_prompt1 == "1":
#                 video_id = input("Please enter Video ID:  ")
#                 title = input("Please enter title: ")
#                 release_date = input('Enter a date in YYYY-MM-DD format:  ')
#                 total_inventory = input("Please enter total inventory: ")
#                 print(f"Video profile '{title}' has been updated.")   
#                 response = video.update_video(video_id=video_id, title=title, release_date=release_date, total_inventory=int(total_inventory))
            
#             if v_task_prompt1 == "2":
#                 video_id = input("Please enter valid Video ID:  ")
#                 if video_id.isnumeric():
#                     video_id = int(video_id)
#                     info = customer.get_customer(video_id=video_id)
#                     print(info)

#             v_task_prompt2 = input("Enter DELETE to delete video, UPDATE to update video, Q to return to Main Menu:   ")
#             if v_task_prompt2 == "DELETE":
#                 delete = input("Are you sure you want to delete, action cannot be undone. Enter Y or N:  ")
#             if delete == "Y":
#                 response = video.delete_video()
#                 print(f"Customer id '{video_id}' has been deleted")
#             else:
#                 pass

#             if task_prompt2 == "UPDATE":
#                 video_id = input("Please enter Video ID:  ")
#                 title = input("Please enter title: ")
#                 release_date = input('Enter a date in YYYY-MM-DD format:  ')
#                 total_inventory = input("Please enter total inventory: ")
#                 print(f"Video profile '{title}' has been updated.")   
#                 response = video.update_video(video_id=video_id, title=title, release_date=release_date, total_inventory=int(total_inventory))

#         if choice == "R":
#             pass   
        
#         selected_customer_task = input("")
    

# # def main():
# #     print("WELCOME TO RETRO VIDEO STORE")
# #     #look up snowman project
# #     list_options()
# #     customer = Customer() 
# #     print(customer.all_customers())
    

# if __name__ == "__main__":
#     run_cli()
#     #main()