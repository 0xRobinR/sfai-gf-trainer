class Professor:
    def __init__(self, address):
        self.address = address

    # handles training the model
    def train_fetch_data(self, data):
        print(self.address)
        train_model = ModelTrain.train(data)
        return train_model
