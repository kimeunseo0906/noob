"""
for i in range(3):
    print(f"{i}")

i = 0
while i<3:
    print(f"{i}")
    i=i+1
    pass
"""

"""
for a in range(2,10):
    for b in range(1,10):
      print(f"{a} x {b} : {a*b}")
    print()
"""

"""
numbers=[43,1325,521,2314,32,532,678,9,3,2]
for i in range(len(numbers)): 
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for n in numbers:
    print(n)

리스트 갯수 세기 > 전체 정렬을 몇번 반복하는지 결정 > 현재 리스트 개수 10개
인접한 숫자 비교횟수. 점점 줄어든다. > 
-1하는 이유는 인덱스가 j+1이기 때문이고, 똑같은 연산을 반복하지 않기위해 i를 뺀다.
if문을 사용해서 앞 숫자가 뒤 숫자보다 크면 뒤로 자리를 바꾼다.

"""

"""
def print_hello():
    print(f"hello")
    
print_hello()
"""

def mod(a,b):
    return a%b

print(mod(1,2))
