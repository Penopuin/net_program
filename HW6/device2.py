import socket
import random

HOST = 'localhost'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Device 2 대기 중...')
    conn, addr = s.accept()
    with conn:
        print('접속됨:', addr)
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                heart = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                send_data = f"{heart},{steps},{cal}"
                conn.sendall(send_data.encode())
            elif data == 'quit':
                print("Device 2 종료")
                break
