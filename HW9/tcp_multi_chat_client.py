import socket
import threading

def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

def main():
    server_ip = 'localhost'
    server_port = 2500

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))

    my_id = input("ID를 입력하세요: ")
    sock.send(f"[{my_id}] 입장".encode())

    th = threading.Thread(target=receive, args=(sock,))
    th.daemon = True
    th.start()

    while True:
        msg = input()
        if msg.lower() == 'quit':
            sock.send(f"[{my_id}] 퇴장".encode())
            break
        full_msg = f"[{my_id}] {msg}"
        sock.send(full_msg.encode())

    sock.close()

if __name__ == '__main__':
    main()
