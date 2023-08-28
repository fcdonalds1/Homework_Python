password = '2233'
a = input()
count = 0
while a != password:
    print('Введите корректный пароль')
    a = input()
    count += 1
else:
    print('Пароль корректен')
    print('Вы потратили,', count, 'попыток')




