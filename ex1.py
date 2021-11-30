from tools import zp

time = int(input('Введите количество часов - '))
cost = int(input('Введите ставку - '))
bonus = int(input('Введите премию - '))
print(f'Заработная плата - {zp(time, cost, bonus)}')
