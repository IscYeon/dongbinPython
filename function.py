#함수: 특정한 입력을 받아서 처리를 한 이후에. 특정한 출력을 하는 모듈
# 함수를 이용하면 특정한 소스코드의 반복을 줄일 수 있다는 특징
'''
def add(a, b):
    sum = a + b
    return sum

a = add(1, 2)
print(a)
'''


# return 없이도 사용 가능
'''
def add(a, b):
    print(a + b)

add(1, 2)
'''

'''
# 가변 인자 : 함수의 매개변수가 가변적일 수 있을 때 사용
def function(*data):
    print(data)

function(1, 2, 3)
'''

#전역변수와 지역변수
#전역변수 : 소스코드 전체 어디에서든자 사용 가능한 변수
#지역변수 : 특정한 함수(블록) 안에서만 사용할 수 있는 변수
'''
def add(a):
    a = a + 5 # 지역 변수

a = 2 # 전역 변수
add(a)
print(a)
'''

'''
def add(a):
    global a # 전역 변수
    a = a + 5

a = 2
add(a)
print(a)
'''


# 파이썬의 함수는 반환 값이 여러개일 수 있다
def function():
    a = 5
    b = [1, 2, 3]
    return a, b

a , b = function()
print(a)
print(b)
