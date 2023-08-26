# Глобальные переменные, переменные доступные в любой области программы
# Локальные переменные - переменные объявленные в блоке программы

def nFunk(x):
    for i in range(x):
        global a
        a = 7
        n = i + 1
        print(n)

nFunk(5)

name = 'Anna'

def print_1():
    name = 'Jack'
    print('Первая функция '+ name)
    def print_2():
        print('Вторая функция ' + name)
    print_2()

print_1()




