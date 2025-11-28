import random
# 파일명 random은 랜덤(난수)과 관련된 여러 함수를 모아놓은 파일
# from random import *
# from random import randint
# 위 두개의 명령어 중 하나로 대체할 때 결과값을 예상해보기

print(random.randint(1, 10))
# .은 ~안에, ~의로 해석된다.
# randint함수는 두 매개변수 사이의 값 중에서 랜덤한 값 반환

print(random.randrange(10))
print(random.randrange(2,10))
print(random.randrange(2,10,3))
# range랑 동일한 개념

print(random.choice(['A', 'B', 'C']))

print(random.sample(['봄', '여름', '가을', '겨울'], 2))
# sample함수는 매개변수로 오는 리스트 중에서 리스트 뒤에 오는 정수 매개변수를 활용해 그 값의 개수만큼 랜덤한 값을 하나의 리스트로 정리하여 반환한다.
# 중복은 불가.

temp=[5,1,3,4,2]
random.shuffle(temp)
print(temp)
# shuffle함수는 요소들의 순서를 뒤섞는다.



import time as t
# 시간의 기준은 1970.01.01 00:00:00
# 시간과 관련된 모듈을 모아놓은 파일
# as 키워드를 활용하여 모듈을 모듈이름이 아닌 모듈별명으로 대체하여 함수들을 활용할 수 있다.

print(t.time())
# 기준 시간부터 현재까지의 초단위 계산 출력

# time.sleep(5)
# 매개변수의 값만큼 실행을 멈추는 함수

start= t.time()
Li=[]
for i in range(100000):
    Li.insert(0,i)
end=t.time()
print((end - start))

import math
# 수학과 관련된 모듈을 모아놓은 파일
print(math.ceil(3.14))
# 올림
print(math.floor(3.82))
# 내림
print(math.factorial(5))
print(math.pow(5,2))
# 제곱
print(math.sqrt(25))
# 제곱근

print("=====모듈 실습1=====")
'''
문제1. 1~100까지의 updown게임. 10번의 기회가 주어진다. 10번의 기회동안 1~100까지의 랜덤한 값을 맞추는 게임으로, 10번의 정수 입력이 주어지고 입력 결과는 정답이 입력한 값보다 크다면 up, 작다면 down으로 출력된다. 10번의 기회동안 정답을 맞추면 "성공"을 출력하고 프로그램이 종료되고, 오답일 경우 "오답"이라고 출력된다. 만약 10번의 기회를 모두 소진한다면 "탈락"이라고 출력하고 프로그램 종료

실행결과1
Up&Down 게임!!!
입력 : 50
up
입력 : 75
down
입력 : 60
down
입력 : 52
up
입력 : 55
up
입력 : 57
down
입력 : 56
정답
프로그램 종료!
'''
# 다시 생각하기
import random

print('Up&Down 게임!!')
right=random.randint(1, 100)
for i in range(10):
    your = int(input("입력: "))
    if your>right:
        print('up')
    elif your<right:
        print('down')
        # 정답이 입력보다 커도 다운만 뜨고 있음.
    else:
        print('성공')
print('오답')
print('탈락')
print('프로그램 종료!')




result = random.randint(1, 100) # 정답
print("Up & Down 게임!!!")
i = 0

# while을 통한 해답
while i < 10:
    print("남은 횟수 : %d" % (10 - i))
    number = int(input("입력 : "))

    if number < 1 or number > 100:
        print("입력값은 1부터 100까지의 값이어야 합니다.\n패널티! 횟수 하나 차감!")
        i+=1
        continue

    if number < result:
        print("Up")
    elif number > result:
        print("Down")
    elif number == result:
        print("정답!")
        break
    if i == 9:
        print("오답!")
        break
    i+=1



# for을 통한 해답
for i in range(10):
    print("남은 횟수 : %d" %(10 - i))
    number = int(input("입력 : "))

    if number < 1 or number > 100:
        print("입력값은 1부터 100까지의 값이어야 합니다.\n패널티! 횟수 하나 차감!")
        continue

    if number < result:
        print("Up")
    elif number > result:
        print("Down")
    elif number == result:
        print("정답!")
        break
    if i == 9:
        print("오답!")

print("=====모듈 실습2=====")
'''
문제2. 가위바위보 프로그램을 작성하세요. 가위 바위 보 중에서 하나를 입력받아 랜덤으로 반환되는 가위 바위 보와 게임을 합니다.

실행결과1
입력 : 가위
결과 : 프로그램은 바위를 냈습니다. 패배하셨습니다!

실행결과2
입력 : 보
결과 : 프로그램은 바위를 냈습니다. 승리하셨습니다!

실행결과3
입력 : 바위
결과 : 프로그램은 가위를 냈습니다. 승리하셨습니다!

실행결과4
입력 : 바위
결과 : 프로그램은 바위를 냈습니다. 비겼습니다!
'''
result=random.choice(['가위', '바위', '보'])
your=input('입력: ')
print(f'프로그램은 {result}를 냈습니다.')
if result==your:
    print(f'비겼습니다!')
elif (result='바위' and your='가위') or (result='가위' and your='보') or (result='보' and your='바위'):
    print('패배하셨습니다!')
elif (result='바위' and your='보') or (result='가위' and your='바위') or (result='보' and your='가위'):
    print('승리하셨습니다!')
else:
    print('이 프로그램의 명령어는 가위, 바위, 보로 이루어져 있습니다.')