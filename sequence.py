#시퀀스(Sequence) : 문자열, 리스트, 튜플 등의 인덱스(index) 가지는 자료형

'''
string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string)
print(list)
print(tuple)
'''

'''
string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string[0])
print(list[0])
print(tuple[0])
'''

'''
string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string[0 :5])
print(list[0: 5])
print(tuple[0: 5])
'''

'''
string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
for i in tuple:
    print(i)
'''

'''
string1 = "Hello World"
string2 = ", Python"
print(string1 + string2)
'''
#len(시퀀스 자료형): 시퀀스 자료형의 길이를 출력하는 함수

'''
string1 = "Hello World"
string2 = ", Python"
print(len(string1 + string2))
'''
#반목문 등에서 사용될수 있음
'''
list = [1, 2, 3, 4, 5]
print(6 in list)
'''

list = [1, 2, 3, 4, 5]
if 3 in list:
    print("3을 포함하고 있습니다.")
