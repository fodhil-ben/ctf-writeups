"""
we have  a python code but it is obfuscated

but not really we see that there is some variable base64 encoded we decode them and one of them have this

```
echo 'KQJzHwAAAGluZ2VuaXVtc3t0NG0zZF90aDNfdzFsZF9zbjRr' | base64 -d

```

we got this

```
)singeniums{t4m3d_th3_w1ld_sn4k
```
we remove some bad chars and submit this 

ingeniums{t4m3d_th3_w1ld_sn4k}

"""


_______="ZT5yBQAAAAEAAABzDgAAAPADAQEB2AcpgASABIAEcgMAAAA=";_____="KQJzHwAAAGluZ2VuaXVtc3t0NG0zZF90aDNfdzFsZF9zbjRr";______="sVHZv1GPIovPn5WayR3c8gg+AAAAAMPApeUQMZEBaHQKO13M";____="LjNNNNNNNNNNNNNNNNRNNNNNNNNN8jbNNNPKNTDNJtOxNIZN";__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 61])).decode()).exec(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([98, 87, 70, 121, 99, 50, 104, 104, 98, 65, 61, 61])).decode()).loads(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 109, 70, 122, 90, 84, 89, 48])).decode()).b64decode(__import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 50, 57, 107, 90, 87, 78, 122])).decode()).decode(____, __import__(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 109, 70, 122, 90, 84, 89, 48])).decode()).b64decode("cm90MTM=").decode())+_____+______[::-1]+_______)))


