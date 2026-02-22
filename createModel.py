from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

input_dim = 160
output_dim = 256
epochs = 2500
batch_size = 256


def createAndSaveModel(firstDenseDimension, hiddenDenseLayers, heightDenseLayer, file, x, y):
    sequential_array = []

    # Input layer – relu instead sigmoid (faster, no Vanishing-Gradient-Problem)
    sequential_array.append(layers.Dense(firstDenseDimension, activation='relu', input_shape=(input_dim,)))
    sequential_array.append(layers.BatchNormalization())

    # Hidden layers with BatchNorm and Dropout
    for i in range(hiddenDenseLayers):
        sequential_array.append(layers.Dense(heightDenseLayer, activation='relu'))
        sequential_array.append(layers.BatchNormalization())
        sequential_array.append(layers.Dropout(0.2))

    # Output layer – sigmoid, output binary (0/1 per Bit)
    sequential_array.append(layers.Dense(output_dim, activation='sigmoid'))

    model = Sequential(sequential_array)

    model.compile(
        optimizer='adamax',
        loss='binary_crossentropy',
        metrics=['accuracy', 'mae']
    )

    model.summary()

    callbacks = [
        # Stopp Training if 50 Epochs do not deliver better resulta
        EarlyStopping(patience=50, restore_best_weights=True, verbose=1),
        # Save the model
        ModelCheckpoint(file, save_best_only=True, verbose=1)
    ]

    model.fit(
        x, y,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.1,  # 10% of Data for validation
        callbacks=callbacks
    )