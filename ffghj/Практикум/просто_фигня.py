# Подвиг 5. Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать эти данные в
# список целых чисел. Затем, перебрать этот список в цикле for и просуммировать все нечетные значения.
# Результат вывести на экран.
#
# Sample Input:
#
# 8 11 -2 4 0 13 19 12 7

# numbers = list(map(int, input().split()))
# summa = 0
# new_summa = 0
# for elements in numbers:
#     if elements % 2 != 0:
#         summa += elements
#     else:
#         new_summa += elements
# print(summa)
# print(new_summa)

# Подвиг 7. Вводится натуральное число n. С помощью цикла for найти все делители этого числа.
# Найденные делители выводить сразу в столбик без формирования списка.
#
# Sample Input:
#
# 12

# n = int(input())
# numbers = 0
# for element in range(1, n + 1):
#     if n % element == 0:
#         print(element)
#         numbers += element
#


# Подвиг 6. Вводятся названия городов в одну строчку через пробел.
# Необходимо преобразовать входные данные в список.
# Затем, перебрать его циклом for и заменить значения элементов на длину названия соответствующего города.
# Результат вывести на экран в виде последовательности чисел через пробел в одну строчку.
#
# Sample Input:
#
# Москва Уфа Караганда Тверь Минск Казань
# Sample Output:
#
# 6 3 9 5 5 6

# cities = list(input().split())
#
# count_alfa = 0
#
# for element in cities:
#     b = (len(element))
#     count_alfa += 1
#     print(b, end=' ')

# Подвиг 8. Вводится натуральное число n. С помощью цикла for определить,
#     является ли оно простым (то есть, делится нацело только на само себя и на 1).
# Вывести на экран ДА, если n простое и НЕТ - в противном случае.
#
# Sample Input:
#
# 11
# Sample Output:
#
# ДА


# Подвиг 10. Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n, которые кратны или 3 или 5.
# Результат (сумму) вывести на экран. Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.

# n = int(input())
# summa = 0
#
# for element in range(1, n):
#     if element % 3 == 0 or element % 5 == 0:
#         summa += element
#
# print(summa)

# Подвиг 9. Вводится список названий городов в одну строчку через пробел.
# Перебрать все эти названия с помощью цикла for и определить, начинается ли название следующего города на последнюю букву предыдущего города в списке.
# Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
# Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае



# number = int(input())
#
# buy =[]
# for i in range(number):
#     buy.append(input())
# print(*buy, sep='\n')

# count = int(input())
#
# spis = [input() for i in range(count)]
# search = input()
# for j in range(len(spis)):
#     if search in spis[j]:
#         print(spis[j])

# count = int(input()) # колличество целых чисел, введенных с клавиатуры
# spisok = [int(input()) for i in range(count)]
#
# for j in range(1, len(spisok)):
#     print(spisok[j] + spisok[j - 1])

# count = int(input())
# white_spis = [input() for i in range(count)]
# new_count = int(input())
# search = [input() for j in range(new_count)]
# for j in range(len(search)):
#     if search[j] in white_spis:
#         print(search[j])

# n = int(input())
# spis = [input() for i in range(n)]
# print('\n'.join(spis))
# print('')
# five = '5'
# four = '4'
# for i in spis:
#     if five in i or four in i:
#         print(i)

# n = int(input())
# A = []
# for i in range(1, n + 1):
#     A.append(i)
# print(A)

# x, y = map(int, input().split())
# A = []
#
# for i in range(x, x + y):
#     A.append(i)
#
# for y in A:
#     print(y, end=' ')

# n = int(input())
# A = []
#
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         A.append(i)
#
# for j in A:
#     print(j, end=' ')


# n = int(input())
# kol_chet = 0
#
# while n > 0:
#     last_number = n % 10
#     if last_number % 2 == 0:
#         kol_chet += 1
#
#     n // 10
#
# print(kol_chet)

# n = int(input())
# summa = 0
#
# while n != 0:
#     summa = summa + n
#     n = int(input())
# print(summa)

