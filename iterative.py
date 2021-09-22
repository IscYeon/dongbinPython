# 반복문 : 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현 : range(시작, 끝)

'''
sum = 0
for i in range(1, 10):
    print(i)
    sum = sum + i
print("합계: ", sum)
'''

'''
count = 0
for i in "Hello World":
    print(i)
'''

'''
count = 0
for i in "Hello World":
    if i == 'o':
        count = count + 1
print("o의 개수는", count, "개 입니다")
'''

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    sum = sum + i
print("합계:", sum)
'''

# continue: continue를 만났을 때 더 이상 명령어를 실행하지 않고 다음 반복을 진행합니다.
# break: break를 만나면 반복문을 벗어납니다.

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1: # 홀수일 경우 건너뜀
        continue
    sum = sum + i
print("합계 :", sum)
'''

'''
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    if i % 2 == 1:
        break
    sum = sum + i
print("합계 :", sum)
'''

i = 0
sum = 0
while i <= 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + i
print("합계 :", sum)
