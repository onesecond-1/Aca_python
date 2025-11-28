print("=====문제1=====")
'''
countMeasure이라는 함수를 선언할 것이다. 매개변수는 없고, 함수 실행 시 하나의 정수를 입력받고, 해당 값의 약수의 개수를 반환하는 함수를 작성하세요.

실행결과1
입력: 8
결과: 4개

실행결과2
입력:12
결과: 6개
'''
# 다시 생각해보기(함수를 실행 후에 시작하는거임.)
"""
measure=0
num=int(input("정수입력:"))
def countMeasure():
    for i in range(1,num+1):
"""

def countMeasure():
    num = int(input("정수입력:"))
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count+=1
    return count
print(f"결과: {countMeasure()}", end="개")
print()

print("=====문제2=====")
'''
두 개의 정수를 입력받고, printMultipleNumber함수에서 매개변수의 인자로 활용하려고 한다. 정수 a와 b라고 한다면 a라는 값으로 printMultipleNumber의 인자로 활용하면 1부터 a까지 진행하게 된다. 그리고 b라는 값은 printMultipleNumber의 인자로 활용하면 1부터 a까지 중 b의 배수만 출력하게 한다. 위와 같은 함수를 작성하세요.

실행결과1
입력1 : 100
입력2 : 5
printMultipleNumber(100, 5) 실행
결과 : 5 10 15 20 25 30 ..... 90 95 100

실행결과2
입력1 : 10
입력2 : 3
printMultipleNumber(10, 3) 실행
결과 : 3 6 9
'''
a=int(input("입력1:"))
b=int(input("입력2:"))
def printMultipleNumber(a,b):
    for i in range(1,a+1):
        if i % b ==0:
            print(i, end=" ")
printMultipleNumber(a,b)

def printMultipleNumber(a,b):
    for i in range(1,a+1):
        if i % b ==0:
            print(i, end=" ")
num1=int(input("입력1:"))
num2=int(input("입력2:"))
print("결과: ", end="")
printMultipleNumber(num1,num2)

#다시 생각하기
print("=====문제3=====")
'''
여러 개의 정수값을 입력받아 각각의 값들의 총합을 출력하세요.
'''
a= input("여러개의 정수값 입력:").split()
sum=0
for i in range(len(a)):
    sum+=int(a[i])
print(sum)

sum=0
for i in a:
    sum+=int(i)
print(sum)

print("=====문제4=====")
'''
여러 개의 정수값을 입력하고, 짝수 값만 출력하는 코드를 작성하세요.
'''
# 다시 생각하기
"""
a= input("여러 개의 정수값 입력:").split()
for i in range(len(a)):
    if i%2==0:
"""


num= input("여러 개의 정수값 입력:").split()
for i in range(len(num)):
    if int(num[i])%2==0:
        print(num[i], end=" ")

print("=====문제5=====")
'''
여러 개의 정수 값을 입력하고, 값 중에서 0이라는 값이 존재하면 더 이상 출력하지 않는 반복문을 작성하세요.

실행결과1
입력: 1 2 3 0 4 5
결과: 1 2 3

실행결과2
입력: 9 8 7 6 5 0 4 3
결과: 9 8 7 6 5
'''
# 다시 생각하기
a=input("여러 개의 정수값: ").split()
for i in a:
    if i == 0:
        break

a=input("여러 개의 정수값: ").split()
for i in a:
    if int(i) == 0:
        break
    print(i, end=" ")

"""
idx=0
while int(num[idx]) !=0:
    print(num[idx], end=" ")
    idx += 1
print()
"""
print("=====문제6=====")
'''
maxValue라는 함수를 선언하려 한다. 매개변수는 없는 형태이며, 함수 실행 시 여러 개의 정수값을 입력받아 리스트로 만든다. 해당 리스트에서 가장 큰 값을 반환하는 함수를 작성하세요.
'''
#다시 생각하기
"""
a=input("여러 개의 정수값:").split()
def maxValue():
    b=int(a[0])
    for i in a:
        if i > b:
            b=i
        return b
print(f"{maxValue()}")
"""

def maxValue():
    num=input("여러 개의 정수 값 입력: ").split()
    standard = int(num[0])
    for i in range(1, len(num)):
        num[i]=int(num[i])
        if standard < num[i]:
            standard = num[i]
    return standard
print(f"최대값: {maxValue}")

def maxValue():
    num=input("여러 개의 정수 값 입력: ").split()
    standard = int(num[0])
    for i in range(len(num)):
        num[i]=int(num[i])
    return max(num)
print(f"최대값: {maxValue}")