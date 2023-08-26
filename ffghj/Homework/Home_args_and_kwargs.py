def kwargs(*args):
    num = args
    summa = 0
    for i in num:
        summa = summa + i
    mid = summa / len(num)
    print(round(mid ,2))

kwargs(1.45, 2, 3, 7)


def max_in_args(*args):
    sort_list = sorted(args)
    max_num = sort_list[-1]
    min_num = sort_list[0]
    print(f'Максимальное число {max_num}, минимальное число {min_num}')



max_in_args(43, 12, 67, 89, 111)













