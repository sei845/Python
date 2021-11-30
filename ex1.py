def div(arg_1, arg_2):

    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        res = arg_1 / arg_2
    except ValueError:
        return 'Неверный ввод'
    except ZeroDivisionError:
        return "Деление на ноль"

    return round(res, 4)


print(div(input('Введите первое число - '), input('Введите второе число - ')))
