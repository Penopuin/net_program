# 클라이언트

import socket as soc

sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

# 본인의 이름을 문자열로 전송
sock.send(b'Seoyeon Jun')

# 본인의 학번을 수신 수 출력
student_id = sock.recv(4)
print(int.from_bytes(student_id, 'big'))

sock.close()