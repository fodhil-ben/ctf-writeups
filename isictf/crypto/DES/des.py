from Crypto.Cipher import DES

# flag = b"ISICTF{fake_flag}"
# flag = flag.ljust( len(flag) + (8 - (len(flag) % 8)), b'\x00')
# iv = b"13371337"
# des = DES.new(key, DES.MODE_OFB, iv)
# ct = des.encrypt(flag)
# f = open('output', 'wb')
# f.write(ct)

#solution

"""
the vulnerability is in the key after some searching and trying some commen
vulnerable keys it worked :)
"""

key =b"\xe0\xe0\xe0\xe0\xf1\xf1\xf1\xf1"

iv = b"13371337"
des = DES.new(key, DES.MODE_OFB, iv)
f = open('output', 'rb')
cipher = f.read()
plain = des.encrypt(cipher)

print(plain.decode())
