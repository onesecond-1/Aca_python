print("=====클래스 상속=====")
"""class Person:
    def __init__(self, name):
        self.name=name
    def eat(self, food):
        print(f"{self.name}이(가) {food}를 먹습니다.")

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        # 매개변수인 name을 전달하여 부모클래스의 생성자 실행
        self.school=school
    def study(self):
        print(f"{self.name}은(는) {self.school}에서 공부합니다.")

pr1=Student("홍길동", "노원초등학교")
pr1.study()
pr1.eat("햄버거")

pr2=Person("김철수")
pr2.eat("피자")"""

print("=====하나의 부모 클래스, 여러 개의 자식 클래스=====")
class Person:
    def __init__(self, name):
        self.name=name
    def sleep(self):
        print(f"{self.name}은(는) 잠을 잔다.")

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school=school
    def study(self):
        print(f"{self.name}은(는) {self.school}에서 공부합니다.")

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company=company
    def work(self):
        print(f"{self.name}은(는) {self.company}에서 근무합니다.")

st1=Student("짱구", "코리아IT아카데미")
st1.sleep()
st1.study()

em1=Employee("철수", "GS25")
em1.work()
em1.sleep()

print("=====클래스 실습1=====")
'''
문제. Calculator()라는 클래스를 선언하려고한다.
해당 클래스에는 생성자가 존재하며 2개의 매개변수를 입력받는다.
위에서 실행할 생성자를 통해서 2개의 정수가 정해지며,
2개의 정수의 합을 반환하는 add() 메서드,
2개의 정수의 차를 반환하는 sub() 메서드,
2개의 정수의 곱을 반환하는 mul() 메서드,
2개의 정수의 나눗셈(몫)을 반환하는 div() 메서드가 포함되어 있는
Calculator() 클래스를 작성하고 실행하세요.
'''
class Calculator():
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        plus=self.a+self.b
        return(plus)
    def sub(self):
        minus=self.a-self.b
        return(minus)
    def mul(self):
        multiple=self.a*self.b
        return(multiple)
    def div(self):
        division=self.a//self.b
        return(division)

temp1=Calculator(2,5)
print(temp1.add())
print(temp1.sub())
print(temp1.mul())
print(temp1.div())



class Calculator():
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        result=self.a+self.b
        return result
    def sub(self):
        result=self.a-self.b
        return result
    def mul(self):
        result=self.a*self.b
        return result
    def div(self):
        result=self.a//self.b
        return result

temp1=Calculator(2,5)
print(temp1.add())
print(temp1.sub())
print(temp1.mul())
print(temp1.div())


cal=Calculator(10,0)
print(temp1.add())
print(temp1.sub())
print(temp1.mul())
print(temp1.div())

# 메서드 오버라이딩하는 NewCalculator
class NewCalculator(Calculator):
    # pass 수행문을 비움.
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    # 부모 클래스를 활용하기 위해서는 부모 클래스의 생성자와 맞는 형식의 생성자를 자식 클래스에서도 만들어주어야 함.

    # Calculator.div() 메서드 오버라이딩
    def div(self):
        if self.b !=0:
            return self.num1//self.num2
        else:
            return -1


newCal1=NewCalculator(10,0)
print(newCal1.add())
print(newCal1.sub())
print(newCal1.mul())
print(newCal1.div())

print("=====클래스 실습2=====")
'''
문제2. Myself라는 클래스를 선언하려고 한다.
해당 클래스는 생성자가 존재하며 5개의 매개변수가 존재한다.
각각의 데이터 속성들은 이름(name), 나이(age), 키(height), 전화번호(phone), 혈액형(bloodType)이다.
그리고 해당 클래스에는 아래와 같은 메서드들이 존재한다.
sayMyName이라는 메서드는 본인 이름을 출력하는 메서드이고,
sayMyAge라는 메서드는 본인의 나이를 출력하는 메서드이고,
introduceMyself라는 메서드는 이름, 나이, 키, 전화번호, 혈액형을 소개하는 메서드며,
updatePhoneNumber라는 메서드는 전화번호를 새로 수정하여 저장하는 메서드이다.
위와같은 클래스를 작성하세요.
'''

class Myself():
    def __init__(self, name, age, height, phone, blood):
        self.name=name
        self.age=age
        self.height=height
        self.phone=phone
        self.blood=blood
    def sayMyName(self):
        print(self.name)
    def sayMyage(self):
        print(self.age)
    def introduceMyself(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}, 키는 {self.height}, 전화번호는 {self.phone}, 혈액형은 {self.blood}입니다.")
    def updatePhoneNumber(self):
        self.phone=input("새 전화번호 입력: ")
        # newNumber = input("전화번호 입력: ")
        # self.phone = newNumber   >>>>>>>>>>>위와 동일한 결과

intro=Myself("마찬호", 27, 182, 8298845781, "b")
intro.sayMyName()
intro.sayMyage()
intro.introduceMyself()
intro.updatePhoneNumber()
intro.introduceMyself()


intro.updatePhoneNumber(8299998888)
intro.introduceMyself()