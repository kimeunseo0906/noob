"""
for i in range(99):
    if i==20:
        break
    print(f"forloop가 돌아요 : i={i}")

for i in range (10):
    if 1%2!=0:
        continue
    print(f"i:{i})
    pass
    
def fsum(a):
    if a<=1:
        return a
    return a+fsum(a-1)10

tsum=fsum(5)
print(tsum)

typing=input("f(숫자를 입력하세요):")
num=int(typing)
if num % 2 != 0:
    print(f"{num} : 이 숫자는 홀수입니다")
elif num % 2 == 0:
    print(f"{num} : 이 숫자는 짝수입니다")


typing=int(input(f"숫자를입력하세요 : "))
if typing < 2 :
    print(f"{typing}은 소수가 아닙니다")
else :
    for x in range (2, typing):
        if typing % x == 0:
            print(f"{typing}은 소수가 아닙니다")
            break
        else:
            print(f"{typing}은 소수입니다")


def fPrinmNum(a):
    bPrimeNum=True
    for i in range(2,a):
        bPrimeNum=False
        break
    return bPrimeNum
num1=int(input("숫자를입력하세요"))
if typing % x == 0:
            print(f"{typing}은 소수가 아닙니다")
else:
            print(f"{typing}은 소수입니다")

mytype="" 
mytype=input("수학수식을 넣어주세요.")
result=eval(mytype)
print(f"{mytype} : {result}")
    
"""
from random import shuffle  
list1=[]
for i in range(1,46):
    list1.append(i)
shuffle(list1)
print(f"추첨번호:{list1[0:6]}")

"""
모듈 설정
리스트 설정
폴 루프 설정 for i in range (숫자,숫자 (a~b까지)) <<< a부터 b번까지 반복함
    리스트.append(i)
셔플(리스트) <<< 랜덤으로 리스트에서 섞는다
프린트하기(f"내용:{리스트이름[a:b]})<<a번째부터 b번쨰까지 나타내기 
"""


from random import shuffle
list2=[]
for i in range(1,100):
    list2.append(i)
shuffle(list2)
print(f"추첨번호 : {list2[0:1]}")