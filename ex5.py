profit = float(input("Введите выручку фирмы: "))
izd = float(input("Введите издержки фирмы: "))
if profit > izd:
    print(f"Фирма работает с прибылью. Рентабельность:  {((profit-izd) / profit)*100:.2f} %")
    workers = int(input("Введите количество сотрудников: "))
    print("Прибыль на каждого сторудника сотавила: %.2f" % (profit / workers))
elif profit == izd:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")