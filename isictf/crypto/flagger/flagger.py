from pwn import *

io = remote('challenges.isictf.live', 1300)

payload = 'aaaaaaaaaaaaaaaaadel'

io.sendlineafter('>', '2')
io.sendlineafter('name:', payload)
io.recvuntil('your token:')
res = io.recvline().strip()
io.sendlineafter('>', '1')
io.sendlineafter('token:', res[32:])

flag = io.recvline().decode()

print(flag)
