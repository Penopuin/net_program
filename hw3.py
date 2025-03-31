import socket as soc

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM) #ipv4, tcp
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    client.close()
    