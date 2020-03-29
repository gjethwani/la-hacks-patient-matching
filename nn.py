from numpy import loadtxt, genfromtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = genfromtxt('nn.csv', delimiter=',', filling_values=-1)

# split into input (X) and output (y) variables
X = dataset[:,2:19]
y = dataset[:,19]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=17, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, validation_split=0.2)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")