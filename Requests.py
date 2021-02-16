#Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
#Первое слово в тексте последнего файла: "We".

#Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

#Все файлы располагаются в каталоге по адресу:
#https://stepic.org/media/attachments/course67/3.6.3/

#Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.



import requests


def find_a_link():
    link = 'https://stepic.org/media/attachments/course67/3.6.3/'
    ending = '699991.txt'
    while True:
        print(ending)
        needed_link = requests.get(link + ending)
        if needed_link.text.startswith('We'):
            return needed_link.text
        else:
            ending = needed_link.text.strip()
            
print(find_a_link())
