import socket
import time

device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device1.connect(('localhost', 9001))

device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2.connect(('localhost', 9002))

def write_data(log):
    with open('data.txt', 'a') as f:
        f.write(log + '\n')

count1 = 0
count2 = 0

while True:
    user_input = input("1: Device1 요청, 2: Device2 요청, quit: 종료 >> ")

    if user_input == '1':
        device1.sendall(b"Request")
        data = device1.recv(1024).decode()
        temp, humid, illum = data.split(',')
        now = time.ctime()
        log = f"{now}: Device1: Temp={temp}, Humid={humid}, Iilum={illum}"
        write_data(log)
        print(log)
        count1 += 1

    elif user_input == '2':
        device2.sendall(b"Request")
        data = device2.recv(1024).decode()
        heart, steps, cal = data.split(',')
        now = time.ctime()
        log = f"{now}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}"
        write_data(log)
        print(log)
        count2 += 1

    elif user_input == 'quit':
        device1.sendall(b"quit")
        device2.sendall(b"quit")
        break

    else:
        print("잘못된 입력입니다.")

print("종료되었습니다.")
device1.close()
device2.close()
