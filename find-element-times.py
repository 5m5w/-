import collections

a = [4, 2, 4, 5, 2, 3, 1, 1, 1, 1]


number_count = collections.Counter(a)

for key, value in number_count.items():
    print(f'{key}:{value}')
    
print("")
b = ['a', 'a', 'b', 'b', 'b', 'c', 'c']

cha_count = collections.Counter(b)

for key, value in cha_count.items():
    print(f'{key}:{value}')