#!/usr/bin/env python3

import string
import itertools    # if you want, it is not necessary

XOR_KEY='??' # can be only letters

# read the file with the encrypted message
with open('encrypted', 'rb') as f:
    encrypted_message=f.read()


def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

target = b"spritz"


for key_bytes in itertools.product(range(256), repeat=2):
    key = bytes(key_bytes)
    decrypted = xor_decrypt(encrypted_message, key)
    
    if target in decrypted:  # cerca in tutto il file
        print(f"Chiave trovata: {key}")
        print(f"Flag completa: {decrypted.decode(errors='ignore')}")
        break

    print(f"Chiave in corso: {key}")