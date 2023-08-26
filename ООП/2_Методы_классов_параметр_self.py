class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return(self.x, self.y)


# Cоздаем экземпляр класса
pt = Point()
pt_new = Point()

# Присваиваем значения экземплярам класса
pt.set_coords(1, 2)
pt_new.set_coords(10, 20)

# Набор атрибутов экземпляров класса
print(pt.__dict__)
print(pt_new.__dict__)

# Выводим значение экземпляров класса через функцию
print(pt.get_coords())
print(pt_new.get_coords())


f = getattr(pt, 'get_coords')
print(f())
