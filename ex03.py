print("=====문자열 연산=====")
a= "사과"
b= "바나나"
z= a+b
print(z)
print(a*5)
# 문자열을 더하거나 곱하여서 연산을 완료했다면, 하나의 문자열로 만들어지는게 포인트이다.
print("=====포맷코드를 활용한 포맷팅=====")
name="홍길동"
age=30
print("제 이름은 %s이고, 나이는 %d살 입니다." %(name, age))
print("제 이름은 %d이고, 나이는 %s살 입니다." %(age, age)) #인터프리터여서 가능한 코딩임. 자동전환된거임.
print("제 이름은 %s이고, 나이는 %d살 입니다." %("이름", age))
temp=35.2
print("오늘 최고기온은 %f도 입니다." %(temp))
temp=35.2234234234
print("오늘 최고기온은 %.3f도 입니다." %(temp))
# %f 사용시 %와 포맷코드 f 사이에 .n가 있다면 소숫점 n자리까지 나타낸다.
print("=====f-string()함수를 활용한 포맷팅=====")
print(f"제 이름은 {name}이고, 나이는 {age}살입니다.")
print(f"오늘 최고 기온은 {temp}도 입니다.")
print(f"오늘 최고 기온은 {temp : .3f}도 입니다.")
# f-string()함수에서 소숫점 자리수 옵션은 중괄호 안에서 소수값의 자릿수를 콜론 뒤에 .nf로 n은 정수값으로 표현한다.
print("=====문자열 포맷팅 실습=====")
'''
문제: 여러분들의 이름과 나이, 키를 name과 age, key라는 변수에 저장하고, 포맷팅을 통해서 아래와 같이 출력하는 코드를 작성하라
결과: 제 이름은 홍길동이고, 나이는 30살, 키는 173.3cm입니다.
'''
name="홍길동"
age=30
key=173.3
print(f"제 이름은 {name}이고, 나이는 {age}살, 키는 {key}cm입니다.")
print("제 이름은 %s이고, 나이는 %d살, 키는 %.1fcm입니다." %(name, age, key))

a= "123"
print(a,type(a))
print(int(a), type(int(a)))
#위의 두 코드와 같이 문자열 값이 정수였다면, 그 문자열 값을 정수로 형 변환이 가능하다.
# 단, 정수로 표현된 값일때만 정수로 형 변환이 가능하다.
b= "123.4"
print(b, type(b))
print(float(b), type(b))
c=567
print(c,type(c))
print(str(c), type(str(c)))
d=567.8
print(d,type(d))
print(str(d), type(str(d)))

name = input("이름 입력:")
print(f"이름:{name}")
print("이름:"+name) #실행창에서 입력하면 됨.

age=int(input("나이 입력:"))
print(f"나이: {age}")
print("나이:", age) #type이 다른 자료형이 되었기에 + 사용불가.

height=float(input("키 입력:"))
print(f"키:{height:.1f}")
print("키:", height)

print("=====입력을 통한 실습=====")
'''
문제: 3개의 정수를 입력받을 것이고, 3개의 정수의 합과 3개의 정수의 곱을 각각 출력하는 코드를 작성하라

결과:
입력1: 2
입력2: 3
입력3: 4
합: 9
곱: 24
'''
a1=int(input("입력1:"))
a2=int(input("입력2:"))
a3=int(input("입력3:"))
print(f"합:{a1+a2+a3}")
print(f"곱:{a1*a2*a3}")

x=int(input("입력1:"))
y=int(input("입력2:"))
z=int(input("입력3:"))
math_sum=x+y+z
math_mul=x*y*z
print(f"합:{math_sum}")
print(f"곱:{a1*a2*a3}")

print("=====총정리 실습=====")
'''
문제: 본인의 이름과 나이, 키를 입력받아서 저장하고, 아래와 같이 출력하게끔 포멧팅을 통해서 출력하라

결과:
이름: 김지훈
나이: 29
키: 173.35
제 이름은 김지훈이고, 나이는 29살이며, 키는 173.3cm입니다.
'''
name=input("이름:")
age=int(input("나이:"))
height=float(input("키:.1f"))
print(f"제 이름은 {name}이고, 나이는 {age}이며, 키는 {height}cm입니다.")

