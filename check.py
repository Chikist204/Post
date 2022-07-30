with open('itmo/15_03_06.txt') as file:
    f = list(map(lambda x: x.strip(), file.readlines()))
with open('itmo/15_03_04.txt') as file:
    f2 = list(map(lambda x: x.strip(), file.readlines()))
with open('itmo/27_03_04.txt') as file:
    f3 = list(map(lambda x: x.strip(), file.readlines()))
with open('itmo/24_03_02.txt') as file:
    f4 = list(map(lambda x: x.strip(), file.readlines()))

f += f2
f += f3
f += f4

with open('spgu/data_big_data') as file:
    f5 = list(map(lambda x: ''.join(''.join(x.split('-')).strip().split()), file.readlines()))
# with open('spgu/data.txt') as file:
#     f5 += list(map(lambda x: ''.join(''.join(x.split('-')).strip().split()), file.readlines()))
# with open('spgu/data_tech.txt') as file:
#     f5 += list(map(lambda x: ''.join(''.join(x.split('-')).strip().split()), file.readlines()))

k = 0
for i in f:
    if i in f5:
        k += 1
        print(i)
print(k)