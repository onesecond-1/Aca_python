print("=====함수 실습 1번=====")
'''
문제. printList라는 함수를 선언하려고 한다. 
해당 함수는 하나의 매개변수를 받는데, 매개변수의 형태는 리스트로 입력받는다.
하나의 리스트를 입력받고, 해당 함수 실행 시 아래와 같은 결과가 출력된다. 
아래와 같은 결과가 나오도록 코드를 작성하세요.

실행 결과 1                     실행 결과 2                     실행 결과 3
입력 : 1 3 5 7 9               입력 : 5 1 3 6 4 2 8            입력 : 사과 바나나 배 참외
1                              5                              사과
1 3                            5 1                            사과 바나나
1 3 5                          5 1 3                          사과 바나나 배
1 3 5 7                        5 1 3 6                        사과 바나나 배 참외
1 3 5 7 9                      5 1 3 6 4
                               5 1 3 6 4 2
                               5 1 3 6 4 2 8
'''
#다시 생각하기
def printList(x):
    for i in x:
        for j in range(i+1):
            print(i, end=" ")
        print()
temp=input("입력: ").split()
printList(temp)


def printList(tempList):
    # 2. 입력 개수만큼 반복
    for i in range(len(tempList)):
        ''' 
        3. 반복횟수마다 하나씩 증가하여 출력된다.
        첫번째 반복 0번째 까지
        두번째 반복 1번째 까지
        세번째 반복 2번째 까지
                 .
                 .
                 .
        N번째 반복 N-1번째 까지
        '''
        for j in range(i+1):
            print(tempList[j], end=" ")
        # 4. 줄내림
        print()


# 1. 여러개의 값 입력
temp = input("입력 : ").split()
printList(temp)

print("=====함수 실습 2번=====")
'''
문제. printReverseList라는 함수를 선언하려고 한다. 
해당 함수는 하나의 매개변수를 받는데, 매개변수의 형태는 리스트로 입력받는다.
하나의 리스트를 입력받고, 해당 함수 실행 시 아래와 같은 결과가 출력된다. 
아래와 같은 결과가 나오도록 코드를 작성하세요.

실행 결과 1                     실행 결과 2                     실행 결과 3
입력 : 1 3 5 7 9               입력 : 5 1 3 6 4 2 8            입력 : 사과 바나나 배 참외
1 3 5 7 9                     5 1 3 6 4 2 8                   사과 바나나 배 참외
1 3 5 7                       5 1 3 6 4 2                     사과 바나나 배
1 3 5                         5 1 3 6 4                       사과 바나나
1 3                           5 1 3 6                         사과
1                             5 1 3
                              5 1
                              1
'''
#다시 생각하기
def printReverseList(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            print(i, end=" ")
        print()
temp = input("입력: ").split()
printReverseList(temp)


print("=====함수 실습 3번=====")
'''
문제. printTriangle 함수를 선연하려고 한다. 
해당 함수의 매개변수는 없으며, 함수 실행시 하나의 정수를 입력받는다.
입력 받은 정수를 활용하여 아래와 같은 모양이 출력된다. 
아래와 같은 결과가 출력되도록 코드를 작성하세요.
(출력시 보이는 빼기기호(-)는 띄어쓰기를 가시적으로 표현한 것이다.)

입력 : 5              입력 : 7                      입력 : 4
----1                 ------1                      ---1
---123                -----123                     --123
--12345               ----12345                    -12345
-1234567              ---1234567                   1234567
123456789             --123456789
                      -1234567891011
                      12345678910111213
'''
#다시 생각하기
def printTriangle():
    x = int(input("정수입력: "))
    for i in x-1:
        print(" ", end="")
    for j in x+2:
        print()




def printTriangle():
    # 입력
    num = int(input("입력 : "))

    # 전체 반복
    for i in range(num):
        # 공백 출력 반복
        for j in range(num-1-i):
            print(end=" ")
        # 숫자 출력 반복
        for k in range(1+2*i):
            print(k+1, end="")
        # 줄 내림
        print()
printTriangle()

