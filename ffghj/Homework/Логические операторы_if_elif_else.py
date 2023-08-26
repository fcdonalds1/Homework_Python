print('Ведите число от 1 до 6')
x = int(input())

if 0 < x < 7:
    if x%2 == 0:
        print('Четное число')
        if 1 < x < 3:
            print('Это число 2')
        elif 3 < x < 5:
            print('Это число 4')
        else:
            print('Это число 6')
    elif x%2 != 0:
        print('Это нечетное число')
        if 2 < x < 4:
            print('Это число 3')
        elif 4 < x < 6:
            print('Это число 5')
        else:
            print('Это число 1')
else:
    print('Ведите число от 1 до 6')

fib_1 = 1
fib_2 = 1

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
    print(fib(2))

