def print_stars():
    print("\n************************************************\n")

def get_main_menu_choice():
    print_stars()
    print("Welcome to the Video Store CLI\n")
    print("\n*********** Main Menu ************\n")
    options = {
        "A": "Check customer records", 
        "B": "Check video records",
        "C": "Check out rental", 
        "D": "Chech in rental", 
        "E": "Quit"
        }
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print("\n**********************************\n")
    main_menu_choice = input("\nMake your selection using the option letter: ").lower()

    return main_menu_choice