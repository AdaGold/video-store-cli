import requests

class Rental:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", selected_rental = None):
        self.url = url
        self.selected_rental = selected_rental