# Dizionario Morse -> Lettere
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-....-': '-', '-..-.': '/', '.--.-.': '@', '-.--.': '(', '-.--.-': ')',
    '-...-': '=', '.-.-.': '+', '-.-.-.': ';', '---...': ':',
    '..--.-': '_', '...-..-': '$', '.-..-.': '"', '.----.': "'"
}

def morse_to_text(morse_code: str) -> str:
    # Divide le parole
    words = morse_code.split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


# Stringa Morse che mi hai passato
morse_string = "--. .-. . .- - -.-.-. / -.-- --- ..- .----. ...- . / -.-. .-.. . .- .-. . -.. / - .... . / ..-. .. .-. ... - / ... - . .--. -.-.-. / .. / .... .- -.. / - --- / . -. -.-. .-. -.-- .--. - / - .... . / -- . ... ... .- --. . / - --- / .--. .-. . ...- . -. - / .. - / ..-. .-. --- -- / -... . .. -. --. / .. -. - . .-. -.-. . .--. - . -.. .-.-.- / -.-. --- -. - .. -. ..- . / - --- / -.. . -.-. .-. -.-- .--. - -.-.-."

#print(morse_to_text(morse_string))


# HASH usato sito E ANCHE PER INDOVINARE LETTERE


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    plaintext = []
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) - ord('a') for i in key]
    ciphertext = ciphertext.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Calcolo shift
            shift = key_as_int[key_index % key_length]
            # Decriptazione (mod 26)
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Mantiene spazi, punteggiatura ecc.
            plaintext.append(char)

    return ''.join(plaintext)


# Esempio d'uso:
cipher = "nxxmgd{Uynbe_Fhr_Jyuqk_Tbs}"  # classico esempio ("attack at dawn" cifrato con "lemon")
key = "vigenere"


print(vigenere_decrypt(cipher, key))

# flag: spritz{Dusty_Bun_Suzie_Poo}