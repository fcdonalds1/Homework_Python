class Cat:
    def __init__(self, name):
        self.verify_name(name)

        self.name = name.lower()

    def __repr__(self):
        return f'{self.__class__} : {self.name}'


    def __str__(self):
        return f'{self.name}'

    @classmethod
    def verify_name(cls, name):
        if type(name) != str:
            raise TypeError('Имя должно быть строкой')


cat = Cat('Ginger')
print(cat)



class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)


    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -45)
print(len(p))
print(abs(p))