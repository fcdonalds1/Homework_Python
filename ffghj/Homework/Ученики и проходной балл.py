student_ivan= 'ivan'

ivan_chem = 67
ivan_math = 78
ivan_rus = 78

student_joe = 'joe'

joe_chem = 78
joe_math = 98
joe_rus = 55

student_lee = 'lee'

lee_chem = 67
lee_math = 76
lee_rus = 95

student_neo = 'neo'

neo_chem = 76
neo_math = 56
neo_rus = 51

student_vivien = 'vivien'

vivien_chem = 55
vivien_math = 63
vivien_rus = 99

#Переопределение баллов
neo_rus = 78
joe_math = 90

#Сумма всех баллов
all_point_ivan = ivan_chem + ivan_math + ivan_rus
print(all_point_ivan)

all_point_joe = joe_chem + joe_math +joe_rus
print(all_point_joe)

all_point_neo = neo_chem +neo_math + neo_rus
print(all_point_neo)

all_point_vivien = vivien_chem + vivien_math + vivien_rus
print(all_point_vivien)

#Cредний балл
mid_point = (all_point_ivan + all_point_joe + all_point_neo + all_point_vivien)/4
print(mid_point)

print(all_point_ivan >= mid_point)
print(all_point_joe >= mid_point)
print(all_point_vivien >= mid_point)
print(all_point_neo >= mid_point)





