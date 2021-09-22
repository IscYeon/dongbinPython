# open(): 파일을 특정한 모드로 여는 함수입니다. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수입니다

'''
f = open("input.txt", "r", encoding="UTF-8")
data = f.read()
print(data)
f.close()
'''

'''
f = open("input.txt", "r", encoding="UTF-8")
f.seek(9)
data = f.read()
print(data)
f.close()
'''

#readline() : 파일 객체로부터 한 줄씩 문자열을 읽은 함수
'''
f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
     data = f.readline()
     count = count + 1
     print("%d번째 줄: %s" %(count, data), end='')
f.close()
'''

#readlines() : 전체 내용을 한 번에 리스트에 담는 함수.
'''
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
for i, data in enumerate(list):
    print("%d번쨰 줄: %s" %(i + 1, data), end='')
f.close()
'''

# with : close() 없이도 작업이 끝나면 자동으로 메모리 할당이 사라짐 + 소스코드 짧아짐
'''
with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i + 1, data), end='')
'''

#
def process(filename):
    with open(filename, "r") as f:
        dict = {} #키 : 알파벳, 값: 빈도수
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dic = process("input.txt")
# 빈도수를 기준으로 내림차순 정렬을 수행합니다.
dic = sorted(dic.items(), key=lambda a:a[1], reverse=True)
print(dic)
for dat, count in dic:
    if dat == '\n' or dat == ' ':
        continue
    print("%d번 출현: [%c]" %(count, dat))
