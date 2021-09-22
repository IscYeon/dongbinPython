# 튜플(Tuple): 리스트(List)와 비슷한 자료형 (변경 불가)

'''
tuple = (1, 2, 3)
for i in tuple:
    print(i)
'''

'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
print(tuple)
'''

'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
tuple[0] = [7, 8, 9]
print(tuple[0][1])
'''

'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
tuple[0][1] = 7
print(tuple[0][1])
# 즉 튜플의 원소 자체는 바꿀수 없지만 튜플의 원소로 리스트가 있을때에는 그 리스트의 값은 바꿀수 있습니다.
'''


#인덱싱, 슬라이싱 등의 문법도 그대로 사용이 가능
'''
tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple[0:5])
'''

tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple[0:5] * 3)
