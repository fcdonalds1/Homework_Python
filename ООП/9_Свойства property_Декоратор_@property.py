class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

# Возвращает закрытое приватное свойство имя - __old
    @property
    def old(self):
        return self.__old

# Принимает доп параметр old и приватному параметру old присваивать новое значение
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Сергей', 20)
del p.old
p.old = 48
print(p.__dict__)