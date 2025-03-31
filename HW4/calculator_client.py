#client

import socket

address = ("localhost", 8000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
print('사칙연산 계산기(+,-,*,/만 사용하시오): ', end='')
while True:
    data = input("")
    s.send(data.encode())
    result = s.recv(1024)
    if not data:
        break
    print("계산결과: ", result.decode(), '\n')

s.close()
