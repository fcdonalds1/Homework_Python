#Магические dunder методы  __str__ и __repr__ служат для строкового представления объекта
#Метод возвращает строковое представление заданного атрибута класса
#Конструкция:
        #def __str__(self):
            #return self.atr

#Чаще всего, используется метод str.

class New():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

new_obj = New('Nick')
print(new_obj)

#Для вывода ошибки в лог файл имеет смысл записывать через __repr__
#Для вывода объекта на сайт - __str__