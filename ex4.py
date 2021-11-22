n = int(input("Введите целое положительное число: "))
max = n % 10
while n > 0:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    else:
        print("Максимальная цифра в числе: ", max)
        break