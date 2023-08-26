#1. Декоратор - функция обертка, которая оборачивает другую функцию в свой
#функционал, без изменения основной функции.

#2. @decorator - синтаксис применения

#3. Используйте модуль 'datetime' для тестирования функций (timecode)

#4. @wraps необходим для передачи значений из документации основной функции
# в help() при использовании декораторов

def tagMaker(func):
    def wrapper(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return wrapper


@tagMaker
def printText(text):
    print(text)

printText('hello world')

import time
import datetime

def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        print(f'Функция завершена за {done} времени')
    return wrapper

@recTime
def sfunc():
    time.sleep(3)
    print('Завершено')

sfunc()