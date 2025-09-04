#!/usr/bin/env python3

import base64
import string
import binascii

# Stesso alfabeto usato nello script originale
ALPHABET = list(string.printable)
LEN = len(ALPHABET)

# Funzioni inverse di ROTencode
def ROTdecode(message, pos):
    decoded = ''
    for c in message:
        i = ALPHABET.index(c)
        decoded += ALPHABET[(i - pos) % LEN]
    return decoded

# Funzioni di decodifica Base64 e Base32
def base64decode(message):
    return base64.b64decode(message.encode('ascii')).decode('ascii')

def base32decode(message):
    return base64.b32decode(message.encode('ascii')).decode('ascii')

# XOR è simmetrico, basta riapplicare la stessa chiave
def XORdecode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)]
    xored = ''.join([chr(a ^ ord(b)) for a,b in zip(message, key)])
    return xored

# Inserisci qui il testo decifrato (hex string)
hex_encrypted = open("encrypted_flag.txt", "r").read().strip()

# Passaggi inversi
# 1. Hex → bytes
xor_encrypted = binascii.unhexlify(hex_encrypted)

# 2. XOR decode
encrypted = XORdecode(xor_encrypted)

# 3. Inverti il ciclo di ROT/B32/Base64 15 volte
for _ in range(15):
    encrypted = ROTdecode(encrypted, 3)      # inverti ROT3
    encrypted = base32decode(encrypted)      # decodifica base32
    encrypted = ROTdecode(encrypted, 13)     # inverti ROT13
    encrypted = base64decode(encrypted)      # decodifica base64

# 4. Rimuovi il prefisso
prefix = "Encode as if there's no tomorrow: "
if encrypted.startswith(prefix):
    FLAG = encrypted[len(prefix):]
else:
    FLAG = encrypted  # sicurezza nel caso qualcosa sia cambiato

print("FLAG:", FLAG)
