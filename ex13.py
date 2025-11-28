print("=====chr()=====")
print(chr(65), type(chr(65)))

print("=====eval()=====")
print("100+200")
print(eval("100+200"))

print("=====abs()=====")
print(abs(-178))
print(abs(8))

print("=====divmod()=====")
print(10//3)
print(10%3)
print(divmod(10,3))

print("=====pow()=====")
print(10**2)
print(pow(10,2))

print("=====round()=====")
print(round(1.5))
print(round(3.14))
print(round(3.14, 1))

print("=====enumerate()=====")
temp= [1,2,3]
for i in enumerate(temp):
    print(i, type(i))

print("=====range()=====")
print(range(1,11,2), type(range(1,11,2)))
print(list(range(1,11,2)))
print(set(range(1,11,2)))

print("=====len()=====")
print(len("hello"))

print("=====sort()/sorted()=====")
a=[5,1,3,4,2]
print(a.sort())
print(sorted(a))

print(sorted(a, reverse=True))

print("=====zip()=====")
name=["A", "B", "C", "D", "E"]
score=[88,92,76,41]
height=[150.2,152.7,161.2,154.3]
for i in zip(name, score, height):
    print(i, type(i))
# 이게 무슨 의미?????
for i, j, k in zip(name, score, height):
    print(i,j,k)

print("=====내장함수 실습1=====")
'''
문제. day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]라는 
리스트가 존재하고, 1월~12월의 월과 마지막일을 같이 출력하는 코드르 작성하세요.
(단, enumerate함수를 사용하여 1번, zip함수를 사용하여 1번 총 2개의 코드를 작성하세요.)

실행결과
1월: 31일
2월: 28일
3월: 31일
4월: 30일
5월: 31일
6월: 30일
7월: 31일
8월: 31일
9월: 30일
10월: 31일
11월: 30일
12월: 31일
'''
day=[31,28,31,30,31,30,31,31,30,31,30,31]
for month, day in enumerate(day):
    print(f"{month+1}월 : {day}일")

day=[31,28,31,30,31,30,31,31,30,31,30,31]
month=[1,2,3,4,5,6,7,8,9,10,11,12]
month=list(range(1,13,1))
for i, j in zip(month, day):
    print(i, j)

print("=====.format()=====")
print("10자리 폭 왼쪽 정렬 : '{:<10d}'".format(123))
# '123-------'