from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://abit.itmo.ru/rating/bachelor/budget/16021'
options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
browser = webdriver.Chrome(options=options)

browser.get(url)
generated_html = browser.page_source

soup = BeautifulSoup(generated_html, 'lxml')
items = soup.find_all('div', {"class": "RatingPage_table__fMs6t"})

time.sleep(5)

prioritet = ''
cnt = 0
summ = ''
sogl_zach = ''
sogl_zach_cnt = 0
original = ''
original_cnt = 0
snilss = []

write_data = []
index = 0
for i in items[1:]:
    item = i.find_all('a')
    for j in item:
        item2 = j.find_all('div', {"class": "RatingPage_table__info__2gWiU"})
        # time.sleep(1)
        for x in j.find_all('div', {"class": "RatingPage_table__name__3LfzS"}):
            snilss.append(x.find_all('p')[0].text.split()[1][1:])

        data = []
        for x in item2:
            data.append(x.find_all('div'))
        # [0][0] - [0]
        # [1] - [1],
        data_check = []
        for x in data:
            for y in x:
                for z in y.find_all('p'):
                    data_check.append(z)
        prioritet = data_check[0].find('span').text
        time.sleep(0.005)
        sogl_zach = data_check[5].find('span').text
        time.sleep(0.005)
        original = data_check[-1].find('span').text
        if len(data_check) == 10:
            summ = data_check[7].find('span').text
        else:
            summ = 0
        if int(prioritet) <= 3 and int(summ) >= 272:
            cnt += 1
            write_data.append([prioritet, snilss[index], summ, sogl_zach])
        if sogl_zach == 'да':
            sogl_zach_cnt += 1
        if original == 'да':
            original_cnt += 1
        index += 1
        print(prioritet)
        print(summ)
        print(sogl_zach)
        print(original)
        print()

print(cnt)
print(write_data)
time.sleep(1)
print(snilss)
# with open('itmo/full_24-03-02.txt', 'w') as file:
#     for i in write_data:
#         print(' '.join(i), file=file)
browser.quit()


# 18 / 15
# 27 / 17
# 79 / 68
# 17 / 20


# 1 - 4, 2 - 4, 3 - 6 --- 14 / 15
# 1 - 6, 2 - 12, 3 - 9 --- 27 / 17
# 1 - 30, 2 - 11, 3 - 38 --- 79 / 68
# 1 - 4, 2 - 5, 3 - 9 --- 18 / 20