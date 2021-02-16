#За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
import sys
from collections import defaultdict

stdin = [x.split(';') for x in sys.stdin.read().split('\n')]
            
teams = defaultdict(lambda: {'Игры': 0, 'Победы': 0, 'Ничья': 0, 'Поражения': 0, 'Очки': 0})

for first_name, first_goals, second_name, second_goals in stdin[1:]:
    first_goals = int(first_goals)
    second_goals = int(second_goals)
    
#посчитать кол-во игр всего у каждой команды и добавить в словарь по значению:  
    teams[first_name]['Игры'] += 1
    teams[second_name]['Игры'] += 1
    
#посчитать кол-во побед, поражений и ничьих, очков и добавить в словарь в значение:      
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
