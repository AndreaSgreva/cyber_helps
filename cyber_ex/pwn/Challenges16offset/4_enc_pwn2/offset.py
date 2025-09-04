from pwn import *
elf = context.binary = ELF("./pwn2")
io = process(elf.path)
io.sendline(cyclic(100))
io.wait()
core = io.corefile
offset = cyclic_find(core.eip)
print("Offset:", offset)