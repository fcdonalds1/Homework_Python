import math


class Counter:
    def __init__(self):
        self.__counter = 0


# Создаем функцию ,где вызываем метод call и увеличиваем счетчик на единицу
# и возвращаем новый счетчик
    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter

c = Counter()
c2 = Counter()
c()
c(2)
res = c(20)
res2 = c2(-5)
print(res, res2)



class StripCars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)


s1 = StripCars('?!;,. ')
s2 = StripCars(' ')
result = s1(' Hello World! ')
result2 = s2(' Hello World! ')
print(result)
print(result, result2, sep='\n')




class Derivate:
    def __init__(self, funk):
        self.__fn = funk

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)



#df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))
