from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8000))
sock.listen(1)
conn, adress = sock.accept()
print('connected by', adress)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if data == 'q':
        print('프로그램 종료')
        conn.close()
        sock.close()
        break
    operator = None
    for i, char in enumerate(data):
        if char in ('+', '-', '*', '/'):
            operator = char
            left = data[:i].strip()
            right = data[i+1:].strip()
            break
    if operator is None:
        result = "Invalid operator"
    else:
        try:
            left = float(left)
            right = float(right)
            if operator == '+':
                result = round(left + right)  
            elif operator == '-':
                result = round(left - right)  
            elif operator == '*':
                result = round(left * right)  
            elif operator == '/':
                if right != 0:
                    result = round(left / right, 1)
                else:
                    result = "Division by zero"
        except ValueError:
            result = "Invalid input"
    
    conn.send(str(result).encode())

conn.close()
sock.close()
