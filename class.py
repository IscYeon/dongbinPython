# 클래스(Class): 반복되 불필요한 소스코드를 최소하 하면서 현실 세계의 사물을 컴퓨터에 프로그래밍 상에서 쉽게 표현할 수 있드록 해주는 프로그래밍 기술

# 인스턴스 : 클래스로 정의된 객체를 프로그 상에서 이요할 수 있게 만든 변수

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수, 메소드라고도 부릅니다.

class Car:
    #클래스의 생성자
    def __init__(self, name, color):
        self.name = name # 클래스의 멤버
        self.color = color # 클래스의 멤버
    # 소멸자
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")
    # 클래스의 메소드
    def show_info(self):
        print("이름:", self.name, "/ 색상:", self.color)
    # Setter 메소
    def set_name(self, name):
        self.name = name

'''
car1 = Car("소나타", "빨간색")
car1.show_info()

car2 = Car("아반떼", "검은색")
car2.show_info()
'''

'''
car1 = Car("소나타", "빨간색")
car1.set_name("아반떼")
print(car1.name, "을(를) 구매했습니다!")
'''

car1 = Car("소나타", "빨간색")
car1.set_name("아반떼")
car1.show_info()
del car1 # 메모리에서 할당 해제
car1.show_info() # 할당 해제됬기때문에 오류가 나옵니다.
