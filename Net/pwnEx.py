from pwn import *

print(cyclic(50))
print(cyclic_find('laaa'))

print(shellcraft.sh())
#print(hexdump(asm(shellcraft.sh())))

#p = process('/bin/sh')
#p.sendline('echo hello;')
#p.interactive()

#r = remote("127.0.0.1", 1234)
#r.sendline('Hello!')
#r.interactive()
#r.close()

print(p32(0x1333758)) #32-bit encode
print(hex(u32(p32(0x13376785)))) #32-bit decode

if 1==2:
    L = ELF('/bin/bash')
    print(hex(L.address))
    print(hex(L.entry))
    print(hex(L.got['write']))
    print(hex(L.plt['write']))
    
    for address in L.search(b'/bin/sh\x00'):
        print(hex(address))
    print(hex(next(L.search(asm('jmp esp')))))
    
    r = ROP(L)
    print(r.rbx)
    print(xor(xor("A", "B"), "A"))

# Various encryption protocols provided with Pwn
print(b64e(b"test"))
print(b64d(b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

print(bits(b'a'))
