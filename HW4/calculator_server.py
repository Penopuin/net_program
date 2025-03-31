from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8000))
sock.listen(1)

conn, adress = sock.accept()
print('connected by', adress)

while True:
    data = conn.recv(1024)
    if not data:
        break

    expr = data.decode()
    print("Received message:", expr)

    # 연산자 찾기
    for i in range(len(expr)):
        j = expr[i]
        if j in ('+', '-', '*', '/'):
            left = expr[:i].strip()  # 연산자 앞부분 숫자
            right = expr[i+1:].strip()  # 연산자 뒷부분 숫자
            break
    
    try:
        # 숫자로 변환
        left = float(left)
        right = float(right)
        
        # 계산 수행
        if j == '+':
            result = left + right
        elif j == '-':
            result = left - right
        elif j == '*':
            result = left * right
        elif j == '/':
            if right != 0:
                result = left / right
            else:
                result = "Division by zero"
        else:
            result = "Invalid operator"

    except ValueError:
        result = "Invalid input"

    # 결과를 문자열로 변환하여 전송
    conn.send(str(result).encode())

conn.close()
sock.close()
