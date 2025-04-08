name = 'My name is Seoyeon Jun'

# 문자열의문자수를출력하라.
print(len(name))
# 문자열을10번반복한문자열을출력하라.
for i in range(10):
    print(name)
# 문자열의첫번째문자를출력하라.
print(name[0])
# 문자열에서처음4문자를출력하라.
print(name[:4])
# 문자열에서마지막4문자를출력하라.
print(name[-4:])
# 문자열의문자를거꾸로출력하라.
print(name[::-1])
# 문자열에서첫번째문자와마지막문자를제거한문자열을출력하라.
print(name[1:-1])
# 문자를모두대문자로변경하여출력하라.
print(name.upper())
# 문자를모두소문자로변경하여출력하라.
print(name.lower())
# 문자열에서'a'를 'e'로 대체하여 출력하라
print(name.replace('a', 'e'))