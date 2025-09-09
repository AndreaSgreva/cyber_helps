ciphertext = "yxyxxyy yxyxxxx yxyxxyx yxxyxxy yxyxyxx yxyyxyx yxxxxyy yxyxyxx yxxxyyx yyyyxy yyyyxyy yyxxyxy yyxyyyx yyxxxyy yyyxxyx yyyyxxy yyyxxxx yyyxyxx yyxyxxy yyxyyyy yyxyyyx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxy yyyyyxy"

#replace x with 0 and y with 1
binario = ciphertext.replace("x","0").replace("y","1")
print(binario)

#decoding from binary
def binary7_to_text(binary_string: str) -> str:
    # Divido la stringa in blocchi da 7 bit separati da spazi
    blocks = binary_string.strip().split()

    result = ""
    for block in blocks:
        # Converto ogni blocco da binario a intero
        value = int(block, 2)
        # Poi lo converto nel corrispondente carattere ASCII
        result += chr(value)
    return result


# Conversione
decoded_text = binary7_to_text(binario)

print("Testo decodificato:", decoded_text)
