# . Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
# 2. Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
# 1. Если первое значение  больше чем сумма второго и третьего вывести a - b - c
# 1. Если первое значение меньше чем сумма второго и третьего вывести b + c - a
# 1. Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
# 1. Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"

#
# a = int(input())
# b = int(input())
# c = int(input())
#
# result = 'Нет ни одного нуля' or a or b or c
# print(result)

# a = int(input())
# b = int(input())
# c = int(input())
#
# res = a or b or c
# print(res)

# a = int(input())
# b = int(input())
# c = int(input())
#
# all_zero = 'Введены все нули' or  a or b or c
# print(all_zero)

a = int(input())
b = int(input())
c = int(input())

if a > b + c:
    print(a - b - c)

a = int(input())
b = int(input())
c = int(input())

if a < b + c:
    print(b + c - a)

a = int(input())
b = int(input())
c = int(input())

if a > 50 and (b > a) or (c > a):
    print('Петя')

a = int(input())
b = int(input())
c = int(input())

if a > 5 or b == 7 and c == 7:
    print('Петя')






