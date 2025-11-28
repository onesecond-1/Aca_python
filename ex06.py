print("=====관계연산자=====")
a=10
b=5
print(a<b)
print(a==b)

print("=====논리연산자=====")
a=5>3
b=10<7
print(a)
print(b)
print(a and b)

print("=====딕셔너리 자료형=====")
temp = {"김철수" : 90, "홍길동":70, "신짱구":[10,20,30]}
print(temp,type(temp))
print(temp["김철수"])
print(temp["신짱구"],type("신짱구"))
print(temp["신짱구"][1])
print(temp.get("홍길동"))
print(list(temp.keys()))
print((list(temp.values())))
print((list(temp.items())))

print("=====삼항연산자=====")
num1=int(input("정수1입력:"))
num2=int(input("정수2입력:"))
print("num1이 더 큽니다." if num1>num2 else "num2이 더 큽니다.")

print("=====조건문=====")
if not True:
    print("조건문의 수행문1")
    print("조건문의 수행문2")
#위의 코드에서 print("조건문의 수행문") 앞에 공백이 존재하는데, 이 공백을 들여쓰기라고 한다. 들여쓰기는 파이썬에서 조건문과 반복문의 수행문의 처음과 끝을 알 수 있게 한다.

if True:
    print("조건문의 수행문1")
print("조건문의 수행문2")


"""
 if True:
    print("가나다")
print("ABC") #조건문의 진행을 끊어버린 형태. 밑에도 오류남.
    print(1234)
"""

num=int(input("정수 입력:"))
if num > 10:
    print("입력한 값이 10보다 큽니다")
print("프로그램 종료")
