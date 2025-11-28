print("=====이중루프=====")
for i in [10,20,30]:
    for j in ['A','B','C']:
        print(i,j)

'''
print("=====디지털 시계=====")
for i in range(24):
    for j in range(60):
        for k in range(60):
            print("%02d : %02d : %02d" %(i,j,k))
'''

print("=====구구단=====")
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end="\t") #단이 넘어가지 않으면 줄을 바꾸지 않고 열을 맞추기 위함.
    print() #단이 넘어가면 줄을 바꾸기 위함.

print("=====구구단 열변경=====")
for i in range(1,10):
    for j in range(2,10):
        print(f"{j}*{i}={i*j}", end="\t")
    print()

print("=====별 찍기1=====")
'''
*
**
***
****
*****
'''

for i in range(6):
    print("*"*i) # C, java에서는 불가능

for i in range(5):
    for j in range(i+1): #별의 갯수에 변동이 있기 때문에
        print("*",end="")
    print()

print("=====별 찍기2=====")
'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
'''
1
12
123
1234
12345
'''
# 다시 생각해보기
for i in range(5):
    for j in range(i+1):
        print(i+1, end="")
    print()

for i in range(5):
    for j in range(i + 1):
        print(i+1, end="")
        i+=1
    print()

print("=====별 찍기3=====")
'''
    *
   **
  ***
 ****
*****
'''
# 다시 생각해보기
for i in range(5):
    for j in range(i):
        print(end="")
    print()

for i in range(5):
    for j in range(4-i):
        print(' ', end="")
    for k in range(i+1):
        print("*", end="")
    print()

print("=====별 찍기4=====")
'''
  *
 ***
*****
'''
for i in range(3):
    for j in range(2-i):
        print(' ', end="")
    for k in range(i*2+1):
        print("*", end="")
    print()

print("=====별 찍기5=====")
'''
*****
 ***
  *
'''
for i in range(3):
    for j in range(i):
        print(' ', end="")
    for k in range(5-i*2):
        print("*", end="")
    print()

