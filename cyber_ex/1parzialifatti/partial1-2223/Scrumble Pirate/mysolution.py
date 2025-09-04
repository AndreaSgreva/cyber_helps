with open("challenge.txt", "r") as file:
    cipher = ''.join(file.readlines())


message = cipher.replace("D", "s").replace("M", "p").replace("P", "r").replace("X", "i").replace("S", "t").replace("T", "z")
message = message.replace("E", "o").replace("N", "y").replace("R", "u").replace("K", "m").replace("H", "a").replace("L", "e")
message = message.replace("O", "n").replace("U", "l").replace("G", "j").replace("A", "h").replace("Z", "c").replace("F", "b").replace("V", "f").replace("W", "g").replace("Y", "d").replace("C", "w").replace("Q", "k")

print(message)