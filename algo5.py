# Algo 5
# 해시테이블 이론 및 실습

hash_table = list([i for i in range(10)])

print(hash_table)


def hash_func(key):
    return key % 5


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() : 문자의 아스키코드를 리턴
print(ord(data1[0]), ord(data2), ord(data3))


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func()
    hash_table[hash_address] = value


storage_data('Andy', '010-1234-5678')
storage_data('Dave', '010-2222-2222')
storage_data('Trump', '010-3333-3333')


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func()
    return hash_table[hash_address]
