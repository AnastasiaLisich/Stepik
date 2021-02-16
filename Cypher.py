#В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.
#В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, 
#т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
#Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, 
#на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
#и ещё одна строка, которую нужно расшифровать.
#Пусть, например, на вход программе передано:
#abcd
#*d%#
#abacabadaba
##*%*d*%
#Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
#Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
#*d*%*d*#*d*
#dacabac

import sys
from collections import defaultdict

stdin = [x for x in sys.stdin.read().split('\n')]
cypher_dict = {}
decypher_dict = {}
symbols = stdin[0]
cypher = stdin[1]

for i, elem in enumerate(symbols):
    cypher_dict[elem] = cypher[i]
    
for key, value in cypher_dict.items():
    decypher_dict[value] = key

table_cypher = str.maketrans(cypher_dict)
text = stdin[2]
code_cypher = text.translate(table_cypher)

table_decypher = str.maketrans(decypher_dict)
text = stdin[3]
code_decypher = text.translate(table_decypher)



print(code_cypher)
print(code_decypher)
