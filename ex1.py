# В силу сдачи ДЗ после её разбора попробовал реализовать
# функции в некоторые задачи, чтобы не повторяться

my_list = [10, 5.5, None, 'String', True, {1: 'one', 2: 'two'},
           [3, 4], {5, 6}]


def my_type(i):
    for i in range(len(my_list)):
        print(f"{my_list[i]} {type(my_list[i])}")
    return


my_type(my_list)