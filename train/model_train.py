import tensorflow as tf
from tensorflow import keras


class ModelTrain:
    def __init__(self, config):
        self.config = config
        self.model = None

    def train(self, data_dir):
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=5)

        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
        print("\nTest accuracy:", test_acc)
