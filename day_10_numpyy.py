import numpy as np

sentences=[
    "나는 밥을 먹었다",
    "너는 밥을 안먹었다",
    "나는 학교에 갔다"
]

word_to_index={}
index=0

for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word not in word_to_index:
            word_to_index[word]=index
            index+=1

print(f"단어사전:{word_to_index}")

vectorized_sentenes=[]

for sentnece in sentences:
    words = sentence.split()
    vector = [word_to_index[word]for word in words]
    vectorized_sentenes.append(vector)
print(f"숫자 벡터화:",vectorized_sentenes)

max_len = max(len(v)for v in vectorized_sentenes)
print(f"max_len:{max_len}")

padded_array=np.zeros((len(sentences),max_len),dtype=int)
print(f"padded_array.shape:{padded_array.shape}")

for i,vector in enumerate(vectorized_sentenes):
    padded_array[i,:len(vector)]=vector

print(f"numpy sentence:")
print(padded_array)

