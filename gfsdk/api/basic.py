import requests


class Basic:
    def __init__(self):
        self.name = "basic"
        self.url = ""

    @staticmethod
    def createRequest(url, data):
        response = requests.post(url, json=data)
        return response

    # handles signing the request data using the private key
    def signMessageUsingPrivateKey(self, message, privateKey):
        pass
