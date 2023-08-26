# Множества - математическое понятие и представляет собой
# представляет собой последовательность уникальных
# обектов.
# Синтаксис - {'', '', }

first_set = {'Alex', 'John', 'George', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))

# Добавление объекта функция 'add'
first_set.add('Maxim')
print(first_set)

# Для проверки, присутствует ли элемент в множестве
# используем конструкцию 'in'.

print('Maxim' in first_set)

# Для удаления элемента - функция 'remove'

first_set.remove('Alex')
print(first_set)

#Для полной очистки множества - функция 'clear'

first_set.clear()
print(first_set)

# Поддерживает сложение списков функция 'union'

first_set = {'Alex', 'John', 'George', 'Alex'}
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set)
print(third_set)

# 'intersection' - Функция показывающая ножества элементов
# Которые есть и в первом и во втором множестве - повторяю
# щиеся

fourth_set = first_set.intersection(second_set)
print(fourth_set)

# Разность множеств функция 'difference' - возвращает эле
# менты, которые присутствуют только в первом множестве
# отстутствуют во втором

fifth_set = first_set.difference(second_set)
print(fifth_set)

# Такую же операцию можно произвести вычитанием

print(fifth_set - second_set)

# Можно проверить, является ли множество подмножеством
# второго множества 'issubset' надмножеством 'issuperset'

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_1.issubset(set_2))
print(set_2.issuperset(set_1))

# Нельзя обратиться по индексу к множеству

print(set_1[0])