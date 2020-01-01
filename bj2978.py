import sys

n, m = sys.stdin.readline().split()

n = int(n)
m = int(m)

input_list = list(sys.stdin.readline().split())

max_num = 0

for i in input_list[:n-2]:
    for j in input_list[input_list.index(i)+1:n-1]:
        for k in input_list[input_list.index(j)+1:n]:
            if (max_num < int(i) + int(j) + int(k)) and (m >= int(i) + int(j) + int(k)):
                max_num = int(i) + int(j) + int(k)

print(max_num)


