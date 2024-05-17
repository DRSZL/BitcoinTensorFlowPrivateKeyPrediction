import tensorflow
import datetime
import converter
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

bitsSecret = 256
bitsP2PKH = 160

def createTextFileFromModelPrediction(file_name, x_array):
    model = tensorflow.keras.models.load_model(file_name)
    
    textFileName = f"{'prediction_'}{datetime.datetime.now().timestamp()}.txt"

    prediction = model.predict(x_array)

    with open(textFileName, 'w') as f:      
                       
            # generate txt file with predicted keys from public key
            for i in range(len(prediction)):
                # 64 entries long, 256 Bits = 64 Hex-digits
                possible_secret = converter.float_array_to_hex(prediction[i], 64)
                f.write(f"{possible_secret}\n")
