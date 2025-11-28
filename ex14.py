from 코딩.파이썬.강의자료.day13.ex01 import result

print("=====문자열 메서드=====")
temp='aaaaabbbbbbbcccccccddddddd'
print(temp.count('a'))

print(temp.find('a'))
# 맨 앞의 값을 찾아옴

print(temp.upper())
print(temp.lower())
print(temp.isupper())
print(temp.islower())
print('/'.join(temp))
print(temp.split('b'))

temp='a b c d e f g'
print(temp.split())
print(temp.replace(' ', ''))
temp = '-'.join(temp)
print(temp)
temp=temp.split('-')
print(temp)


print("=====문자열 메서드 실습1=====")
'''
문제1. 영어로 된 문자열을 하나 입력받고, 특정 코드를 통해  소문자는 대문자로, 대문자는 소문자로 출력하게 하는 코드를 작성하세요.

실습결과1 
입력 : AbCdE
결과 : aBcDe

실습결과2
입력 : aPPle
결과 : AppLE 
'''
temp=list(input('문자열 입력: '))
for i in range(len(temp)):
    if temp[i].isupper():
        print(temp[i].lower(), end='')
    else:
        print(temp[i].upper(), end='')

result=''
for i in range(len(temp)):
    if temp[i].isupper():
        result += temp[i].lower()
    else:
        result += temp[i].upper()
print(result)

print('=====클래스=====')
class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_age(self, age):
        self.age=age
    def get_age(self):
        return self.age
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 나이는 {self.age}살 입니다.')

pr1=Person()
print(pr1, type(pr1))

pr1.set_age(20)
pr1.set_name('홍길동')
pr1.introduce()


class Phone:
    def __init__(self, owner, number):
        self.owner = owner
        self.number = number

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def printPhone(self):
        print(f"핸드폰 주인은 {self.name}이고, 번호는 {self.number}입니다.")

