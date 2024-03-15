import random
import converter
from bit.crypto import ECPrivateKey, ripemd160_sha256, sha256

# private key has 256 bits and public has 160 bits
bitsSecret = 256
bitsP2PKH = 160

def createTrainingData(length, seed):

    #init empty arrays
    secrets_array = []
    xUncompressed_array = []
    xCompressed_array = []
    xSegwit_array = []
    
    # set seed for random values
    random.seed(seed)

    # loop to create training data
    for i in range(length):
        # generate random private key
        secret_key = random.getrandbits(bitsSecret)
        secrets_array.append(secret_key)
        myPrivate = ECPrivateKey.from_int(secret_key)     
        
        # generate un- and compressed public key
        publicKeyUncompressed = myPrivate.public_key.format(compressed=False)
        publicKeyCompressed = myPrivate.public_key.format(compressed=True)
        
        # do some ripemd and sha256 magic
        myHashUncompressed = ripemd160_sha256(publicKeyUncompressed)
        myHashCompressed = ripemd160_sha256(publicKeyCompressed)
        myHashSegwitAddress = ripemd160_sha256(b'\x00\x14' + ripemd160_sha256(publicKeyCompressed))
        
        # convert values
        myHashUncompressedAsInt = converter.intFromBytes(myHashUncompressed)
        myHashCompressedAsInt = converter.intFromBytes(myHashCompressed)
        myHashSegwitAddressAsInt = converter.intFromBytes(myHashSegwitAddress)
        
        # append to array
        xUncompressed_array.append(myHashUncompressedAsInt)
        xCompressed_array.append(myHashCompressedAsInt)
        xSegwit_array.append(myHashSegwitAddressAsInt)
     
    secrets_bin_array = converter.convert_to_binary_arrays(secrets_array, bitsSecret)
    xUncompressed_bin_array = converter.convert_to_binary_arrays(xUncompressed_array, bitsP2PKH)
    xCompressed_bin_array = converter.convert_to_binary_arrays(xCompressed_array, bitsP2PKH)
    xSegwit_bin_array = converter.convert_to_binary_arrays(xSegwit_array, bitsP2PKH)
     
    # convert binary array into float32 np array
    secrets_f32_array = converter.binArray2float32array(secrets_bin_array)
    xUncompressed_f32_array = converter.binArray2float32array(xUncompressed_bin_array)
    xCompressed_f32_array = converter.binArray2float32array(xCompressed_bin_array)
    xSegwit_f32_array = converter.binArray2float32array(xSegwit_bin_array)

    return secrets_f32_array, xUncompressed_f32_array, xCompressed_f32_array, xSegwit_f32_array
