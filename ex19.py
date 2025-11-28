print('=====재귀함수=====')
# 팩토리얼 계산
def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

'''
sumNumber라는 함수를 선언하려고 한다. 해당 함수는 하나의 정수 매개변수가 존재하며, 매개변수를 활용하여 1부터 매개변수의 값까지의 합을 반환하는 함수를 작성하세요.
'''
# 재귀함수를 통한 해답
def sumNumber1(x):
    if x==1:
        return 1
    else:
        return x + sumNumber1(x-1)
# for문을 통한 해답
def sumNumber2(x):
    sum=0
    for i in range(x):
        sum += i
    return sum

'''
sumList라는 함수를 선언하려고 한다. 해당 함수는 하나의 리스트 매개변수를 받으며, 해당 함수 실행 시 리스트 안에 저장된 모든 요소의 값을 반환한다. sumList 함수를 작성하시오.
'''
"""
다시 생각하기
def sumList(x):
    y=int(len(x))
    if y==0:
        return x[0]
    else:
        return x[y], sumList(x[y-1])
print(sumList([1,2,3,4,5,6,7,8]))
"""


# for문
def sumList1(a):
    result=0
    for i in range(len(a)):
        result += a[i]
    return result

#재귀함수
def sumList2(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sumList2(a[1:])


'''
reverseString이라는 함수를 선언하려고 한다. 해당 함수는 하나의 문자열을 매개변수로 받으며, 해당 함수 실행 시 매개변수로 받은 문자열 값을 뒤집은 형태로 반환된다. 위와 같은 함수를 작성하세요.

print(rever-('abcd')
>>dcba
'''
"""
다시 생각하기
def reverseString(x):
    if len(x) == 0:
        return x[-len(x)]
    else:
        return x[-1] + reverseString(x[-1:])
print(reverseString('abcd'))
"""

# for문 해답
def reverseString1(str):
    result=''
    for i in range(len(str)-1, -1, -1):
# 시작점을 매개변수 str의 길이에서 1 감소시킨 값으로 설정,
# 끝점을 -1로 설정한 이유는 공통적으로 끝 값이 0이기 때문에 끝다음인 -1로 설정.
# 증감을 -1로 설정한 이유는 인덱스가 1씩 감소하기 때문.
        result += str[i]
    return result

# 재귀함수 해답
def reverseString2(str):
    if len(str) == 1:
        return str
    else:
        return reverseString2(str[1:]) + str[0]

