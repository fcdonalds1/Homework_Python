class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

# Магический метод __getattribute__

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

# Setattr - автоматически вызывается каждый раз, когда идет присвоение определенного
# значения синтаксис (def __setattr__(self, key, value):

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)


# getattr вызывается каждый раз, когда идет обращение к
# несуществующему экземпляру класса

    def __getattr__(self, item):
        return False


# delattr - вызывается каждый раз, когда удаляется определенный атрибут из экземпляра
# класса

    def __delattr__(self, item):
        print('__delattr__: '+ item)
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.y = 5
print(pt1.yy)
del pt1.x
print(pt1.__dict__)