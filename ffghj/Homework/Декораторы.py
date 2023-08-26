import time


def make_list(n):
    empty_list = []
    for i in range(0, n):
        empty_list.append(i)
    for i in empty_list:
        print(empty_list[i])

make_list(10)

def make_list(n, type = None):
    empty_list = []
    for i in range(0, n):
        empty_list.append(i)
    if type is None:
        print(empty_list[i])
    elif type == 't':
        new_tuple = tuple(empty_list)
        for i in new_tuple:
            print(new_tuple[i])

make_list(10,'t')


import datetime
import time

def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        print(f'Функция подсчета  завершена за {done} времени')
    return wrapper

@recTime
def make_list(n, type = None):
    time.sleep(2)
    empty_list = []
    for i in range(0, n):
        empty_list.append(i)
    if type is None:
        print(empty_list[i])
    elif type == 't':
        new_tuple = tuple(empty_list)
        for i in new_tuple:
            print(new_tuple[i])


make_list(10, 't')
make_list(10)


