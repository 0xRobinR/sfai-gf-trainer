import requests


class GFSdk:
    def __init__(self, base_url):
        self.base_url = base_url

    # handles fetching data from the Greenfield
    def fetch(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response

    # handles uploading trained model to the Greenfield
    def upload(self, endpoint, file):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, files=file)
        return response
