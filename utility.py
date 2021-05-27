def print_stars():
    print("\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:.\n")

def print_logo():
    print(
"    ____       __                                         _    ___     __\n"
"   / __ \___  / /__________ _      ______ __   _____     | |  / (_)___/ /__  ____\n"
"  / /_/ / _ \/ __/ ___/ __ \ | /| / / __ `/ | / / _ \    | | / / / __  / _ \/ __ \ \n"
" / _, _/  __/ /_/ /  / /_/ / |/ |/ / /_/ /| |/ /  __/    | |/ / / /_/ /  __/ /_/ / \n"
"/_/ |_|\___/\__/_/   \____/|__/|__/\__,_/ |___/\___/     |___/_/\__,_/\___/\____/\n"
    )

def to_integer(input):
    '''
    converts data type of input to integer
    if not convertible, print error message
    '''
    if input.isnumeric():
        input = int(input)
    else:
        print("Could not select. Please enter id or title.")
