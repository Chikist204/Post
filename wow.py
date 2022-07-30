import pandas as pd

with open('itmo/full_27-03-04.txt') as file:
    f = list(map(lambda x: x.split(), file.readlines()))
s = 'https://cabinet.spbu.ru/Lists/1k_EntryLists/index_full_list.html'
calls_df, = pd.read_html(s, header=0)
d2 = calls_df['СНИЛС/Уникальный код поступающего']
check = []
for i in f:
    s = i[1]
    check.append(s[:3] + '-' + s[3:6] + '-' + s[6:9] + ' ' + s[9:])
k = 0
for i in d2:
    if i in check:
        print(i)
        k += 1
print(k)