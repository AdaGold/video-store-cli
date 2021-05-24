import requests 
def main():
    url = "https://calm-ridge-59728.herokuapp.com"
    response = requests.get(url)
    name = response.json()['name']
    greeting = response.json()['message']
    
    print("********************")
    print(f"Welcome to {name}")
    print(greeting)
    print("********************")

main()