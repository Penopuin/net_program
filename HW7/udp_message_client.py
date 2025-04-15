import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    user_input = input("Enter the message -> ex: \"send (mboxID) (message)\" *OR* \"receive (mboxID)\": ")
    client_socket.sendto(user_input.encode(), ('localhost', 9999))

    if user_input.strip() == "quit":
        break

    response, _ = client_socket.recvfrom(1024)
    print(response.decode())
