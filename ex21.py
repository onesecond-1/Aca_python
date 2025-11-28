'''
계산기 프로그램을 만들려고 한다.
프로그램 실행 시 아래와 같이 출력된다.
=====계산기 프로그램=====
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료

번호 입력 :

이후 번호를 1~4까지 입력하면 연산을 수행하고,
5번을 누르면 아래와 같이 프로그램이 종료되게 처리할 것이다.
=====계산기 프로그램=====
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료

번호 입력 : 5

프로그램 종료!!

만약 번호를 1~4사이의 값을 입력하면 아래와 같이 두개의 정수를 입력 받은 후 결과를 출력하고
=====계산기 프로그램=====
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료

번호 입력 : 1

=====2개의 정수 덧셈=====
정수1 : 10
정수2 : 5

결과 : 15

=====계산기 프로그램=====
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료

번호 입력 :

다시 처음으로 돌아가서 반복하게하는 프로그램을 작성하라.
(단, 각각의 연산은 메서드를 통해 표현하세요.
덧셈 add, 뺄셈 sub, 곱셈 mul, 나눗셈 div로 표현하세요.)
'''
class Calculator:
    def add(self):
        print('=====2개의 정수 덧셈=====')
        num1=int(input('정수1: '))
        num2=int(input('정수2: '))
        print()
        print('결과: ', num1+num2)
    def sub(self):
        print('=====2개의 정수 뺄셈=====')
        num1=int(input('정수1: '))
        num2=int(input('정수2: '))
        print()
        print('결과: ', num1-num2)
    def mul(self):
        print('=====2개의 정수 곱셈=====')
        num1=int(input('정수1: '))
        num2=int(input('정수2: '))
        print()
        print('결과: ', num1*num2)
    def div(self):
        print('=====2개의 정수 나눗셈=====')
        num1=int(input('정수1: '))
        num2=int(input('정수2: '))
        print()
        print('결과: ', num1//num2)
        # num2에 0을 제외해야함.
cal = Calculator
choice = 0
while choice!=5:
    print('=====계산기 프로그램=====')
    print('1. 덧셈')
    print('2. 뺄셈')
    print('3. 곱셈')
    print('4. 나눗셈')
    print('5. 종료')
    print()
    choice = int(input('번호 입력: '))
    if choice == 1:
        cal.add()
    if choice == 2:
        cal.sub()
    if choice == 3:
        cal.mul()
    if choice == 4:
        cal.div()
    if choice == 5:
        print('프로그램 종료!!')