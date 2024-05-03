import tensorflow
import datetime
import converter
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

bitsP2PKH = 160

# model 
file_name = "model.keras"

# example public key
public_key = "e954123abe469e5d293167aac708da1943e48481"

# load model
model = tensorflow.keras.models.load_model(file_name)

# some converting
public_key_as_hexHash = bytes.fromhex(public_key)
public_key_as_int = converter.intFromBytes(public_key_as_hexHash)

public_key_as_int_arr = []
public_key_as_int_arr.append(public_key_as_int)

bit_array = converter.convert_to_binary_arrays(public_key_as_int_arr, bitsP2PKH)

# predict
prediction = model.predict(bit_array)

# print readable key
possible_secret = converter.float_array_to_hex(prediction[0], 64)
print(str(possible_secret))