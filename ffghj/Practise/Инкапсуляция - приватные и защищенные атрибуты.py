#Атрибуты бывают:
#Публичные
#Защищенные
#Приватные
#Вызов приватных методов с помощью публичных

    #def publicmethod(self):
        #    self.__privatemethod()

    #def__privatemethod(self):
#obj.publicmethod()

class VkAccountInWebSite():
    """Аккаунт в вк, на сайте VK """
    """Чтобы создать защищенный атрибут в пайтон - нужно добавить нижнее подчеркивание _name"""
    """перед нимв блоке инициализации и в методах класса. Нижнее подчеркивание не решит проблему"""
    """Чтобы создать приватный атрибут - нужно добавить двойное нижнее подчеркивание __name"""

    def __init__(self, name, login_id, password):
        self.__name = name
        self.__login_id = login_id
        self.__password = password

    def publicLogin(self):
        self.__loginVk()

    def __loginVk(self):
        if self.__login_id == 123 and self.__password == 456:
            print(f'Привет ' + self.__name)
        return True


vkakk = VkAccountInWebSite('Виталий', 123, 456)
vkakk.publicLogin()
#print(vkakk.__name)

#Приватные методы обозначаются двойным подчеркиванием обозначаются внутри



