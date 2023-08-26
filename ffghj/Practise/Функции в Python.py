#Функция - именнованая часть кода, которая может принимать в себя
#аргументы, производить операции и выдавать результат.

#print()
#type()
#len()
#sqrt()
#round()
#upper()


#синтаксис - def имя функции ([список аргументов]):
            #оператор (действие) 1
            #оператор (действие) 2
            #....
            #оператор (действие) N
#набор операторов внутри тела функции

def printText():
    print('Hello world')

printText()
printText()
printText()

#Функции с аргументами

r = 10
s = 3.1415*(r**2)
print(s)

def sqRing(p):
    s = 3.1415 * (p ** 2)
    print(s)

sqRing(2)
sqRing(4)

def sqRing(p):
    s = 3.1415 * (p ** 2)
    return s

a = 30

print(sqRing(a))


def getSquare(w, h):
    return 2*(w+h), w*h
print(type(getSquare(3, 5)))

print(getSquare(3, 5))

def printText(msg, end = '!'):
    print(msg + end)

printText('Text')
printText('Text', '?')

a = False

if a:
    def sFunc(x, y, z):
        return print(x+y+z)
else:
    def sFunc(a, b, c):
        x = a+b/c
        print(x)

sFunc(10, 20, 30)

def funct(a, b, c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a+b+c

help(funct)

