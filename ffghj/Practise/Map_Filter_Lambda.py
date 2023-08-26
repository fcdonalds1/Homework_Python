#1. Функция 'map' применяет другую функцию к каждому элементу последовательности

    #def map(function, iterable):
        #for i in iterable:
            #yield function(i)

# 2. Функция 'Filter' применяет на другую функцию с проверки результата типа 'bool'
# к каждому элементу последовательности отфильтровывая значение с True

# 3. 'Lambda' - анонимная функция без объявления, служит для сокращения записи
# простых функций, злоупотреблять не стоит.


# Первый аргумент - некая функция - обработчик, второй - итерируемый объект.
# Итерабельная последовательность - спискт, кортежи, словари, функции 'Range', строки и т. д.
# то, что можно обойти в цикле 'for'.

def sq(x):
    return x**2

a = [-2, -1, 5, 7, 3]

b = map(sq, a)
print(b)

c = list(map(sq, a))
print(c)

a = ['hello', 'abc', 'good']

b = list(map(str.upper, a))
print(b)


# 'Filter' - одной из задач является некая фильтрация объектов

age = [11, 20, 18, 33, 14, 12]

def is_adult(age):
    return age >= 18

f = filter(is_adult, age)
print(f)

f = list(filter(is_adult, age))
print(f)

# Формат записи функции без ее объявления

age = [11, 20, 18, 33, 14, 12]

is_adult = lambda age: age >= 18
f = list(filter(is_adult, age))
print(f)

def cube(x):
    return x**3

a = [3, 13, 32]

b = map(cube, a)
print(b)

c = list(map(cube, a))
print(c)

def num(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return num(n - 1) + num(n - 2)

print(num(8))


age = [1, 23, 34, 13]
is_over = lambda age: age >= 13
f = filter(is_over, age)
print(f)
f = list(filter(is_over, age))
print(f)

age = [1, 23, 34, 13]
def is_over(age):
    return age >= 10
print(age)

a = filter(is_over, age)
print(a)

b = list(filter(is_over, age))
print(b)
