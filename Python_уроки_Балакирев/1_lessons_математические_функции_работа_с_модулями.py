import math

# abs = работа с модулями
a = abs(-31)
print(a)

# min = минимальное число в списке
b = min(13, 24, 0, -17)
print(b)


# max = максимальное число в списке
c = max(13, 1, 45, 90)
print(c)

# pow = возведение в степень
d = pow(3, 5)
print(d)

# round = округление чисел
g = round(4.5)
print(g)

h = round(4.5765745, 2)
print(h)

# Разрешается вложенность
f = max(1, 2, abs(min(10, 5, -3)), -10)
print(f)

import math
x = math.ceil(5.2)
print(x)

k = math.factorial(6)
print(k)

l = math.log10(1000)
print(l)

r = math.log(2.7)
print(r)

a, b = map(int, input().split())
res = math.sqrt(a ** 2 + b ** 2)
print(round(res, 2))


