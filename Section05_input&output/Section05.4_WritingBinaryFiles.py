__author__ = "Crypto"

# Let's writing and reading binary file

# writing

# with open("binary", "bw") as bin_file:      # "bw" is binary writing
#     for i in range(17):
#         bin_file.write(bytes([i]))      # bytes() is build for binary file, we passed the list to bytes()

# another way for writing the file by using range()

with open("binary", "bw") as bin_file:  # "bw" is binary writing
    bin_file.write(bytes(range(17)))  # bytes() is build for binary file, we passed the list to bytes()

# reading
with open("binary", "br") as bin_file:  # "br" is binary reading
    for b in bin_file:
        print(b)
# ----------------------------------------------------------------------------------------------
print('=' * 40)
#
# and now let's try some writing and reading using binary data

# variables

a = 65534  # FF FE         2 bytes
b = 65535  # FF FF         2 bytes
c = 65536  # 00 01 00 00   4 bytes
x = 2998302  # 02 2D C0 1E   4 bytes

with open("binary2", "bw") as binFile:  # Binary Writing
    binFile.write(a.to_bytes(2, "big"))  # to_bytes() is a function to convert int to bytes
    #                                        parameters:
    #                                                       first parameter: bytes' size
    #                                                       second parameter: referred to Big indian or little indian
    #                                                                         that's related to the "Most significant bytes"
    #                                                                         "1010 1101 1101 1011"
    #                                                                         which stored as "big indian" and
    #                                                                    "least significant bytes" stored as "little indian"
    #                                                                         "0110 0010 1111 0001"
    binFile.write(b.to_bytes(2, "big"))
    binFile.write(c.to_bytes(4, "big"))
    binFile.write(x.to_bytes(4, "big"))
    binFile.write(x.to_bytes(4, "little"))

with open("binary2", "br") as binFile:
    e = int.from_bytes(binFile.read(2), "big")
    print(e)
    f = int.from_bytes(binFile.read(2), "big")
    print(f)
    g = int.from_bytes(binFile.read(4), "big")
    print(g)
    h = int.from_bytes(binFile.read(4), "big")
    print(h)
    i = int.from_bytes(binFile.read(4), "big")  # when we changed the indian into the big indian,
    #                                                 it produces totally different integer number
    print(i)
