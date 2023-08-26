a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

a, b, c = 'string', 20, 3.14

print(a)
print(b)
print(c)

#Если больше элементов - то выбъет ошибку. Добавляя '*' идет присвоение элементов
#по позиции
*a, b, c = 'string', 20, 3.14, 'Text', 30, 4.14

print(a)
print(b)
print(c)


s = [4, 10]
print(list(range(*s)))

def func(a, b, c, d):
    print(a, b, c, d)

a = ('Hello', True, 78, [3, 4, 5])

func(*a)


#Когда мы указываем '*' перед аргументами - все значения упаковываются в эту
# переменную в виде кортежа
def func(*args):
    print(sum(args) * 0.06)

func(12, 13)

#Передаем в функцию именнованные аргументы '**kwargs' так же в неограниченном
#колличестве



def funk(**kwargs):
    print(kwargs)


#Результат функции - словарь
funk(a = 1, b = 4, c = 34)

#Можно комбинировать эти два способа - сначала указываем '*args'
# потом '**kwargs'
#Первое значение, которое пераем идет в 'args' в виде кортежа
#Второе значение 'kwargs' идет в виде словаря


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 3, 56, 235, 'print', a = 3, b = 5, c = 100)