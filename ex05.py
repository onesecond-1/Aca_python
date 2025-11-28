a=[10,20,30,40]
print(a[1])
print(a[-3])

#리스트 슬라이싱
print(a[1:3:2])

b=[1,2,3,"가나다",4,5,6]
print(b[3])
print(b[3][1])

c=[10,20,"ABCD", ["EFGH",30,40],"JKL",50]
#c리스트를 인덱싱하여 `A` 출력
print(c[2][0])
print(c[-4][-4])
#c리스트를 인덱싱하여 `D` 출력
print(c[2][3])
#c리스트를 인덱싱하여 `G` 출력
print(c[3][0][2])
print(c[3][0][1:3]) #리스트 속 리스트의 슬라이싱
print(c[-3][-3][-2])
#c리스트를 인덱싱하여 30 출력
print(c[3][1])
#c리스트를 인덱싱하여 `k` 출력
print(c[4][1])

#리스트 값 추가
a=[10,20,30]
a.append(40)
print(a)
a.insert( 1, 50) # 자동으로 입력됨.
print(a)

a.remove(50)
print(a)

a.append(100)
a.append(60)
a.append(100)
a.append(70)
print(a)

a.remove(100)
print(a)
#앞의 값부터 삭제한다.

temp1=a.pop(1)
print(a)
print("pop한 값:",temp1)

temp2=a.pop()
print(a)
print("pop한 값: ",temp2)
#반환하는 함수를 결과값이 있는 함수라고 하고, 반환하지 않는 함수는 결과값이 없는 함수라고 한다.

d=[5,1,3,4,2]
d.sort()
print(d)
d.sort(reverse=True)
print(d)

d.clear()
print(d)

# del d 코드는 del연산자를 활용하여 d변수 자체를 삭제시킨다.

e=["사과","바나나","배"]
print("사과" in e)
print("수박" in e)
print("수박" not in e)

temp=e.count("사과")
print(temp)

z=[1,2,3,'가','나','다']
z.reverse()
print(z)

a=[1,2,3]
b=[10,20,30]
print(a+b)
print(a*3)

a=(1,2,3)
print(a,type(a))

b=('ab','cd')
print(a+b)
print(b*3)

c=(4,)
print(c)

d=(1,2,3,[4,5,6])
d[3][2]=7
print(d) #튜플에 리스트가 들어갈 수 있고 그 리스트는 수정, 추가, 삭제가 가능하다.

a=[1,1,1,1,2,2,2,2,3,3,3,3,3]
aSet=set(a) #리스트를 집합으로 변환하고 aSet변수로 저장.
print(aSet)