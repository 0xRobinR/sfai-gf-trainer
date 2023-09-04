import requests


class Object:
    def __init__(self):
        self.name = "object"
        self.bucket = None
        self.data = None
        self.metadata = None

    @staticmethod
    def fetch_object_from_gf(object_id):
        requests.post(f"/object/{object_id}")
        return Object()
