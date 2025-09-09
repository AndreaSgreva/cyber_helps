import random
import datetime

#decrypt the following
ciphertext = "ZSUASRZDTF?~jesj_flkojqkjfy5?;5u0y"

def XOR(text, seed):
    #set the seed to allow reproducibility
    random.seed(seed)
    return ''.join([chr(ord(x)^random.randint(0,10)) for x in text])

def h(x, y = 123):
    z = x
    while z >= y:
        z = z - y
    return z

def encrypt(text):
    year = datetime.date.today().year
    cipher = XOR(text, h(year))
    return cipher

def decrypt(text, seed):
    if seed <=10000:
        raise Exception(f"Not so easy! The value {seed} cannot be accepted")

    plaintext = XOR(text, h(seed))
    return plaintext


print(XOR(ciphertext, h(2021)))
print(h(10016))
print(decrypt(ciphertext, 14321))

#ho aggiunto a 2021 una cifra in modo tale da avere lo stesso risultato sottraendo 123
# quindi ho fatto 2021+12300