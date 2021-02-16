#Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#Формат ввода следующий:
#В первой строке указано целое число n — количество завершенных игр.
#После этого идет n строк, в которых записаны результаты игры в следующем формате:
#Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#Вывод программы необходимо оформить следующим образом:
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#Конкретный пример ввода-вывода приведён ниже.
#Порядок вывода команд произвольный.
#Sample Input:
#3
#Спартак;9;Зенит;10
#Локомотив;12;Зенит;3
#Спартак;8;Локомотив;15
#Sample Output:
#Спартак:2 0 0 2 0
#Зенит:2 1 0 1 3
#Локомотив:2 2 0 0 6

import sys
from collections import defaultdict

stdin = [x.split(';') for x in sys.stdin.read().split('\n')]
            
teams = defaultdict(lambda: {'Игры': 0, 'Победы': 0, 'Ничья': 0, 'Поражения': 0, 'Очки': 0})

for first_name, first_goals, second_name, second_goals in stdin[1:]:
    first_goals = int(first_goals)
    second_goals = int(second_goals)
    teams[first_name]['Игры'] += 1
    teams[second_name]['Игры'] += 1
         
    if first_goals > second_goals:
        teams[second_name]['Поражения'] += 1
        teams[first_name]['Победы'] += 1
        teams[first_name]['Очки'] += 3      
    elif first_goals < second_goals:
        teams[first_name]['Поражения'] += 1
        teams[second_name]['Победы'] += 1
        teams[second_name]['Очки'] += 3    
    else:
        teams[first_name]['Ничья'] += 1
        teams[first_name]['Очки'] += 1
        teams[second_name]['Ничья'] += 1
        teams[second_name]['Очки'] += 1

for team, stats in teams.items():
    print(f"{team}:{stats['Игры']} {stats['Победы']} {stats['Ничья']} {stats['Поражения']} {stats['Очки']}")
