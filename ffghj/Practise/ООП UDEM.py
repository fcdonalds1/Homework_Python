#class NameClass():
    #атрибуты класса и инициализация
    #def __init__(self. atr1, atr2, atr3):
        #self.atr1 = atr1
        #self.atr1 = atr1
        #self.atr1 = atr1
    #метод класса
    #def func(self)
        #Действие с atr...


# Класс машин
# объект - машина
# атрибуты - марка, модель, скорость -
# функции - движение, остановка и т.д.

class CommentFromWebSite():
    """Комментарии с сайта"""
    def __init__(self, data, text, likes):
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComment(self):
        """Вывести комментарий в консоль"""
        print(f'\nКомментарий с сайта, \n дата: {self.data},'
              f'\n текст: {self.text}, лайков: {self.likes}')

    def changeLikes(self):
        """При вызове колличество лайков будет увеличено на 1"""
        self.likes = self.likes + 1

    def changeComment(self, new_text):
        """Изменение комментария, нужно будет что-то написать"""
        self.text = new_text

new_comment = CommentFromWebSite('11/09/22', 'Первый комметарий', '13')
new_comment2 = CommentFromWebSite('13/08/19', 'Второй комметарий', '78')


new_comment2.showComment()
new_comment2.changeLikes()
new_comment2.showComment()
new_comment.showComment()
new_comment.changeComment('Новый!!!')
new_comment.showComment()
new_comment.changeLikes()
new_comment.showComment()

