class Bucket:
    def __init__(self, storageProvider, visibility, privateKey):
        self.name = "bucket"
        self.storageProvider = storageProvider
        self.visibility = visibility
        self.privateKey = privateKey

    # get create bucket approval from greenfield
    def getApproval(self):
        pass
