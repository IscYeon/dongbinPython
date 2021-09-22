# 사전(Dictionary) : 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
'''
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'Effort'
dict['안녕'] = 'Hi'
del dict['기적']
'''

'''
if '노력' in dict:
    print("노력이라는 키가 존재합니다.")
'''

'''
values = dict.values()
value_list = list(values)
print("값 리스트 : ", value_list)
'''

'''
keys = dict.keys()
key_list = list(keys)
print("키 리스트: ", key_list)
'''
# dict.clear()

# print("사전 자료형의 길이", len(dict))


# print(dict)

'''
for i, k in enumerate(dict):
    print("[인덱스:", i, "] 한글:", k, "/ 영어:", dict[k])
'''


scores = {}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한올'] = 85
print(sorted(scores)) # 키로 정렬하기
print(sorted(scores, reverse=True)) # 키로 내림차순 정렬하기
print(sorted(scores.values())) # 값을 정렬하기
