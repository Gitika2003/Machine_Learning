#Load MNIST Handwritten Digit Dataset
#Gitika Chouksey 0827CI201068
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()


#Pre-processing Dataset
#Gitika Chouksey 0827CI201068
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape the input data to have a depth of 1
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


#Define CNN Architecture
#Gitika Chouksey 0827CI201068
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the CNN architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])


Train CNN using Backpropagation algorithm
# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, tf.keras.utils.to_categorical(y_train), epochs=5, batch_size=32)

#Testing Performance
#Gitika Chouksey 0827CI201068
# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, tf.keras.utils.to_categorical(y_test))
print('Test accuracy:', test_acc)


