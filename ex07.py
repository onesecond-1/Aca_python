print("=====if문=====")
a=10
if a>5:
     print("a의 값은 5보다 큽니다.")
print("프로그램 종료")

b=15
if b>20:
     print("20보다 큽니다.")
elif b>15:
     print("15보다 큽니다.")
elif b>10:
     print("10보다 큽니다.")
elif b>5:
     print("5보다 큽니다.")
else:
     print("5보다 작습니다.")

print("=====조건문 실습예제1=====")
'''
문제1. 하나의 정수를 입력받아서, 그 정수가 홀수라면 '(값)은 홀수입니다.' 출력하고, 짝수라면 '(값)은 짝수입니다.'를 출력하는 코드를 작성하세요.

실습결과 1
정수 입력 : 5
5는 홀수입니다.

실습결과2
정수 입력 : 10
10는 짝수입니다.
'''
num=int(input("정수입력:"))
if num%2==1:
     print(f"{num}은/는 홀수입니다.")
else:
     print(f"{num}은/는 짝수입니다.")

print("=====조건문 실습예제2=====")
'''
문제2. 하나의 정수를 입력받아서, 입력 받은 정수의 값이 2의 배수 또는 3의 배수라면 '(입력한 값)은 2의 배수 또는 3의 배수입니다.'라고 출력하고 그렇지 않으면 '(입력한 값)은 2의 배수 또는 3의 배수가 아닙니다.' 코드를 작성하세요.
'''
num=int(input("정수입력:"))
if num%2==0 or num%3==0:
     print(f"{num}은/는 2의 배수 또는 3의 배수입니다.")
else:
     print(f"{num}은/는 2의 배수 또는 3의 배수가 아닙니다.")

print("=====조건문 실습예제3=====")
'''
문제3. 하나의 정수를 입력받을건데, 그 입력값을 점수(score)로 표현한다. 
만약 점수가 90점 이상이면 "A학점", 
80점 이상 90점 미만이면 "B학점", 
70점 이상 80점 미만이면 "C학점", 
60점 이상 70점 미만이면 "D학점", 
나머지는 "F학점"을 출력하는 코드를 작성하세요.
'''
score=int(input("점수입력:"))
if score>=90:
     print("A힉점")
elif score>=80:
     print("B학점")
elif score >= 70:
     print("C학점")
elif score>=60:
     print("D학점")
else:
     print("F학점")

print("=====조건문 실습예제4=====")
'''
문제4. 하나의 문자열을 입력받고, 또 하나의 문자열을 입력받을 것이다. 두번째에서 입력하는 문자열 값이 첫번째에서 입력하는 문자열 안에 있다면, Yes출력 그렇지 않으면 No출력
'''
a=input("문자열1:")
b=input("문자열2:")
if b in a:
     print("Yes")
else:
     print("No")

print("=====while반복문=====")
while False:
     print("while 반복문의 수행문")
print("프로그램 종료")

count=0
while count!=10:
     print(f"while 반복문의 수행문 {count}")
     count+=1

print("=====while반복문 실습예제1=====")
'''
문제1. 1부터 100까지 출력되는 코드를 작성하세요.
'''
num=1
while num<=100:
     print(num)
     num+=1

print("=====while반복문 실습예제2=====")
'''
문제2. 100부터 1까지 짝수만 출력하세요.
'''
num=100
while num<=100 and num>0:
     print(num)
     num+=-2

num=100
while num>=2:
     if num%2==0:
          print(num)
          num+=-2

num=100
while num>=2:
     if num%2==1:
          num+=-2
          continue
     print(num)
     num+=-1