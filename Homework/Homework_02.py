height = float(input('Введите ваш рост: '))
weight = int(input('Ведите ваш вес: '))


bmi = weight/height**2
print('Ваш индекс массы тела: ', round(bmi))

start_scale = 16
end_scale = 50

len_1 = round(bmi - start_scale)
len_2 = round(end_scale - bmi)

scale_logic = '16' + '=' * int(len_1 - 1) + '|' + '=' * int(len_2 - 1) + '50'

print(scale_logic)



