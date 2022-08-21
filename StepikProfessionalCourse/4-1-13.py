import sys

studenslen = [*map(int, sys.stdin.readlines())]
print(f'Рост самого низкого ученика: {min(studenslen)}\n'
      f'Рост самого высокого ученика: {max(studenslen)}\n'
      f'Средний рост: {sum(studenslen)/len(studenslen)}'
      if len(studenslen) > 0 else 'нет учеников')