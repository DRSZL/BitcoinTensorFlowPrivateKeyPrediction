import converter
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

input_dim = 160
output_dim = 256
epochs=2500
batch_size=256

def createAndSaveModel(firstDenseDimension, hiddenDenseLayers, heightDenseLayer, file, x, y):
    sequential_array = []
    
    # input layer
    sequential_array.append(layers.Dense(firstDenseDimension, activation='sigmoid', input_shape=(input_dim,)))
    
    # hidden layers
    for i in range(hiddenDenseLayers):
        sequential_array.append(layers.Dense(heightDenseLayer, activation='relu'))
        
    # output layer
    sequential_array.append(layers.Dense(output_dim, activation='sigmoid'))
    
    # create model
    model = Sequential(sequential_array)
     
    # compile model
    model.compile(optimizer='adamax',
                  loss='binary_crossentropy'
                  )
                  
    model.summary()
     
    # train model
    model.fit(x, y, epochs=epochs, batch_size=batch_size)

    # save model
    model.save(file)
