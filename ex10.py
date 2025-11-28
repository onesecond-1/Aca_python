print("=====함수와 메서드=====")
#함수
print("출력함수")
a=input("입력함수:")
#메서드
b=[10,20,30]
b.append(40)

print("=====함수 선언=====")
def add(x,y):
    print(x+y)
result1=add(10,5)
print(result1) # None으로 뜸. 함수 끝에 print로 끝나 출력하고 없어졌기 때문. 이것이 결과값이 없다는 의미임.

def sub(x,y):
    result=x-y
    return result
result2=sub(20,10) # 함수가 완료되면 더이상 변수가 아닌 값으로 취급됨. 이것이 return문의 결과값이 있다는 의미.
print(result2)

# 입력값 결과값 없음.
def temp1():
    print("temp1")
# 입력값 있고, 결과값 없음.
def temp2(x):
    print("temp2"+x)
# 입력값 없고, 결과값 있음.
def temp3():
    return "temp3"
# 입력값 있고, 결과값 있음.
def temp4(x):
    return "temp4"+x

print("=====함수 실습1=====")
'''
문제1. numberSum이라는 함수를 선언하려고 한다. numberSum함수는 3개의 정수를 입력받고, 입력받은 3개의 값을 반환하는 함수이다. numberSum함수를 실행시켜 반환값을 출력하는 코드를 작성하세요.

실행결과1               실행결과2
numberSum(3,4,5)       numberSum(1,3,5)
결과 : 12              결과 : 9
'''
# 다시 생각하기
def numberSum(x,y,z):
    return "x"+x
    return 'y'+y
    return 'z'+z
    print(x+y+z)

def numberSum(a,b,c):
    return a+b+c
result=numberSum(3,4,5)
print(result)

print("=====함수 실습2=====")
'''
문제2. printList라는 함수를 선언하고, 매개변수는 리스트로 1개 받을 것이다. printList함수는 말 그대로 리스트를 매개변수로 입력받으면 리스트안에 있는 값들을 모두 출력하는 함수이다. printList함수를 선언하고 실행하는 코드를 작성하세요.

실행결과1
printList([10,20,30])
결과 : 10 20 30

실행결과2
printList(["사과", "바나나", "배"])
결과 : 사과 바나나 배
'''
# 다시 생각하기
"""
def printList([10,20,30])
    print(printList)
"""

def printList(x):
    for i in x:
        print(i, end=" ")

    for i in range(len(x)):
        print(x[i], end=" ")

print("=====함수 실습3=====")
'''
문제3. printDan()이라는 함수를 선언하려고 한다. 해당 함수는 매개변수가 1개이며 정수이다. 정수를 한개 입력받아서 인자로 받아 실행하면 아래와 같이 출력하는 함수를 작성하여 실행하세요.

실행결과1
입력 : 5
결과 : 
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45

실행결과2
입력 : 7
결과 : 
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
'''
# 다시 생각하기
def printDan(x):
    int(input("입력:")+x)
    for i in range(1,10):
        print(x*i, end=" ")

def printDan(x):
    for i in range(1,10):
        print(f"{x}*{i}={x*i}")
num=int(input("입력:"))
printDan(num)

print("=====함수 실습4=====")
'''
문제4. printMeasure()라는 함수를 선언하려고 한다. 해당 함수의 매개변수는 정수를 1개 받는다. 정수를 입력받아 printMeasure()함수의 인자로 사용하며, 실행 시 아래와 같은 결과가 출력된다. 아래와 같은 결과가 나오도록 코드를 작성하세요.

실습결과1
입력 : 8
결과 : 1 2 4 8

실습결과2
입력 : 13
결과 : 1 13

실습결과3
입력 : 25
결과 : 1 5 25
'''
#다시 생각하기
def printMeasure(x):
    for i in range(x):
        num%i==0
        print(i)
num=int(input("입력:"))
printMeasure(num)

def printMeasure(number):
    for i in range(1, number+1):
        if num%i==0:
            print(i, end=" ")
num=int(input("입력:"))
printMeasure(num)


print("=====함수 실습5=====")
'''
문제5. countMeasure()함수는 매개변수로 정수를 1개 받고, 입력받은 매개변수의 값에 대한 약수의 개수를 반환하는 함수이다. countMeasure()함수를 선언하고 정수를 한개 입력받아 해당 함수의 인자로 사용하여 실행하는 코드를 작성하세요.

실행결과1
입력 : 8
결과 : 4개

실행결과2
입력 : 12
결과 : 6개
'''
#다시 생각하기
def countMeasure(num):
    for i in range(1, num+1):
        if num%i==0:
            #count
        print()
num=int(input("입력:"))
countMeasure(num)

def countMeasure(num):
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    return count
            #count
num=int(input("입력:"))
print(f"{countMeasure(num)}개")