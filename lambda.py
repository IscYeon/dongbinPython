# 람다식: 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법

add = lambda x, y: x + y
print(add(1, 2))

# map(): 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있드록 도와주는 문법

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
my_function = lambda a, b : a * b
result = map(my_function, list1, list2)
print(list(result))
