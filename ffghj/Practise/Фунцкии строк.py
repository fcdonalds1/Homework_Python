x = 'some long and awesome TEXT'

#Колличество символов в строке
print(len(x))

#Обращение к последнему элементу
print(x[len(x)-1])

#Срез
print(x[len(x)-4:len(x)])

#Функция 'Count' подсчитывает, сколько одинаковых элементов в строке
print(x.count('o'))

#'Find' Показывает, где находится символ
print(x.find('a'))
print(x.find('o'))

#Дополнительный параметр функции 'Find' - диапазон поиска индексов
#Передаются через запятую
print(x.find('o', 3, 7))
print(x.find('o', 7))

#Поиск фразы, откуда начинается
print(x.find('and'))
print(x.find('TEXT'))

#'Capitalize' - преобразует строку, первая буква становится большой
print(x.capitalize())
print(x.upper())
print(x.lower())
print('Old text: '+x)

upper_case = x.upper()
lower_case = x.lower()

#Функция проверки на верхний и нижний регистр элементов
print(upper_case.isupper())
print(lower_case.islower())

#Проверка исходной строки
print(x.isupper())
print(x.islower())

#Проверка состоит ли из цифр и букв
#Cостоит только из букв
print('xxx777'.isalnum())
print('xxx777!'.isalnum())
print('xxx777'.isalpha())

#Функции startswith и endswith
x = str('hello')
print(x.startswith('he'))
print(x.endswith('lo'))

#'Сплит' - разбивает строку на части
split = x.split('l')
print(type(split))
print(split)

#Преобразование данных из строки(str) в список(list)
some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')
print(separated_data)
print(separated_data[3])