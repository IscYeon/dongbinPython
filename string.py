#문자열 자료형 뒤집기: 슬라이싱 활용

str = "Hello World"
print(str[::-1])

#len(): 문자열의 길이를 출력
str = "Hello World"
print(len(str))

#isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인
str = "HelloWorld"
print(str.isalpha())

#isdigit():특정한 문자열이 숫자로만 이루어져 있는지 확인
str = "123 123"
print(str.isdigit())

#isalnum(): 특전한 문자열이 문자와 숫자로만 이루어져 있는지 확인
str = "abc#123"
print(str.isalnum())

#join(리스트 자료형): 여러개의 문자열을 구분자와 함께 합치는 함수
list =['Hello', 'World', '홍길동']
print('-'.join(list))

#sorted(문자열 자료형): 각 문자를 정렬하는 함수
str = "helloworld"
list = sorted(str)
print(list)
print(''.join(list))
list = sorted(str, reverse=True)
print(''.join(list))

#split(토큰): 문자열을 토큰에 따라서 분리하는 함수
str = "I-wanna-watch-a-movie."
list = str.split('-')
print(list)

#find(서브 문자열): 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
str = "I like like you."
print(str.find('like', 5))

#upper(), lower): 문자열을 대문자로 혹은 소문자로 변환해주는 함수
str = "Hello World"
print(str.upper())
print(str.lower())

# strip() : 좌우로 특정한 문자열을 제거하는 함수
# lstrip(), rstrip() : 왼쪽만 or 오른쪽만
str = "ttHello Worldtt"
print(str.strip('t'))

#eval() : 문자열 수식을 계산해주는 함수
exp = "(203+705)*3-(30/6)"
print(eval(exp))
