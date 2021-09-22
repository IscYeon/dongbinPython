# 모듈(Module): 미리 작성된 함수 코드를 모아놓은 파이썬 파일
'''
import math
print(math.pow(3, 8))
print(math.sqrt(64))
print(math.gcd(72, 24))
'''

'''
import lib

print(lib.add(3, 7))
'''

'''
from lib import add
print(add(3, 7))
'''

import lib as t

print(t.add(3, 7))
