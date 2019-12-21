import binascii

d = {}
for i in range(0, 256):
    d[binascii.crc32(bytes(chr(i), "utf-8"))] = chr(i)


print(d)

s = "1b0ecf0b 916b06e7 82079eb1 6b9df6f 856a5aa8 76d32be0 15d54739 9606c2fe f0f9344 9606c2fe 862575d efda7a5a 862575d 6b9df6f 916b06e7 efda7a5a 71beeff9 f26d6a3e 6c09ff9d efda7a5a 862575d 29d6a3e8 6b9df6f 6c09ff9d 6b9df6f 6dd28e9b 1ad5be0d 29d6a3e8 f0f9344 1d41b76 f0f9344 7808a3d2 fcb6e20c".split(" ")

for i in s:
    print(d[int(i, 16)], end="")