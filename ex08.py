print("=====for반복문=====")

num=0
while num<=9:
        num+=1
        print(num)
num=1
while num<=10:
    print(num)
    num+=1

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
for i in "1,2,3,4,5,6,7,8,9,10":
    print(i, end = "/")
    #문자열은 요소 하나하나가 값으로 취급, 1 , 2 , 1 0 다 각각의 값임.

num=1
while num<=100:
    print(num)
    num+=1

for i in (1, 101, 1):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(5,105,5):
    print(i)

for i in range(100,0,-1):
    if i % 5 == 0:
        print(i)

num=1
while num<=100:
    num+=1
    if num % 5==0:
        print(num)

# **다시 생각해보기**
count = 0
for i in range(1,101):
    if i%2==0 or i%3==0:
        count +=1
print("2의 배수 또는 3의 배수의 개수:%d" %(count))

sum = 0
for i in range(1,101):
    sum+=i
print(sum)

"""
**다시 생각해보기**
n=input("정수 입력:")
for i in range(1,n+1):
    if n%i>=0:
        print()
"""

num=int(input("입력:"))
print("약수:",end="")
for i in range(1,num+1):
    if num%i==0:
        print(i,end="")

print("=====기타제어문=====")
for i in range(1,101):
    if i == 50:
        break
    print(i)

for i in range(1,101):
    if i % 2 == 0:
        continue
    print(i)

'''
num=1
while num <= 10:
    if num % 2 == 0:
        continue
    print(i)
    num+=1
while은 수행문에서 값 변화가 없이 continue하면 무한반복된다. !!주의할것!!
'''


