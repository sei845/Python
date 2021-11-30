my_list = [1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 12, 13, 13, 14, 14, 15]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список: ', my_list)
print(f'Измененный список: ', my_new_list)

