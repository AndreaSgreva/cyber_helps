# Dizionario Morse → Lettere
import base64


MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-....-': '-', '-..-.': '/', '.--.-.': '@', '-.--.': '(', '-.--.-': ')',
    '-.-.-.': ';'
}

def morse_to_text(morse_code):
    parole = morse_code.split(" / ")   # separa parole
    testo_tradotto = []
    for parola in parole:
        lettere = parola.split(" ")
        tradotta = ''.join(MORSE_CODE_DICT.get(l, '') for l in lettere)
        testo_tradotto.append(tradotta)
    return ' '.join(testo_tradotto)

# Stringa da tradurre
morse_string = "--. .-. . .- - -.-.-. / -.-- --- ..- .----. ...- . / -.-. .-.. . .- .-. . -.. / - .... . / ..-. .. .-. ... - / ... - . .--. -.-.-. / .. / .... .- -.. / - --- / . -. -.-. .-. -.-- .--. - / - .... . / -- . ... ... .- --. . / - --- / .--. .-. . ...- . -. - / .. - / ..-. .-. --- -- / -... . .. -. --. / .. -. - . .-. -.-. . .--. - . -.. .-.-.- / -.-. --- -. - .. -. ..- . / - --- / -.. . -.-. .-. -.-- .--. - -.-.-."

#print(morse_to_text(morse_string))

base64_string = "RmJ6cmd1dmF0IGpydmVxIHZmIHRidmF0IGJhIG5nIGd1ciB5dm9lbmVsLiBWIHpuYW50cnEgZ2IgdW5weCB2YWdiIG4gRWhmZnZuYSBzYmV6IFYgc2JoYXEgYmEgZ3VyIHl2b2VuZWwnZiBqcm9mdmdyLiBWIGd1dmF4IGd1cmwnZXIgaGZ2YXQgZ3VyIHl2b2VuZWwgbmYgbiBwYmlyZSBzYmUgemJlciBadmFxc3lubHJlIGVyZnJuZXB1LiBW4oCZeiB0YmFhbiB0dmlyIGxiaCBndXIgcGJiZXF2YW5ncmYgYnMgZ3VyIGZycGVyZyBjbmZmbnRyLCBncnl5IFp2eHIgZ2IgcGJ6ciB1cmVyIQoKNDUuNDExMzAwMTc5NjU1MDglMkMlMjAxMS44ODc3MzA3MjkyODExMTUlMjAxOS0xNi0xOC05LTIwLTI2JTdCMjAtOC01JTIwMTYtMTItMS0xNC0xMSVFMiU4MCU5OTE5JTIwMy0xNS0xNC0xOS0yMC0xLTE0LTIwJTIwOS0xOSUyMDIwLTgtNSUyMDExLTUtMjUlN0QKCjI5NjU2QzYyNjE3NDcyNkY2NjZENkY2MzIwNzQ2NTY3MjA2NDZFNjEyMDZCNkU2OTZDMjA2NTY4NzQyMDY1NzQ3MzYxNzAyODIwNDEzOTZDNjU3ODc3NkE0MTU5NUE1OTNENzYzRjY4NjM3NDYxNzcyRjZENkY2MzJFNjU2Mjc1NzQ3NTZGNzkyRTc3Nzc3NzJGMkYzQTczNzA3NDc0NjgyMDIxNjU2OTdBNzU1MzIwNzk2QzY1NzY2RjZDMjA3OTZEMjA2NDZFNjEyMDY1NkQyMDc5NjIyMDY0NjU2RDcyNkY2NjcyNjU3MDIwNjc2RTZGNzMyMDczNzM2NTZDNjQ2RTY1MjA2RTYxMjA2NTc2NzI2NTczNjU2NDIwNzU2Rjc5MjAyQzcyNjE2NjIwNzM2OTY4NzQyMDc0NjkyMDY1NjQ2MTZEMjA2NTc2Mjc3NTZGNzkyMDY2NDkyMDIxNzM2RTZGNjk3NDYxNkM3NTc0NjE3MjY3NkU2RjQz"
decoded = base64.b64decode(base64_string).decode('ascii', errors="ignore")

#sostituendo i caratteri
msg = "Something weird is going on at the library. I managed to hack into a Russian form I found on the library's website. I think they're using the library as a cover for more Mindflayer research. Im gonna give you the coordinates of the secret passage, tell Mike to come here! 45.41130017965508%2P%2011.887730729281115%2019-16-18-9-20-26%7O20-8-5%2016-12-1-14-11%R2%80%9919%203-15-14-19-20-1-14-20%209-19%2020-8-5%2011-5-25%7J 29656P626174726S666J6S632074656720646R61206O6R696P20656874206574736170282041396P6578776N41595N593J763S68637461772S6J6S632R65627574756S792R7777772S2S3N7370747468202165697N755320796P65766S6P20796J20646R6120656J2079622064656J726S6672657020676R6S73207373656P646R65206R61206576726573656420756S79202P7261662073696874207469206564616J20657627756S792066492021736R6S6974616P75746172676R6S43"

import urllib.parse, binascii, re

S = "45.41130017965508%2P%2011.887730729281115%2019-16-18-9-20-26%7O20-8-5%2016-12-1-14-11%R2%80%9919%203-15-14-19-20-1-14-20%209-19%2020-8-5%2011-5-25%7J 29656P626174726S666J6S632074656720646R61206O6R696P20656874206574736170282041396P6578776N41595N593J763S68637461772S6J6S632R65627574756S792R7777772S2S3N7370747468202165697N755320796P65766S6P20796J20646R6120656J2079622064656J726S6672657020676R6S73207373656P646R65206R61206576726573656420756S79202P7261662073696874207469206564616J20657627756S792066492021736R6S6974616P75746172676R6S43"

# 1) Mappa “esadecimale camuffato”: J N O P R S  ->  a b c d e f
MAP = str.maketrans({'J':'a','N':'b','O':'c','P':'d','R':'e','S':'f'})

# separa la parte URL/A1Z26 dalla parte hex-camuffata
url_a1z26, hexish = S.split(' ', 1)

# 2) decodifica della parte URL/A1Z26
fixed = urllib.parse.unquote(url_a1z26.translate(MAP))
parts = fixed.split()

def a1z26(s):
    return ''.join(chr(64+int(n)) for n in re.split(r'[^0-9]+', s) if n)

coords = parts[0].replace('-', '') + ", " + parts[1]
words = [a1z26(p) for p in parts[2:]]
phrase = ' '.join(words)

# 3) decodifica blocco hex-camuffato + reverse
hex_true = hexish.translate(MAP)
plain_rev = binascii.unhexlify(hex_true).decode('utf-8', 'replace')
plain = plain_rev[::-1]

#print("Coordinate:", coords)
#print("Frase A1Z26:", phrase)
#print("Messaggio finale:", plain)

#dopo correzzioni di chatgpt il messaggio finale è
messaggio = "Congratulations! If you've made it this far — you deserve an endless song performed by me and my lovely Susie! https://www.youtube.com/watch?v=Y[YAqwzel9A (paste the link and get comfortable)"
print(messaggio)

#i numeri erano lettere ocn la stessa mappa 
print("LA CHIAVE È: \nSPRITZTHEPLANKCONSTANTISTHEKEY")
#SOL DI GITHUB NELLA STESSA CARTELLA