def triale(a, b):
    s = a * b
    print(s)

triale(3, 5)

def newFunk(a, b, type=None):
    if type is None:
        s = a * b
        p = (a + b) * 2
        print(f'Площадь прямоугольника равна {s}, периметр равен {p}.')
    elif type == 's':
        s = a * b
        print(f'Площадь прямоугольника равна {s}.')
        print(s)
    elif type == 'p':
        p = (a+b)*2
        print(f'Периметр прямоугольника равен {p}.')

newFunk(10, 10, None)
newFunk(10, 10, 's')
newFunk(10, 10, 'p')


def max_in_list(list):
    sort_list = sorted(list)
    max_num = sort_list[-1]
    print(f'Максимальное число в списке {max_num}')


new_list = [9, 1, 7, 3, 5, 6, 4]
max_in_list(new_list)








