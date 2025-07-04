"""
pip install pandas
"""

import pandas

"""
dictionary : 
무조건 {} 나오고
안에 {'키'} 나오고
{'키': 값} 이런형태를 가지고 있다
값은 무조건 list여야 한다
각 리스트 갯수도 서로 같아야한다

이 자료구조 법칙을 어기면 DataFrame() 함수는 작동을 안한다
"""
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'data2': [3, 7, 2],
}

"""
dictionary를 pandas로 읽는건, 무조건 
pandas.DataFrame(mydataset)
이 코드로 정해져있다
"""
myvar = pandas.DataFrame(mydataset)

#print(myvar)



import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

"""
DataFrame or Series을 통해서 dictionary의 값을 table 형태로 보기
column 은 집값
row 의 이름은 년도

"""

data = {
  "집값": [50, 40, 45,55]
}

df = pd.DataFrame(data, index = [2025, 2024, 2023,2022])


df = pd.read_csv('test1.csv')

print(df) 