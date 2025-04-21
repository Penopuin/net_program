# 슬라이싱 연습 문제 (문자 수 약 12자짜리 문자열 하나로 구성)
text = "HelloSeoyeon!" 

# 1. 처음 5글자 출력
print("문제 1:", text[:5])  # 출력 예시: Hello

# 2. 마지막 3글자 출력
print("문제 2:", text[-3:])  # 출력 예시: on!

# 3. 문자열 전체 거꾸로 출력
print("문제 3:", text[::-1])  # 출력 예시: !noyeoeSolleH

# 4. "Seoyeon"만 출력
print("문제 4:", text[5:-1])  # 출력 예시: Seoyeon

# 5. 짝수 인덱스 문자만 출력
print("문제 5:", text[::2])  # 출력 예시: Hloeyo!

# 6. 홀수 인덱스 문자만 출력
print("문제 6:", text[1::2])  # 출력 예시: elSoen

# 7. 가운데 문자 출력
print("문제 7:", text[len(text)//2])  # 출력 예시: o

# 8. "Hello"를 거꾸로 출력
print("문제 8:", text[:5][::-1])  # 출력 예시: olleH

# 9. 첫 글자와 마지막 글자 출력
print("문제 9:", text[0]+text[-1])  # 출력 예시: H!

# 10. 문자열 길이 출력
print("문제 10:", len(text))  # 출력 예시: 13
