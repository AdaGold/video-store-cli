import requests
import datetime

class Rental:
    def __init__(self, URL="https://retro-video-store-api.herokuapp.com", rental=None):
        self.url = URL
        self.rental = rental
