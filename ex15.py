from tkinter.font import names

print("=====클래스 선언 및 실행=====")
# 클래스 선언
class Person:
    # 메서드 선언
    def __init__(self): # 기본 생성자를 다시 재정의하여 클래스 내에서 사용될 멤버 변수들을 초기화 값으로 초기화.
        self.name=""
        self.age=0

    def __init__(self, call, old): # 생성자 선언
        self.name=call
        self.age=old

    def set_name(self, name):
        # set_name함수는 메서드이므로 클래스 안에 포함되며, 소괄호 안에 self가 무조건 와야한다.
        self.name=name
       #ㄴ멤버 변수 ㄴ일반 변수
        #set_name 메서드의 수행문에서 self.name이라는 클래스에 속해 있는 멤버 변수를 선언하고 name이라는 파라미터를 활용하여 초기화하였다. 따라서 멤버 변수 선언 및 초기화는 메서드에서 이루어진다.
    def get_name(self, name):
        return self.name
        #      ㄴset_name의 수행문과 같은 self.name
        # 클래스 내에서 공통으로 사용할 수 있는 멤버 변수 self.name을 반환한다.
    def set_age(self, age):
        self.age=age
    def get_age(self):
        return self.age
    def ageOld(self):
        return self.age+10
    def ageOld(self, x):
        return self.age+x
    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살 입니다.")
# 클래스 객체화
"""pr1=Person()
pr1.set_name("김철수")
pr1.set_age(30)
pr1.introduce()

pr2=Person()
pr2.set_name("김영희")
pr2.set_age(35)
pr2.introduce()

pr3=Person()
pr3.name="신짱구"
pr3.age=5
pr3.height=150
# 기존 클래스에 선언되지 않은 멤버 변수를 선언
pr3.introduce()
print(pr3.height)

pr4=Person()
print(pr4.ageOld())"""

pr5=Person("손흥민", 36)
pr5.introduce()