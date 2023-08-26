
def calc(a, b, type):
    if type == '+':
        print(a + b)
    elif type == '-':
        print(a - b)
    elif type == '*':
        print(a * b)
    elif type == '/':
        print(a / b)
    else:
        print('Введите один из параметров type')

calc(10, 10, '*')

def calc(a, b, type):
    if type == '+':
        print(a + b)
    elif type == '-':
        print(a - b)
    elif type == '*':
        print(a * b)
    elif type == '/':
        try:
            print(a / b)
        except ZeroDivisionError:
            print('Ошибка! На ноль делить нельзя!')
        else:
            print('Введите один из параметров type')

calc(10, 0, '/')

