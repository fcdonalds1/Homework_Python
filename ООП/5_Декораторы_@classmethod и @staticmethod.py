class Vector:
    # В класс добавляем 2 атрибута - атрибуты
    # класса они принадлежат именно классу Vector
    MIN_COORD = 0
    MAX_COORD = 100

    # Объявляем метод класса:

    @classmethod

    # Объявляем метод - метод класса работает только с атрибутами
    # самого класса
    # Чтобы вызвать - прописываем имя класса.имя функции класса(и аргумент)
    # print(Vector.validate())
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD


    def __init__(self, x, y):
        self.x = self.y = 0
        # Лучше прописывать self вместо имени класса
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

        # Лучше использовать SELF
        print(self.norm_2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y



    # Статический метод - можно спокойно вызывать внутри обычных методов
    @staticmethod
    def norm_2(x, y):
        return x * x + y * y


v = Vector(10, 20)
print(Vector.validate(10))
res = Vector.get_coords(v)
print(res)
print(res)
print(Vector.norm_2(5, 6))

# Помимо этих методов мы еще можем работать с двумя типами методов
# статические и методы класса
# Методы класса определяются при помощи декоратора @classmethod
# Методы статические при помощи @staticmethod