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
        break  # 종료 후 루프를 빠져나옵니다.
    
    # 연산자 위치 찾기
    operator = None
    for i, char in enumerate(data):
        if char in ('+', '-', '*', '/'):
            operator = char
            left = data[:i].strip()  # 연산자 앞부분 숫자
            right = data[i+1:].strip()  # 연산자 뒷부분 숫자
            break
    
    # 연산자가 없으면 처리
    if operator is None:
        result = "Invalid operator"
    else:
        try:
            # 숫자로 변환
            left = float(left)
            right = float(right)
            
            # 연산 수행
            if operator == '+':
                result = round(left + right)  # 소수점 없이 정수로 반올림
            elif operator == '-':
                result = round(left - right)  # 소수점 없이 정수로 반올림
            elif operator == '*':
                result = round(left * right)  # 소수점 없이 정수로 반올림
            elif operator == '/':
                if right != 0:
                    result = round(left / right, 1)  # 소수점 1자리로 반올림
                else:
                    result = "Division by zero"
        except ValueError:
            result = "Invalid input"
    
    # 결과를 문자열로 변환하여 전송
    conn.send(str(result).encode())

conn.close()
sock.close()
