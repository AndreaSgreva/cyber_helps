def xor_hex_strings(hex1, hex2):
    # Convertiamo le stringhe hex in byte
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)

    # XOR byte per byte
    xor_result = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

    # Convertiamo il risultato in hex e ritorniamo
    return xor_result.hex()


X1 =    "b840946f97ffe078ce6581d145ff3bd86cdfd0add863fc718300"
X2_X1 = "34f5785a7e42586044a7fc15bd7eed3b1f71045f7ecc177b22e0"
X2_X3 = "f7a5269d0cf0804431df076ec7e00df66d4bc1593c99f6bfff86"
FLAG_X1_X2_X3 = "3c95c09bef751b579adff6e0eb6b69416fcb6391949f6bba01"

#x2 = xor_hex_strings(X1, X2_X1)
#x3 = xor_hex_strings(x2, X2_X3) 

FLAG_X1 = xor_hex_strings(FLAG_X1_X2_X3, X2_X3)

result = xor_hex_strings(FLAG_X1, X1)
print(result)


def hex_to_ascii(hex_str):
    # Convertiamo la stringa hex in bytes
    bytes_data = bytes.fromhex(hex_str)
    # Convertiamo i bytes in stringa ASCII
    ascii_str = bytes_data.decode('ascii')
    return ascii_str


ascii_result = hex_to_ascii(result)
print(ascii_result)  
