#__init__(self)   инициализатор класса - вызывается сразу после создания экземпляра класса
#__del__(self)    финализатор класса - вызывается перед его удалением


class Point:
    color = 'red'
    circle = 2

#Существует 2 магических метода - __init__(self)   инициализатор класса
#                                 __del__(self)    финализатор класса

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y


    def get_coords(self):
        return self.x, self.y

pt = Point(10, 2)
print(pt.__dict__)
