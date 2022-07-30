import pandas as pd

with open('spgu/data_big_data') as file:
    f = file.readlines()

# spisok = [
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_3bffd628-b6f7-479f-8386-ebba3f2ab5c1.html', #1 Программирование и информационные технологии
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_2df3cab7-781a-4467-be96-3302b6f105ae.html', #2 Прикладная математика, фундаментальная информатика и программирование
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_8ea405e1-7f6e-4ff7-b0bd-fc9d2647bb54.html', #3 Математика
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_2257c623-1e5e-4c86-b0af-655de0a99871.html', #4 Прикладная математика, программирование и искусственный интеллект
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_071a53e5-c6b0-4134-a89f-793db1c177d9.html', #5 Современное программирование
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_846c2a25-562d-4005-9a39-a54804b939e7.html', #6 Механика и математическое моделирование
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_0aa95bd2-8183-4273-a61f-88fdab9f9d16.html', #7 Фундаментальная математика
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_b9167a2a-6eae-4b3b-8efd-19f0360b5214.html', #8 Фундаментальная механика
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_68acc7a9-eac6-4726-b4df-ade7888e212b.html', #9 Математика и компьютерные науки
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_5280d407-3a61-43c8-84a8-48818ec97282.html', #10 Науки о данных
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_c91f57a1-c31a-427a-8f57-e41bdb877a80.html', #11 Технологии программирования
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_68eeb71c-c4eb-4278-9683-ef633e2ed81d.html', #12 Картография и геоинформатика
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_6768f77a-da13-491f-b02f-665272bc4376.html', #13 Гидрометеорология
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_c3e7f0d7-b891-4fb4-aa80-ca909a53b74b.html', #14 Прикладная информатика в области искусств и гуманитарных наук
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_73b489e3-e98f-4193-bfc7-160a9ded4532.html', #15 Программная инженерия
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_aa717992-918e-4f59-8860-ef91c5d77685.html', #16 Нефтегазовое дело
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_515246aa-c08d-4e23-91c4-9d667e957f37.html', #17 Кадастр недвижимости: оценка и информационное обеспечение
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_d0c2b4ab-5af1-476d-ad5b-8795341a90c0.html', #18 Экономико-математические методы
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_e238a2bf-c589-450b-af32-dd0a1b36302a.html', #19 Бизнес-информатика
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_5897ca44-cb74-47c0-b701-b934c8576b5f.html', #20 Социологические исследования в цифровом обществе
#     'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_59d4e60e-1448-40fd-8cbd-74aaab615c32.html' #21 Прикладная, компьютерная и математическая лингвистика (английский язык)
# ]
#
# used = []
# ans = 0
# for k, i in enumerate(spisok):
#     s = i
#     cnt = 0
#     data = []
#     calls_df, = pd.read_html(s, header=0)
#     d1 = calls_df['П']
#     d2 = calls_df['СНИЛС/Уникальный код поступающего']
#     d3 = calls_df['Σ общ']
#     d4 = calls_df['Согласие на зачисление']
#     d5 = calls_df['№ п/п']
#     for i in d2:
#         data.append(i)
#
#     for j, i in enumerate(f):
#         s1 = i.strip()
#         if s1 not in used and s1 in data and d1[j] < 3 and d5[j] <= 100:
#             cnt += 1
#             used.append(s1)
#     ans += cnt
#     print(k + 1, cnt)
# print()
# print(ans)
s = 'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_2df3cab7-781a-4467-be96-3302b6f105ae.html'
calls_df, = pd.read_html(s, header=0)
d1 = calls_df['П']
d2 = calls_df['СНИЛС/Уникальный код поступающего']
d3 = calls_df['Σ общ']
d4 = calls_df['Согласие на зачисление']


k = 0
for i in range(len(calls_df)):
    if d3[i] == 'nan' or d3[i] // 100 >= 272:
        if d1[i] <= 1:
            k += 1
            print(d2[i], d4[i])
        # print(d1[i], d2[i], d3[i] / 100)
print(k)
# k = 0
# for i in f:
#     s1 = i.strip()
#     if s1 in cur_data:
#         k += 1
# print(k)

# № п/п
# СНИЛС/Уникальный код поступающего
# Тип конкурса
# П
# Σ общ
# Σ ЕГЭ
# ВИ 1
# ВИ 2
# ВИ 3
# Σ ИД
# Согласие на зачисление
# Индивидуальные достижения
# Примечания
#
# for i in calls_df:
#     print(i)