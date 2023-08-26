#Dictionary - словарь. Список пар: КЛЮЧ - ЗНАКЧЕНИЕ
#Ключи - уникальное значение, не может быть дубликата
#Синтаксис - { ключ : значение, ключ : значение}

students = {
    'alex' : 258,
    'max' : 227,
    'anna' : 278
}
print(students)

#Чтобы прочитать значение словаря по ключу
#Ключ в [] - квадратных скобках.
#Или с помощью функции 'GET' в круглых скобочках

print(students['anna'])
print(students.get('alex'))

#Для того чтобы добавить новую пару ключ - значение
#Или обновить данные - обычная операция присвоения ['ключ'] = значение

students['andrey'] = 268
print(students)

#Для новых данных так же ['ключ'] = значение

students['andrey'] = 177
print(students)

#В случае, если нужно создать пару, а значений нет -
#Функция 'setdefault'. Добавляет с пустым значением NONE

students.setdefault('oleg')
print(students)

#Для удаления пар словаря - функция 'pop'  - в аргумент передается ключ

students.pop('oleg')
print(students)

#Чтобы получить все ключи из словаря  - метод 'keys'

print(students.keys())
print(type(students.keys()))

#Преобразование при поможи функции 'list'

key_list = list(students.keys())
print(key_list)
print(type(key_list))

#Чтобы получить значение - функция 'value'

print(students.values())
print(type(students.values()))

#Проверка, находится ли ключ в словаре ('ключ' in словарь) или 'not in'

print('anna' in students)
print('iggy' not in students)



