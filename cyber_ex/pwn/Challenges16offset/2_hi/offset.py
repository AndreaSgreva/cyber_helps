from pwn import *
elf = context.binary = ELF("./hi")
io = process(elf.path)
io.sendline(cyclic(100))
io.wait()
core = io.corefile
offset = cyclic_find(core.read(core.rsp, 8))
print("Offset:", offset)