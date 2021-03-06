from keras.datasets import mnist
(train_img, train_label), (test_img, test_label) = mnist.load_data()

from keras import models
from keras import layers

nwk = models.Sequential()
# nwk.add(layers.Dense(16, activation="relu", input_shape=(28 * 28,)))
# nwk.add(layers.Dense(16, activation="relu"))
# nwk.add(layers.Dense(16, activation="relu"))
nwk.add(layers.Dense(256, activation="relu", input_shape=(28 * 28,)))
nwk.add(layers.Dense(64, activation="relu", input_shape=(28 * 28,)))
nwk.add(layers.Dense(10, activation="softmax"))

nwk.compile(optimizer="rmsprop",
            loss="categorical_crossentropy", metrics=["accuracy"])

train_img = train_img.reshape((60000, 28 * 28))
train_img = train_img.astype("float32") / 255

test_img = test_img.reshape((10000, 28 * 28))
test_img = test_img.astype("float32") / 255

from keras.utils import to_categorical

train_label = to_categorical(train_label)
test_label = to_categorical(test_label)

nwk.fit(train_img, train_label, epochs=5, batch_size=128)
