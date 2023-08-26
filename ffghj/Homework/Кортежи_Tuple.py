guns = ['axl', 'slash', 'dizzy', 13, 3.14 ]
print(guns)
print(type(guns))

roses = tuple(guns)
print(roses)
print(type(roses))

print(roses[2])

iron = list(roses)
print(iron)
print(type(iron))

iron[2] = 'fildi'
print(iron)
x = 2
