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

    with open(textFileName, 'w') as f:

        for i in range(len(x_array)):
            p2pkh_hex = converter.float_array_to_hex(x_array[i], 40)
                      
            p2pkh_binary = converter.convert_to_binary(int(p2pkh_hex, 16), bitsP2PKH)
            prediction = model.predict([p2pkh_binary])
            
            # 64 entries long, 256 Bits = 64 Hex-digits
            possible_secret = converter.float_array_to_hex(prediction[0], 64)
            
            # generate txt file with predicted keys from public key
            f.write(str(possible_secret))
            f.write('\n')
