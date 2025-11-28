print('=====실습 문제 1=====')
'''
문제1. 여러 개의 정수를 입력받아, 가장 큰 값과 가장 작은 값을 출력하는 printMaxMin함수를 작성하세요.

실행결과1
여러 개의 정수 입력: 1 2 3 4 5 6 7 8 9 10
최댓값: 10
최솟값: 1
'''
def printMaxMin():
    try:
        your=input('여러 개의 정수 입력: ').split()
        tempMax=your[0]
        tempMin=your[0]
        for i in range(len(your)):
            if your[i] > tempMax:
                tempMax=your[i]
            elif your[i] < tempMin:
                tempMin=your[i]
            else:
                pass
        print('최댓값: '+tempMax)
        print('최솟값: '+tempMin)
    except ValueError:
        print('정수만 입력할 수 있습니다.')
    except Exception:
        print('알 수 없는 예외가 발생했습니다.')
printMaxMin()


print('=====실습 문제 2=====')
'''
문제2. printNumbers라는 함수를 선언하려고 한다. 해당 함수는 매개변수가 없으며, 함수 실행 시 여러 개의 값을 입력받으며, 각각의 값들을 출력하는 줄 수와 일치하게 출력하는 함수를 작성하세요.

실행결과1
여러 개의 값 입력: 11 12 13 14 15
11
11 12
11 12 13
11 12 13 14
11 12 13 14 15

실행결과2
여러 개의 값 입력: AB CD EF
AB
AB CD
AB CD EF
'''
def printNumbers():
    temp = input("여러 개의 값 입력: ").split()
    for i in range(len(temp)):
        for j in range(i+1):
            print(temp[j], end=" ")
        print()
printNumbers()


print('=====실습 문제 3=====')
'''
문제2. printValues라는 함수를 선언하려고 한다. 해당 함수는 매개변수가 없으며, 함수 실행 시 여러 개의 값을 입력받으며, 각각의 값들을 출력하는 줄 수와 일치하게 출력하는 함수를 작성하세요.

실행결과1
여러 개의 값 입력: 11 12 13 14 15
11 12 13 14 15
11 12 13 14
11 12 13
11 12
11

실행결과2
여러 개의 값 입력: AB CD EF
AB CD EF
AB CD
AB
'''
def printValues():
    temp = input("여러 개의 값 입력: ").split()
    for i in range(len(temp)):
        for j in range(len(temp)-i):
            print(temp[j], end=" ")
        print()
printValues()