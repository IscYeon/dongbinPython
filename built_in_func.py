# input() : 사용자로부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 변환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 최소값 을 변환
# bin(), hex(): 10진수 -> 2진수 변환, 10진수 -> 16진수 변환 (반환값 문자열)
# round() : 반올림을 수행
# type() : 자료형의 종류


'''
user_input = input('정수를 입력하세요: ')
print("제곱: ", int(user_input) ** 2 )
'''

'''
list = [5, 6, 7, 8, 356, 1]
print(max(list))
print(min(list))
'''

'''
print(bin(128))
print(hex(230))
print(int('0xe6', 16))
'''

'''
print(round(123.789, 2))
print(round(123.789, -1))
'''

int = 1
str = "문자열"
list = [1, 2, 3]
dict = {'apple' : '사과'}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))
