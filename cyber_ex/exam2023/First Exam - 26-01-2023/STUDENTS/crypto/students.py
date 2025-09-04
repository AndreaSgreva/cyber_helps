import base64
import string
import binascii

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)

with open('encrypted_flag.txt', 'r') as f:
    encrypted_message=f.read()

def ROTdecode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - pos)%LEN]
    return rot13_enc

rotated_back = ROTdecode(encrypted_message, 13)

print(rotated_back)

decoded = base64.b64decode(rotated_back).decode('ascii', errors="ignore")

print("Stringa decodificata:", decoded)