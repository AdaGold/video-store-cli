import requests


class RentalList:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental