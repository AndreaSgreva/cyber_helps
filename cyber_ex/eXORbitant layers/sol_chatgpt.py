from binascii import unhexlify

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

# Dati dell'esercizio
X1_hex = "b840946f97ffe078ce6581d145ff3bd86cdfd0add863fc718300"
X2X1_hex = "34f5785a7e42586044a7fc15bd7eed3b1f71045f7ecc177b22e0"
X2X3_hex = "f7a5269d0cf0804431df076ec7e00df66d4bc1593c99f6bfff86"
FLAG_X123_hex = "3c95c09bef751b579adff6e0eb6b69416fcb6391949f6bba01"

# Conversione in bytes
X1 = unhexlify(X1_hex)
X2X1 = unhexlify(X2X1_hex)
X2X3 = unhexlify(X2X3_hex)
FLAG_X123 = unhexlify(FLAG_X123_hex)

# --- Allineamento ---
max_len = max(len(X1), len(X2X1), len(X2X3), len(FLAG_X123))
def pad(b: bytes, n: int) -> bytes:
    return b.ljust(n, b"\x00")

X1 = pad(X1, max_len)
X2X1 = pad(X2X1, max_len)
X2X3 = pad(X2X3, max_len)
FLAG_X123 = pad(FLAG_X123, max_len)

# Ricostruzione step by step
X2 = xor_bytes(X2X1, X1)
X3 = xor_bytes(X2, X2X3)
X123 = xor_bytes(xor_bytes(X1, X2), X3)
FLAG = xor_bytes(FLAG_X123, X123)

print("X1 =", X1.hex())
print("X2 =", X2.hex())
print("X3 =", X3.hex())

try:
    print("FLAG =", FLAG.decode())
except UnicodeDecodeError:
    print("FLAG (raw bytes) =", FLAG)
    print("FLAG (hex) =", FLAG.hex())
