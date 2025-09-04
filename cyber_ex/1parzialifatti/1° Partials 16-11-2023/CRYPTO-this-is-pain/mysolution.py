# -*- coding: utf-8 -*-
import re
import base64

# STEP 1: leggi il file e sostituisci Z->0, O->1
with open("ciphertext.txt", "r", encoding="utf-8") as f:
    raw = f.read()

binario = raw.replace("Z", "0").replace("O", "1")

# STEP 2: converti il testo binario in testo ASCII
def binario_to_ascii(binario_input):
    # Dividiamo la stringa nei blocchi di 7 bit usando lo spazio
    blocchi = binario_input.split()
    
    # Convertiamo ogni blocco binario in un carattere ASCII
    risultato = ''
    for blocco in blocchi:
        # Convertiamo da binario a decimale
        decimale = int(blocco, 2)
        # Convertiamo da decimale a carattere ASCII
        risultato += chr(decimale)
    
    return risultato

# Esempio di utilizzo
testo_binario = binario
ascii_tradotto = binario_to_ascii(testo_binario)
print("Testo ASCII:", ascii_tradotto)

# STEP 3: decodifica base64
base64_decoded = base64.b64decode(ascii_tradotto).decode("utf-8")
print("Testo decodificato:", base64_decoded)

# STEP 4: sostituisci le lettere per ottenere la flag
messaggio = base64_decoded.replace("è", "}").replace("é", "{")

print("", messaggio)

messaggio = messaggio.replace("R", "i").replace("W", "m").replace("Y", "e").replace("B", "s")
messaggio = messaggio.replace("N", "p").replace("O", "r").replace("T", "t").replace("U", "z")
messaggio = messaggio.replace("A", "o").replace("Q", "h").replace("K", "a").replace("J", "l")
messaggio = messaggio.replace("L", "x").replace("G", "n").replace("S", "k").replace("V", "d")
messaggio = messaggio.replace("E", "w").replace("Z", "y").replace("F", "u").replace("C", "c").replace("P", "v")


print(messaggio)