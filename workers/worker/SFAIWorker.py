import numpy as np
import tensorflow as tf


class TrainModel(tf.keras.Model):
    def __init__(self):
        super(TrainModel, self).__init__()
        self.dense = tf.keras.layers.Dense(1)

    def call(self, x):
        return self.dense(x)


class SFAIWorker:
    def __init__(self):
        self.model = TrainModel()

    def train(self, data):
        print("training the model")
        cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()
        print(cluster_resolver.task_type)
        strategy = tf.distribute.experimental.ParameterServerStrategy(cluster_resolver)

        with strategy.scope():
            self.model.compile(optimizer='adam', loss='mean_squared_error')

        X_train = np.linspace(0, 10, 1000)
        y_train = 3 * X_train + np.random.randn(1000)
        self.model.fit(X_train, y_train, epochs=10)

    def predict(self, data):
        return self.model.predict(data)
