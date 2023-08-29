a = int(input())
b = int(input())
c = int(input())

no_zero = a > 0 and b > 0 and c > 0 and 'Нет нулевых значений!!!'
print(no_zero)

a = int(input())
b = int(input())
c = int(input())

all_zero = (a == 0) and (b == 0) and (c == 0) and 'Введены все нули'
print(all_zero)
print(a)

first_number = a or b or c
print(first_number)

a = int(input())
b = int(input())
c = int(input())


if a > (b + c):
    print(a - b - c)

a = int(input())
b = int(input())
c = int(input())

if a < (b + c):
    print(a + b - c)

a = int(input())
b = int(input())
c = int(input())

if a > 50 and (b > a or c > a):
    print('Вася')

a = int(input())
b = int(input())
c = int(input())

if a > 5 or (b == 7 and c == 7):
    print('Петя')


