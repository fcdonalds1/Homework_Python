# Для предотвращения ошибок, используем проверки пользуясь конструкцией
# if, elif, else.

# Применяем конструкцию try, except finally

# try:
# код программы
# except <error name>:
# действие при ошибке <error name>

# общий except Exception as e:
# действие с e и type(e)
# finally:
# действие которое должно произойти в любом случае

# Ошибки бывают: 1 синтаксические
# 2

while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a / b)
    except ValueError:
        print('Произошла ошибка! ValueError! Введите число, а не текст!')
    except ZeroDivisionError:
        print('Произошла ошибка! ZeroDivisionError! На ноль делить нельзя!')
    except Exception as e:
        print(e, type(e))
    finally:
        print('Операция завершена')

import requests
import time
from datetime import datetime

while True:
    try:
        a = requests.get('https://getwebcode.ru')
        print(a)
        time.sleep(3)
        if a == '<Response [200]>':
            pass
        elif a == '<Response [503]>':
            print('ошибка сайта')
        else:
            print('иная ошибка')
    except requests.exceptions.ConnectionError:
        error_time = datetime.now()
        print('Сервер упал!\n ' + str(error_time))
