import random
import converter
from multiprocessing import Pool, cpu_count
from bit.crypto import ECPrivateKey, ripemd160_sha256

# private key has 256 bits and public has 160 bits
bitsSecret = 256
bitsP2PKH = 160


def _generateSingleKey(secret_key):
    # Generate all Hashes one Private Key. 
    # as Top-Level-Function for Multiprocessing needed.
    myPrivate = ECPrivateKey.from_int(secret_key)

    publicKeyUncompressed = myPrivate.public_key.format(compressed=False)
    publicKeyCompressed = myPrivate.public_key.format(compressed=True)

    hashUncompressed = converter.intFromBytes(ripemd160_sha256(publicKeyUncompressed))
    hashCompressed = converter.intFromBytes(ripemd160_sha256(publicKeyCompressed))
    hashSegwit = converter.intFromBytes(
        ripemd160_sha256(b'\x00\x14' + ripemd160_sha256(publicKeyCompressed))
    )

    return secret_key, hashUncompressed, hashCompressed, hashSegwit


def createTrainingData(length, seed):
    random.seed(seed)
    secrets = [random.getrandbits(bitsSecret) for _ in range(length)]

    print(f"Generating keys using {cpu_count()} CPU cores...")

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(_generateSingleKey, secrets)

    # split resulta 
    secrets_array, xUncompressed_array, xCompressed_array, xSegwit_array = zip(*results)

    # binary
    secrets_bin = converter.convert_to_binary_arrays(secrets_array, bitsSecret)
    xUncompressed_bin = converter.convert_to_binary_arrays(xUncompressed_array, bitsP2PKH)
    xCompressed_bin = converter.convert_to_binary_arrays(xCompressed_array, bitsP2PKH)
    xSegwit_bin = converter.convert_to_binary_arrays(xSegwit_array, bitsP2PKH)

    # Float32 konvert
    secrets_f32 = converter.binArray2float32array(secrets_bin)
    xUncompressed_f32 = converter.binArray2float32array(xUncompressed_bin)
    xCompressed_f32 = converter.binArray2float32array(xCompressed_bin)
    xSegwit_f32 = converter.binArray2float32array(xSegwit_bin)

    return secrets_f32, xUncompressed_f32, xCompressed_f32, xSegwit_f32