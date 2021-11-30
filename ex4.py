def my_pow_fun(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Ошибка! х должен быть больше нуля, а у должен быть меньше 0'
        else:
            result =1
            for _ in range(abs(y)):
                result *= 1 / x
            return f'Результат возведения х в степень у: {round(result,6)}'
    except ValueError:
        return 'Программа работает только с числами'


a = input('Введите х - ')
b = input('Введите у - ')
print(my_pow_fun(a, b))

