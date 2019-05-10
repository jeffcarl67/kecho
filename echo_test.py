import socket
import random
import time
import sys

address = ('127.0.0.1', 12345)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
t0 = time.process_time_ns()
for i in range(int(sys.argv[1])):
    b = random.sample('abcdefghijklmnopqrstuvwxyz', 5)
    s.send(''.join(b).encode())
    data = s.recv(4096)
    # print(data)
t1 = time.process_time_ns()
s.close()
print(t1-t0)
