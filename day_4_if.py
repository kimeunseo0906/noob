if(True):
    print(f"조건문이 true라서 여기가 실행 됐네요")
    pass
if False:
    print(f"조건문이 false라서 여기는 실행 안됐네요")

a= "      "
if(a):
    print(f"a : {a}")

x=10
x="문자열"
x=[1,2,3]
x={"key1":"엘렐레"}
x=0.0000001
if(x):
    print(f"x:{x}")

if list:
    print(f"조건문 실행")
if "문자열":
    print(f"조건문 실행")
if 1:
    print(f"조건문 실행")

def dummyfunc():
    return True

if dummyfunc():
    print(f"함수도 조건문 수식으로 쓸수있어요 {dummyfunc()}")
    pass

a=3
b=2
if a>b:
    pass
if a==b:
    pass
if a<b:
    pass

a=True
b=False
c=False
if b:
    print(f"if문")
    pass
elif c:
    print(f"elif문")
    pass
else :
    print(f"else문")
    pass

if a:
    pass
elif a:
    pass
"""
my_typing=input("숫자를 입력하세요")
print(f"my_typing: {my_typing}")
print(f"my_typing type: {type(my_typing)}")
my_number=int(my_typing)

"""


my_typing=0
#my_typing=input("아무 숫자나 입력하세요")
print(f"my_typing: {my_typing}")
my_number=int(my_typing)
if my_number % 2 == 0  :
     print(f"이 숫자는 짝수입니다")
else :
     print(f"이 숫자는 홀수입니다")


#my_typing=int(input("아무 숫자나 입력하세요"))

"""
rade=int(input("점수를 입력해주세요"))
if grade >= 90 :
    print(f"A")
elif grade >= 80 :
    print(f"B")
elif grade >= 70 :
    print(f"C")
elif grade > 60 :
    print(f"D")
else : 
    print (f"F")


    cm=int(input("키를 입력해주세요"))
kg=int(input("몸무게를 입력해주세요"))
m=cm/100
bmi=kg/(m**2)
if bmi < 18.5 :
    print(f"저체중입니다")
if 18.5<bmi<23:
    print(f"정상입니다")
if 23<=bmi<25:
    print(f"과체중입니다")
if 25<=bmi :
    print(f"비만입니다")
"""

person1={"이름": "김은서" , "비밀번호" : "1234"}
password=input("비밀번호")

if password == person1['비밀번호']:
    print("로그인 성공")
else :
    print("비밀번호가 틀렸습니다")