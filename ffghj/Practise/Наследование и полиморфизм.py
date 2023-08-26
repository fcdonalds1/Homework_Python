class CarsClass():


    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = int(probeg)

    def showCar(self):
        print(f'{self.brand}, {self.model}, '
              f'{self.year} год, {self.probeg} km')

    def drowCar(self, km):
        """Метод поездки автомобиля"""
        self.probeg = self.probeg + km


class Battery():
    """Класс батареи"""
    def __init__(self, battery = 100):
        self.battery = battery

    def description_battery(self):
        """Выводит информацию о заряде батареи"""
        print(f'Значение батареи равно : ' + str(self.battery) + '%')

# Cоздаем новый класс для электромобилей с показанием расхода заряда батареи
# Проводим наследование

class ElectroCar(CarsClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = Battery()
    def description_battery(self):
        """Выводит информацию о заряде батареи"""
        print(f'Значение батареи равно : ' + str(self.battery) + '%')

#Для того чтобы переопределить родительский метод у потомка, копируем род метод
# и копипастим в потомка прпивер ниже и меняем поведение метода. Удаляем
# из метода год и пробег


    def showCar(self):
        print(f'{self.brand}, {self.model}')


s_car = CarsClass('Ford', 'Mustang', '2022', '10')
tesla = ElectroCar('Tesla', 'Mjolnir', '2022', 10000)
s_car.showCar()
s_car.drowCar(100)
s_car.showCar()
tesla.showCar()
#tesla.description_battery()
tesla.showCar()

tesla.battery.description_battery()






