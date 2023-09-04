import tensorflow as tf

from train.model_train import ModelTrain


class Professor:
    def __init__(self, address):
        self.address = address
        self.model = None

    # handles training the model
    def train_fetch_data(self, data):
        print(self.address)
        cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()
        strategy = tf.distribute.experimental.ParameterServerStrategy(cluster_resolver)

        with strategy.scope():
            model = ModelTrain()
            model.compile(optimizer='adam', loss='mean_squared_error')

    # for listening data from bnb smart chain
    def listen_for_events(self, timeout=0):
        print("listening for events")
        pass
