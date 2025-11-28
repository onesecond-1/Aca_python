"""import Calculator
temp=Calculator
cal1=temp.Calculator(10,5)
print(cal1.add())

temp= Calculator(10, 5)
print(temp.add()) # 위와 동일함"""

print('=====예외처리1=====')
num1=int(input('정수 입력1: '))
num2=int(input('정수 입력2: '))
if num2==0:
    print('0으로 나눌 수 없습니다.')
else:
    print(num1//num2)
print('프로그램 종료')

print('=====예외처리2=====')
try:
    num1=int(input('정수 입력1: '))
    num2=int(input('정수 입력2: '))
    print(f'{num1}//{num2}={num1 // num2}')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:  # Exception: 발생할 수 있는 모든 예외
    print('알 수 없는 예외가 발생했습니다.')
print('프로그램 종료')

print('=====예외처리3=====')
try:
    arr=['h', 'e', 'l', 'l', 'o']
    print(arr[1])
    print(arr[8])
    print('try 수행문')
except:
    print('except 수행문')
else:
    print('else 수행문')
finally:
    print('finally 수행문')

print('=====예외처리 실습1=====')
'''
문제1. 하나의 정수를 입력받아, 1부터 입력한 값까지 출력하려고 한다.
단, 정수의 입력이 절대적이여야 하며
다른 형태의 값이 나요면 '정수를 입력하세요'라고 출력될 것이다.
그리고 입력 형태에 상관없이 프로그램이 완료되면 맨 마지막에 '프로그램 종료'라고 출력된다.
'''
try:
    num=int(input('정수 입력: '))
    for i in range(num):
        print(i+1)
except:
    print('정수를 입력하세요')
finally:
    print('프로그램 종료')

print('=====예외 발생시키기=====')
num=int(input('1~5 사이의 정수 입력: '))
if num<1 or num>5:
    # print('범위를 벗어났습니다.)
    raise ValueError('범위를 벗어났습니다.')

class Animal:
    def sound(self):
        raise NotImplementedError # implemented: 구현된 # 추상 매서드
        #추상 매서드이므로 자식 클래스에서 상속하여 사용할 때 매서드 오버라이딩이 필요.

class Dog(Animal):
    # 메서드 오버라이딩
    def sound(self): # NotImplementedError로 추상 매서드가 됨.
        print('강아지는 멍멍하고 짖습니다.')

class Cat(Animal):
    def sound(self):
        print('고양이는 야옹하고 소리냅니다.')

dog1=Dog
dog1.sound()

cat1=Cat()
cat1.sound()


print('=====클래스, 예외처리 실습1=====')
'''
문제1. Phone클래스를 선언하려고 한다. 
해당 클래스는 생성자를 통해서 전화번호(number), 주인이름(owner)을 선언 및 초기화한다.
해당 클래스의 메서드는 전화걸기(call), 메세지보내기(message), 유튜브시청(youtube), 운영체제(operatingSystem)가 존재한다.
call메서드는 하나의 문자열 매개변수를 받고, 실행 시
"{owner}님께서 {파라미터, 전화번호를 받는다.}번호로 전화를 겁니다."를 출력한다.
message메서드는 하나의 문자열 매개변수를 받고, 실행 시
"{owner}님께서 {파라미터, 전화번호를 받는다.}번호로 메세지를 보냅니다."를 출력한다.
youtube메서드는 매개변수가 없으며, 실행 시
"{owner}님께서 유튜브를 시청합니다."를 출력한다.
operatingSystem메서드는 매개변수는 없으며, 수행문을 raise NotImplementedError로 설정한다.
'''

"""
class Phone:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
    def call(self, calnum):
        self.calnum = calnum
        calnum=input('문자열 입력: ')
        print(f'{owner}님께서 {calnum}번호로 전화를 겁니다.')
    def message(self, mesnum):
        self.mesnum = mesnum
        mesnum = input('문자열 입력: ')
        print(f'{owner}님께서 {mesnum}번호로 전화를 겁니다.')
    def youtube(self):
        print(f'{owner}님께서 유튜브를 시청합니다.')
    def operatimgSystem(self):
        raise NotImplementedError
        """


class Phone:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
    def call(self, number):
        print(f'{self.owner}님께서 {number}번호로 전화를 겁니다.')
    def message(self, number):
        print(f'{self.owner}님께서 {number}번호로 전화를 겁니다.')
    def youtube(self):
        print(f'{self.owner}님께서 유튜브를 시청합니다.')
    def operatimgSystem(self):
        raise NotImplementedError

print('=====클래스, 예외처리 실습2=====')
'''
Samsung 클래스를 선언하려고 한다. 해당 클래스는 Phone클래스를 상속받는다.
해당 클래스에는 생성자가 존재하며 핸드폰기종(model)이라는 변수를 선언 및 초기화한다.
메서드는 samcungPay라는 매서드가 존재하며, 하나의 정수형 매개변수를 통해
'owner님께서 삼성페이를 활용해 (매개변수)원을 지불하였습니다.'가 출력된다.
Phone클래스에서 상속받은 operatingSystem메서드를 오버라이딩하여
'Android OS 사용!'이라고 출력하게 만드세요.
'''
class Samsung(Phone):
    def __init__(self, number, owner, model):
        self.number = number
        self.owner = owner
        self.model = model
    def samsungPay(self, money):
        print(f'{self.owner}님께서 삼성페이를 활용해 {money}원을 지불하였습니다.')
    def operatimgSystem(self):
        print('Android OS 사용!')



class Samsung(Phone):
    def __init__(self, number, owner, model):
        super().__init__(owner, number)
        self.model = model
    def samsungPay(self, money):
        print(f'{self.owner}님께서 삼성페이를 활용해 {money}원을 지불하였습니다.')
    def operatimgSystem(self):
        print('Android OS 사용!')

class Apple(Phone):
    def __init__(self, number, owner, model):
        super().__init__(owner, number)
        self.model = model
    def operatimgSystem(self):
        print('iOS 사용!')