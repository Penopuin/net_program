import socket
import random

HOST = 'localhost'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Device 1 대기 중...')
    conn, addr = s.accept()
    with conn:
        print('접속됨:', addr)
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                temp = random.randint(0, 40)
                humid = random.randint(0, 100)
                illum = random.randint(70, 150)
                send_data = f"{temp},{humid},{illum}"
                conn.sendall(send_data.encode())
            elif data == 'quit':
                print("Device 1 종료")
                break
