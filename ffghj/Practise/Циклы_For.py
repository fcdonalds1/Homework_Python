#Циклы - конструкция языка, которые помогают выполнять описанные в
# теле циклыvдействия некоторое коллияество раз.
#Циклично выполняемые операции.

#Синтаксис - for x in iterable:
                        #действие x
#Где x - локальная переменная в рамках цикла for, которая хранит в себе
#каждый элемент последовательности iterable, столько раз, сколько есть
#элементов в данной последовательности

#Действие с x в рамках уикла for, происходит с каждым элементом
#последовательности

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in numbers:
    print(i)

for i in numbers:
    print(i*i)

#C помощью цикла for мы можем строить списки с помощью range.

numbers = range (1, 6)
for i in numbers:
    print(i)

numbers = range(1, 100)
print(numbers)

new_list = []

for i in numbers:
    new_list.append(i)

print(new_list)

#Внутри цикла можно делать ветвление при помощи операторов
#if - elif - else

for i in range(1, 16):
    if i % 2 == 0:
        print(f'{i} Это четное число')
    else:
        print(f'{i} Это нечетное число')

#C помощью цикла for мы можем обратиться по индексу к элементу
#итерируемого объекта

numbers = [1, 2, 3, 4]

for x, item in enumerate(numbers):
    numbers[x] += 30

print(numbers)

name = 'Alex Johnson'

for x in name:
    print(x)

for _ in range(1, 5):
    print('Ошибка!!')

some_tuple = (11, 'Alex', 3.14)

for x in some_tuple:
    print(x)

some_list = [('John', 22), ('Alex', 33),('Artem', 44)]

for (name, age) in some_list:
    print(f'{name} is {age} years old')

#Применение цикла for Относительно словарей

some_dict =  {
    'Alex': 111,
    'Maxim': 222,
    'Anna': 333,
}

for x in some_dict.items():
    print(x)

print(type(x))

some_dict =  {
    'Alex': 111,
    'Maxim': 222,
    'Anna': 3,
}

for x, y in some_dict.items():
    print(f'Ключ {x}  Значение {y}')

for value in some_dict.values():
    print(value)


