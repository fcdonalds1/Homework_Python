x = 'Alex'
print(x)
y = 'Some text 123'
print(y)
z = "some 'long' text"
print(z)

# Экранированная последовательность
x = 'Some \'long\', and \'awesome\' text'
print(x)

#Двойной слэш \\
y = 'C:\\Users\\Desktop\\Python\\Lessons_Py'
print(y)

#Через букву "r"
y = r'C:\Users\Desktop\Python\Lessons_Py'
print(y)#

y = 'Some long \nand awesome \ntext'
print(y)

#Обращение по индексу
text = str('Hello world')
print(text)
print(text[3])

#Конкатенация - сложение частей текста \ обращение к последнему элементу
print(text[3]+text[6])
print(text[-1]+text[3])

#Срез части текста + одна буква [6:]
print(text[6:]+ text[1])

#Cрез + пробел + текст от и до [6:] до [:6]
print(text[6:]+' '+text[:6])

#Шаг по дефолту шаг в единицу. Расстояние захвата элементов
print(text[::1])
print(text[::2])
print(text[::3])
