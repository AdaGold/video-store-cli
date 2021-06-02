import requests
import datetime

class Customer:
    def __init__(self, URL="https://retro-video-store-api.herokuapp.com", customer=None):
        self.url = URL
        self.customer = customer
