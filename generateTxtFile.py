import tensorflow
import datetime
import converter

bitsSecret = 256
bitsP2PKH = 160

def createTextFileFromModelPrediction(file_name, x_array):
model = tensorflow.keras.models.load_model(file_name)

textFileName = f"prediction_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

print(f"Running predictions for {len(x_array)} inputs...")
prediction = model.predict(x_array, verbose=1)

with open(textFileName, 'w') as f:
    for i, pred in enumerate(prediction):
        # 64 Hex-chars = 256 Bits
        possible_secret = converter.float_array_to_hex(pred, 64)
        f.write(f"{possible_secret}\n")

print(f"Predictions written to {textFileName}")
return textFileName