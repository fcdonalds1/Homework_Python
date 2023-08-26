#Создание класса с какими-то свойствами и на основе этих свойств создаются объекты
#При помощи методов создается описание класса, которое он передаст определенному объекту
#В __init__(self) записываем свойство класса

#class NameClass():
    #атрибуты класса и инициализация
    #def __init__(self. atr1, atr2, atr3):
        #self.atr1 = atr1
        #self.atr1 = atr1
        #self.atr1 = atr1
    #метод класса
    #def func(self)
        #Действие с atr...


class House():
    """Описание дома (Описание класса)"""
    def __init__(self, street, number):
        """Cвойства дома - улица, номер"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """Этот метод строит дом"""
        print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен.')

    def age_of_house(self, year):
        """высчитывает возраст дома"""
        self.age += year


"""Объекты класса"""
House_1 = House('Московская', 20)
House_2 = House('Московская', 56)

"""Обращение объекта к описанию класса"""
print(House_1.street)
print(House_2.number)
"""Обращение объекта к описанию класса 'build'"""

House_1.build()
print(House_1.age)

House_1.age_of_house(6)
print(House_1.age)


#Наследование - Родитель - потомок


class ProspectHouse(House):
    """Унаследование - дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse('Рокоссовского', 12)
print(PrHouse.prospect)
print(PrHouse.number)



