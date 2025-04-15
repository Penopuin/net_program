import socket
from collections import defaultdict, deque

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9999))

mailboxes = defaultdict(deque)

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()

    if message.startswith("send"):
        _, mboxID, msg = message.split(' ', 2)
        mailboxes[mboxID].append(msg)
        server_socket.sendto("OK".encode(), addr)

    elif message.startswith("receive"):
        _, mboxID = message.split(' ', 1)
        if mailboxes[mboxID]:
            msg = mailboxes[mboxID].popleft()
            server_socket.sendto(msg.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)

    elif message.strip() == "quit":
        break
