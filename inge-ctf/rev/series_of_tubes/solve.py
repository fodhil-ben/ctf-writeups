"""
the program take an input from the user and do some operation on it

you can see that by decompiling the binary in ghidra

after some operation we find that it compares the result with a specific value which is
"""

enc_flag = [0x2d, 0x29, 0x31, 0x34, 0x2c, 0x32, 0x27, 0x30, 0x2b, 0x24, 0x4c, 0x39, 0x6f, 0x44, 0x73, 0x37, 0x32, 0x74, 0x36, 0x3b, 0x77, 0x57, 0x4d, 0x8c, 0x71, 0x50, 0x79, 0x3f, 0x3d, 0x50, 0x69, 0x38]

a1 = [0x2d]
a2 = []
a3 = []
a4 = []
for i in range(1, 0x20):
    a1.append((enc_flag[i])-i)



for i in range(0x20):
    a2.append((a1[i])+(0x69))



for i in range(0x20):
    a3.append(chr(255 -a2[i]))


print(''.join(a3))

# ingeniums{Th3_1nt3rn3T_7rucK}