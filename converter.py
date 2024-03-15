import numpy as np

def intFromBytes(byteS):
    return int.from_bytes(byteS, "big")
    
def binArray2float32array(bin_array):
    return np.array(bin_array).astype(np.float32)

def float_array_to_hex(array, fill):
    # convert float into 0 or 1 depending on >0.5    
    binary_string = ''.join(['1' if bit > 0.5 else '0' for bit in array])

    # fill array with leading zeros  
    hex_value = hex(int(binary_string, 2))[2:].zfill(fill)  
    
    return hex_value

def convert_to_binary(element, bits):
    # remove '0b', convert number to binary string and fill with leading zeros
    binary = bin(element)[2:].zfill(bits)
    # convert binaty string into list of integer
    binary_array = [int(bit) for bit in binary]
    return binary_array

def convert_to_binary_arrays(given_array, bits):
    # init empty array
    result = []
    for element in given_array:
        result.append(convert_to_binary(element, bits))
    return result
