# Форматирование строк
x = '10'
y = 'cold'
print('Weather: + {} and it\'s very {} '.format(x,y))
print('Weather: +{0} and it\'s very {1} '.format(x,y))
print(f'Weather: +{x} and it\'s very {y}')

x = 'German'
y = 'Vitali'
z = '32'
print(f'Привет, меня зовут {x} {y} и мне {z} года')

#Перенос строк
x = '-Почему для всех ребят \nлета не хватает? \n-Лето словно шоколад\nочень быстро тает'
print(x)

#Поиск нужного элемента
text = 'Hello World'
print(text.find('W'))

#Срезы
text = ('abrakadabra')
print(text[0]+text[3]+text[4]+text[5]+text[6]+text[7]+text[10])
print(text[2:7]+text[9:11])
text = 'abrakadabra'
index_letter_ab_1 = text.find('ab')
imdex_letter_ab_2 = text.find('ab',1)
text = 'abrakadabra'

index_letter_ab_1 = text.find('ab')

index_letter_ab_2 = text.find('ab', 1)
new_text = text[index_letter_ab_1+2:index_letter_ab_2] + text[index_letter_ab_2+2:]
print(new_text)


text = str ('abrakadabra')
print(text[1]+text[3]+text[2]+text[8]+text[7]+text[9:11])
#Увеличение заглавной буквы
x = 'barbara'
print(x.capitalize())
#Уеличение всех букв
x = 'win!'*3
print(x.upper())

#Поиск нужного символа в элементе
x = 'find'
print(x.find('d'))
