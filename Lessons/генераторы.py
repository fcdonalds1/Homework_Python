import math
a = [23, 13.5, 'tools', 'nigga']

def int_numbers(a):
    return [i for i in a if type(i) is str]

int_numbers(a)
print(int_numbers(a))

a = [23, 'goor', '14', 56]

def num():
    return [i**2 for i in a if type(i) is int]

num()
print(num())

b = ['12', '23', '48']

def func():
    return [int(x) for x in b]

func()
print(func())

c = {'hook' : 13, 'john' : 23}

def fact(num):

