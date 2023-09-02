from pwn import *

io = remote('challs.n00bzunit3d.xyz', 13541)

# How many 2's appear till 672?
def get_values():
    io.recvuntil('How many ')
    key = (io.recvuntil("'s", drop=True)).decode()
    io.recvuntil('till ')
    total = io.recvuntil("?", drop=True).decode()
    return(key, total)


def solve(key, total):
    all_num = ''
    for i in range(1, int(total)):
        all_num += str(i)

    all_num = list(all_num)

    cpt = 0
    for i in all_num:
        if str(i) == str(key):
            cpt+=1
    return cpt

while True:
    key, total = get_values()
    s = solve(key, total)
    io.sendline(str(s))
    io.recvline()
    io.recvline()
    res = io.recvline().decode()
    print(res)
    if 'n00bz' in res:
        exit(0)





