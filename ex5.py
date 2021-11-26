my_list = [9, 9, 8, 7, 6, 6, 5, 2, 1]
print(my_list)
new_number = int(input('Введите новый элемент рейтинга: '))
i=0

for n in my_list:
    if new_number <= n:
        i += 1

    elif new_number > n:
        break

my_list.insert(i, float(new_number))
print(my_list)
