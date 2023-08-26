

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
        self.probeg = self.probeg + km

class Battery():
        def __init__(self, battery=100):
            self.battery = battery

        def description_battery(self):
            print(f'Значение батареи равно : ' + str(self.battery) + '%')

class ElectroCar(CarsClass):
        def __init__(self, brand, model, year, probeg):
            super().__init__(brand, model, year, probeg)
            self.battery = Battery()

        def description_battery(self):
            print(f'Значение батареи равно : ' + str(self.battery) + '%')

        def showCar(self):
            print(f'{self.brand}, {self.model}')
