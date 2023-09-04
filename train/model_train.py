import tensorflow as tf


class ModelTrain(tf.keras.Model):
    def __init__(self):
        super(ModelTrain, self).__init__()
        self.dense = tf.keras.layers.Dense(1)

    def call(self, x):
        return self.dense(x)
