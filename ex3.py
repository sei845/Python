arg1 = int(input('Введите первое число - '))
arg2 = int(input('Введите второе число - '))
arg3 = int(input('Введите третье число - '))

my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)

print(f'Сумма наимольших элементов - ', my_func(arg1, arg2, arg3))
