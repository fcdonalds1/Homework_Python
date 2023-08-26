#__new__() вызывается перед созданием объекта класса

                        # Объект класса

# __init__() - вызывается сразу после создания объекта класса

class Point:

# Cls ссылается на текущий экземпляр класса  - Point на сам класс

    def __new__(cls, *args, **kwargs):
        print('Вызов метода __new__ для ' + str(cls))
        return super().__new__(cls)

# self из __init__ ссылается уже на создаваемый (созданный) и self
# ссылается на экземпляр

    def __init__(self, x = 0, y = 0):
        print('Вызов метода __init__ для ' + str(self))
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)


class DataBase:
    # Прописываем атрибут класса: __instance - ссылка на экземпляр класса
    # Если его нет - принимает значение None
    # Если есть - то ссылка на экземпляр класса
# Для управления созданием новых объектов переопределяем магический метод __new__
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        print('Данные из БД')

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', '1234', 80)
db_2 = DataBase('root_2', '5678', 40)
print(id(db), id(db_2))

db.connect()
db_2.connect()