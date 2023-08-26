# Механизм инкапсуляции - защита из вне
# attribute (без одного или двух подчеркиваний вначале) - публичное свойство(public)

# _attribute(с одним подчеркиванием) - режим доступа protected (служит для обращения
# внутри класса и во всех его дочернних классах)

# __attribute(с двойным подчеркиванием) - режим доступа (private) - служит для
# обращения только внутри класса

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # Приватный метод записывается так же, как и приватная переменная
    @classmethod
    def __check_value(cls, x):
        return type(x) in(int, float)




    def set_coords(self, x, y):
        # Проверка на тип значений
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')


    def get_coords(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coords(10, 20)
print((pt._Point__x))