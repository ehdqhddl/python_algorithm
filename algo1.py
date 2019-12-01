# Algo 1
# 배열의 활용

# 1차원 배열 구현

data = [1,2,3,4,5]
print(data)
print(data[0])

# 2차원 배열 구현

data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)
print(data[0])
print(data[0][0])
print(data[0][1])
print(data[0][2])

print(data[2][-1::-1])

dataset = ['Abc','bbAd','we','SDFFbBbrA','aaSaA','eweA'] # A : 5번

cnt = 0
for lst in dataset:
    cnt += lst.count('A')
print(cnt)

for lst in dataset:
    for index in range(len(lst)):
        print(lst[index])
