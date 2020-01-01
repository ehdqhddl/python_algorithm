import sys

input_list = list(sys.stdin.readline().split())

asc_num = 1
desc_num = 8

for x in input_list:
    if int(x) == asc_num:
        asc_num += 1

for x in input_list:
    if int(x) == desc_num:
        desc_num -= 1

if desc_num == 0:
    print('descending')
elif asc_num == 9:
    print('ascending')
else:
    print('mixed')
