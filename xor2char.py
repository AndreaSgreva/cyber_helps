import itertools

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open("encrypted", "rb") as f:
    encrypted_data = f.read()

target = b"spritz"

for key_bytes in itertools.product(range(256), repeat=2):
    key = bytes(key_bytes)
    decrypted = xor_decrypt(encrypted_data, key)
    
    if target in decrypted:  # cerca in tutto il file
        print(f"Chiave trovata: {key}")
        print(f"Flag completa: {decrypted.decode(errors='ignore')}")
        break

    print(f"Chiave in corso: {key}")