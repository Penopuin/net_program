# 서버

import socket as soc

sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM) #ipv4, tcp
sock.bind(('', 9000))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    
    #학생의 이름을 수신한 후 출력
    student_name = client.recv(1024)
    print(student_name.decode())
    
    #학생의 학번을 전송
    client.send((20221296).to_bytes(4, 'big'))
    
    client.close()
    