import socket
import threading

clients = []  # 클라이언트 소켓 리스트

def handle_client(conn, addr):
    print(f"[접속] {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"{addr}: {message}")
            
            # 모든 클라이언트에게 메시지 전송
            for client in clients:
                if client != conn:
                    client.send(data)
        except:
            break

    print(f"[종료] {addr}")
    clients.remove(conn)
    conn.close()

def main():
    host = '0.0.0.0'
    port = 2500

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("[서버 시작] 대기 중...")

    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        th = threading.Thread(target=handle_client, args=(conn, addr))
        th.start()

if __name__ == '__main__':
    main()
