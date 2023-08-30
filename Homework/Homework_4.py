a = int(input())
b = int(input())
c = int(input())

result = 'Нет ни одного нуля' or a or b or c
print(result)

a = int(input())
b = int(input())
c = int(input())

res = a or b or c
print(res)

a = int(input())
b = int(input())
c = int(input())

all_zero = 'Введены все нули' or  a or b or c
print(all_zero)

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

print()
print()
print()





