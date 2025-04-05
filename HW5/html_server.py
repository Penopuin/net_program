from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)
print("서버가 실행 중입니다...")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    if len(req) < 1:
        c.close()
        continue

    request_line = req[0]
    print("요청:", request_line)

    tokens = request_line.split()
    if len(tokens) < 2 or tokens[0] != "GET":
        c.close()
        continue

    path = tokens[1]
    filename = path[1:]

    if filename == '':
        filename = 'index.html'
    if os.path.exists(filename):
        if filename.endswith(".html"):
            mimeType = 'text/html'
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
                header = 'HTTP/1.1 200 OK\r\n'
                header += 'Content-Type: ' + mimeType + '\r\n'
                header += '\r\n'
                c.send(header.encode())
                c.send(data.encode('euc-kr'))
        elif filename.endswith(".png"):
            mimeType = 'image/png'
            with open(filename, 'rb') as f:
                data = f.read()
                header = 'HTTP/1.1 200 OK\r\n'
                header += 'Content-Type: ' + mimeType + '\r\n'
                header += '\r\n'
                c.send(header.encode())
                c.send(data)
        elif filename.endswith(".ico"):
            mimeType = 'image/x-icon'
            with open(filename, 'rb') as f:
                data = f.read()
                header = 'HTTP/1.1 200 OK\r\n'
                header += 'Content-Type: ' + mimeType + '\r\n'
                header += '\r\n'
                c.send(header.encode())
                c.send(data)
        else:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
            response += '<BODY>Not Found</BODY></HTML>'
            c.send(response.encode())
    else:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        c.send(response.encode())

    c.close()
