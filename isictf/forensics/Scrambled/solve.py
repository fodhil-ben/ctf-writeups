import struct
import itertools


def is_valid_png(file_path):
    with open(file_path, 'rb') as file:
        # Check the PNG signature
        signature = file.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            return False

        # Check the IHDR chunk
        while True:
            chunk_length = struct.unpack('!I', file.read(4))[0]
            chunk_type = file.read(4)
            if chunk_type == b'IHDR':
                # Skip the IHDR chunk data
                file.seek(chunk_length + 4, 1)
                break
            else:
                # Skip other chunks
                file.seek(chunk_length, 1)
                file.read(4)  # Skip the CRC

            if file.tell() >= chunk_length:
                return False

        # Check the IEND chunk
        while True:
            chunk_length = struct.unpack('!I', file.read(4))[0]
            chunk_type = file.read(4)
            if chunk_type == b'IEND':
                # Skip the IEND chunk data
                file.seek(chunk_length, 1)
                file.read(4)  # Skip the CRC
                break
            else:
                # Skip other chunks
                file.seek(chunk_length, 1)
                file.read(4)  # Skip the CRC

            if file.tell() >= chunk_length:
                return False

    return True



files = ['C', 'Y', '3']
first_file = ['X', 'N']
last_file = ['0']
all_possibilities = list(itertools.permutations(files))
poss= []

for possibility in all_possibilities:
    poss.append(first_file+list(possibility)+last_file)
    print(poss)





output_filename = 'flag'
ext = '.png'
for i in range(len(poss)):
    with open(output_filename+str(i)+ext, 'wb') as flag:
        for ele in poss[i]:
            flag.write(open(ele, 'rb').read())