my_list = [31, 25, 7, 10, 8, 15, 19, 17, 105, 65, 43, 98]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Измененный список: {my_new_list}')