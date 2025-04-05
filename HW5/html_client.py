from socket import *

client = socket()
client.connect(("127.0.0.1", 80))  # 포트 확인

request = "GET /HW5/index.html HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
client.send(request.encode())

data = client.recv(4096)

# HTTP 헤더와 본문을 분리해서 출력
header_body = data.split(b"\r\n\r\n", 1)

header = header_body[0].decode()
body = header_body[1].decode('euc-kr', errors='replace')  # 서버가 euc-kr로 보냈기 때문

print(header)
print()
print(body)

client.close()
