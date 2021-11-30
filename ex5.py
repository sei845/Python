from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
my_new_list = reduce(lambda el1, el2: el1 * el2, my_list)
print(f'Список четных значений: {my_list}')
print(f'Результат перемножения всех элементов списка {my_new_list}')
