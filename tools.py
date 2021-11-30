def zp(time, cost, bonus):
    return (time * cost) + bonus


def iter_num(start):
    from itertools import count

    i = 0
    for el in count(start):
        i += 1
        if i == 20:
            break
        print(el)


def iter_list():
    from itertools import cycle

    my_list = ['Ехали', 'медведи', 'на', 'велосипеде']
    i = 0
    for el in cycle(my_list):
        i += 1
        if i == 20:
            break
        print(el)
